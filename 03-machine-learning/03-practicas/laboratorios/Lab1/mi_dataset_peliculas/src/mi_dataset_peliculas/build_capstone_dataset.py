"""Build the local, validated movies.csv snapshot used by the UD3 capstone."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from .merge import FORBIDDEN_COLUMNS, RATING_HIGH_THRESHOLD, SCHEMA, capstone_record
from .omdb import OmdbClient
from .tmdb import TmdbClient

REPOSITORY_ROOT = Path(__file__).resolve().parents[7]
CAPSTONE_ROOT = REPOSITORY_ROOT / "03-machine-learning/03-practicas/midterm-capstone/Peliculas/Practica_Peliculas_OK"
DEFAULT_SNAPSHOT = CAPSTONE_ROOT / "data/movies.csv"
DEFAULT_MANIFEST = CAPSTONE_ROOT / "movies.manifest.json"


def validate_output_paths(snapshot: Path, manifest: Path) -> tuple[Path, Path]:
    """Resolve output paths and reject destinations outside the repository."""

    repository = REPOSITORY_ROOT.resolve()
    resolved = []
    for label, path in (("snapshot", snapshot), ("manifest", manifest)):
        candidate = path.resolve()
        try:
            candidate.relative_to(repository)
        except ValueError as error:
            raise ValueError(f"La ruta de {label} está fuera del repositorio: {candidate}") from error
        resolved.append(candidate)
    if resolved[0] == resolved[1]:
        raise ValueError("El snapshot y el manifiesto deben usar rutas diferentes.")
    return resolved[0], resolved[1]


def validate_dataset(df: pd.DataFrame, *, min_rows: int = 100, min_class_proportion: float = 0.20) -> dict[str, Any]:
    """Fail loudly when the snapshot cannot support the intended exercises."""

    if list(df.columns) != list(SCHEMA):
        raise ValueError(f"Esquema inválido. Esperado: {list(SCHEMA)}; recibido: {list(df.columns)}")
    if FORBIDDEN_COLUMNS & set(df.columns):
        raise ValueError("El snapshot contiene identificadores o métricas de valoración prohibidas.")
    invalid_dtypes = {
        column: {"expected": expected, "received": str(df[column].dtype)}
        for column, expected in SCHEMA.items()
        if str(df[column].dtype) != expected
    }
    if invalid_dtypes:
        details = "; ".join(
            f"{column}: esperado {values['expected']}, recibido {values['received']}"
            for column, values in invalid_dtypes.items()
        )
        raise ValueError(f"Tipos de datos inválidos: {details}.")
    if len(df) < min_rows:
        raise ValueError(f"Filas insuficientes: {len(df)}; mínimo configurado: {min_rows}.")
    if df.isna().any().any():
        raise ValueError("El snapshot contiene valores nulos.")
    if df.duplicated().any():
        raise ValueError("El snapshot contiene filas duplicadas.")
    if not df["release_year"].between(1888, datetime.now().year + 1).all():
        raise ValueError("release_year contiene valores fuera de rango.")
    if not df["runtime_minutes"].between(40, 400).all():
        raise ValueError("runtime_minutes contiene valores fuera de rango.")
    if (df["budget_usd"] < 0).any() or (df[["production_countries_count", "production_companies_count"]] < 0).any().any():
        raise ValueError("Las cantidades no pueden ser negativas.")
    if not df[["is_collection", "adult", "rating_high"]].isin([0, 1]).all().all():
        raise ValueError("Las columnas binarias deben contener exclusivamente 0 o 1.")
    distribution = df["rating_high"].value_counts(normalize=True).sort_index()
    if set(distribution.index) != {0, 1}:
        raise ValueError("rating_high debe contener las dos clases.")
    if distribution.min() < min_class_proportion:
        raise ValueError(
            f"rating_high está demasiado desbalanceada: {distribution.to_dict()}; "
            f"mínimo configurado: {min_class_proportion:.0%}."
        )
    return {"rows": len(df), "class_distribution": {str(key): round(float(value), 6) for key, value in distribution.items()}}


def build_dataframe(*, pages: int, delay_seconds: float) -> tuple[pd.DataFrame, dict[str, int]]:
    from .config import get_api_keys

    tmdb_key, omdb_key = get_api_keys()
    tmdb = TmdbClient(tmdb_key)
    omdb = OmdbClient(omdb_key)
    records: list[dict[str, Any]] = []
    stats = {
        "tmdb_candidates": 0,
        "duplicate_tmdb_candidates": 0,
        "without_imdb_id": 0,
        "without_omdb_record": 0,
        "discarded_by_contract": 0,
    }
    seen_tmdb_ids: set[int] = set()
    tmdb_id_by_imdb_id: dict[str, int] = {}

    for page in range(1, pages + 1):
        for summary in tmdb.discover_movies(page):
            stats["tmdb_candidates"] += 1
            tmdb_id = summary["id"]
            # Popularity-based discover pages are not a stable snapshot: while
            # acquisition is running, the same movie can move onto a later page.
            if tmdb_id in seen_tmdb_ids:
                stats["duplicate_tmdb_candidates"] += 1
                continue
            seen_tmdb_ids.add(tmdb_id)
            details = tmdb.movie_details(tmdb_id)
            imdb_id = (details.get("external_ids") or {}).get("imdb_id")
            if not imdb_id:
                stats["without_imdb_id"] += 1
                continue
            previous_tmdb_id = tmdb_id_by_imdb_id.get(imdb_id)
            if previous_tmdb_id is not None:
                raise ValueError(
                    f"Conflicto de identidad: imdb_id {imdb_id} aparece asociado a "
                    f"TMDB {previous_tmdb_id} y {tmdb_id}."
                )
            tmdb_id_by_imdb_id[imdb_id] = tmdb_id
            omdb_record = omdb.by_imdb_id(imdb_id)
            if omdb_record is None:
                stats["without_omdb_record"] += 1
                continue
            record = capstone_record(details, omdb_record)
            if record is None:
                stats["discarded_by_contract"] += 1
                continue
            records.append(record)
            if delay_seconds:
                time.sleep(delay_seconds)
    return pd.DataFrame(records, columns=SCHEMA).astype(SCHEMA), stats


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(*, snapshot: Path, snapshot_sha256: str, pages: int, validation: dict[str, Any], acquisition: dict[str, int]) -> dict[str, Any]:
    """Create manifest data for the exact snapshot bytes written to disk."""

    manifest = {
        "dataset": "movies.csv",
        "snapshot_path": str(snapshot.relative_to(REPOSITORY_ROOT)),
        "snapshot_sha256": snapshot_sha256,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "sources": {"primary": "TMDB API v3", "enrichment": "OMDb API queried exclusively by imdb_id"},
        "parameters": {"tmdb_discover_pages": pages, "rating_high_rule": f"OMDb imdbRating >= {RATING_HIGH_THRESHOLD}"},
        "schema": SCHEMA,
        "predictor_exclusions": sorted(FORBIDDEN_COLUMNS),
        "validation": {**validation, **acquisition},
    }
    return manifest


def write_outputs(
    df: pd.DataFrame,
    *,
    snapshot: Path,
    manifest: Path,
    pages: int,
    validation: dict[str, Any],
    acquisition: dict[str, int],
) -> None:
    """Write snapshot and manifest from prepared temporary files.

    Each target is replaced atomically.  The manifest is derived from the
    temporary CSV bytes and replaced last, so a normal write failure cannot
    publish a manifest for a partially written snapshot.
    """

    snapshot, manifest = validate_output_paths(snapshot, manifest)
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    manifest.parent.mkdir(parents=True, exist_ok=True)
    snapshot_tmp: Path | None = None
    manifest_tmp: Path | None = None
    snapshot_backup: Path | None = None
    manifest_backup: Path | None = None
    snapshot_existed = snapshot.exists()
    manifest_existed = manifest.exists()
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", dir=snapshot.parent, delete=False) as stream:
            snapshot_tmp = Path(stream.name)
            df.to_csv(stream, index=False)
            stream.flush()
            os.fsync(stream.fileno())

        manifest_data = build_manifest(
            snapshot=snapshot.resolve(),
            snapshot_sha256=sha256(snapshot_tmp),
            pages=pages,
            validation=validation,
            acquisition=acquisition,
        )
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=manifest.parent, delete=False) as stream:
            manifest_tmp = Path(stream.name)
            json.dump(manifest_data, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())

        if snapshot_existed:
            with tempfile.NamedTemporaryFile(dir=snapshot.parent, delete=False) as stream:
                snapshot_backup = Path(stream.name)
            shutil.copyfile(snapshot, snapshot_backup)
        if manifest_existed:
            with tempfile.NamedTemporaryFile(dir=manifest.parent, delete=False) as stream:
                manifest_backup = Path(stream.name)
            shutil.copyfile(manifest, manifest_backup)

        os.replace(snapshot_tmp, snapshot)
        snapshot_tmp = None
        try:
            os.replace(manifest_tmp, manifest)
            manifest_tmp = None
        except BaseException as publish_error:
            rollback_errors = []
            for target, backup, existed in (
                (snapshot, snapshot_backup, snapshot_existed),
                (manifest, manifest_backup, manifest_existed),
            ):
                try:
                    if existed and backup is not None:
                        os.replace(backup, target)
                        if target == snapshot:
                            snapshot_backup = None
                        else:
                            manifest_backup = None
                    else:
                        target.unlink(missing_ok=True)
                except OSError as rollback_error:
                    rollback_errors.append(rollback_error)
            if rollback_errors:
                raise RuntimeError("Falló la publicación y no se pudo restaurar el par anterior.") from publish_error
            raise
    finally:
        for temporary in (snapshot_tmp, manifest_tmp, snapshot_backup, manifest_backup):
            if temporary is not None:
                temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages", type=int, default=10, help="Páginas TMDB discover a consultar (máximo 500).")
    parser.add_argument("--request-delay", type=float, default=0.1, help="Pausa tras cada registro aceptado de OMDb.")
    parser.add_argument("--min-rows", type=int, default=100)
    parser.add_argument("--min-class-proportion", type=float, default=0.20)
    parser.add_argument("--snapshot", type=Path, default=DEFAULT_SNAPSHOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args(argv)
    if not 1 <= args.pages <= 500:
        parser.error("--pages debe estar entre 1 y 500.")
    try:
        args.snapshot, args.manifest = validate_output_paths(args.snapshot, args.manifest)
    except ValueError as error:
        parser.error(str(error))

    df, acquisition = build_dataframe(pages=args.pages, delay_seconds=args.request_delay)
    validation = validate_dataset(df, min_rows=args.min_rows, min_class_proportion=args.min_class_proportion)
    write_outputs(
        df,
        snapshot=args.snapshot,
        manifest=args.manifest,
        pages=args.pages,
        validation=validation,
        acquisition=acquisition,
    )
    print(f"Snapshot validado: {args.snapshot} ({validation['rows']} filas)")
    print(f"Manifiesto: {args.manifest}")


if __name__ == "__main__":
    main()

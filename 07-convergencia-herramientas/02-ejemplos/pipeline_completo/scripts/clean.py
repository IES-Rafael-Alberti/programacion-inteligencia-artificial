"""
clean.py — Limpieza y validación de datos con Pandera.

Valida esquemas, imputa nulos, elimina duplicados, y reporta calidad.

Uso:
    python clean.py --input data/raw/datos_extraidos.csv --output data/clean/datos_limpios.csv
"""

import argparse
from pathlib import Path
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame


# Esquema de validación para incidencias técnicas
class IncidenciasSchema(pa.DataFrameModel):
    """Esquema esperado para el dataset de incidencias."""

    id_incidencia: int = pa.Field(ge=0, nullable=False)
    titulo: str = pa.Field(nullable=False)
    descripcion: str = pa.Field(nullable=True)
    categoria: str = pa.Field(isin=[
        "red", "database", "security", "application", "hardware", "otros"
    ], nullable=False)
    severidad: str = pa.Field(isin=["baja", "media", "alta", "critica"], nullable=True)
    estado: str = pa.Field(isin=["abierto", "en_progreso", "resuelto", "cerrado"])
    fecha_creacion: str = pa.Field(nullable=False)
    fecha_resolucion: str = pa.Field(nullable=True)
    usuario_asignado: str = pa.Field(nullable=True)


def validate_schema(df: pd.DataFrame) -> pd.DataFrame:
    """Valida el DataFrame contra el esquema y reporta errores."""
    schema = IncidenciasSchema.to_schema()
    try:
        schema.validate(df, lazy=True)
        print("[OK] Validación de esquema superada")
    except pa.errors.SchemaErrors as e:
        print(f"[WARN] Errores de esquema encontrados:\n{e}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza básica del dataset."""
    n_antes = len(df)

    # Eliminar duplicados exactos
    df = df.drop_duplicates(subset=["id_incidencia"])
    dups = n_antes - len(df)
    if dups:
        print(f"[INFO] Eliminados {dups} duplicados")

    # Imputar severidad faltante como 'baja'
    df["severidad"] = df["severidad"].fillna("baja")

    # Imputar usuario asignado desconocido
    df["usuario_asignado"] = df["usuario_asignado"].fillna("no_asignado")

    return df


def report_quality(df: pd.DataFrame) -> dict:
    """Genera reporte de calidad de datos."""
    report = {
        "total_registros": len(df),
        "columnas": list(df.columns),
        "nulos_por_columna": df.isnull().sum().to_dict(),
        "tipos": df.dtypes.astype(str).to_dict(),
        "categorias_unicas": {c: df[c].nunique() for c in df.select_dtypes("object").columns},
    }
    print("\n=== Reporte de Calidad ===")
    for k, v in report.items():
        print(f"  {k}: {v}")
    return report


def main():
    parser = argparse.ArgumentParser(description="Limpieza y validación de datos")
    parser.add_argument("--input", default="data/raw/datos_extraidos.csv")
    parser.add_argument("--output", default="data/clean/datos_limpios.csv")
    parser.add_argument("--report", default="data/clean/quality_report.json")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    print(f"[OK] Cargados {len(df)} registros desde {args.input}")

    df = validate_schema(df)
    df = clean_data(df)
    report = report_quality(df)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"\n[OK] Datos limpios guardados en {args.output}")

    import json
    with open(args.report, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"[OK] Reporte de calidad guardado en {args.report}")


if __name__ == "__main__":
    main()

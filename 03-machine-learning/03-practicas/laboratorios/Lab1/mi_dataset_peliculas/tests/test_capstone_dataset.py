import sys
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from mi_dataset_peliculas.build_capstone_dataset import (
    REPOSITORY_ROOT,
    build_dataframe,
    main,
    sha256,
    validate_dataset,
    write_outputs,
)
from mi_dataset_peliculas.merge import FORBIDDEN_COLUMNS, SCHEMA, capstone_record


class CapstoneDatasetContractTests(unittest.TestCase):
    def frame(self):
        rows = []
        for index in range(10):
            rows.append({
                "release_year": 2000 + index,
                "runtime_minutes": 90 + index,
                "budget_usd": index * 1_000_000,
                "genres": "Drama|Science Fiction",
                "original_language": "en",
                "production_countries_count": 1,
                "production_companies_count": 1,
                "is_collection": index % 2,
                "adult": 0,
                "rating_high": index % 2,
            })
        return pd.DataFrame(rows, columns=SCHEMA).astype(SCHEMA)

    def test_valid_snapshot_reports_rows_and_balance(self):
        result = validate_dataset(self.frame(), min_rows=10, min_class_proportion=0.2)
        self.assertEqual(result["rows"], 10)
        self.assertEqual(result["class_distribution"], {"0": 0.5, "1": 0.5})

    def test_rejects_duplicate_rows(self):
        frame = self.frame()
        frame.iloc[1] = frame.iloc[0]
        with self.assertRaisesRegex(ValueError, "duplicadas"):
            validate_dataset(frame, min_rows=10)

    def test_rejects_columns_with_dtypes_outside_contract(self):
        for column, expected_dtype in SCHEMA.items():
            with self.subTest(column=column, expected_dtype=expected_dtype):
                frame = self.frame()
                if expected_dtype == "int64":
                    frame[column] = frame[column].astype("float64")
                else:
                    frame[column] = frame[column].astype("object")

                with self.assertRaisesRegex(ValueError, rf"{column}.*{expected_dtype}"):
                    validate_dataset(frame, min_rows=10)

    def test_rejects_one_class_and_forbidden_columns(self):
        frame = self.frame()
        frame["rating_high"] = 1
        with self.assertRaisesRegex(ValueError, "dos clases"):
            validate_dataset(frame, min_rows=10)
        self.assertTrue({"imdb_rating", "vote_average", "vote_count", "imdb_id", "tmdb_id"} <= FORBIDDEN_COLUMNS)

    def test_write_outputs_publishes_matching_snapshot_and_manifest(self):
        with tempfile.TemporaryDirectory(dir=REPOSITORY_ROOT) as directory:
            root = Path(directory)
            snapshot = root / "data/movies.csv"
            manifest = root / "movies.manifest.json"

            write_outputs(
                self.frame(),
                snapshot=snapshot,
                manifest=manifest,
                pages=1,
                validation={"rows": 10, "class_distribution": {"0": 0.5, "1": 0.5}},
                acquisition={"tmdb_candidates": 10},
            )

            metadata = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(metadata["snapshot_sha256"], sha256(snapshot))

    def test_write_outputs_restores_both_files_if_manifest_replace_fails(self):
        with tempfile.TemporaryDirectory(dir=REPOSITORY_ROOT) as directory:
            root = Path(directory)
            snapshot = root / "movies.csv"
            manifest = root / "movies.manifest.json"
            snapshot.write_text("old snapshot\n", encoding="utf-8")
            manifest.write_text('{"state": "old manifest"}\n', encoding="utf-8")
            old_snapshot = snapshot.read_bytes()
            old_manifest = manifest.read_bytes()
            real_replace = os.replace
            replacements = 0

            def fail_second_replace(source, target):
                nonlocal replacements
                replacements += 1
                if replacements == 2:
                    raise OSError("simulated manifest replacement failure")
                return real_replace(source, target)

            with patch("mi_dataset_peliculas.build_capstone_dataset.os.replace", side_effect=fail_second_replace):
                with self.assertRaisesRegex(OSError, "simulated manifest"):
                    write_outputs(
                        self.frame(),
                        snapshot=snapshot,
                        manifest=manifest,
                        pages=1,
                        validation={"rows": 10, "class_distribution": {"0": 0.5, "1": 0.5}},
                        acquisition={"tmdb_candidates": 10},
                    )

            self.assertEqual(snapshot.read_bytes(), old_snapshot)
            self.assertEqual(manifest.read_bytes(), old_manifest)

    def test_write_outputs_rejects_snapshot_outside_repository_before_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            snapshot = root / "movies.csv"
            manifest = root / "movies.manifest.json"

            with self.assertRaisesRegex(ValueError, "fuera del repositorio"):
                write_outputs(
                    self.frame(),
                    snapshot=snapshot,
                    manifest=manifest,
                    pages=1,
                    validation={"rows": 10, "class_distribution": {"0": 0.5, "1": 0.5}},
                    acquisition={"tmdb_candidates": 10},
                )

            self.assertFalse(snapshot.exists())
            self.assertFalse(manifest.exists())

    @patch("mi_dataset_peliculas.build_capstone_dataset.build_dataframe")
    def test_cli_rejects_external_snapshot_before_acquisition(self, build_dataframe_mock):
        with tempfile.TemporaryDirectory() as directory:
            snapshot = Path(directory) / "movies.csv"
            with patch("sys.stderr"):
                with self.assertRaises(SystemExit):
                    main(["--snapshot", str(snapshot)])

            build_dataframe_mock.assert_not_called()
            self.assertFalse(snapshot.exists())

    def test_rating_is_only_used_to_derive_label(self):
        tmdb = {
            "release_date": "2018-05-01", "runtime": 110, "budget": 100,
            "genres": [{"name": "Drama"}], "original_language": "en",
            "production_countries": [{"iso_3166_1": "US"}],
            "production_companies": [{"id": 1}], "belongs_to_collection": None,
            "adult": False, "vote_average": 9.9, "vote_count": 12345,
        }
        record = capstone_record(tmdb, {"imdbRating": "7.0"})
        self.assertEqual(record["rating_high"], 1)
        self.assertFalse(set(record) & FORBIDDEN_COLUMNS)

    @patch("mi_dataset_peliculas.config.get_api_keys", return_value=("tmdb-key", "omdb-key"))
    @patch("mi_dataset_peliculas.build_capstone_dataset.OmdbClient")
    @patch("mi_dataset_peliculas.build_capstone_dataset.TmdbClient")
    def test_repeated_tmdb_candidate_across_pages_is_acquired_once(self, tmdb_class, omdb_class, _keys):
        tmdb = tmdb_class.return_value
        tmdb.discover_movies.side_effect = [[{"id": 42}], [{"id": 42}]]
        tmdb.movie_details.return_value = {
            "external_ids": {"imdb_id": "tt0000042"},
            "release_date": "2018-05-01", "runtime": 110, "budget": 100,
            "genres": [{"name": "Drama"}], "original_language": "en",
            "production_countries": [{"iso_3166_1": "US"}],
            "production_companies": [{"id": 1}], "belongs_to_collection": None,
            "adult": False,
        }
        omdb_class.return_value.by_imdb_id.return_value = {"imdbRating": "7.0"}

        frame, stats = build_dataframe(pages=2, delay_seconds=0)

        self.assertEqual(len(frame), 1)
        self.assertEqual(stats["duplicate_tmdb_candidates"], 1)
        tmdb.movie_details.assert_called_once_with(42)

    @patch("mi_dataset_peliculas.config.get_api_keys", return_value=("tmdb-key", "omdb-key"))
    @patch("mi_dataset_peliculas.build_capstone_dataset.OmdbClient")
    @patch("mi_dataset_peliculas.build_capstone_dataset.TmdbClient")
    def test_conflicting_tmdb_ids_for_same_imdb_id_fail_loudly(self, tmdb_class, _omdb_class, _keys):
        tmdb = tmdb_class.return_value
        tmdb.discover_movies.return_value = [{"id": 42}, {"id": 84}]
        tmdb.movie_details.side_effect = [
            {"external_ids": {"imdb_id": "tt0000042"}},
            {"external_ids": {"imdb_id": "tt0000042"}},
        ]

        with self.assertRaisesRegex(ValueError, "imdb_id tt0000042.*TMDB 42.*84"):
            build_dataframe(pages=1, delay_seconds=0)


if __name__ == "__main__":
    unittest.main()

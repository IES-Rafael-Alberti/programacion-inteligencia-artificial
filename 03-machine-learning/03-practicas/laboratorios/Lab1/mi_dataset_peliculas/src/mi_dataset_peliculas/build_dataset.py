"""Build the exploratory Lab1 dataset independently from the capstone."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .merge import merge_tmdb_omdb
from .omdb import get_omdb_data
from .tmdb import get_popular_movies


def build_lab1_dataset(*, pages: int = 1) -> pd.DataFrame:
    """Acquire and merge the small title-based dataset studied in Lab1."""

    candidates = []
    seen_ids = set()
    for page in range(1, pages + 1):
        for movie in get_popular_movies(page=page):
            identity = movie.get("id")
            if identity is not None and identity in seen_ids:
                continue
            if identity is not None:
                seen_ids.add(identity)
            candidates.append(movie)
    return pd.DataFrame(merge_tmdb_omdb(candidates, get_omdb_data))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages", type=int, default=1, help="Páginas de películas populares que se consultarán.")
    parser.add_argument("--output", type=Path, default=Path("data/dataset_peliculas.csv"))
    args = parser.parse_args(argv)
    if args.pages < 1:
        parser.error("--pages debe ser al menos 1.")

    dataframe = build_lab1_dataset(pages=args.pages)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(args.output, index=False)
    print(f"Dataset de Lab1 guardado: {args.output} ({len(dataframe)} filas)")


if __name__ == "__main__":
    main()

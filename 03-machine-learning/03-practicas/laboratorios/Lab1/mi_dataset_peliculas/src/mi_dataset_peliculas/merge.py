"""Transform API responses into the capstone's deliberately small schema."""

from __future__ import annotations

from datetime import date
from typing import Any

SCHEMA: dict[str, str] = {
    "release_year": "int64",
    "runtime_minutes": "int64",
    "budget_usd": "int64",
    "genres": "string",
    "original_language": "string",
    "production_countries_count": "int64",
    "production_companies_count": "int64",
    "is_collection": "int64",
    "adult": "int64",
    "rating_high": "int64",
}

FORBIDDEN_COLUMNS = {"tmdb_id", "imdb_id", "id", "title", "imdb_rating", "vote_average", "vote_count"}
RATING_HIGH_THRESHOLD = 7.0


def merge_tmdb_omdb(
    tmdb_list: list[dict[str, Any]],
    omdb_getter: Any,
) -> list[dict[str, Any]]:
    """Merge TMDB summaries with OMDb title results for the Lab1 exercise.

    Title matching is deliberately retained here because evaluating its
    ambiguity is part of Lab1.  The capstone does not use this function: it
    matches exclusively by IMDb identifier through :func:`capstone_record`.
    """

    result = []
    for movie in tmdb_list:
        title = movie.get("title")
        if not title:
            continue
        omdb = omdb_getter(title)
        if omdb.get("Response") == "True":
            result.append({
                "title": title,
                "release_date": movie.get("release_date"),
                "vote_average": movie.get("vote_average"),
                "runtime": omdb.get("Runtime"),
                "director": omdb.get("Director"),
                "imdb_rating": omdb.get("imdbRating"),
            })
    return result


def capstone_record(tmdb: dict[str, Any], omdb: dict[str, Any]) -> dict[str, Any] | None:
    """Create one record without retaining identifiers or post-release ratings.

    The OMDb rating is used once to derive the label and is never written to the
    snapshot. TMDB vote metrics are neither copied nor used as predictors.
    """

    release_date = tmdb.get("release_date") or ""
    try:
        release_year = int(release_date[:4])
    except (TypeError, ValueError):
        return None

    runtime = tmdb.get("runtime")
    try:
        runtime_minutes = int(runtime)
    except (TypeError, ValueError):
        return None

    try:
        imdb_rating = float(omdb.get("imdbRating"))
    except (TypeError, ValueError):
        return None

    if not 1888 <= release_year <= date.today().year + 1 or not 40 <= runtime_minutes <= 400 or not 0 <= imdb_rating <= 10:
        return None

    genres = sorted({item.get("name", "").strip() for item in tmdb.get("genres", []) if item.get("name")})
    if not genres:
        return None

    return {
        "release_year": release_year,
        "runtime_minutes": runtime_minutes,
        "budget_usd": max(0, int(tmdb.get("budget") or 0)),
        "genres": "|".join(genres),
        "original_language": str(tmdb.get("original_language") or "und").lower(),
        "production_countries_count": len(tmdb.get("production_countries") or []),
        "production_companies_count": len(tmdb.get("production_companies") or []),
        "is_collection": int(tmdb.get("belongs_to_collection") is not None),
        "adult": int(bool(tmdb.get("adult", False))),
        "rating_high": int(imdb_rating >= RATING_HIGH_THRESHOLD),
    }

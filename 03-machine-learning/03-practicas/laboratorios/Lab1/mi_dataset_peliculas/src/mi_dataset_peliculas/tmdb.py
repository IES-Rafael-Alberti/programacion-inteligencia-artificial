"""Small TMDB v3 client used by the teaching dataset pipeline."""

from __future__ import annotations

from typing import Any

import requests

from .config import get_api_keys


def get_popular_movies(
    page: int = 1,
    *,
    session: requests.Session | None = None,
    timeout: int = 30,
) -> list[dict[str, Any]]:
    """Return one TMDB popular-movies page for the Lab1 exercise.

    This intentionally keeps the small function-based API used in Lab1.  The
    capstone uses :class:`TmdbClient` below and has a separate data contract.
    """

    tmdb_key, _ = get_api_keys()
    requester = session or requests.Session()
    response = requester.get(
        f"{TmdbClient.BASE_URL}/movie/popular",
        params={"api_key": tmdb_key, "language": "es-ES", "page": page},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()["results"]


class TmdbClient:
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, api_key: str, *, session: requests.Session | None = None, timeout: int = 30) -> None:
        self.api_key = api_key
        self.session = session or requests.Session()
        self.timeout = timeout

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        response = self.session.get(
            f"{self.BASE_URL}{path}",
            params={"api_key": self.api_key, **params},
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response.json()

    def discover_movies(self, page: int) -> list[dict[str, Any]]:
        payload = self._get(
            "/discover/movie",
            language="en-US",
            sort_by="popularity.desc",
            include_adult="false",
            include_video="false",
            page=page,
        )
        return payload.get("results", [])

    def movie_details(self, tmdb_id: int) -> dict[str, Any]:
        # append_to_response avoids a second request while keeping the TMDB id
        # internal to the acquisition process.
        return self._get(f"/movie/{tmdb_id}", language="en-US", append_to_response="external_ids")

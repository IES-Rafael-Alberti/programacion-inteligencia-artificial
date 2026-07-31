"""OMDb client.  Matching is intentionally restricted to IMDb identifiers."""

from __future__ import annotations

from typing import Any

import requests

from .config import get_api_keys


def get_omdb_data(
    title: str,
    *,
    session: requests.Session | None = None,
    timeout: int = 30,
) -> dict[str, Any]:
    """Look up a title for the exploratory Lab1 merge exercise."""

    _, omdb_key = get_api_keys()
    requester = session or requests.Session()
    response = requester.get(
        "https://www.omdbapi.com/",
        params={"apikey": omdb_key, "t": title, "type": "movie"},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


class OmdbClient:
    BASE_URL = "https://www.omdbapi.com/"

    def __init__(self, api_key: str, *, session: requests.Session | None = None, timeout: int = 30) -> None:
        self.api_key = api_key
        self.session = session or requests.Session()
        self.timeout = timeout

    def by_imdb_id(self, imdb_id: str) -> dict[str, Any] | None:
        response = self.session.get(
            self.BASE_URL,
            params={"apikey": self.api_key, "i": imdb_id, "type": "movie"},
            timeout=self.timeout,
        )
        response.raise_for_status()
        payload = response.json()
        return payload if payload.get("Response") == "True" else None

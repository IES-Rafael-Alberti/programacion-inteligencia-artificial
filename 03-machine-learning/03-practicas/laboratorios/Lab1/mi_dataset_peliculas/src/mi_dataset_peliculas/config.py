"""Local configuration for movie-data API clients.

Secrets are deliberately read only when an API request is about to be made, so
unit tests and schema validation never need credentials.
"""

from __future__ import annotations

import os


def get_api_keys() -> tuple[str, str]:
    """Return the locally configured TMDB and OMDb credentials.

    ``.env`` is local and ignored by git.  Do not put values in source files,
    notebooks, manifests, terminal captures, or issue reports.
    """

    # Import lazily so schema-only validation works without the API feature.
    from dotenv import load_dotenv

    load_dotenv()
    tmdb_key = os.getenv("TMDB_API_KEY")
    omdb_key = os.getenv("OMDB_API_KEY")
    missing = [name for name, value in (("TMDB_API_KEY", tmdb_key), ("OMDB_API_KEY", omdb_key)) if not value]
    if missing:
        raise RuntimeError(
            "Faltan claves API locales: "
            + ", ".join(missing)
            + ". Crea un archivo .env local; consulta .env.example."
        )
    return tmdb_key, omdb_key

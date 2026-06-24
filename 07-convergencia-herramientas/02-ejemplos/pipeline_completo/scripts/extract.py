"""
extract.py — Extracción de datos multi-fuente para el pipeline ML.

Soporta:
- CSV local
- API REST (fallback a CSV si no hay conexión)
- Logs estructurados

Uso:
    python extract.py --source csv --path datos_incidencias.csv
    python extract.py --source api --url https://api.example.com/tickets
"""

import argparse
import json
from pathlib import Path
from typing import Optional
import pandas as pd
import requests


def extract_csv(path: str) -> pd.DataFrame:
    """Extrae datos desde un archivo CSV."""
    if not Path(path).exists():
        raise FileNotFoundError(f"No se encuentra el archivo: {path}")
    return pd.read_csv(path)


def extract_api(url: str, params: Optional[dict] = None) -> pd.DataFrame:
    """Extrae datos desde una API REST."""
    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list):
            return pd.DataFrame(data)
        if isinstance(data, dict) and "results" in data:
            return pd.DataFrame(data["results"])
        return pd.DataFrame([data])
    except requests.RequestException as e:
        print(f"[WARN] API no disponible ({e}), usando CSV de respaldo")
        return extract_csv("data/respaldo_incidencias.csv")


def extract_logs(path: str) -> pd.DataFrame:
    """Extrae y parsea logs estructurados (formato JSONL)."""
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return pd.DataFrame(records)


def main():
    parser = argparse.ArgumentParser(description="Extracción de datos para pipeline ML")
    parser.add_argument("--source", choices=["csv", "api", "logs"], default="csv")
    parser.add_argument("--path", default="data/incidencias.csv")
    parser.add_argument("--url", default=None)
    parser.add_argument("--output", default="data/raw/datos_extraidos.csv")
    args = parser.parse_args()

    if args.source == "csv":
        df = extract_csv(args.path)
    elif args.source == "api":
        df = extract_api(args.url or "http://localhost:8000/tickets")
    elif args.source == "logs":
        df = extract_logs(args.path)
    else:
        raise ValueError(f"Fuente no soportada: {args.source}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"[OK] Extraídos {len(df)} registros desde {args.source} → {args.output}")


if __name__ == "__main__":
    main()

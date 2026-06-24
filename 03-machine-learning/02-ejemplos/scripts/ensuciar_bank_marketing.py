"""Introduce nulos y outliers en el CSV original para practicar limpieza."""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def make_dirty(input_path: Path, output_path: Path, random_state=42) -> None:
    df = pd.read_csv(input_path, sep=';')
    rng = np.random.default_rng(random_state)

    # Introduce missing values en columnas numéricas y categóricas
    for col in ['age', 'balance', 'job', 'marital']:
        if col in df.columns:
            mask = rng.choice(df.index, size=int(0.02 * len(df)), replace=False)
            df.loc[mask, col] = np.nan

    # Introduce outliers en balance y campaign
    if 'balance' in df.columns:
        mask = rng.choice(df.index, size=int(0.01 * len(df)), replace=False)
        df.loc[mask, 'balance'] = df.loc[mask, 'balance'].fillna(0) * 10

    if 'campaign' in df.columns:
        mask = rng.choice(df.index, size=int(0.01 * len(df)), replace=False)
        df.loc[mask, 'campaign'] = df.loc[mask, 'campaign'].fillna(0) * 20

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, sep=';', index=False)
    print(f"Archivo sucio generado en {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description='Genera una versión con nulos/outliers del dataset Bank Marketing.')
    parser.add_argument('input_csv', type=Path, help='Ruta al CSV original (bank-additional-full.csv)')
    parser.add_argument('--output', type=Path, default=Path('datos/bank-additional-full-dirty.csv'))
    parser.add_argument('--random-state', type=int, default=42)
    args = parser.parse_args()

    if not args.input_csv.exists():
        raise FileNotFoundError(f"No se encontró el CSV original en {args.input_csv}")

    make_dirty(args.input_csv, args.output, random_state=args.random_state)


if __name__ == '__main__':
    main()

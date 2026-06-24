"""
split.py — División train/test estratificada para pipelines ML.

Uso:
    python split.py --input data/features/features.parquet --output data/split/
"""

import argparse
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


def stratified_split(
    df: pd.DataFrame,
    target_col: str = "categoria_encoded",
    test_size: float = 0.2,
    val_size: float = 0.1,
    random_state: int = 42,
) -> tuple:
    """
    Divide en train/val/test con estratificación.

    Returns:
        (train_df, val_df, test_df)
    """
    # Primero: separar test
    train_val, test = train_test_split(
        df,
        test_size=test_size,
        stratify=df[target_col],
        random_state=random_state,
    )

    # Segundo: separar val de train
    val_frac = val_size / (1 - test_size)
    train, val = train_test_split(
        train_val,
        test_size=val_frac,
        stratify=train_val[target_col],
        random_state=random_state,
    )

    return train, val, test


def split_by_date(
    df: pd.DataFrame,
    date_col: str = "fecha_creacion",
    train_cutoff: str = "2025-09-01",
    val_cutoff: str = "2025-11-01",
) -> tuple:
    """
    División temporal (para evitar data leakage).
    """
    df[date_col] = pd.to_datetime(df[date_col])
    train = df[df[date_col] < train_cutoff]
    val = df[(df[date_col] >= train_cutoff) & (df[date_col] < val_cutoff)]
    test = df[df[date_col] >= val_cutoff]
    return train, val, test


def main():
    parser = argparse.ArgumentParser(description="División train/val/test")
    parser.add_argument("--input", default="data/features/features.parquet")
    parser.add_argument("--output", default="data/split/")
    parser.add_argument("--method", choices=["random", "temporal"], default="random")
    parser.add_argument("--target", default="categoria_encoded")
    args = parser.parse_args()

    df = pd.read_parquet(args.input)
    print(f"[OK] Cargados {len(df)} registros desde {args.input}")

    if args.method == "temporal":
        train, val, test = split_by_date(df)
    else:
        train, val, test = stratified_split(df, target_col=args.target)

    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    train.to_parquet(output_path / "train.parquet", index=False)
    val.to_parquet(output_path / "val.parquet", index=False)
    test.to_parquet(output_path / "test.parquet", index=False)

    print(f"\n[OK] División completada:")
    print(f"  Train: {len(train)} ({len(train)/len(df)*100:.1f}%)")
    print(f"  Val:   {len(val)} ({len(val)/len(df)*100:.1f}%)")
    print(f"  Test:  {len(test)} ({len(test)/len(df)*100:.1f}%)")
    print(f"\n  Guardado en: {output_path.resolve()}")


if __name__ == "__main__":
    main()

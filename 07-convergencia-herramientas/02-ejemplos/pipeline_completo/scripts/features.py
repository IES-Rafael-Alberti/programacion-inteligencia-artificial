"""
features.py — Ingeniería de características para clasificación de incidencias.

Genera:
- TF-IDF sobre texto (título + descripción)
- Codificación de variables categóricas
- Features temporales

Uso:
    python features.py --input data/clean/datos_limpios.csv --output data/features/features.parquet
"""

import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import joblib


def engineer_text_features(df: pd.DataFrame, max_features: int = 500) -> pd.DataFrame:
    """Extrae features TF-IDF del texto combinado (título + descripción)."""
    # Combinar texto
    df["texto_completo"] = df["titulo"].fillna("")
    if "descripcion" in df.columns:
        df["texto_completo"] += " " + df["descripcion"].fillna("")

    # Vectorizar
    vectorizer = TfidfVectorizer(
        max_features=max_features,
        stop_words="english",
        ngram_range=(1, 2),
    )
    tfidf_matrix = vectorizer.fit_transform(df["texto_completo"])

    # Crear DataFrame con features
    feature_names = [f"tfidf_{w}" for w in vectorizer.get_feature_names_out()]
    tfidf_df = pd.DataFrame(
        tfidf_matrix.toarray(),
        columns=feature_names,
        index=df.index,
    )

    # Guardar vectorizer para usar en inferencia
    joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
    print(f"[OK] Generadas {len(feature_names)} features TF-IDF")

    return pd.concat([df, tfidf_df], axis=1)


def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """Codifica variables categóricas como numéricas."""
    cat_cols = ["categoria", "severidad", "estado"]
    encoders = {}

    for col in cat_cols:
        if col in df.columns:
            le = LabelEncoder()
            df[f"{col}_encoded"] = le.fit_transform(df[col].astype(str))
            encoders[col] = le

    joblib.dump(encoders, "models/label_encoders.pkl")
    print(f"[OK] Codificadas {len(cat_cols)} variables categóricas")
    return df


def engineer_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    """Extrae features de fechas."""
    if "fecha_creacion" not in df.columns:
        return df

    df["fecha_creacion"] = pd.to_datetime(df["fecha_creacion"], errors="coerce")
    df["dia_semana"] = df["fecha_creacion"].dt.dayofweek
    df["mes"] = df["fecha_creacion"].dt.month
    df["hora"] = df["fecha_creacion"].dt.hour
    df["es_fin_semana"] = df["dia_semana"].isin([5, 6]).astype(int)

    if "fecha_resolucion" in df.columns:
        df["fecha_resolucion"] = pd.to_datetime(df["fecha_resolucion"], errors="coerce")
        df["tiempo_resolucion_horas"] = (
            df["fecha_resolucion"] - df["fecha_creacion"]
        ).dt.total_seconds() / 3600

    print(f"[OK] Generadas features temporales")
    return df


def main():
    parser = argparse.ArgumentParser(description="Ingeniería de características")
    parser.add_argument("--input", default="data/clean/datos_limpios.csv")
    parser.add_argument("--output", default="data/features/features.parquet")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    print(f"[OK] Cargados {len(df)} registros desde {args.input}")

    df = engineer_text_features(df)
    df = encode_categorical(df)
    df = engineer_temporal_features(df)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(args.output, index=False)
    print(f"[OK] Features guardadas en {args.output}")


if __name__ == "__main__":
    main()

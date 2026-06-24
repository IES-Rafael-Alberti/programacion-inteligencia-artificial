"""
Script de exportación de modelos para la mini API NLP.

Qué exporta:
- TF-IDF + modelo clásico -> joblib
- LSTM + tokenizer -> .keras + .json

Uso recomendado:
1. Entrena tus modelos en un notebook.
2. Llama a las funciones de este script para guardarlos.
3. Copia los archivos generados a la carpeta `models/` de la API.

Ejemplo rápido:

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf

texts = ["me encanta este curso", "odio este producto", "me gusta mucho", "no me gusta nada"]
labels = [1, 0, 1, 0]

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
clf = LogisticRegression()
clf.fit(X, labels)

export_tfidf_assets(vectorizer, clf)

# LSTM
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
seq = tokenizer.texts_to_sequences(texts)
X_pad = pad_sequences(seq, maxlen=10, padding="post", truncating="post")

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=1000, output_dim=16, input_length=10),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_pad, labels, epochs=5, verbose=0)

export_lstm_assets(model, tokenizer)
"""

from __future__ import annotations

from pathlib import Path
import json
import shutil
from typing import Any

import joblib


DEFAULT_OUTPUT_DIR = Path("exported_models")


def ensure_dir(output_dir: str | Path = DEFAULT_OUTPUT_DIR) -> Path:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def export_tfidf_assets(vectorizer: Any, model: Any, output_dir: str | Path = DEFAULT_OUTPUT_DIR) -> tuple[Path, Path]:
    """
    Guarda vectorizador TF-IDF y modelo clásico en formato joblib.
    """
    out = ensure_dir(output_dir)
    vectorizer_path = out / "tfidf_vectorizer.joblib"
    model_path = out / "tfidf_model.joblib"

    joblib.dump(vectorizer, vectorizer_path)
    joblib.dump(model, model_path)

    print(f"[OK] TF-IDF vectorizer guardado en: {vectorizer_path}")
    print(f"[OK] Modelo TF-IDF guardado en: {model_path}")
    return vectorizer_path, model_path


def export_lstm_assets(model: Any, tokenizer: Any, output_dir: str | Path = DEFAULT_OUTPUT_DIR) -> tuple[Path, Path]:
    """
    Guarda modelo LSTM en formato .keras y tokenizer en JSON.
    """
    out = ensure_dir(output_dir)
    model_path = out / "lstm_model.keras"
    tokenizer_path = out / "lstm_tokenizer.json"

    model.save(model_path)

    tokenizer_json = tokenizer.to_json()
    tokenizer_path.write_text(tokenizer_json, encoding="utf-8")

    print(f"[OK] Modelo LSTM guardado en: {model_path}")
    print(f"[OK] Tokenizer LSTM guardado en: {tokenizer_path}")
    return model_path, tokenizer_path


def export_label_mapping(label_mapping: dict[Any, Any], output_dir: str | Path = DEFAULT_OUTPUT_DIR) -> Path:
    """
    Guarda un mapping opcional de etiquetas.
    Útil si en vez de 0/1 quieres luego mostrar etiquetas como positivo/negativo.
    """
    out = ensure_dir(output_dir)
    mapping_path = out / "label_mapping.json"
    mapping_path.write_text(json.dumps(label_mapping, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Label mapping guardado en: {mapping_path}")
    return mapping_path


def copy_to_api_models(export_dir: str | Path = DEFAULT_OUTPUT_DIR, api_models_dir: str | Path = "models") -> None:
    """
    Copia los archivos exportados a la carpeta models/ de la mini API.
    """
    src = Path(export_dir)
    dst = Path(api_models_dir)
    dst.mkdir(parents=True, exist_ok=True)

    if not src.exists():
        raise FileNotFoundError(f"No existe el directorio de exportación: {src}")

    copied = 0
    for file_path in src.iterdir():
        if file_path.is_file():
            shutil.copy2(file_path, dst / file_path.name)
            copied += 1
            print(f"[OK] Copiado: {file_path.name} -> {dst / file_path.name}")

    print(f"[OK] Total archivos copiados: {copied}")


def export_all(
    *,
    tfidf_vectorizer: Any | None = None,
    tfidf_model: Any | None = None,
    lstm_model: Any | None = None,
    lstm_tokenizer: Any | None = None,
    label_mapping: dict[Any, Any] | None = None,
    output_dir: str | Path = DEFAULT_OUTPUT_DIR,
) -> None:
    """
    Exportación combinada.
    Exporta solo los artefactos que reciba.
    """
    if tfidf_vectorizer is not None and tfidf_model is not None:
        export_tfidf_assets(tfidf_vectorizer, tfidf_model, output_dir=output_dir)

    if lstm_model is not None and lstm_tokenizer is not None:
        export_lstm_assets(lstm_model, lstm_tokenizer, output_dir=output_dir)

    if label_mapping is not None:
        export_label_mapping(label_mapping, output_dir=output_dir)

    print("[OK] Exportación completada.")


if __name__ == "__main__":
    print(
        "Este script está pensado para importarse desde un notebook.\n"
        "Ejemplo:\n"
        "from export_models import export_tfidf_assets, export_lstm_assets\n"
    )

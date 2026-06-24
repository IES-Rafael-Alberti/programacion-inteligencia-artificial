#!/usr/bin/env python3
"""
Demo: Embeddings con SVD y PMI (sin redes neuronales)
Para demostrar a alumnos cómo se pueden crear embeddings sin deep learning.
"""

import numpy as np
from collections import defaultdict
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def build_vocabulary(corpus):
    """Construir vocabulario con índice."""
    vocab = {}
    for sentence in corpus:
        for word in sentence.lower().split():
            if word not in vocab:
                vocab[word] = len(vocab)
    return vocab

def build_cooccurrence_matrix(corpus, vocab, window_size=2):
    """Construir matriz de co-ocurrencia."""
    n = len(vocab)
    cooc = np.zeros((n, n))
    
    for sentence in corpus:
        words = sentence.lower().split()
        for i, word1 in enumerate(words):
            start = max(0, i - window_size)
            end = min(len(words), i + window_size + 1)
            for j in range(start, end):
                if i != j:
                    word2 = words[j]
                    cooc[vocab[word1]][vocab[word2]] += 1
    
    return cooc

def compute_pmi(cooc):
    """Calcular PMI (Pointwise Mutual Information)."""
    total = cooc.sum()
    row_sums = cooc.sum(axis=1, keepdims=True)
    col_sums = cooc.sum(axis=0, keepdims=True)
    
    expected = (row_sums * col_sums) / total
    pmi = np.log2(np.maximum(cooc, 1) / np.maximum(expected, 1e-10))
    
    pmi = np.maximum(pmi, 0)
    
    return pmi

def get_embeddings(pmi, vocab, n_components=10):
    """Extraer embeddings usando SVD."""
    svd = TruncatedSVD(n_components=n_components, random_state=42)
    embeddings = svd.fit_transform(pmi)
    
    idx_to_word = {v: k for k, v in vocab.items()}
    
    return embeddings, idx_to_word

def visualize_embeddings(embeddings, idx_to_word, method='pca'):
    """Visualizar embeddings en 2D."""
    try:
        if method == 'pca':
            from sklearn.decomposition import PCA
            reducer = PCA(n_components=2, random_state=42)
        else:
            reducer = TSNE(n_components=2, random_state=42, perplexity=min(5, len(idx_to_word)-1))
        
        coords = reducer.fit_transform(embeddings)
        
        plt.figure(figsize=(10, 8))
        for idx, word in idx_to_word.items():
            plt.scatter(coords[idx, 0], coords[idx, 1], s=100)
            plt.annotate(word, (coords[idx, 0], coords[idx, 1]), fontsize=12)
        
        plt.title(f'Embeddings 2D ({method.upper()})')
        plt.savefig(f'embeddings_{method}.png', dpi=150, bbox_inches='tight')
        plt.show()
        print(f"Visualización guardada en: embeddings_{method}.png")
    except Exception as e:
        print(f"\nVisualización 2D ({method}):")
        print(f"  (Para ver gráficos, ejecuta en entorno con matplotlib)")
        print(f"  Coords 2D aprox:")
        coords_2d = embeddings[:, :2]
        for idx, word in idx_to_word.items():
            print(f"    {word}: ({coords_2d[idx, 0]:.2f}, {coords_2d[idx, 1]:.2f})")

def main():
    corpus = [
        "el gato come pescado",
        "el gato duerme en el sofa",
        "el perro corre en el parque",
        "el perro ladra al gato",
        "la gata cuida sus gatitos",
        "el humano alimenta al gato",
        "el humano pasea al perro",
        "el pescado es alimento del gato",
        "el sofa es lugar de descanso",
        "el parque es lugar para correr",
        "gatitos juegan con el gato",
        "humano es amigo del perro",
        "gato y perro son mascotas",
        "comida del perro esta en el plato",
        "cama del gato esta en el sofa",
    ]
    
    print("=" * 60)
    print("DEMO: Embeddings sin Redes Neuronales (SVD + PMI)")
    print("=" * 60)
    
    vocab = build_vocabulary(corpus)
    print(f"\n1. Vocabulario ({len(vocab)} palabras):")
    print(f"   {vocab}")
    
    cooc = build_cooccurrence_matrix(corpus, vocab)
    print(f"\n2. Matriz de co-ocurrencia ({cooc.shape}):")
    print(f"   (filas y columnas = palabras)")
    
    pmi = compute_pmi(cooc)
    print(f"\n3. PMI aplicado:")
    print(f"   (valores más altos = mayor asociación)")
    
    embeddings, idx_to_word = get_embeddings(pmi, vocab, n_components=min(10, len(vocab)-1))
    print(f"\n4. Embeddings extraídos con SVD:")
    print(f"   Dimensión: {embeddings.shape}")
    
    print("\n5. Embeddings por palabra (primeros 3 componentes):")
    for idx, word in idx_to_word.items():
        print(f"   {word}: {embeddings[idx][:3].round(3)}")
    
    print("\n6. Visualizando con PCA y t-SNE...")
    visualize_embeddings(embeddings, idx_to_word, 'pca')
    visualize_embeddings(embeddings, idx_to_word, 'tsne')
    
    print("\n7. Semejanza entre palabras (coseno):")
    def cosine_sim(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    pairs = [
        ("gato", "perro"),
        ("gato", "gatitos"),
        ("gato", "pescado"),
        ("perro", "parque"),
        ("sof", "descanso"),
    ]
    
    for w1, w2 in pairs:
        if w1 in vocab and w2 in vocab:
            sim = cosine_sim(embeddings[vocab[w1]], embeddings[vocab[w2]])
            print(f"   '{w1}' vs '{w2}': {sim:.3f}")

if __name__ == "__main__":
    main()

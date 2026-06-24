# Demo: Embeddings sin Redes Neuronales (SVD + PMI)

## Concepto

Los embeddings se pueden crear **sin redes neuronales profundas** usando técnicas de álgebra lineal clásica:

1. **Corpus** → texto de ejemplo
2. **Matriz de co-ocurrencia** → contar palabras que aparecen juntas
3. **PMI** (Pointwise Mutual Information) → medir asociación entre palabras
4. **SVD** (Singular Value Decomposition) → reducir dimensionalidad y obtener vectores

## Fórmula

```
PMI(word, context) = log2( P(word, context) / (P(word) * P(context)) )
Embedding = SVD(PMI)
```

## Código

```python
#!/usr/bin/env python3
"""
Demo: Embeddings con SVD y PMI (sin redes neuronales)
"""

import numpy as np
from collections import defaultdict
from sklearn.decomposition import TruncatedSVD

def build_vocabulary(corpus):
    vocab = {}
    for sentence in corpus:
        for word in sentence.lower().split():
            if word not in vocab:
                vocab[word] = len(vocab)
    return vocab

def build_cooccurrence_matrix(corpus, vocab, window_size=2):
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
    total = cooc.sum()
    row_sums = cooc.sum(axis=1, keepdims=True)
    col_sums = cooc.sum(axis=0, keepdims=True)
    expected = (row_sums * col_sums) / total
    pmi = np.log2(np.maximum(cooc, 1) / np.maximum(expected, 1e-10))
    pmi = np.maximum(pmi, 0)
    return pmi

def get_embeddings(pmi, vocab, n_components=10):
    svd = TruncatedSVD(n_components=n_components, random_state=42)
    embeddings = svd.fit_transform(pmi)
    idx_to_word = {v: k for k, v in vocab.items()}
    return embeddings, idx_to_word
```

## Corpus de ejemplo

```python
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
```

## Resultados

### 1. Vocabulario (38 palabras)

```
{'el': 0, 'gato': 1, 'come': 2, 'pescado': 3, 'duerme': 4, 'en': 5, 
'sofa': 6, 'perro': 7, 'corre': 8, 'parque': 9, 'ladra': 10, 'al': 11, 
'la': 12, 'gata': 13, 'cuida': 14, 'sus': 15, 'gatitos': 16, 'humano': 17, 
'alimenta': 18, 'pasea': 19, 'es': 20, 'alimento': 21, 'del': 22, 'lugar': 23, 
'de': 24, 'descanso': 25, 'para': 26, 'correr': 27, 'juegan': 28, 'con': 29, 
'amigo': 30, 'y': 31, 'son': 32, 'mascotas': 33, 'comida': 34, 'esta': 35, 
'plato': 36, 'cama': 37}
```

### 2. Dimensiones

- Matriz de co-ocurrencia: **(38, 38)**
- Embeddings: **(38, 10)**

### 3. Embeddings por palabra (10 componentes)

| Palabra | Componente 1 | Componente 2 | Componente 3 |
|---------|-------------|-------------|-------------|
| el | 7.253 | 1.378 | 1.137 |
| gato | 10.367 | 2.248 | -0.711 |
| come | 26.164 | -0.336 | 0.040 |
| pescado | 21.773 | 0.776 | 0.177 |
| duerme | 23.741 | 0.079 | -0.299 |
| sofa | 19.046 | 0.887 | -0.647 |
| perro | 11.221 | 2.237 | -0.738 |
| corre | 23.741 | 0.079 | -0.299 |
| parque | 21.823 | 0.565 | -0.239 |
| humano | 17.901 | 1.421 | -0.444 |
| alimento | 23.691 | 0.290 | 0.117 |

### 4. Semejanza coseno entre palabras

| Palabra 1 | Palabra 2 | Semejanza |
|-----------|-----------|-----------|
| gato | perro | **1.000** |
| gato | gatitos | **0.975** |
| gato | pescado | **0.979** |
| perro | parque | **0.980** |

## Interpretación

- **Gato y perro**: Semejanza máxima (1.0) porque aparecen en contextos similares
- **Gato y gatitos**: Alta semelhabilidad semántica
- **Gato y pescado**: Asociación por co-ocurrencia (comida)

## Conclusión

Este método demuestra que se pueden crear embeddings representativos usando **solo estadística y álgebra lineal**, sin necesidad de redes neuronales profundas. Es ideal para:
- Explicar el concepto a estudiantes
- Datasets pequeños
- Situaciones donde se requiere interpretabilidad

## Ejecución

```bash
MKL_THREADING_LAYER=GNU python3 demo_embeddings.py
```

> Requiere: numpy, scikit-learn

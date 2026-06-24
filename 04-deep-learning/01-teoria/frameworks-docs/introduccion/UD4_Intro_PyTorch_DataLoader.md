# Introducción a PyTorch - Datasets y DataLoader

En PyTorch, la forma recomendada de manejar datos es mediante las clases `Dataset` y `DataLoader`.

- `torch.utils.data.Dataset`: representa una colección de datos y debe implementar `__len__` y `__getitem__`.
- `torch.utils.data.DataLoader`: itera sobre un `Dataset` y soporta batching, shuffling y múltiples procesos de lectura.

Ejemplo: `NumpyDataset` que envuelve arrays NumPy.

```python
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

class NumpyDataset(Dataset):
    def __init__(self, X, y=None):
        self.X = X
        self.y = y
    def __len__(self):
        return len(self.X)
    def __getitem__(self, idx):
        if self.y is None:
            return self.X[idx]
        return self.X[idx], self.y[idx]

# Uso
X = np.random.randn(100, 16)
y = np.random.randint(0, 2, size=(100,))
nd = NumpyDataset(X, y)
loader = DataLoader(nd, batch_size=16, shuffle=True)
for xb, yb in loader:
    xb = torch.from_numpy(xb).float()
    yb = torch.from_numpy(yb).long()
    # entrenar paso
```

Collate functions: cuando los ejemplos tienen tamaños variables, use `collate_fn` para controlar cómo agruparlos en batches.

Ejemplo de `pad_collate` para secuencias variables:

```python
import numpy as np
import torch
from torch.nn.utils.rnn import pad_sequence

def pad_collate(batch):
    """Batch is a list of (seq, label) where seq is a 1D numpy array."""
    seqs, labels = zip(*batch)
    seqs = [torch.from_numpy(s).float() for s in seqs]
    labels = torch.tensor(labels)
    seqs_padded = pad_sequence(seqs, batch_first=True)
    lengths = torch.tensor([len(s) for s in seqs])
    return seqs_padded, lengths, labels

# Uso con DataLoader
# loader = DataLoader(dataset, batch_size=4, collate_fn=pad_collate)
```

Con esto puedes construir pipelines robustos tanto para entrada fija como variable.
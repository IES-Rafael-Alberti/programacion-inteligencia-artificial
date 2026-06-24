# Poda de Redes Neuronales en PyTorch

## Conceptos

### Unstructured vs Structured Sparsity

| Tipo | Descripción | Ventaja | Desventaja |
|------|-------------|---------|------------|
| **Unstructured** | Ceros distribuidos aleatoriamente | Mayor flexibilidad, mejor compresión teórica | Sin aceleración GPU |
| **2:4 Structured** | 2 de cada 4 elementos son cero | Soporte hardware nativo, ~2x speedup | Menos flexible |

### N:M Sparsity
Patrón regular donde en cada bloque de M elementos, N son cero:
- **2:4 sparsity**: 50% de sparsity, 2x throughput en NVIDIA Ampere+
- Soportado en GPUs A100, H100 y posteriores

---

## PyTorch básico (unstructured)

```python
import torch.nn.utils.prune as prune

# Podar 30% de conexiones por magnitud L1
prune.l1_unstructured(model.layer, name='weight', amount=0.3)

# Podar canales enteros (structured)
prune.ln_structured(model.layer, name='weight', amount=0.5, n=2, dim=0)

# Poda aleatoria
prune.random_unstructured(model.layer, name='weight', amount=0.3)

# Hacer la poda permanente
prune.remove(model.layer, 'weight')
```

### Métodos disponibles en `torch.nn.utils.prune`
- `random_unstructured` / `random_structured`
- `l1_unstructured`
- `ln_structured`
- `global_unstructured`

---

## 2:4 Sparsity con ModelOpt (NVIDIA)

```python
import modelopt.torch.sparsity as mts
from transformers import AutoModelForCausalLM

# Cargar modelo
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3-8b")

# Aplicar 2:4 sparsity
mts.sparsify(model, mts.SparsityConfig())

# Guardar modelo disperso
model.save_pretrained("model-2-4-sparse")
```

---

## Transformar Unstructured a 2:4

```python
from modelopt.torch.sparsity import transform_unstructured_to_semistructured

# Convertir modelo ya podado al formato 2:4
transform_unstructured_to_semistructured(model, sparsity=0.5)
```

---

## Herramientas relacionadas

| Herramienta | Uso |
|-------------|-----|
| `torch.nn.utils.prune` | Poda básica en PyTorch |
| `modelopt.torch.sparsity` | 2:4 sparsity con NVIDIA |
| `torchao` | Kernels optimizados en PyTorch |
| `cuSPARSELt` / `CUTLASS` | APIs de NVIDIA para sparsity |
| NVIDIA ASP | Automatic SParsity library |
| SparseGPT | Poda data-driven para LLMs |

---

## Recursos

- [PyTorch Blog: Why 2:4 Sparsity Matters (2025)](https://pytorch.org/blog/when-quantization-isnt-enough-why-24-sparsity-matters/)
- [The Lottery Ticket Hypothesis (ICLR 2019)](https://arxiv.org/abs/1803.03635)
- [SparseGPT (arXiv:2302.11695)](https://arxiv.org/abs/2302.11695)

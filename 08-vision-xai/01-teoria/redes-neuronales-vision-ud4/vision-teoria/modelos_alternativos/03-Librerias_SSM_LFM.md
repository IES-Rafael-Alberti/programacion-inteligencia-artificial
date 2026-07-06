# Librerías y herramientas para LFMs, Mamba y SSMs
## Uso de implementaciones existentes vs. implementaciones didácticas

---

## 1. Resumen de opciones disponibles

### Mamba / SSM

| Librería | Descripción | Instalación |
|----------|-------------|-------------|
| **mamba-ssm** | Paquete oficial con kernels CUDA optimizados | `pip install mamba-ssm` |
| **mambapy** | Implementación pura en PyTorch (más legible) | `pip install mambapy` |
| **transformers** | Integración oficial en Hugging Face | `pip install transformers` |
| **mamba3-minimal** | Implementación pura de Mamba-3 | GitHub |

### Liquid Foundation Models (LFM)

| Librería | Descripción | Instalación |
|----------|-------------|-------------|
| **transformers** | Integración oficial LFM2 en Hugging Face | `pip install transformers>=4.57` |
| **lfm2** | Implementación mínima en PyPI | `pip install lfm2` |
| **lfm-torch** | Implementación comunitaria | `pip install lfm-torch` |

---

## 2. Usar Mamba con Hugging Face Transformers

### Instalación

```bash
pip install transformers torch
```

Opcional (para kernels rápidos):
```bash
pip install mamba-ssm causal-conv1d
```

### Cargar modelo pre-entrenado

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "state-spaces/mamba-370m"  # Disponible: 130m, 370m, 790m, 1.4b, 2.8b
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
```

### Inferencia

```python
input_text = "The future of AI is"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

output = model.generate(**inputs, max_new_tokens=50, temperature=0.8)
print(tokenizer.decode(output[0]))
```

### Fine-tuning

```python
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./mamba-finetuned",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    learning_rate=1e-4,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)
trainer.train()
```

---

## 3. Usar Mamba con mambapy (implementación pura PyTorch)

### Instalación

```bash
pip install mambapy
```

### Uso básico

```python
import torch
from mambapy.mamba import Mamba, MambaConfig

# Configuración
config = MambaConfig(
    d_model=256,      # Dimensión del modelo
    n_layers=12,      # Número de capas
    d_state=16,        # Estado SSM
    d_conv=4,         # Ancho de convolución
)

model = Mamba(config)

# Forward pass
batch_size, seq_len = 4, 128
x = torch.randint(0, 32000, (batch_size, seq_len))
logits = model(x)  # (batch, seq_len, vocab_size)
```

### Modelo completo de lenguaje

```python
from mambapy.lm import MambaLM, MambaLMConfig

config = MambaLMConfig(
    vocab_size=32000,
    d_model=256,
    n_layers=12,
)
model = MambaLM(config)

# Training
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
loss = model(x, labels=x).loss
loss.backward()
optimizer.step()
```

### Generación

```python
def generate(model, tokenizer, prompt, max_new_tokens=50, temperature=0.8):
    input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"]
    output = model.generate(input_ids, max_new_tokens=max_new_tokens, temperature=temperature)
    return tokenizer.decode(output[0])
```

---

## 4. Usar Mamba-2

### Instalación

```bash
pip install mamba-ssm
```

### Uso con Hugging Face

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "state-spaces/mamba2-2.8b"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

### Implementación mínima (mamba2-minimal)

```python
# https://github.com/tommyip/mamba2-minimal
from mamba2 import Mamba2LMHeadModel, Mamba2Config

config = Mamba2Config(
    d_model=768,
    n_layer=24,
    vocab_size=50277,
    d_state=128,
)
model = Mamba2LMHeadModel(config)
```

---

## 5. Usar LFM2 con Hugging Face Transformers

### Requisitos

```bash
pip install transformers>=4.57 torch
```

### Cargar modelo pre-entrenado

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "LiquidAI/LFM2-1.2B"  # Disponible: 350M, 700M, 1.2B

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype="bfloat16",
)
```

### Inferencia

```python
input_text = "El futuro de la inteligencia artificial es"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

output = model.generate(
    **inputs,
    max_new_tokens=50,
    temperature=0.8,
    top_p=0.9,
)
print(tokenizer.decode(output[0]))
```

### Fine-tuning con LoRA

```python
from transformers import TrainingArguments
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.05,
)

model = get_peft_model(model, lora_config)
```

### Usar como modelo base

```python
from transformers import Lfm2Model, Lfm2Config

# Configuración personalizada
config = Lfm2Config(
    hidden_size=1024,
    num_hidden_layers=16,
    num_attention_heads=8,
)
model = Lfm2Model(config)
```

---

## 6. Usar lfm2 (implementación mínima en PyPI)

### Instalación

```bash
pip install lfm2
```

### Uso

```python
import torch
from lfm2.main import create_lfm2_model

# Crear modelo
model = create_lfm2_model(
    model_size="700M",  # "350M", "700M", "1.2B"
    device="cuda",
)

# Forward pass
batch_size, seq_len = 4, 128
input_ids = torch.randint(0, model.vocab_size, (batch_size, seq_len))
logits = model(input_ids)
```

---

## 7. Comparativa: implementaciones didácticas vs. librerías

### MiniMamba / MiniLiquid (las creadas)

| Aspecto | Implementación didáctica | Librería oficial |
|---------|--------------------------|------------------|
| **Rendimiento** | Básico, para aprender | Optimizado para producción |
| **Velocidad** | Lento (scan secuencial) | Rápido (CUDA, parallel scan) |
| **Memoria** | Mayor uso | Optimizado |
| **Modelos pre-entrenados** | No | Sí |
| **Complejidad** |Simple, legible | Más complejo |
| **Dependencias** | Solo PyTorch | mamba-ssm, CUDA |

### Cuándo usar cada una

**Para aprender** → Implementaciones didácticas (MiniMamba, MiniLiquid)
- Entiendes cada componente
- Fácil de modificar
- No necesitas rendimiento óptimo

**Para producción** → Librerías oficiales
- Necesitas modelo pre-entrenado
- Importa la velocidad de inferencia
- Tienes GPU con CUDA

---

## 8. Mejorar las implementaciones didácticas

Si quieres que los MiniMamba / MiniLiquid sean más competitivos:

### Añadir parallel scan (más rápido)

```python
# En lugar de scan secuencial:
def ssm_sequential(x, A, B, C, dt):
    h = torch.zeros_like(B)
    ys = []
    for t in range(x.shape[1]):
        h = torch.exp(dt[:, t] * A) * h + B[:, t] * x[:, t]
        y = torch.sum(C[:, t] * h, dim=-1)
        ys.append(y)
    return torch.stack(ys, dim=1)

# Usar parallel scan de mambapy:
from mambapy.pscan import pscan

def ssm_parallel(x, A, B, C, dt):
    return pscan(x, A, B, C, dt)
```

### Añadir selección dinámica de estados (Mamba)

```python
class ImprovedMambaBlock(nn.Module):
    def __init__(self, d_model, d_state=16, d_conv=4):
        super().__init__()
        self.d_model = d_model
        self.d_state = d_state
        
        # Proyección con selección
        self.in_proj = nn.Linear(d_model, 2 * d_model + 2 * d_state)
        
        # Convolución
        self.conv1d = nn.Conv1d(
            d_model + 2 * d_state,
            d_model + 2 * d_state,
            d_conv,
            padding=d_conv - 1,
        )
        
        # Parámetros SSM (seleccionables)
        self.x_proj = nn.Linear(d_model, 2 * d_state, bias=False)
        self.dt_proj = nn.Linear(d_model, d_model, bias=True)
        
        # Matrices SSM
        self.A_log = nn.Parameter(torch.randn(d_model, d_state))
        self.D = nn.Parameter(torch.ones(d_model))
        
        self.out_proj = nn.Linear(d_model, d_model)
```

### Añadir RoPE (posiciones)

```python
def apply_rope(x, cos, sin):
    x1, x2 = x[..., :x.shape[-1]//2], x[..., x.shape[-1]//2:]
    return torch.cat([
        x1 * cos - x2 * sin,
        x1 * sin + x2 * cos,
    ], dim=-1)
```

### Añadir SwiGLU (como LFM2)

```python
class SwiGLU(nn.Module):
    def forward(self, x):
        x1, x2 = x.chunk(2, dim=-1)
        return F.silu(x1) * x2
```

### Usar RMSNorm en lugar de LayerNorm

```python
class RMSNorm(nn.Module):
    def __init__(self, d_model, eps=1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(d_model))
    
    def forward(self, x):
        norm = x.pow(2).mean(-1, keepdim=True).add(self.eps).rsqrt()
        return x * norm * self.weight
```

---

## 9. Tabla resumen: qué usar según tu objetivo

| Objetivo | Herramienta recomendada |
|----------|------------------------|
| **Aprender la arquitectura** | MiniMamba / MiniLiquid (las creadas) |
| **Ver código legible** | mambapy (mamba.py) |
| **Usar modelo pre-entrenado** | transformers (Mamba, LFM2) |
| **Producción con GPU** | mamba-ssm + CUDA |
| **Edge / CPU** | LFM2 (transformers) |
| **Experimentar con Mamba-2** | mamba-ssm o mamba2-minimal |
| **Implementar desde cero para clase** | Versión mejorada de arriba |

---

## 10. Recursos adicionales

- [Mamba paper](https://arxiv.org/abs/2312.00752)
- [LFM2 Technical Report](https://arxiv.org/abs/2511.23404)
- [Hugging Face Mamba](https://huggingface.co/docs/transformers/model_doc/mamba)
- [Hugging Face LFM2](https://huggingface.co/docs/transformers/model_doc/lfm2)
- [mambapy GitHub](https://github.com/alxndrTL/mamba.py)
- [LFM2 GitHub (kyegomez)](https://github.com/kyegomez/LFM2)
- [Liquid AI Docs](https://docs.liquid.ai/)
# Tarea: Ampliación de Vocabulario y Comparación con Transformers Pre-entrenados

## Objetivo

Ampliar al máximo el vocabulario de **uno de los ejemplos** de transformers implementados desde cero, entrenar el modelo hasta obtener resultados decentes, e importar un transformer pre-entrenado equivalente para comparar resultados.

---

## Ejemplos disponibles

| # | Ejemplo | Tipo | Datos | Descripción |
|---|---------|------|-------|-------------|
| 1 | `ejemplo_transformers_1_traduccion_en_es.py` | Encoder-Decoder | `mini_trad_es_en_ampliado.tsv` | Traducción inglés → español |
| 2 | `ejemplo_transformers_2_generacion_decoder_only.py` | Decoder-only | `mini_estilo_quijote.txt` | Generación de texto estilo Quijote |
| 3 | `ejemplo_transformers_3_reformulacion.py` | Encoder-Decoder | `mini_reformulacion_es.tsv` | Reformulación de texto |
| 4 | `ejemplo_transformers_4_encoder_only_clasificacion.py` | Encoder-only | `mini_clasificacion_intenciones.tsv` | Clasificación de intenciones |

---

## Parte 1: Ampliación del vocabulario

### Tareas

1. **Elegir uno de los 4 ejemplos** disponibles en `ejemplos`

2. **Ampliar los datos** de entrenamiento:
   - Añadir más datos al archivo TSV/TXT correspondiente en `../datos/`
   - O crear un nuevo dataset con datos externos (traducciones, textos, etc.)
   - O combinar múltiples fuentes de datos

3. **Maximizar el vocabulario**:
   - Si es tokenización por palabras: eliminar o reducir tokens unknown (`<unk>`)
   - Si es tokenización por caracteres: ampliar el conjunto de caracteres
   - Considerar subword tokenization (BPE, SentencePiece) para vocabularios grandes

4. **Documentar**:
   - Vocabulario original (tamaño y ejemplos)
   - Vocabulario ampliado (tamaño y ejemplos)
   - Fuentes de datos añadidas
   - Preprocesamiento aplicado

### Recomendación para el ejemplo del Quijote

Dispones del texto completo del Quijote en `el_quijote.txt`. Se recomienda:

- **Opción A**: Usar solo el archivo `mini_estilo_quijote.txt` (reducido) para experimentar rápido
- **Opción B**: Usar el Quijote completo para mejores resultados
- **Opción C**: Combinar el Quijote con otros textos del Siglo de Oro español

**Pregunta a investigar**: ¿Realmente funciona mejor con más datos? ¿Cuánto mejora? ¿A partir de qué cantidad de texto deja de mejorar significativamente?
¿Hay que tocar algo del tamaño de la red para entrenar con más o menos texto?
---

## Parte 2: Entrenamiento optimizado

### Tareas

1. **Ajustar hiperparámetros** para mejorar resultados:
   - Aumentar `d_model` (ej: 128, 256, 512)
   - Aumentar `num_layers` (ej: 4, 6, 8)
   - Aumentar `num_heads` proporcionalmente
   - Aumentar `d_ff`
   - Ajustar learning rate y batch size
   - Añadir warmup y scheduling

2. **Entrenar hasta obtener buenos resultados**:
   - Monitorear loss y métricas
   - Guardar checkpoints
   - Entrenar durante suficientes epochs
   - Considerar early stopping

3. **Evaluar**:
   - Generar/traducir/clasificar ejemplos
   - Calcular métricas relevantes (BLEU, accuracy, etc.)
   - Mostrar casos de éxito y fracaso

---

## Parte 3: Comparación con modelo pre-entrenado

### Tareas

1. **Importar un modelo pre-entrenado** de HuggingFace:

   | Ejemplo | Modelo recomendado |
   |---------|-------------------|
   | Traducción | `Helsinki-NLP/opus-mt-en-es` o `facebook/mbart-large-50-many-to-many-mmt` |
   | Generación texto | `gpt2` o modelos en español (`DeepESP/gpt2-spanish`) |
   | Reformulación | Usar modelo de traducción o `t5-small` |
   | Clasificación | Usar modelo con cabeza de clasificación (`distilbert-base-uncased`) |

2. **Comparar resultados**:
   - Mismo input → outputs de ambos modelos
   - Análisis cualitativo: ¿cuál es mejor? ¿por qué?
   - Análisis cuantitativo: métricas cuando sea posible
   - Diferencias en velocidad, tamaño, recursos

3. **Reflexionar** sobre:
   - ¿Por qué el modelo pre-entrenado es mejor/peor en algunos casos?
   - ¿Cuánto entreno vs cuánto entrenó el modelo pre-entrenado?
   - ¿Vale la pena entrenar desde cero? ¿Cuándo sí y cuándo no?

---

## Recursos

### Librerías sugeridas

```bash
pip install transformers datasets sentencepiece sacrebleu torch
```

### Modelos pre-entrenados recomendados

```python
# Traducción
from transformers import MarianMTModel, MarianTokenizer
model_name = "Helsinki-NLP/opus-mt-en-es"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Generación de texto
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name = "gpt2"  # o "DeepESP/gpt2-spanish"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Clasificación
from transformers import AutoModelForSequenceClassification, AutoTokenizer
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
```

---

## Entrega

Consultar el documento `Tarea-Transformer-Ampliar-Entrega.md` para ver los requisitos específicos de entrega.

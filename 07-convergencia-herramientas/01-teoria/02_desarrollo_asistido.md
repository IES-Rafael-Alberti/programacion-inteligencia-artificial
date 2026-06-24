# F1 — Desarrollo Asistido por IA

**RA/CE**: RA3a  
**Duración**: 4h teoría + 4h práctica  
**Prerrequisitos**: Ninguno específico de UD5/UD6

---

## Problema: El código que no escribes solo

Imagina que tienes clara la arquitectura de tu pipeline: sabes qué datos necesitas, qué modelo quieres entrenar y cómo debería servir las predicciones. Pero escribir todo ese código desde cero te llevaría días. Y además, sabes que hay fragmentos —validación con Pydantic, un preprocesador de texto, un endpoint REST— que ya has escrito decenas de veces.

**Los asistentes de código basados en IA** (GitHub Copilot, Cursor, Claude Code) prometen acelerar este proceso. Pero no son magia: generan código que puede contener errores sutiles, malas prácticas o vulnerabilidades.

El reto no es solo **usar** estas herramientas, sino **evaluar críticamente** lo que producen y **decidir cuándo confiar** en sus sugerencias.

---

## 1. ¿Qué es el Desarrollo Asistido por IA?

El desarrollo asistido por IA utiliza modelos de lenguaje entrenados con código público para **sugerir, completar y generar** fragmentos de código en tiempo real. No es automatización total —es **colaboración hombre-máquina** donde el programador mantiene el control.

### 1.1 Principales herramientas

| Herramienta | Entorno | Modelo base | Fortaleza |
|-------------|---------|-------------|-----------|
| **GitHub Copilot** | VS Code, JetBrains, Neovim | OpenAI Codex (GPT-4o) | Madurez, integración Git, contexto del proyecto |
| **Cursor** | Editor propio (fork VS Code) | Claude + GPT-4 | Comprensión multi-archivo, edición contextual |
| **Claude Code** | Terminal (CLI) | Claude | Análisis de proyectos grandes, refactorización masiva |

### 1.2 ¿Qué aportan al flujo convergente?

En el contexto de UD7, el desarrollo asistido no es un fin en sí mismo —es una **palanca para acelerar la construcción del pipeline**. En lugar de escribir cada función manualmente:

- **Generamos el esqueleto del pipeline** con prompts en lenguaje natural
- **Refactorizamos código existente** para adaptarlo al stack convergente
- **Depuramos errores** con la ayuda del asistente
- **Documentamos y añadimos tipos** mientras escribimos

**Conexión con RA3a**: Unificar el proceso de ideación, código y depuración reduce la fricción entre la idea y su implementación, una de las ventajas clave de la convergencia tecnológica.

---

## 2. Patrones de Uso Efectivo

### 2.1 Prompting para código

La calidad del código generado depende directamente de cómo describas lo que necesitas:

```
❌ "Haz un pipeline"
✅ "Escribe una función en Python que cargue un CSV desde data/raw/,
    limpie los valores nulos aplicando imputación por la mediana,
    y guarde el resultado en data/processed/ con timestamp en el nombre"
```

**Reglas de oro**:
1. **Especifica el contexto**: librerías, versiones, convenciones del proyecto
2. **Describe la entrada y salida**: tipos de datos, estructura esperada
3. **Indica restricciones**: rendimiento, seguridad, manejo de errores
4. **Divide problemas grandes**: un prompt por función, no por sistema

### 2.2 Revisión crítica del código generado

El código generado por IA **SIEMPRE debe revisarse**. Errores comunes:

| Error | Ejemplo | Riesgo |
|-------|---------|--------|
| Lógica incorrecta | Bucle que no termina o condición invertida | Resultados erróneos sin aviso |
| Fuga de datos | `test` incluido en `train_test_split` sin separar | Métricas irreales en producción |
| Dependencia insegura | `eval()` sobre input de usuario | Inyección de código |
| Falta de manejo de errores | `open(archivo)` sin `try/except` | Caída del pipeline |
| Sesgo implícito | Algoritmo que penaliza grupos demográficos | Discriminación no intencionada |

**Protocolo de revisión**:

1. **Lee** el código generado —no lo aceptes sin entenderlo
2. **Ejecuta** en un entorno aislado primero
3. **Prueba** casos borde (inputs vacíos, nulos, extremos)
4. **Compara** con la lógica que tú habrías escrito
5. **Modifica** lo necesario antes de integrar

### 2.3 Refactorización asistida

Los asistentes destacan en refactorización: extraer funciones, añadir tipos, renombrar variables.

```python
# Código original (generado por IA, funcional pero mejorable)
def process(d):
    r = []
    for i in d:
        if i['score'] > 0.5:
            r.append(i)
    return sorted(r, key=lambda x: x['score'], reverse=True)

# Prompt: "Refactoriza esta función con type hints, docstring,
#           y nombres descriptivos. Añade logging."
def filter_high_confidence_predictions(
    predictions: list[dict],
    threshold: float = 0.5
) -> list[dict]:
    """Filtra predicciones con confianza superior al umbral.

    Args:
        predictions: Lista de diccionarios con clave 'score'
        threshold: Umbral mínimo de confianza

    Returns:
        Lista filtrada y ordenada por score descendente
    """
    logger.info(f"Filtrando {len(predictions)} predicciones, umbral={threshold}")
    filtered = [p for p in predictions if p.get('score', 0) > threshold]
    result = sorted(filtered, key=lambda x: x['score'], reverse=True)
    logger.info(f"Resultado: {len(result)} predicciones superan el umbral")
    return result
```

---

## 3. Desarrollo Asistido en el Pipeline Convergente

En esta unidad usaremos el desarrollo asistido para **acelerar la construcción del pipeline**, no como un fin en sí mismo.

### 3.1 Flujo de trabajo recomendado

1. **Diseña en lenguaje natural**: describe el componente que necesitas
2. **Genera con IA**: obtén una primera versión
3. **Revisa críticamente**: encuentra errores y malas prácticas
4. **Adapta al contexto**: ajusta al stack de UD7 (MLflow, Prefect, FastAPI)
5. **Documenta**: añade comentarios, tipos y docstrings
6. **Versiona**: commit con el código revisado

### 3.2 Ejemplo: Generar un endpoint de predicción

**Prompt inicial**:
> "Generate a FastAPI endpoint /predict that receives a JSON with 'text'
> field, loads a sklearn model from 'models/classifier.pkl', vectorizes
> the text with a saved TfidfVectorizer, returns the predicted class
> and probabilities. Include Pydantic models for request/response."

El asistente generará el código. Tu trabajo es **revisar** que:
- Los imports son los correctos para el proyecto
- El manejo de errores cubre archivo no encontrado y error de carga
- Los modelos Pydantic validan correctamente
- El logging está presente para trazabilidad

---

## 4. Conexión con el Flujo Convergente

```
F1: Desarrollo asistido → genera el código base del pipeline
 │                           │
 │                           ▼
 │                    F2: Pipeline datos (usa el esqueleto ETL)
 │                    F3: MLflow (usa la función de entrenamiento)
 │                    F5: FastAPI (usa el endpoint generado)
 │
 └───► El asistente acelera cada fase, pero el humano
       valida y adapta cada fragmento al stack completo
```

**¿Qué significa esto para RA3a?** El desarrollo asistido unifica el proceso de creación de software: reduces el tiempo entre "tengo una idea" y "tengo código funcionando". Pero la verdadera convergencia ocurre cuando conectas ese código con el resto del stack —y para eso, necesitas entender qué hace cada pieza.

---

## 5. Referencias a UD5 y UD6

Esta fase no requiere prerrequisitos específicos de UD5/UD6. Sin embargo, los ejemplos de código que generaremos se basan en:

- **FastAPI** (visto en UD6 práctica `103_fastapi_serving_modelos.ipynb`)
- **MLflow** (visto en UD5 teoría y UD6 práctica `100_mlflow_llamaindex_rag.ipynb`)
- **Scikit-learn pipelines** (visto en UD2 y UD3)

> Si no has trabajado con FastAPI o MLflow antes, revisa los materiales de UD6 antes de la práctica de esta fase.

---

## Resumen y Claves

1. **El desarrollo asistido por IA** acelera la escritura de código, pero requiere supervisión humana constante.
2. **Prompting efectivo**: sé específico sobre contexto, entrada, salida y restricciones.
3. **Revisión crítica obligatoria**: errores lógicos, de seguridad y sesgos son responsabilidad del programador.
4. **El asistente es una herramienta del stack convergente**, no un sustituto del conocimiento técnico.
5. **Cada fragmento generado debe integrarse** en el flujo mayor del pipeline.

**En la práctica F1**: Configurarás tu asistente, generarás el esqueleto del pipeline de clasificación de incidencias, y revisarás críticamente el código producido.

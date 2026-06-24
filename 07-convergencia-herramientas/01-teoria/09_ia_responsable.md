# F8 — IA Responsable en la Práctica

**RA/CE**: RA3d (convergencia tecnológica y seguridad en los negocios)
**Duración**: 3h teoría + 4h práctica
**Prerrequisitos**: F5 (serving APIs), F6 (agentes RAG)

---

## Problema: Tu modelo funciona, pero ¿es seguro?

En F5 aprendiste a servir modelos con seguridad a nivel de API (autenticación, rate limiting). En F6 construiste agentes autónomos que toman decisiones. Pero:

- **¿Qué pasa si un usuario envía un prompt malicioso y el modelo responde con contenido inapropiado?**
- **¿Tu modelo trata igual a todos los grupos demográficos, o está sesgado contra algunos?**
- **Si un alumno recibe una predicción negativa, ¿puedes explicar por qué el modelo tomó esa decisión?**
- **¿Qué ocurre si un agente autónomo ejecuta una acción dañina porque nadie validó sus outputs?**

La IA responsable no es un concepto abstracto —es un conjunto de **técnicas aplicables** que protegen a los usuarios, a la organización y al propio sistema de IA.

---

## 1. ¿Qué es la IA Responsable?

### 1.1 Dimensiones de la IA Responsable (RA3d)

```
┌─────────────────────────────────────────────────────────────┐
│                    IA RESPONSABLE                            │
├──────────────┬──────────────┬──────────────┬────────────────┤
│  SEGURIDAD   │  EQUIDAD     │  EXPLICABIL. │ TRANSPARENCIA  │
│  (Guardrails)│  (Bias)      │  (SHAP/LIME) │  (Auditoría)   │
├──────────────┼──────────────┼──────────────┼────────────────┤
│ Filtrar      │ Detectar     │ Entender     │ Registrar      │
│ entradas     │ sesgos en    │ por qué el   │ decisiones     │
│ y salidas    │ datos y      │ modelo       │ para          │
│ dañinas      │ predicciones │ predice X    │ auditoría     │
├──────────────┼──────────────┼──────────────┼────────────────┤
│ RA3d:        │ RA3d:        │ RA3d:        │ RA3d:          │
│ seguridad    │ seguridad    │ trazabilidad │ cumplimiento   │
│ en negocio   │ en negocio   │ y confianza  │ normativo      │
└──────────────┴──────────────┴──────────────┴────────────────┘
```

> **Conexión RA3d**: La convergencia tecnológica aporta seguridad al negocio cuando cada herramienta del stack incorpora capas de protección —guardrails en la API, detección de sesgos en los datos, explicabilidad en las predicciones— creando un sistema que no solo es eficiente, sino también fiable y auditable.

### 1.2 Marco Regulatorio (Contexto)

La IA responsable no es solo ética —cada vez más es ley:

| Regulación | Ámbito | Exigencias clave | Impacto en UD7 |
|-----------|--------|-----------------|----------------|
| **EU AI Act** | Unión Europea | Evaluación de riesgo, transparencia, supervisión humana | Los sistemas clasificadores de incidencias entran en riesgo limitado → obligación de transparencia |
| **GDPR** | UE | Derecho a explicación (Art. 22), protección de datos | Las predicciones automatizadas deben ser explicables si afectan al usuario |
| **EEUU (Blueprint)** | Federal | Guías no vinculantes pero marcan tendencia | Framework de IA responsable como referencia |

---

## 2. Guardrails de Seguridad

### 2.1 ¿Qué son los Guardrails?

Los **guardrails** son capas de protección que filtran entradas y salidas del modelo para evitar:

- **Contenido tóxico**: insultos, amenazas, discursos de odio
- **PII (Información Personal Identificable)**: números de teléfono, emails, DNI
- **Alucinaciones**: respuestas inventadas que parecen factuales
- **Salidas fuera de dominio**: respuestas sobre temas no autorizados
- **Prompt injection**: intentos de manipular el comportamiento del modelo

### 2.2 Guardrails AI (NeMo Guardrails)

NeMo Guardrails de NVIDIA permite definir políticas de conducta como reglas configurables:

```python
from nemoguardrails import RailsConfig, LLMRails

# Cargar configuración de guardrails
config = RailsConfig.from_path("config/guardrails")
rails = LLMRails(config)

# Solicitud protegida
response = rails.generate(
    messages=[{"role": "user", "content": prompt}],
    options={"temperature": 0.7}
)
```

**Estructura de configuración**:

```
config/guardrails/
├── config.yml              ← Configuración general (modelo, proveedor)
├── rails.co               ← Reglas de conducta (Colang)
└── prompts.yml            ← Prompts para cada tipo de guardrail
```

**Ejemplo de regla en Colang**:

```colang
# rails.co
define bot greeting
  "Hola, soy el asistente de soporte técnico. ¿En qué puedo ayudarte?"

define bot answer unknown
  "Lo siento, solo puedo ayudar con incidencias técnicas. "
  "Si tu pregunta es sobre otro tema, contacta con el departamento correspondiente."

define flow
  user express something not about technical support
  bot answer unknown
  bot refuse to answer

define guardrail check input for toxicity
  if $input.is_toxic
    bot "Lo siento, no puedo procesar esa solicitud. Por favor, reformúlala."
    stop
```

### 2.3 Guardrails en la API (Conexión F5)

Los guardrails se integran naturalmente en el endpoint de inferencia:

```python
from fastapi import FastAPI, HTTPException
from nemoguardrails import LLMRails, RailsConfig

app = FastAPI(title="API con Guardrails")
config = RailsConfig.from_path("config/guardrails")
rails = LLMRails(config)

@app.post("/v2/predict")
async def predict_with_guardrails(text: str):
    # 1. Validar entrada con guardrails
    input_check = rails.generate(
        messages=[{"role": "user", "content": text}]
    )

    # 2. Si el input es seguro, proceder con la predicción
    if input_check["is_safe"]:
        prediction = model.predict(vectorizer.transform([text]))
        return {"prediction": prediction[0]}

    # 3. Si no, bloquear
    raise HTTPException(
        status_code=400,
        detail="Input bloqueado por política de seguridad"
    )
```

### 2.4 Alternativa: Guardrails AI (Python)

Una alternativa más ligera que NeMo:

```python
from guardrails import Guard
from guardrails.validators import TwoWords, LowerCase

# Definir guardrail de validación de salida
guard = Guard().use(
    LowerCase(),
    on_fail="fix"        # Corrige automáticamente
).use(
    TwoWords(),
    on_fail="exception"  # Lanza excepción
)

# Aplicar guardrail a la salida del modelo
try:
    validated_output = guard.validate(model_output)
    print(f"✅ Salida validada: {validated_output}")
except Exception as e:
    print(f"❌ Salida bloqueada: {e}")
```

---

## 3. Detección y Mitigación de Sesgos

### 3.1 ¿Qué es el Sesgo en IA?

El sesgo ocurre cuando un modelo produce resultados sistemáticamente diferentes para distintos grupos demográficos, incluso cuando el rendimiento global parece aceptable:

| Tipo de sesgo | Descripción | Ejemplo en clasificación de incidencias |
|--------------|-------------|----------------------------------------|
| **Sesgo de datos** | El dataset de entrenamiento no representa equitativamente a todos los grupos | Más incidencias de "hardware" para un departamento que para otro |
| **Sesgo de etiquetado** | Las etiquetas reflejan prejuicios humanos | Incidencias de ciertos equipos se clasifican como "menores" sistemáticamente |
| **Sesgo de medición** | Las features proxy discriminan indirectamente | La ubicación geográfica correlaciona con nivel de servicio |
| **Sesgo de despliegue** | El modelo funciona bien en global pero mal en subgrupos | Alta accuracy global pero baja en incidencias de un equipo concreto |

### 3.2 Métricas de Equidad

| Métrica | Definición | Interpretación |
|---------|-----------|----------------|
| **Demographic Parity** | P(Ŷ=1|A=a) = P(Ŷ=1) para todos los grupos a | La tasa de predicción positiva es igual entre grupos |
| **Equal Opportunity** | TPRₐ = TPR para todos los grupos a | La tasa de verdaderos positivos es igual entre grupos |
| **Equalized Odds** | TPRₐ = TPR Y FPRₐ = FPR | Tanto TPR como FPR son iguales entre grupos |
| **Disparate Impact** | P(Ŷ=1|A=a) / P(Ŷ=1|A=b) | Ratio entre tasas de predicción positiva (seguro: >0.8) |

### 3.3 Auditoría con Fairlearn

```python
from fairlearn.metrics import (
    demographic_parity_difference,
    equal_opportunity_difference,
    MetricFrame
)
from sklearn.metrics import accuracy_score
import pandas as pd

# Datos reales: predicciones vs. ground truth
data = pd.DataFrame({
    "predicted": [1, 0, 1, 1, 0, 0, 1, 0],
    "actual":    [1, 0, 1, 0, 0, 1, 0, 0],
    "group":     ["A", "A", "B", "A", "B", "B", "A", "B"]
})

# Calcular métricas de equidad por grupo
mf = MetricFrame(
    metrics=accuracy_score,
    y_true=data["actual"],
    y_pred=data["predicted"],
    sensitive_features=data["group"]
)

print(f"Accuracy por grupo:")
print(mf.by_group)
print(f"\nDiferencia de parity: {demographic_parity_difference(
    y_true=data['actual'],
    y_pred=data['predicted'],
    sensitive_features=data['group']
):.3f}")
```

### 3.4 Estrategias de Mitigación

| Estrategia | Cuándo usarla | Cómo |
|-----------|--------------|------|
| **Reweighting** | Datos desbalanceados entre grupos | Asignar pesos mayores a muestras de grupos infrarrepresentados |
| **Data Augmentation** | Grupos con pocos ejemplos | Generar datos sintéticos del grupo minoritario |
| **Threshold Adjustment** | Clasificador sesgado | Ajustar umbrales de decisión por grupo |
| **Fairness Constraint** | Durante el entrenamiento | Añadir términos de equidad a la función de pérdida |

---

## 4. Explicabilidad con SHAP

### 4.1 ¿Por qué es Necesaria la Explicabilidad?

Un modelo puede ser preciso pero opaco. Sin explicabilidad:

- No puedes **confiar** en sus decisiones
- No puedes **depurar** errores
- No puedes **justificar** predicciones ante usuarios o reguladores
- No puedes **mejorar** el modelo de forma dirigida

### 4.2 SHAP (SHapley Additive exPlanations)

SHAP explica predicciones individuales asignando a cada feature su contribución al resultado:

```python
import shap
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Entrenar modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Crear explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Explicar una predicción individual
instance = X_test[0:1]
prediction = model.predict(instance)[0]

# Visualizar contribución de features
shap.force_plot(
    explainer.expected_value[1],
    shap_values[1][0],
    instance,
    feature_names=feature_names
)
```

**Interpretación del gráfico SHAP**:

- **Features en rojo**: empujan la predicción hacia arriba (más probabilidad de la clase positiva)
- **Features en azul**: empujan la predicción hacia abajo (menos probabilidad)
- **Longitud de la barra**: magnitud de la contribución
- **Valor base**: predicción media si no tuviéramos información

### 4.3 LIME (Local Interpretable Model-Agnostic Explanations)

LIME es una alternativa agnóstica al modelo (funciona con cualquier clasificador):

```python
from lime.lime_tabular import LimeTabularExplainer

explainer = LimeTabularExplainer(
    X_train.values,
    feature_names=feature_names,
    class_names=["baja", "media", "alta"],
    mode="classification"
)

exp = explainer.explain_instance(
    X_test.iloc[0].values,
    model.predict_proba,
    num_features=5
)

exp.show_in_notebook(show_table=True)
```

### 4.4 SHAP vs. LIME

| Criterio | SHAP | LIME |
|----------|------|------|
| **Base teórica** | Shapley values (teoría de juegos) | Modelo lineal local |
| **Consistencia** | Alta (propiedades matemáticas garantizadas) | Media (sensible a perturbaciones) |
| **Rendimiento** | Lento en modelos grandes | Rápido |
| **Tipo** | Específico (TreeExplainer) / Agnóstico (KernelExplainer) | Agnóstico |
| **Visualización** | Force plot, summary plot, dependence plot | Tabla + gráfico de barras |
| **Cuándo usarlo** | Modelos tree-based, necesidad de rigor | Exploración rápida, modelos black-box |

---

## 5. Integración en el Stack Convergente

```
F5: FastAPI sirve modelo
 │
 ├── Guardrails en endpoint /predict
 │   └── Filtro de input tóxico o fuera de dominio
 │   └── Validación de output antes de responder
 │
F6: Agentes CrewAI
 │
 ├── Guardrails en outputs de agentes
 │   └── El validador comprueba que la respuesta es apropiada
 │
F7: Evidently monitorea
 │
 ├── Detección de drift que puede indicar sesgo emergente
 │   └── Si accuracy cae solo en un grupo → posible sesgo
 │
F8: SHAP + Fairlearn cierran el círculo
 │
 ├── Cada predicción puede ser explicada (SHAP)
 ├── El modelo es auditado por sesgos (Fairlearn)
 └── Los guardrails protegen entradas y salidas
```

> **Conexión RA3d**: La seguridad en los negocios no se consigue con una sola medida. Es la **acumulación de capas**: guardrails en la API (F5), validación en agentes (F6), monitorización continua (F7), y explicabilidad + equidad (F8). Cada capa añade robustez al sistema convergente.

### 5.1 Checklist de IA Responsable para el Stack

Antes de poner un modelo en producción, verifica:

- [ ] **Guardrails de entrada**: ¿el endpoint filtra prompts maliciosos?
- [ ] **Guardrails de salida**: ¿las respuestas del modelo son seguras?
- [ ] **Auditoría de sesgo**: ¿el modelo trata equitativamente a todos los grupos?
- [ ] **Explicabilidad**: ¿puedes explicar cualquier predicción individual?
- [ ] **Transparencia**: ¿los usuarios saben que interactúan con un sistema de IA?
- [ ] **Supervisión humana**: ¿hay un humano en el loop para decisiones críticas?
- [ ] **Registro de auditoría**: ¿cada predicción queda registrada con metadatos?

---

## 6. Referencias a UD5 y UD6

**De UD5 (Cloud/MLOps)**:
- Concepto de governance de datos y compliance
- Calidad de datos como prerequisito para equidad

**De UD6 (LLM/Agentes)**:
- Riesgos de alucinación en LLM
- Prompt injection como vector de ataque
- Sistemas RAG y fuentes de veracidad

> Esta fase asume que comprendes los riesgos básicos de los sistemas de IA (alucinaciones, sesgos, seguridad). Si no es así, revisa los materiales de UD5 sobre governance y UD6 sobre riesgos LLM antes de continuar.

---

## Resumen y Claves

1. **La IA responsable** no es ética abstracta —es un conjunto de técnicas aplicables: guardrails, detección de sesgos, explicabilidad y transparencia.
2. **NeMo Guardrails** permite definir políticas de conducta como reglas configurables que filtran entradas y salidas del modelo.
3. **Fairlearn** proporciona métricas de equidad (demographic parity, equal opportunity) para auditar modelos.
4. **SHAP** asigna a cada feature su contribución a la predicción, permitiendo explicar decisiones individuales.
5. **LIME** es una alternativa más rápida y agnóstica al modelo para exploración inicial.
6. **La seguridad en el negocio (RA3d)** se construye por capas: guardrails + monitoreo + explicabilidad + equidad.
7. **Cada fase del stack convergente** debe incorporar consideraciones de IA responsable —no es un añadido final.

**En la práctica F8**: Implementarás guardrails con NeMo Guardrails o Guardrails AI sobre una API de clasificación, auditarás el modelo con Fairlearn para detectar sesgos, y generarás explicaciones SHAP para predicciones individuales.

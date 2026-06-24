# F2 — Pipeline de Datos Automatizado

**RA/CE**: RA3b (sistemas de conexión), RA3c (evaluación de características)
**Duración**: 3h teoría + 6h práctica
**Prerrequisitos**: UD5 (DVC, feature engineering), UD6 (pipeline ETL básico)

---

## Problema: Tus datos no están listos para producción

Tienes el esqueleto del pipeline de clasificación de incidencias. Pero los datos con los que trabajas en el notebook son un CSV estático que alguien copió a tu máquina. En producción:

- Los datos llegan de **múltiples fuentes**: APIs, bases de datos, formularios web, logs
- El **formato cambia sin avisar**: una columna nueva, un tipo de dato diferente, valores nulos inesperados
- Las **versiones** de los datos no se corresponden con las versiones del modelo
- El **preprocesado** que hiciste en el notebook no está documentado ni reproducible

**Escenario real**: El equipo de soporte actualiza el sistema de tickets y añade una columna "severidad". Tu pipeline se rompe porque esperabas columnas fijas. Sin un pipeline de datos automatizado, cada cambio en la fuente requiere intervención manual.

---

## 1. ¿Qué es un Pipeline de Datos?

Un pipeline de datos es un **conjunto de procesos que extraen, transforman y cargan (ETL)** datos desde su origen hasta un destino listo para análisis o entrenamiento.

### 1.1 El pipeline ETL clásico

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│ EXTRACT  │───►│ TRANSFORM│───►│   LOAD   │
│ (Extraer)│    │ (Transform) │    │  (Cargar)│
└──────────┘    └──────────┘    └──────────┘
     │               │               │
  APIs, CSV,      Limpieza,       Data Lake,
  BD, logs       features,       Feature Store,
                  encoding      Base de datos
```

**Cada fase del pipeline debe ser**:
- **Reproducible**: mismo input → mismo output siempre
- **Versionada**: saber qué versión de los datos usó cada modelo
- **Robusta**: tolerante a cambios en las fuentes
- **Monitoreable**: saber si falló, cuánto tardó, qué produjo

### 1.2 Del ETL básico al Feature Pipeline

En UD6 trabajaste con pipelines ETL sencillos. En UD7 los conectamos con el resto del stack:

| Componente | ETL básico (UD6) | Pipeline automatizado (UD7) |
|------------|------------------|-----------------------------|
| Extracción | CSV manual | API + BD + Webhooks |
| Transformación | Notebook | Script reproducible + DVC |
| Validación | Manual | Automática (esquemas, tests) |
| Versionado | No | DVC + Git |
| Destino | Archivo local | Feature Store + Data Lake |
| Orquestación | Manual | Prefect (F4) |

---

## 2. Versionado de Datos con DVC

DVC (Data Version Control) permite versionar datasets igual que Git versiona código.

### 2.1 ¿Por qué versionar datos?

```python
# Sin versionado: ¿qué datos usé para este modelo?
modelo_version = "v3"  # ¿con qué datos?
datos_usados = "dataset_final.csv"  # ¿cuál de las 20 versiones?

# Con DVC: el commit de git dice exactamente qué versión de datos
# $ git log --oneline
# a1b2c3d feat: update training data with Q3 tickets
# e4f5g6h feat: initial pipeline setup
```

Cada vez que ejecutas `dvc add data/raw/tickets.csv`, DVC:
1. Calcula el hash del archivo
2. Lo almacena en caché
3. Crea un archivo `.dvc` que versionas con Git
4. Permite recuperar cualquier versión histórica

### 2.2 Flujo básico con DVC

```bash
# Inicializar DVC
dvc init

# Añadir datos al control de versiones
dvc add data/raw/tickets_q3.csv

# Git commit del archivo .dvc (no el CSV grande)
git add data/raw/tickets_q3.csv.dvc
git commit -m "feat: add Q3 tickets dataset"

# Recuperar una versión anterior
git checkout a1b2c3d
dvc checkout
```

---

## 3. Transformaciones Reproducibles

### 3.1 El problema del notebook

En un notebook típico, las transformaciones están dispersas entre celdas ejecutadas en orden arbitrario:

```python
# Celda 5 (ejecutada antes que la 4)
df_clean = df_raw.dropna()

# Celda 4 (ejecutada después - depende de variables de celda 5)
# ¡No se puede reproducir en orden!
```

### 3.2 La solución: scripts + pipeline

Cada transformación es un **script independiente** con entrada y salida definidas:

```
data/raw/tickets.csv ──► scripts/clean.py ──► data/processed/tickets_clean.csv
                              │
                              │ (pasa a feature engineering)
                              ▼
                    scripts/features.py ──► data/features/tickets_features.csv
```

**Ventajas**:
- Se ejecutan siempre en el mismo orden
- Cada script es testeable individualmente
- Se pueden orquestar con herramientas como Prefect (F4)
- Se versionan con git (cambios en el código de transformación)

### 3.3 Validación de datos

Los datos que entran al pipeline deben validarse antes de usarse:

```python
import pandera as pa

# Esquema de validación
schema = pa.DataFrameSchema({
    "ticket_id": pa.Column(int, pa.Check.unique()),
    "description": pa.Column(str, pa.Check.str_length(1, 10000)),
    "priority": pa.Column(str, pa.Check.isin(["alta", "media", "baja"])),
    "created_at": pa.Column(pd.DatetimeTZDtype(), nullable=True),
})

# Validar
try:
    schema.validate(df)
    print("✅ Datos válidos")
except pa.errors.SchemaError as e:
    print(f"❌ Datos inválidos: {e}")
```

---

## 4. Conexión con el Flujo Convergente

```
F2: Pipeline de datos
 │
 ├──► Produce datos listos para entrenar modelos (F3)
 ├──► Se orquesta con Prefect (F4) para ejecución programada
 ├──► Se monitorea con Evidently (F7) para detectar deriva
 │
 └──► Los features versionados alimentan el Feature Store
       que conecta con entrenamiento (F3) y serving (F5)
```

**Conexión RA3b**: DVC y los pipelines ETL son sistemas que facilitan la conexión tecnológica entre fuentes de datos dispares y el resto del stack de IA.

**Conexión RA3c**: La evaluación de sistemas de conexión (fiabilidad, escalabilidad, mantenibilidad) se hace comparando pipelines manuales vs. automatizados.

---

## 5. Referencias a UD5 y UD6

**De UD5 (Cloud/MLOps)**:
- `05-cloud-mlops/01-teoria/01-feature-store.md` — Concepto de feature store
- `05-cloud-mlops/01-teoria/03-mlops.md` — Pipeline MLOps completo

**De UD6 (LLM/Agentes)**:
- UD6 prácticas de ETL básico en notebooks secuenciales
- Concepto de pipeline como secuencia de transformaciones en LangChain

> Esta fase no re-enseña DVC ni ETL básico: los **integra** en un flujo automatizado, versionado y validado. Si necesitas repasar DVC, revisa UD5 antes de la práctica.

---

## Resumen y Claves

1. **Un pipeline de datos automatizado** transforma datos crudos en features listos para entrenamiento, de forma reproducible y versionada.
2. **DVC** permite versionar datasets igual que Git versiona código —cada modelo sabe exactamente con qué datos se entrenó.
3. **Las transformaciones en scripts** (no en notebooks) garantizan reproducibilidad y facilitan orquestación.
4. **La validación de datos** previene errores silenciosos: un esquema definido detecta cambios en las fuentes antes de que afecten al modelo.
5. **El pipeline de datos es la base** de todo el stack convergente: de él dependen F3 (entrenamiento), F5 (serving) y F7 (monitorización).

**En la práctica F2**: Construirás un pipeline ETL completo con DVC, validación de esquemas y scripts de transformación independientes, preparando los datos para la experimentación con MLflow.

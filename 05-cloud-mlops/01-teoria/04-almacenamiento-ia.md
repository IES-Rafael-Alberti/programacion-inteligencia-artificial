# Almacenamiento para IA en la nube

## ¿Por qué es importante?

Los proyectos de IA manejan datasets, modelos, embeddings, logs y artefactos de entrenamiento. Por eso el almacenamiento no es un detalle secundario: condiciona el coste, el rendimiento y la integración con el resto del sistema.

## Necesidades típicas

- Lecturas y escrituras masivas.
- Integración con pipelines y jobs de entrenamiento.
- Compatibilidad con formatos columnares.
- Versionado o trazabilidad de artefactos.
- Coste razonable para volúmenes grandes.

---

## Proveedores de object storage

### AWS S3

| Clase | Uso habitual |
|-------|--------------|
| Standard | Datos de acceso frecuente |
| Standard-IA | Datos de acceso menos frecuente |
| Glacier | Archivo y retención |

### Google Cloud Storage

| Clase | Uso habitual |
|-------|--------------|
| Standard | Datos frecuentes |
| Nearline | Acceso ocasional |
| Coldline / Archive | Archivo |

### Azure Blob Storage

| Nivel | Uso habitual |
|-------|--------------|
| Hot | Acceso frecuente |
| Cool | Acceso menos frecuente |
| Cold / Archive | Archivo |

---

## Formatos relevantes para IA

### Parquet

- Formato columnar comprimido.
- Muy adecuado para analítica, entrenamiento y procesamiento tabular.

```python
import pandas as pd

df.to_parquet("datos.parquet", engine="pyarrow")
```

### ORC

- Similar a Parquet.
- Más habitual en ciertos entornos Hadoop.

### Delta Lake, Iceberg y Hudi

- Añaden tabla, metadatos y operaciones avanzadas sobre object storage.
- Permiten transacciones, evolución de esquema y versiones.

---

## Organización del data lake

### Particionado

Ayuda a no escanear todos los datos:

```text
s3://bucket/datos/year=2026/month=04/day=16/
```

### Compresión

| Formato | Cuándo usarlo |
|---------|---------------|
| Snappy | Equilibrio general |
| Gzip | Mejor compresión, menos velocidad |
| Zstd | Muy buena opción para grandes volúmenes |

### Lakehouse

La combinación de object storage y formatos de tabla abiertos permite montar un enfoque tipo lakehouse:

```text
Object storage + tablas abiertas + motores de consulta = lakehouse
```

---

## Costes a considerar

1. Almacenamiento por GB o TB.
2. Operaciones de lectura y escritura.
3. Transferencia de salida.
4. Replicación entre regiones.
5. Retención de artefactos y checkpoints.

En muchos proyectos el coste de transferencia puede ser tan importante como el de almacenamiento.

---

## Herramientas complementarias

### DVC

- Versionado de datasets.
- Buen apoyo para proyectos reproducibles.

### MinIO

- Almacenamiento de objetos compatible con S3.
- Software libre y muy útil para laboratorios o despliegues propios.

### lakeFS

- Capa de versionado sobre data lakes.
- Interesante cuando se quiere control de ramas y versiones en datos.

### MLflow Artifact Store

- Guarda modelos y artefactos de experimentos sobre S3, GCS o Blob.

### Delta Lake e Iceberg

- Útiles cuando no basta con guardar archivos y se necesitan tablas versionadas.

### Alternativas libres o gratuitas

| Herramienta | Tipo | Comentario |
|-------------|------|------------|
| MinIO | Software libre | Alternativa abierta a object storage para prácticas |
| DVC | Software libre | Muy útil para versionado de datasets |
| lakeFS | Software libre | Añade control de versiones al data lake |
| Delta Lake | Software libre | Tablas abiertas con operaciones ACID |
| Apache Iceberg | Software libre | Muy buena opción en ecosistemas analíticos |

---

## Aplicación al proyecto

Al elegir almacenamiento conviene responder:

1. ¿Qué se va a guardar: datos, modelos, embeddings o todo a la vez?
2. ¿Se necesita almacenamiento barato o acceso frecuente?
3. ¿El proyecto requiere tablas transaccionales o solo archivos?
4. ¿Qué servicios de compute o MLOps deben leer esos datos?

Para un proyecto académico suele bastar con object storage y formatos como Parquet. Delta o Iceberg tienen más sentido si el flujo de datos es más exigente.

---

## Recomendaciones generales

| Caso | Recomendación |
|------|---------------|
| Proyecto sencillo | Object storage + Parquet |
| Datos tabulares grandes | S3, GCS o Blob + Parquet |
| Necesidad de tablas versionadas | Delta Lake o Iceberg |
| Versionado de datasets | DVC |
| Laboratorio o entorno propio | MinIO |

---

## Fuentes recomendadas

- Documentación oficial de Amazon S3.
- Documentación oficial de Google Cloud Storage.
- Documentación oficial de Azure Blob Storage.
- Documentación oficial de Delta Lake e Apache Iceberg.
- Documentación oficial de DVC.
- Documentación oficial de MinIO.
- Documentación oficial de lakeFS.

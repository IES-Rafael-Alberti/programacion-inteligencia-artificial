# Checklist de Entrega — UD9: GPU Avanzado

Verifica cada punto antes de hacer la entrega final. Una casilla sin marcar implica deducción en la rúbrica.

---


## Repositorio / ZIP de entrega

- [ ] El directorio raíz tiene un `README.md` con las instrucciones de instalación y ejecución.
- [ ] El entorno está reproducido: `environment.yml` o `pyproject.toml` / `requirements.txt` con versiones fijadas.
- [ ] No hay credenciales, API keys ni rutas absolutas hardcodeadas en el código.
- [ ] El proyecto tiene control de versiones (`.git/`) o se entrega como ZIP con estructura clara.

---

## Aceleración GPU — Notebook `01_project_template.ipynb`

- [ ] Se usa cuDF o JAX sobre datos reales del proyecto (no solo el ejemplo de clase).
- [ ] Existe una comparativa de tiempos CPU vs GPU con `time.perf_counter` o equivalente.
- [ ] Los tiempos están medidos tras un warmup (primera ejecución excluida).
- [ ] Hay un análisis escrito de los resultados: ¿cuánto se aceleró? ¿por qué ese factor?
- [ ] Los datos caben en VRAM o se aplica chunking si son grandes.

---

## Pipeline reproducible — Notebook `03_pipeline_template.ipynb`

- [ ] El pipeline tiene al menos 3 tasks bien diferenciados (p. ej. ingest → transform → train).
- [ ] Los parámetros (rutas, hiperparámetros) están externalizados (no hardcodeados en el cuerpo del task).
- [ ] El pipeline genera artefactos en `artifacts/`:
  - [ ] `model.joblib` o equivalente.
  - [ ] `metrics.json` con al menos 2 métricas.
  - [ ] `clean.csv` o dataset procesado.
- [ ] El pipeline se puede ejecutar de principio a fin sin intervención manual.
- [ ] Hay logs que permiten rastrear qué task falló en caso de error.

---

## Dashboard — Notebook `02_dashboard_template.ipynb`

- [ ] El dashboard arranca sin errores con las instrucciones del README.
- [ ] Hay al menos un control interactivo (slider, dropdown, input de texto).
- [ ] Se visualizan resultados del modelo (predicciones, métricas, gráficos).
- [ ] El dashboard es autónomo: no requiere modificar código para demostrar el proyecto.

---

## Artefactos y calidad técnica

- [ ] `artifacts/model.joblib` existe y carga sin errores.
- [ ] `artifacts/metrics.json` contiene métricas numéricas del modelo final.
- [ ] `artifacts/clean.csv` (o equivalente) contiene los datos procesados.
- [ ] El código no tiene celdas con errores no controlados.
- [ ] Las importaciones están en la primera celda del notebook.

---

## Documentación

- [ ] El README tiene sección de **Instalación** con comandos concretos.
- [ ] El README tiene sección de **Uso** explicando cómo ejecutar el pipeline y el dashboard.
- [ ] El README explica la estructura del proyecto (qué hace cada notebook).
- [ ] Las celdas de los notebooks tienen comentarios que explican los pasos no obvios.

---

## Presentación (si aplica)

- [ ] La presentación dura entre 10 y 15 minutos.
- [ ] Se cubre: problema → datos → técnicas GPU → pipeline → demo del dashboard → conclusiones.
- [ ] La demo del dashboard funciona en directo.
- [ ] Todos los miembros del grupo participan en la exposición.
- [ ] Se entrega la autoevaluación individual (ver plantilla en `05-recursos/plantilla-autoevaluacion.md`).

---

## Verificación final antes de subir

- [ ] Ejecutado todo el pipeline limpio (Kernel → Restart & Run All) sin errores.
- [ ] Dashboard probado en un entorno limpio (nuevo virtualenv o conda env).
- [ ] Comprobado que no queda ninguna celda con error visible.
- [ ] Entregado en el plazo indicado en el calendario del módulo.

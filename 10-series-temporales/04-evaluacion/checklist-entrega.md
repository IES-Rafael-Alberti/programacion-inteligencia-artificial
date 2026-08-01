# Checklist de entrega — UD10 Series Temporales

Usa esta lista antes de entregar el proyecto final capstone (Torneo de Modelos). Primero verifica lo imprescindible; después revisa los detalles que facilitan la corrección.



## Imprescindible

- [ ] El notebook del proyecto final está completo y ejecutado.
- [ ] El flujo principal ejecuta sin errores críticos desde cero (kernel reiniciado).
- [ ] Se fusionan correctamente las fuentes de datos con `resample()` y `merge()` temporal.
- [ ] Existe una partición train/val/test que respeta la flecha del tiempo.
- [ ] Hay al menos un baseline calculado con MAE, RMSE o MAPE sobre el conjunto de test.
- [ ] Hay al menos un modelo avanzado entrenado y evaluado sobre el mismo test.
- [ ] Existe una tabla comparativa con métricas de al menos dos modelos sobre el mismo test.
- [ ] No se entregan claves API, tokens, contraseñas ni credenciales.

## Formato de entrega

- Entregar una carpeta comprimida o repositorio según indique el profesorado.
- El notebook debe incluirse ejecutado con salidas visibles cuando el tamaño lo permita.
- Mantener las rutas portátiles del taller: el notebook localiza los datasets existentes en `05-recursos/` sin copiarlos a otra carpeta.
- Incluir solo material necesario; no subir checkpoints de modelos pesados salvo que el profesorado lo indique.

## Archivos requeridos

- [ ] `10_proyecto_final.ipynb` completado (o nombre equivalente indicado por el profesorado).
- [ ] `README.md` o apartado introductorio con instrucciones de ejecución.
- [ ] Fichero de dependencias: `requirements.txt` o `environment.yml`.
- [ ] Referencia a los datos de `05-recursos/` o, si se usan datos externos, instrucciones para obtenerlos sin duplicar datasets innecesariamente.

## Evidencias mínimas

| Fase | Evidencia requerida |
| --- | --- |
| Fusión (Retail) | DataFrame unido sin NaNs injustificados + comentario sobre el criterio de imputación. |
| Reto Energía | DataFrame fusionado con decisión documentada sobre la granularidad de agregación. |
| Baseline | Tabla o celda con MAE/RMSE/MAPE del baseline sobre test. |
| Modelo avanzado | Curva de pérdida (si DL) o importancia de features (si RF/XGBoost) + métricas sobre test. |
| Torneo | Tabla comparativa de modelos con al menos dos filas y columnas de métricas. |
| Visualización | Gráfico de predicción vs. valores reales sobre el horizonte de test. |

## Comprobaciones antes de entregar

- [ ] He reiniciado el kernel y ejecutado el notebook desde la primera celda.
- [ ] Las rutas de datos son relativas al notebook; no dependen de mi máquina.
- [ ] Los escaladores (MinMaxScaler, StandardScaler, etc.) se ajustan solo sobre train.
- [ ] No hay ninguna celda que cargue datos del futuro antes de la partición temporal.
- [ ] La tabla del Torneo compara modelos evaluados sobre el mismo conjunto de test.
- [ ] Las métricas calculadas son coherentes con la escala de la variable objetivo.
- [ ] Los errores conocidos o limitaciones observadas están documentados brevemente.

## Datos y licencias

- Los datasets del taller son sintéticos o de uso académico; indicar la fuente si se usa un dataset externo.
- Si se usa un dataset propio o externo, describir brevemente su origen, frecuencia temporal y variable objetivo.
- No incluir datasets completos de gran tamaño; usar el script generador o una muestra representativa.

## Cuestionario

Si el profesorado activa el cuestionario GIFT en Moodle, complétalo como verificación conceptual de los 10 temas del taller. Es complemento de la entrega práctica, no sustituto automático de las evidencias técnicas.

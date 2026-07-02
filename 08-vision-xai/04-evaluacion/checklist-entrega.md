# Checklist de entrega — UD8 Visión por Computadora y XAI

Usa esta lista antes de entregar. Primero verifica lo imprescindible; después revisa los detalles que facilitan la corrección.



## Imprescindible

- [ ] La entrega incluye el notebook o notebooks que resuelven la práctica indicada.
- [ ] El flujo principal ejecuta sin errores críticos.
- [ ] Hay al menos una visualización clara por bloque entregado (máscara, trazas de tracking o mapa XAI).
- [ ] Se incluyen las métricas calculadas (IoU/Dice, MOTA/MOTP o importancias SHAP/LIME/Grad-CAM).
- [ ] No se entregan claves API, tokens, contraseñas ni credenciales.
- [ ] Se indica cómo ejecutar o revisar la solución.

## Formato de entrega

- Entregar una carpeta comprimida o repositorio según indique el profesorado.
- Mantener nombres de archivos claros y estructura ordenada.
- Incluir solo material necesario para revisar la práctica.
- Si se entrega un notebook, dejarlo ejecutado con salidas visibles cuando el tamaño lo permita.
- Si se usan datos externos, indicar cómo obtenerlos o incluir una muestra representativa.

## Archivos requeridos

- [ ] Notebook(s) principal(es) completado(s).
- [ ] `README.md` o apartado introductorio con instrucciones de ejecución.
- [ ] Fichero de dependencias si es necesario: `requirements.txt`, `environment.yml` u otro equivalente.
- [ ] Datos de muestra o instrucciones para obtener el dataset utilizado.

## Evidencias mínimas por bloque

| Bloque | Evidencia requerida |
| --- | --- |
| Segmentación | Imagen original + máscara predicha superpuesta + tabla con IoU y Dice Score. |
| Tracking | Fotograma con bounding boxes y trayectorias + tabla con MOTA y MOTP. |
| XAI | Visualización de explicación (heat map, barras de importancia o highlight) + breve interpretación. |

Solo son obligatorias las evidencias de los bloques incluidos en el enunciado.

## Comprobaciones antes de entregar

- [ ] He reiniciado el kernel y ejecutado el notebook desde cero.
- [ ] Las rutas son relativas o están documentadas; no dependen de mi máquina personal.
- [ ] Las visualizaciones tienen título, leyenda o anotaciones suficientes para entenderlas.
- [ ] Las métricas calculadas son coherentes con el código y los datos usados.
- [ ] Los errores conocidos o limitaciones observadas están documentados brevemente.
- [ ] El análisis de resultados está redactado con mis propias palabras.

## Datos y licencias

- Indicar la fuente y licencia de los datasets utilizados.
- No incluir datasets completos en la entrega si su tamaño es excesivo; usar muestras representativas o enlace.
- Si se usa un dataset propio o generado, describir brevemente su origen y estructura.

## Cuestionario

Si el profesorado activa el cuestionario GIFT en Moodle, complétalo como verificación conceptual. Es complemento de la entrega práctica, no sustituto automático de las evidencias técnicas.

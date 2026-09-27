# Matriz de cobertura y seguimiento individual RA/CE - PIA 2026/2027

Esta matriz identifica donde se obtiene evidencia de cada criterio de evaluacion
(CE). Complementa el calificador Moodle: sus categorias ordenan instrumentos y
pesos, pero no sustituyen el registro criterial por RA/CE.

La plantilla editable esta en `plantilla_seguimiento_ra_ce.csv`. Se duplica por
alumno o alumna y se actualiza despues de revisar una evidencia individual.

## Regla de acreditacion

- `NE`: sin evidencia individual evaluada; el CE no esta cerrado.
- `PE`: evidencia entregada o revisada parcialmente; falta calificar o defender.
- `AC`: evidencia individual suficiente, con calificacion del CE igual o superior a 5.
- `NR`: no acreditado; requiere refuerzo o recuperacion del CE.
- Un RA se marca **cerrado** cuando todos sus CE tienen estado `AC` y su media
  ponderada segun Seneca es igual o superior a 5.
- Una actividad grupal solo aporta `AC` tras comprobar la contribucion individual,
  la trazabilidad del proceso y la defensa de la persona evaluada.
- Un cuestionario por si solo no cierra RA2, RA3 ni RA4: debe existir una evidencia
  aplicada, ejecutable o defendida acorde al CE.

## Distribucion principal

| RA | CE | Unidad de evidencia primaria | Refuerzo o contraste | Evidencia individual de cierre |
|---|---|---|---|---|
| RA1 | a | UD1 | UD2 | Practica Python y NumPy con codigo explicado |
| RA1 | b | UD1 | UD2, UD9 | Comparativa de lenguajes y formatos justificada |
| RA1 | c | UD1 | UD3, UD12 | Comparativa con decision de lenguaje para un caso |
| RA1 | d | UD1 | UD2, UD3, UD4, UD9 | Practica Python/NumPy y cuestionario conceptual |
| RA1 | e | UD1 | UD3, UD4, UD9, UD12 | Decision tecnica razonada sobre lenguaje o entorno |
| RA1 | f | UD1 | UD2, UD5, UD6, UD12 | Comparativa de JSON, YAML, Markdown, XML o HTML |
| RA2 | a | UD5 | UD3, UD6, UD7 | Comparativa cloud/MLOps con plataforma seleccionada |
| RA2 | b | UD3 | UD4, UD5, UD8, UD9, UD10 | Laboratorio o capstone con entorno caracterizado |
| RA2 | c | UD3 | UD4, UD8, UD10, UD12 | Modelo elegido y justificado para el problema |
| RA2 | d | UD3 | UD4, UD6, UD8, UD10, UD12 | Aplicacion, notebook, API o pipeline ejecutable |
| RA2 | e | UD3 | UD4, UD6, UD8, UD10, UD12 | Metricas, analisis de resultados y limitaciones |
| RA3 | a | UD7 | UD5, UD12 | Proyecto que integre procesos y describa su mejora |
| RA3 | b | UD7 | UD5, UD6 | Arquitectura con APIs, cloud, pipelines u orquestacion |
| RA3 | c | UD7 | UD5, UD6, UD9 | Comparativa de caracteristicas del sistema integrado |
| RA3 | d | UD7 | UD6, UD12 | Riesgos, seguridad, privacidad y medidas de control |
| RA3 | e | UD7 | UD10, UD12 | Conclusion ejecutiva sustentada en metricas |
| RA4 | a | UD12 | UD7 | Estrategia, proceso y modelo de negocio identificados |
| RA4 | b | UD12 | UD7 | Analisis de usuarios, cliente, datos, activos y recursos |
| RA4 | c | UD7 | UD5, UD12 | Pipeline, API u orquestacion ligada a un requerimiento real |
| RA4 | d | UD12 | UD7, UD10 | Comparacion coste-beneficio, riesgos y alternativa descartada |

UD11 es optativa y no es evidencia primaria de ningun CE. UD2, UD4, UD8, UD9 y
UD10 amplian RA2, pero no obligan a crear una calificacion por cada notebook.

## Uso con Moodle y Seneca

1. Mantener esta matriz fuera del calculo de totales Moodle.
2. Al corregir, registrar solo los CE que demuestre realmente el instrumento.
3. Anotar el ID Moodle, el enlace a la entrega y la evidencia o defensa que
   fundamenta la decision.
4. Registrar en Seneca la nota del CE acreditado, aplicando los pesos de
   `PONDERACION_RA_SENECA_2026_2027.md`.
5. Filtrar por RA y comprobar que no quedan estados `NE`, `PE` o `NR` antes de
   declararlo cerrado.
6. Si un CE queda `NR`, proponer una evidencia equivalente individual; no
   sustituirlo por una nota comun de grupo.

## Limites

La matriz no genera una calificacion automatica ni sustituye las rubricas. Solo
asegura cobertura, trazabilidad y una decision de acreditacion verificable.

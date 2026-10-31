# Entrega de los «hazlo tú» de gráficas

Hay **dos actividades diferentes**, que se entregan cuando el profesor active cada una. La segunda corresponde a otra clase. Puedes trabajar con una pareja, pero cada estudiante completa y entrega su propio cuaderno.

**Valoración:** seguimiento hecho/no hecho, sin nota numérica de acierto. Entregar registra participación/asistencia; se revisa además qué apartados están completos. Si algo falla, registra el error y lo intentado. Puedes completar lo pendiente después de clase según indique el profesor. No se aplican los porcentajes de la rúbrica general de UD2 a estas actividades.

## 1. Gráficas estáticas — piloto del caso

La entrega de este bloque se define en [caso-informe-personal.md](caso-informe-personal.md): cuaderno `informe_personal.ipynb` y `salidas_estaticas/panel_personal.png`/`.svg`.

El cuaderno de trabajo es [02_matplotlib_hazlo_tu.ipynb](02_matplotlib_hazlo_tu.ipynb). La estructura del ZIP, la checklist y la valoración están en la ficha del caso; no se duplican aquí.

## 2. Gráficas interactivas — otra clase, después de Plotly

Cuaderno: [03_plotly_hazlo_tu.ipynb](03_plotly_hazlo_tu.ipynb).

Sube a la tarea Moodle **«Gráficas interactivas — hazlo tú»** un único `apellido_nombre_interactivas.zip` con:

```text
apellido_nombre_interactivas/
├── 03_plotly_hazlo_tu.ipynb
└── salidas_interactivas/
    └── dispersion_interactiva.html
```

Lista de control:

- [ ] Nombre, fecha, intérprete y versiones anotados.
- [ ] Histograma, dispersión con hover, facetas y boxplot ejecutados.
- [ ] Registro real de hover, ocultar/mostrar grupos en la leyenda, zoom y restauración.
- [ ] HTML **autónomo**, con Plotly.js incluido (`include_plotlyjs=True`), abierto en un navegador sin depender de CDN.
- [ ] Explicada una ventaja y una limitación respecto a la gráfica estática del mismo conjunto de datos.
- [ ] Ticket y registro de lo completado/pendiente rellenos.

No hace falta exportar imágenes de Plotly ni instalar Kaleido. El HTML puede ocupar varios MB porque incluye la librería. Si Moodle limita el tamaño, comunícalo al profesor; no cambies a CDN sin indicarlo ni sustituyas el HTML por una captura.

## 3. Registro y declaración (dentro de cada cuaderno)

Rellena la celda final de Markdown con esta información:

| Apartado | Completo / en curso / pendiente | Qué he probado o qué falta |
|---|---|---|
| Preparación del entorno | | |
| Gráficos del cuaderno | | |
| Modificaciones e interpretación | | |
| Exportación y apertura externa | | |

**Ayuda utilizada:** compañero/a, documentación, IA u otra fuente. Indica para qué la usaste y qué comprobaste tú. Si no usaste ayuda, escribe «Ninguna». No entregues solo imágenes ni código que no puedas explicar.

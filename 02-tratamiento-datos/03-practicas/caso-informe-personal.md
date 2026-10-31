# Caso — Informe de personal

**Piloto de Matplotlib · 2 horas · trabajo en parejas, entrega individual**

## 1. Contexto

La dirección de una empresa de servicios digitales va a revisar su política salarial y la carga de trabajo. Te pide un **informe visual breve** para apoyar la decisión.

No quieren una colección de gráficos: quieren saber **qué está pasando y qué harían**.

## 2. Decisión que hay que tomar

Al terminar, deberías poder responder con evidencia:

- ¿Qué departamento cobra más y conviene mirar la media o la mediana?
- ¿Hay salarios extremos que distorsionan la comparación?
- ¿La experiencia se asocia con un salario mayor?
- ¿Hay meses con más carga de trabajo?
- ¿Qué recomendarías para la próxima revisión?

## 3. Datos

El cuaderno genera dos tablas sintéticas. No hay que descargar nada y no contienen personas reales.

**`empleados`** (240 filas):

| Columna | Tipo | Descripción |
|---|---|---|
| `id` | entero | Identificador |
| `departamento` | texto | Datos, Web, Sistemas o Soporte |
| `edad` | entero | Años |
| `experiencia` | entero | Años de experiencia |
| `salario` | decimal | Salario mensual en euros |
| `horas_semana` | decimal | Horas semanales |
| `satisfaccion` | decimal | Valoración de 1 a 10 |

**`mensual`** (12 filas):

| Columna | Tipo | Descripción |
|---|---|---|
| `mes` | entero | 1 a 12 |
| `proyectos` | entero | Proyectos activos |
| `soporte` | entero | Incidencias de soporte |
| `horas_extra` | decimal | Horas extra acumuladas |

## 4. Qué tienes que hacer, en este orden

1. **Evolución mensual.** Representa `proyectos` y `soporte` a lo largo de los 12 meses. Indica qué meses se desvían y qué decisión permitiría tomar.
2. **Comparación por departamento.** Compara el salario entre departamentos. La dirección duda entre media y mediana: muestra ambas o justifica una.
3. **Distribución y valores extremos.** Analiza la distribución salarial y detecta posibles outliers. Usa dos representaciones complementarias.
4. **Experiencia y salario.** Estudia si la experiencia se asocia al salario. No afirmes causalidad.
5. **Panel 2×2.** Reúne los cuatro gráficos en una sola figura, con títulos, unidades y leyendas legibles.
6. **Interpretación.** Escribe tres frases: qué muestra cada bloque, qué no permite concluir y una recomendación para la dirección.
7. **Ticket.** Completa el registro final del cuaderno.

Puedes usar líneas, barras, histograma, dispersión o boxplot. **Elige y justifica** por qué cada uno responde a su pregunta.

## 5. Entregables

Un único ZIP:

```text
apellido_nombre_informe_personal/
├── informe_personal.ipynb
└── salidas_estaticas/
    ├── panel_personal.png
    └── panel_personal.svg
```

El cuaderno debe estar ejecutado **en orden**, con las salidas visibles. El panel debe abrirse correctamente fuera del notebook.

## 6. Checklist antes de entregar

- [ ] El cuaderno se ejecuta de principio a fin sin errores.
- [ ] Cada gráfico responde a la pregunta de su situación.
- [ ] El tipo de gráfico está justificado en una frase.
- [ ] Títulos, ejes, unidades y leyendas son legibles.
- [ ] No hay ejes truncados ni escalas que exageren diferencias.
- [ ] El panel 2×2 está exportado en PNG y SVG.
- [ ] Hay tres frases de interpretación y una recomendación.
- [ ] El ticket y el registro de ayuda están completos.
- [ ] Si has usado IA, indicas para qué y qué comprobaste.

## 7. Entrega y valoración

- **Moodle**, al final de la sesión o cuando indique el profesor.
- **Valoración binaria:** hecho / no hecho. Entregar acredita asistencia; completo acredita seguimiento.
- No es una prueba: no se corrige el acierto ni se pone nota numérica.
- Si no terminas, puedes completarlo después y subirlo igualmente.

## 8. Reglas de trabajo

- Trabaja en pareja, pero **cada estudiante entrega su propio cuaderno**.
- Los datos son sintéticos: no los presentes como una empresa real.
- No hace falta usar datos externos ni instalar nada nuevo.
- Primero la pregunta y la decisión; después el código.
- Si algo falla, anota el error y lo intentado; no borres la celda.

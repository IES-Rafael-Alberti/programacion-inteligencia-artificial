# Checklist de publicación Moodle — UD0 y UD1 — PIA 2026/2027

Los archivos preparados para subir están organizados por unidad en `Moodle/00-UD0/`
y `Moodle/01-UD1/`. Consulta el índice `Moodle/README.md` y los README de cada
subcarpeta para relacionar los archivos con sus fuentes.

## UD0 — Inicio del módulo

- [ ] Crear o completar la sección inicial/UD0 del curso.
- [ ] Publicar la presentación desde `Moodle/00-UD0/01_Presentacion_del_modulo.pdf`.
- [ ] Publicar la guía de acceso desde `Moodle/00-UD0/02_Como_trabajar_los_materiales.pdf`.
- [ ] Publicar las normas desde `Moodle/00-UD0/03_Normas_de_entrega_y_uso_de_IA.pdf`.
- [ ] Crear los foros de avisos y dudas técnicas.
- [ ] Crear la actividad Feedback anónima `Encuesta inicial PIA`, según
  `CONFIGURACION_DIAGNOSTICO_INICIAL_PIA_2026_2027.md`.
- [x] Importar el cuestionario técnico inicial GIFT, no evaluable y excluido del
  calificador.
- [ ] Publicar como acceso principal el portal GitHub Pages:
  `https://ies-rafael-alberti.github.io/programacion-inteligencia-artificial/`.
- [ ] Recordar que no deben subirse claves, tokens, datos personales ni datasets
  no autorizados.

## UD1 — Fundamentos de Python

### Materiales para publicar

- [ ] Crear la sección `UD1 - Fundamentos de Python`.
- [ ] Publicar la documentación preparada en `Moodle/01-UD1/01-documentacion/`.
- [ ] Publicar o confirmar el notebook inicial desde `Moodle/01-UD1/02-ejemplos/`.
- [ ] Publicar el notebook de estructuras adicionales desde
  `Moodle/01-UD1/02-ejemplos/` para la siguiente sesión.
- [ ] Publicar el notebook de repaso desde `Moodle/01-UD1/03-practicas/` como
  recurso sin calificación.
- [ ] Si se alcanza POO en la siguiente sesión, publicar el ejemplo y los
  ejercicios de POO; si no, dejarlos preparados para una sesión posterior.
- [ ] Indicar Pixi `default` para JupyterLab y Google Colab como alternativa
  temporal si un equipo no puede preparar Pixi.

### Preparar sin publicar como evaluable

- [ ] Crear la categoría `UD1 - Fundamentos Python` con media ponderada.
- [ ] Crear la subcategoría `UD1 - Cuestionarios Moodle`.
- [ ] Previsualizar el cuestionario base `01-fundamentos-python/04-evaluacion/cuestionario-base.gift`.
- [ ] Mantener oculto el cuestionario hasta haber trabajado Python y NumPy.
- [ ] Cuando se impartan POO, NumPy y EDA, revisar los GIFT específicos e importar
  solo los cuestionarios que se decida activar; mantenerlos no evaluables u ocultos
  hasta concretar sus condiciones.
- [ ] Aplicar al activar los instrumentos los pesos previstos: práctica de Python
  y NumPy 60 %, comparativa de lenguajes 20 % y cuestionarios 20 %.

## Comprobación con cuenta de prueba

- [ ] La cuenta ve las secciones UD0 y UD1 sin permisos de edición.
- [ ] Los recursos aparecen en la unidad y sección previstas.
- [ ] Los enlaces y archivos descargables se abren correctamente.
- [ ] Los notebooks se pueden descargar para abrirlos y ejecutarlos.
- [ ] No se publica ninguna solución ni material de `99-profesor/`.
- [ ] Los ítems de calificación no duplican tareas o cuestionarios.
- [ ] El total de Moodle se identifica como informativo; Séneca mantiene la nota
  oficial por RA/CE.

## Ciclo de vida del paquete temporal

`Moodle/` está excluida de Git y contiene solo copias preparadas para subir. Tras
subir los recursos y comprobarlos en Moodle, se puede eliminar el contenido
local. Para reponerlo, generar de nuevo los PDF desde sus fuentes Markdown y
copiar los notebooks y el GIFT desde sus fuentes mantenidas en el repositorio.

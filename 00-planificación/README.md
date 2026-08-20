# Prompts base para futuras reformas de módulos

Esta carpeta conserva una copia de los prompts usados como arranque de la reforma de **Sistemas de Big Data**, para poder reutilizar el mismo método en módulos como:

- Programación de Inteligencia Artificial.
- Desarrollo Web en Entorno Servidor.

## Prompts semilla

Los prompts que parecen formar el flujo inicial reutilizable son:

1. `00_prompt_inventario_material_modulo_BASE.md`
   - Define el criterio general de inventario.
   - Sirve como contrato base para decidir qué catalogar y qué excluir.

2. `01_prompt_inventario_p1_barrido_BASE.md`
   - Ejecuta el primer barrido bruto del material.
   - Produce un inventario provisional revisable.

3. `02_prompt_inventario_p2_consolidacion_BASE.md`
   - Consolida el inventario bruto.
   - Genera el inventario final que debe guiar la reorganización.

4. `04_prompt_reorganizacion_materia_BASE_DESDE_PIA.md`
   - Es el prompt de reorganización adaptado para PIA.
   - Para DWES debe adaptarse cambiando nombre del módulo, código, unidades, ruta de destino y criterios específicos.

## Qué adaptar por módulo

Antes de usar estos prompts en otro módulo, revisar y sustituir:

- Nombre completo del módulo.
- Código corto del módulo, si se usa en nombres de carpetas o informes.
- Número y nombre de unidades.
- Ruta origen y ruta destino.
- Tecnologías propias del módulo.
- Criterios de exclusión específicos si hay entregas, correcciones o artefactos distintos.

## Prompts no incluidos como semilla

No se copian aquí como flujo inicial principal:

- `prompt_alineacion_curricular_sbd_bigdata_aplicado.md`
- `prompt_mejora_contenidos_sbd_post_alineacion.md`

Motivo: parecen prompts creados durante la reforma de SBD, después del inventario y la reorganización inicial. Pueden servir como referencia si en PIA o DWES aparece una necesidad equivalente, pero no son imprescindibles para arrancar.

## Flujo recomendado

1. Ejecutar inventario base.
2. Ejecutar primer barrido.
3. Consolidar inventario.
4. Con el inventario final, adaptar el prompt de reorganización al módulo concreto.
5. Tras reorganizar, crear un documento vivo de estado y pendientes equivalente a `ESTADO_ACTUAL_Y_PENDIENTES.md`.

## Plantillas transversales

Además de los prompts de reorganización, esta carpeta contiene plantillas para trasladar posteriormente a la programación didáctica y a los documentos de aula:

- `plantillas/plantilla_declaracion_uso_ia.md`: declaración de uso de IA adaptada a PIA.
- `plantillas/politica_uso_ia_pia.md`: política transversal para permitir IA con trazabilidad, verificación y defensa.
- `plantillas/normas_trabajo_equipo_entregas.md`: base para regular trabajo en equipo, coevaluación y entregas tardías.

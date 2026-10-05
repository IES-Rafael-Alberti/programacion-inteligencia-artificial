# Handoff PIA — próxima sesión (2026-10-05)

Este documento es el punto de reanudación portable para abrir PIA desde otro
ordenador. La hoja de ruta completa sigue en `ESTADO_ACTUAL_Y_PENDIENTES.md` y el
flujo de publicación, en `ESTRATEGIA_REPOSITORIOS.md`.

## Estado del módulo y clase siguiente

- La segunda clase ya se impartió: cuestionario y ejercicios básicos de Python;
  se llegó hasta las estructuras de datos básicas. En el grupo hay alumnado sin
  experiencia previa en Python, así que conviene comprobar comprensión antes de
  acelerar.
- El guion de la tercera clase está en
  `01-fundamentos-python/99-profesor/GUION_TERCERA_CLASE_PIA_UD1.md`.
- Núcleo de la sesión: `Counter`, `defaultdict` y `deque`, con ejemplos y una
  actividad breve de conteo y agrupación. La introducción a POO es opcional y se
  hace solo si queda tiempo: clase/instancia, `__init__`, `self` y un método.
- La conexión con PyTorch/PyTorch Lightning es motivacional: `nn.Module` y
  `Dataset` reutilizan ideas de clases e interfaces. No instalar PyTorch ni
  impartir todavía esos marcos en UD1.

## Comprobaciones para mañana

1. En Moodle, confirmar que está visible el notebook de estructuras adicionales:
   `Moodle/01-UD1/02-ejemplos/02_Estructuras_datos_adicionales.ipynb`.
2. Si se llega a POO, publicar o abrir los recursos de POO de Moodle:
   `Moodle/01-UD1/01-documentacion/06_Orientacion_objetos_Python.pdf`,
   `Moodle/01-UD1/02-ejemplos/03_Orientacion_objetos_python.ipynb` y, si procede,
   `Moodle/01-UD1/03-practicas/02_Ejercicios_orientacion_objetos.ipynb`.
3. Mantener el bloque POO y sus ejercicios ocultos/no asignados si no se alcanza.
4. Los GIFT `cuestionario-poo-python.gift`, `cuestionario-numpy.gift` y
   `cuestionario-eda-numpy.gift` son fuentes docentes con respuestas; todavía
   requieren validación/importación y no deben publicarse en GitHub Pages.

## Paquete Moodle y fuentes

- `Moodle/00-UD0/`: presentación, guía de inicio, normas y diagnóstico inicial.
- `Moodle/01-UD1/`: documentación en PDF, ejemplos y prácticas separados.
- `Moodle/` está excluida de Git y es temporal. Los PDF se regeneran desde
  Markdown; los notebooks y GIFT se copian desde sus fuentes. Después de subir y
  comprobar los recursos, se puede borrar el paquete entero.
- El cuestionario técnico inicial ya se importó a Moodle y no es evaluable. El
  estado del cuestionario base de Python y de la encuesta Feedback debe
  confirmarse en la plataforma, no inferirse a partir de archivos preparados.

## Repositorios y sincronización entre ordenadores

- Último estado verificado: `teacher` sincronizada con `teacher/main`; `main`
  sincronizada con `origin/main`.
- Para continuar desde el ordenador receptor, tras transferir los archivos
  generales con el procedimiento habitual, ejecutar:

  ```bash
  git fetch --all --prune
  git switch teacher
  git pull --ff-only teacher main
  ```

- No copiar ni subir el paquete temporal `Moodle/`, cachés de Graphify ni las
  carpetas locales `.codex/` y `.opencode/`.

## Pendientes del módulo

- Confirmar qué materiales de UD0/UD1 ya son visibles en Moodle y decidir si se
  publican los 13 PDF preparados.
- Configurar y verificar en Séneca los pesos RA/CE; montar y probar el
  calificador Moodle.
- Revisar el contenido de los tres materiales retirados del árbol actual
  público: los notebooks `P2_PyCaret_sol.ipynb` y `P3_Modelo_sol.ipynb`, y
  `Transformers_Test_Moodle.gift`. Después decidir si se solicita purgar esos
  archivos de commits públicos anteriores; la purga reescribe el historial y
  requiere coordinación de clones.
- Las comprobaciones Windows/macOS de Pixi se harán cuando haya equipos
  disponibles.

## Tarea SBD para una sesión futura

El estado de SBD se consulta en
`/datos/RafaelAlberti/RafaelAlberti26_27/Modulos/SBD/00-planificacion/ESTADO_ACTUAL_Y_PENDIENTES.md`.
Antes de crear un guion nuevo, revisar la presentación y las guías ya existentes
de las primeras sesiones; adaptar solo lo que falte y comprobar el Moodle real.

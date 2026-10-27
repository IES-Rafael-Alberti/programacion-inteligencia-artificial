# Entrega — Taller de entornos de Python

> Documento de entrega del taller «hazlo tú». Define **exactamente qué tienes que
> entregar** para que todos entreguemos lo mismo. Sigue esta guía y usa la plantilla;
> no hace falta adornos: hace falta que esté completo.

**Valoración:** binaria (hecho / no hecho) como evidencia de seguimiento.
No puntúa cuántos aciertos tienes: cuenta **qué bloque llegaste a probar de verdad**.
Un bloque que solo viste en una demo no está hecho.

## Qué hay que entregar (lista de control)

Al terminar (o en el punto que alcances), adjunta en Moodle **un único documento**
(`registro-entornos.md` en Markdown o PDF) **más los archivos del código y
dependencias**, siguiendo esta lista. No adjuntes `.venv/`, `.pixi/` ni la
instalación de conda.

- [ ] **Cabecera:** nombre, fecha y equipo (si trabajas en pareja).
- [ ] **Estado por bloque:** para cada herramienta (venv+pip, uv, conda, Pixi),
      marca si está `completo`, `en curso` o `no iniciado`.
- [ ] **Evidencia por bloque:** completar la tabla de cada herramienta (plantilla
      más abajo). La evidencia mínima de un bloque completo es **su prueba
      ejecutada** (`Total: 60` / `PRUEBA OK`) y **su modificación comprobada**
      (p. ej. total `70`).
- [ ] **Tabla de comparación** (sección 5 del taller): una ventaja, un
      inconveniente y un uso para cada herramienta.
- [ ] **Decisiones** (4 casos del taller): tu elección y una razón por caso.
- [ ] **Código y dependencias:** `analisis.py` final + `requirements.txt`,
      `pyproject.toml`/`uv.lock`, `environment.yml`/`environment-exportado.yml` y
      `pixi.toml`/`pixi.lock`, identificados por bloque. Como archivos adjuntos o
      bloques de código dentro del documento. **Sin `.venv/` ni `.pixi/`.**
- [ ] **Ampliación (opcional):** si la haces, `resumen.png` + comando usado.

## Plantilla del registro

Copia este bloque, rellénalo y elimina las instrucciones en cursiva.

```markdown
# Registro — Taller de entornos de Python

**Nombre:** ________________
**Fecha:** ________________

## Estado global

| Bloque | Estado (completo / en curso / no iniciado) |
|---|---|
| venv + pip | |
| uv | |
| conda | |
| Pixi | |

## 1. venv + pip

_Completa la tabla si empezaste el bloque._

| Evidencia | Valor |
|---|---|
| ¿Instalado o ya estaba? / versión | |
| Comando de creación y activación | |
| Ruta de Python (_sys.executable_) | |
| Salida (`Total`, `Por grupo`, `PRUEBA OK`) | |
| Cambio realizado (p. ej. total 70) | |
| `requirements.txt` | |

## 2. uv

| Evidencia | Valor |
|---|---|
| ¿Instalado o ya estaba? / versión | |
| Comando de creación del proyecto | |
| Ruta de Python | |
| Salida (`Total`, `PRUEBA OK`) | |
| Dependencia añadida (rich) | |
| Archivos del manifiesto | |
| Comando para reconstruir desde el lock | |

## 3. conda

| Evidencia | Valor |
|---|---|
| ¿Instalado o ya estaba? / versión | |
| Comando de creación del entorno | |
| Ruta de Python (prefijo de `pia-taller-conda`) | |
| Salida (`Total`, `PRUEBA OK`) | |
| Cambio en el YAML (rich) y exportación | |
| Solver usado | |

## 4. Pixi

| Evidencia | Valor |
|---|---|
| ¿Instalado o ya estaba? / versión | |
| Comando de creación del proyecto | |
| Ruta de Python (en `.pixi/envs/default`) | |
| Salida (`Total`, `PRUEBA OK`) | |
| Tarea `analizar` creada | |
| Comando que instala desde el lock | |

## 5. Comparación

| Opción | Ventaja | Inconveniente | Cuándo la elegiría |
|---|---|---|---|
| venv + pip | | | |
| uv | | | |
| conda | | | |
| Pixi | | | |

## 6. Decisiones (una elección + razón)

1. Script pequeño en un equipo con Python: ________________
2. Proyecto solo Python con lock: ________________
3. Entorno de experimentación con paquetes nativos: ________________
4. Proyecto del módulo reproducible: ________________

## Incidencias (opcional pero útil)

| Error exacto | Intento de solución | Estado final |
|---|---|---|
| | | |

## Ampliación (opcional)

- Comando / archivo generado: ________________
```

## Reglas rápidas

- Los bloques realizados **deben tener su prueba ejecutada en el documento**
  (comando y salida). Sin salida, no es evidencia.
- Los bloques no iniciados se marcan y ya está: **no inventes** una salida; el
  registro es de seguimiento.
- Si el equipo no te dejó completar algo, anota la restricción (p. ej. «sin
  permisos», «red lenta») en `Incidencia` y en el estado.
- Trabajas en pareja para resolver dudas, pero **cada uno entrega su propio
  registro** con lo que ejecutó.

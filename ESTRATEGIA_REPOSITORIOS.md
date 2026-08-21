# Estrategia de repositorios y ramas — PIA

Fecha: 2026-08-21

## Situación actual

El proyecto se mantiene desde un único directorio de trabajo, con dos repositorios remotos:

```text
origin  → https://github.com/IES-Rafael-Alberti/programacion-inteligencia-artificial
          Repositorio público del alumnado y GitHub Pages.

teacher → https://github.com/IES-Rafael-Alberti/programacion-inteligencia-artificial-docente
          Repositorio privado del profesorado.
```

El repositorio privado contiene la rama `main` docente, publicada desde la rama local `teacher`.
Incluye planificación, material `99-profesor`, archivo histórico, Graphify y notas internas.

El repositorio público conserva su propia rama `main`, independiente del historial docente.

## Decisión de trabajo

La fuente de verdad será la rama local `teacher`.

El flujo normal será:

1. Trabajar y consolidar cambios docentes en `teacher`.
2. Subir esos cambios al remoto privado:

   ```bash
   git push teacher teacher:main
   ```

3. Cuando un cambio sea apto para el alumnado, generar una exportación pública filtrada.
4. Revisar la exportación sin planificación, soluciones, material de profesor, secretos ni salidas locales.
5. Publicar únicamente esa exportación en `origin/main`.

## Procedimiento operativo habitual

### Trabajo docente

Comprobar la rama antes de empezar:

```bash
git switch teacher
git status --short
```

Después de trabajar, guardar los cambios en commits normales y subirlos al repositorio privado:

```bash
git add <archivos-correspondientes>
git commit -m "<mensaje del cambio>"
git push teacher teacher:main
```

### Publicar un cambio para el alumnado

No se mezcla `teacher` completo con `main`. Se seleccionan sólo los archivos que deben ser públicos.

Desde `teacher`, anotar las rutas publicables. Después cambiar a la rama pública local:

```bash
git switch main
git status --short
```

Traer desde `teacher` únicamente esas rutas:

```bash
git restore --source=teacher -- \
  docs/ \
  docs/unidades/ud03.md \
  03-machine-learning/01-teoria/README.md
```

El ejemplo anterior es ilustrativo: deben sustituirse las rutas por las que realmente correspondan
al cambio. Revisar siempre el diff antes de confirmar:

```bash
git diff --stat
git diff --check
git diff
```

Validar la publicación pública:

```bash
mkdocs build --strict
python scripts/check_public_unit_links.py
git ls-tree -r --name-only HEAD | rg -i \
  '99-sensible|99-profesor|soluci|profesor|docente|graphify-out|00-planificación'
```

La última orden no debe devolver rutas sensibles. Si todo es correcto:

```bash
git add <archivos-publicables>
git commit -m "docs: update student materials"
git push origin main
git switch teacher
```

### Qué hacer si el cambio afecta a ambos repositorios

Se hacen dos commits independientes:

1. El commit completo o docente se hace en `teacher` y se sube con `git push teacher teacher:main`.
2. El subconjunto público se copia selectivamente a `main`, se valida y se sube con `git push origin main`.

El segundo commit puede tener un mensaje relacionado, pero no debe incluir soluciones ni rutas privadas.

### Comprobación de estado al cerrar la sesión

```bash
git status --short
git branch -vv
git log --oneline --decorate -3 teacher
git log --oneline --decorate -3 main
```

La rama `teacher` debe seguir `teacher/main` y `main` debe seguir `origin/main`.

## Papel de `public-students`

La rama local `public-students` es una instantánea pública de preparación. Tiene historial independiente
y no debe utilizarse como rama habitual de desarrollo docente.

Puede regenerarse cuando cambie el contenido público, pero no se debe hacer un `merge` de `teacher`
en ella: eso podría introducir material privado. La publicación pública debe proceder siempre de una
exportación filtrada y revisada.

## Qué puede pasar al repositorio del alumnado

- Teoría, ejemplos, actividades y enunciados publicables.
- Notebooks iniciales y fixtures pequeños.
- Evaluaciones y rúbricas diseñadas para el alumnado.
- `README`, `docs`, `pixi.toml` y `pixi.lock` cuando sean apropiados.
- Enlaces y rutas que existan realmente en el repositorio público.

## Qué debe permanecer sólo en `teacher`

- `00-planificación`.
- `99-profesor` y soluciones.
- Correcciones, entregas de estudiantes y resultados internos.
- `90-archivo-historico`, salvo que se decida publicar algún recurso concreto.
- `graphify-out` y demás salidas de análisis interno.
- Claves, `.env`, datos privados, modelos locales y configuraciones personales.
- Entornos instalados, cachés, `site` generado y `node_modules`.

## Reglas de seguridad antes de publicar

Antes de actualizar `origin/main`:

```bash
git status --short
git ls-tree -r --name-only HEAD | rg -i '99-sensible|99-profesor|soluci|profesor|docente|graphify-out|00-planificación'
mkdocs build --strict
python scripts/check_public_unit_links.py
```

La búsqueda de rutas sensibles debe devolver cero resultados. Los secretos no se deben solucionar
añadiendo excepciones puntuales: deben quedar fuera de la exportación y fuera del historial público.

## Regla práctica

No se mantienen dos copias manuales del proyecto. Se mantiene un único directorio y se decide en cada
publicación qué parte del trabajo docente merece pasar al repositorio público. El repositorio privado es
la copia completa; el público es una publicación filtrada para el alumnado.

## Trabajo con dos ordenadores y Unison

La organización prevista es:

- GitHub coordina el repositorio PIA, sus commits, ramas e historial.
- Unison sincroniza materiales generales y otros ficheros que no son exclusivamente docentes.
- El disco duro se utiliza como copia de seguridad, no como ubicación habitual de trabajo.

Aunque el disco duro no se modifique normalmente, Unison puede sincronizar `.git` si el perfil no lo
excluye. En ese caso, una copia completa conserva todas las ramas, el historial y la configuración de
los remotos, no sólo la rama activa.

### Protocolo al cambiar de ordenador

Antes de empezar en casa o en el instituto:

```bash
git switch teacher
git pull teacher main
git fetch origin
```

Después de trabajar y antes de cambiar de equipo:

```bash
git status
git push teacher teacher:main
```

Si se han preparado cambios públicos, subir también `origin/main` después de validarlos según el
procedimiento anterior.

Ejecutar Unison sólo después de cerrar editores, notebooks, Jupyter, procesos de Pixi y operaciones Git.
En el segundo ordenador, sincronizar primero con Unison y actualizar después el repositorio desde GitHub.

### Reglas para evitar conflictos

- Trabajar sólo en uno de los dos ordenadores cada vez.
- No modificar simultáneamente el mismo repositorio desde ambas copias.
- No usar el disco duro como copia de trabajo ordinaria.
- Revisar el perfil de Unison para saber si incluye `.git`; buscar exclusiones como `ignore = Name .git`
  o `ignore = Path .git/*`.
- Mantener excluidos los artefactos regenerables y pesados, salvo que exista una razón concreta para
  respaldarlos:

  ```text
  .pixi/
  site/
  .opencode/node_modules/
  __pycache__/
  ```

GitHub debe ser la autoridad para el código y sus ramas. Unison debe ser la autoridad de sincronización
para los materiales generales que no tengan un flujo Git propio.

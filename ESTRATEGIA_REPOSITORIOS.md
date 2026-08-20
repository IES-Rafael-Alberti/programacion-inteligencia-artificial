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
git ls-tree -r --name-only public-students | rg -i '99-sensible|99-profesor|soluci|profesor|docente|graphify-out|00-planificación'
mkdocs build --strict
python scripts/check_public_unit_links.py
```

La búsqueda de rutas sensibles debe devolver cero resultados. Los secretos no se deben solucionar
añadiendo excepciones puntuales: deben quedar fuera de la exportación y fuera del historial público.

## Regla práctica

No se mantienen dos copias manuales del proyecto. Se mantiene un único directorio y se decide en cada
publicación qué parte del trabajo docente merece pasar al repositorio público. El repositorio privado es
la copia completa; el público es una publicación filtrada para el alumnado.


# Scripts — Generación de Imágenes y Backpropagation

## Scripts en esta carpeta

| Script | Descripción |
|--------|-------------|
| `generate_images_cap01.py` | Genera imágenes del **Cap. 01** (Introducción RNA) → `../docs/images/` |
| `generate_images_cap02.py` | Genera imágenes del **Cap. 02** (RNA Artificiales) → `../docs/images/` |
| `generate_images_cap03.py` | Genera imágenes del **Cap. 03** (Representación Matemática) → `../docs/images/` |
| `generate_images_cap04.py` | Genera imágenes del **Cap. 04** (Tensores y Funciones) → `../docs/images/` |
| `generate_images_cap05.py` | Genera imágenes del **Cap. 05** (Activación y Pérdida) → `../docs/images/` |
| `generate_images_cap06.py` | Genera imágenes del **Cap. 06** (Derivadas y Gradientes) → `../docs/images/` |
| `generate_images_cap07.py` | Genera imágenes del **Cap. 07** (Gradiente Descendente) → `../docs/images/` |
| `generate_images_cap08.py` | Genera imágenes del **Cap. 08** (Backpropagation) → `../docs/images/` |
| `backpropagation.py` | Implementación de backpropagation from scratch |
| `gradient_descent_animation.py` | Animación matplotlib del descenso de gradiente |

## Regenerar todas las imágenes

```bash
cd scripts/
for cap in $(seq -w 1 8); do
    python generate_images_cap${cap}.py
done
```

> Las imágenes se guardan en `../docs/images/` y son referenciadas por los capítulos en `../docs/`.

## Documentación relacionada

- 📄 **Cap. 08 — Backpropagation** → [`../docs/UD4_Capitulo_08_Backpropagation.md`](../docs/UD4_Capitulo_08_Backpropagation.md)
- 📄 **Progreso de generación** → [`../docs/PROGRESO_GENERACION_IMAGENES.md`](../docs/PROGRESO_GENERACION_IMAGENES.md)

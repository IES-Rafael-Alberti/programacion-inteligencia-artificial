# Índice combinado de NumPy — a partir de la biblioteca local

Bibliografía docente de apoyo para la UD1 de PIA. El índice cruza los manuales
que ya están en `/datos/RafaelAlberti/RafaelAlberti26_27/Libros/` y los organiza
en un temario de NumPy lo más completo posible.

## Libros considerados (los que tratan NumPy)

| Ref | Libro | Autor / ed. | Formato | Ruta (curso 26_27) |
|-----|-------|-------------|---------|---------------------|
| **PDSH** | Python Data Science Handbook (2.ª ed., 2023) | Jake VanderPlas | EPUB | `Libros/PandasNumpyDataViz/PythonDataScienceHandbook-2023.epub` |
| **McK** | Python for Data Analysis (3.ª ed., 2022) | Wes McKinney | EPUB | `Libros/PandasNumpyDataViz/Python4DataAnalysis-DataWranglingWithPandasNumPyJupyter-2022.epub` |
| **NBeg** | Python NumPy For Beginners (2022) | AI Publishing | EPUB | `Libros/PandasNumpyDataViz/PythonNumPyForBeginners-2022.epub` |
| **MLBeg** | Machine Learning for Beginners … NumPy, Pandas, Matplotlib, Seaborn, SKlearn, TensorFlow 2 (2020) | AI Publishing | EPUB | `Libros/PythonMachineLearning4Beginners…-2020.epub` |
| **EM4DS** | Essential Math for Data Science (2022) | Hadrien Jean | PDF | `RafaelAlberti26_27/EssentialMath4DataScience.pdf` |
| **PDS** | Python for Data Science (2022) | Yuli Vasiliev | EPUB | `Libros/Python4DataScience_Hands-OnIntroduction-2022.epub` |
| **Dummy** | Python for Data Science For Dummies (2.ª ed., 2019) | Mueller & Massaron | EPUB | `Libros/Python4DataScience4Dummies-2ndEd2019.epub` |
| **HdP** | Hands-On Data Analysis with Pandas (2019) | Stefanie Molin | PDF | `Libros/HandsOnDataAnalysisWithPandas-2019.pdf` |

> PDSH (VanderPlas) es el manual de referencia más completo y canónico para NumPy
> (Parte II íntegra). McK (McKinney) aporta lo que PDSH cubre de pasada: álgebra
> lineal, I/O de arrays y generación pseudoaleatoria. NBeg aporta práctica
> aplicada (CSV, estadística, red neuronal con NumPy) y EM4DS da el fundamento
> matemático. El resto son complementos según sea objetivo de ML o datos.

## Temario de NumPy combinado

### Bloque 0. Antes de NumPy

| Tema | Principal | Complementos | Qué hacen |
|------|-----------|--------------|-----------|
| Qué es NumPy y por qué | NBeg §1.1, PDSH (intro) | MLBeg §2.8.1 | Contexto, ventajas (arrays, velocidad, base del ecosistema). |
| Instalación y entorno | NBeg §1.2, PDSH (Preface) | Dummy C3 | Anaconda/Pixi, Colab, Jupyter. |

### Bloque 1. Fundamentos de arrays

| Tema | Principal | Complementos | Qué hacen |
|------|-----------|--------------|-----------|
| El objeto `ndarray` | PDSH C4-C5, McK §4.1 | HdP C1 | Definición, dimensiones, vista multidimensional. |
| Tipos de datos (`dtype`) | PDSH C4, McK §4.1 | NBeg §2.2 | Enteros/flotantes/bool/complejos, elegir precisión. |
| Crear arrays | PDSH C4, McK §4.1 | NBeg §2.3, MLBeg §3.2 | `array`, `arange`, `ones`, `zeros`, `eye`, `empty`, `random`, `linspace`. |
| Atributos de un array | PDSH C5 | — | `ndim`, `shape`, `size`, `dtype`, `itemsize`, `nbytes`. |
| Imprimir/mostrar arrays | NBeg §2.4 | — | Formateo de salida, precisiones de *repr*. |

### Bloque 2. Indexado y rebanado

| Tema | Principal | Complementos | Qué hacen |
|------|-----------|--------------|-----------|
| Indexado básico y slicing | PDSH C5, McK §4.1 | NBeg §3.3, MLBeg §3.4 | Acceso por posición, subarrays en 1D/2D. |
| Vistas vs. copias | PDSH C5 | NBeg §3.5 | Slicing como *view* (sin copia), método `copy`. |
| Reshape y transposición | PDSH C5, McK §4.1 | NBeg §3.2, MLBeg §3.3 | `reshape`, `ravel`, `transpose`, cambio de ejes. |
| Concatenación y splitting | PDSH C5 | — | `concatenate`, `vstack`, `hstack`, `split`. |
| Indexado booleano / máscaras | PDSH C9, McK §4.1 | — | Comparaciones, máscaras, operadores `& \| ~`. |
| Fancy indexing | PDSH C10, McK §4.1 | — | Selección con arrays de índices, combinado. |

### Bloque 3. Operaciones y funciones

| Tema | Principal | Complementos | Qué hacen |
|------|-----------|--------------|-----------|
| Ufuncs (funciones universales) | PDSH C6, McK §4.3 | NBeg §5.1, PDS §C3 | Aritmética, trigonométricas, logs/exp, valores absolutos, ufuncs especializadas. |
| Vectorización y rendimiento | PDSH C6, McK C4 | — | Por qué los bucles van lentos, `%timeit`, operaciones a nivel de array. |
| Agregaciones | PDSH C7, McK §4.4 | NBeg §4.1, HdP | `sum`, `min`, `max`, `mean`, `std`, `var`, con `axis`. |
| Broadcasting | PDSH C8, NBeg §3.4 | — | Reglas de expansión de dimensiones, ejemplos aplicados. |
| `where` y condicionales | McK §4.4 | PDS C3 | Lógica condicional como operación de array. |
| Reducción y `axis` | PDSH C7 | McK §4.4 | Operar a lo largo de ejes. |

### Bloque 4. Ordenación y estructuras avanzadas

| Tema | Principal | Complementos | Qué hacen |
|------|-----------|--------------|-----------|
| Ordenación | PDSH C11, McK §4.4 | NBeg §3.1 | `sort`, `argsort`, `partition`, orden por filas/columnas. |
| `unique` y lógica de conjuntos | McK §4.4 | NBeg §4.2 | `unique`, `in1d`, `intersect1d`, `setxor1d`. |
| Structured arrays / record arrays | PDSH C12 | — | Arrays con campos heterogéneos, `record`. |
| Álgebra lineal | McK §4.6, EM4DS C4 | NBeg §5.2, MLBeg §3.6 | `dot`/`matmul`, `inv`, `det`, `trace`, `eig`, resolver sistemas. |
| Fundamentos matemáticos (vectores/matrices, producto) | EM4DS C4 | — | Concepto de vector, matriz, transformación lineal aplicado con NumPy. |

### Bloque 5. Números aleatorios e I/O

| Tema | Principal | Complementos | Qué hacen |
|------|-----------|--------------|-----------|
| Generación pseudoaleatoria | McK §4.2, PDSH | NBeg §2.3, Dummy | `numpy.random`: seed, `rand`, `randn`, `randint`, «permutación». |
| I/O de arrays binarios | McK §4.5 | NBeg §3.6 | `save`, `load`, `savez`, binario `.npy`. |
| I/O de texto / CSV | NBeg §4.4 | McK §4.5 | `genfromtxt`, `loadtxt`, `savetxt`. |
| Random walks (aplicación) | McK §4.7 | — | Simulación de paseos aleatorios con arrays. |

### Bloque 6. Aplicaciones de ejemplo

| Tema | Principal | Complementos | Qué hacen |
|------|-----------|--------------|-----------|
| k-Nearest Neighbours | PDSH C11 | — | Uso de `argsort` para vecinos cercanos. |
| Estadística descriptiva aplicada | NBeg §4.1 | HdP, Dummy C13 | mean/median/std/correlación sobre arrays. |
| Red neuronal con NumPy | NBeg C6 | — | Feed-forward + backpropación usando arrays. |
| Visualización de arrays | NBeg §4.5 | PDSH C4 (Matplotlib) | Ploteo de arrays de 1D/2D con Matplotlib. |

## Libros según objetivo

- **Fundamentos y referencia canónica de NumPy:** PDSH (Parte II) + McK C4.
- **Práctica supervisada paso a paso:** NBeg (6 capítulos) y MLBeg C3.
- **Matemáticas detrás de NumPy:** EM4DS C4 (álgebra lineal) y McK §4.6.
- **NumPy dentro del flujo de datos/pandas:** HdP, PDS C3, Dummy C7/C9.
- **NumPy hacia ML/DL:** Raschka (ML with PyTorch & scikit-learn), Géron (Hands-On ML).

---

*Índice docente generado a partir de los manuales locales. Las referencias entre
paréntesis apuntan a capítulos (§) o secciones de cada libro según su tabla de
contenidos.*

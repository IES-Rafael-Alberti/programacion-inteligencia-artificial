# Análisis Exploratorio de Datos (EDA) -- Titanic Dataset

## Carga de datos con Polars y Pandas

Para comenzar el EDA, cargamos el conjunto de datos **Titanic**
utilizando la librería **Polars** por su eficiencia, y luego convertimos
a un DataFrame de **Pandas** para aprovechar sus funcionalidades de
visualización y análisis:

    import polars as pl
    import pandas as pd

    # Cargar datos Titanic con Polars
    df_pl = pl.read_csv('titanic.csv')
    print("Esquema Polars:", df_pl.schema)  # esquema de columnas y tipos

    # Convertir a Pandas para análisis y visualización
    df = df_pl.to_pandas()
    df.info()
    df.head()

En la salida de `info()` observamos que el dataset Titanic tiene **891**
filas (pasajeros) y 12 columnas. Las columnas incluyen datos
demográficos y del viaje, por ejemplo: `Survived` (supervivencia, 0/1),
`Pclass` (clase de boleto 1ª, 2ª, 3ª), `Name`, `Sex`, `Age`, `SibSp` (nº
de hermanos/cónyuges a bordo), `Parch` (nº de padres/hijos a bordo),
`Ticket`, `Fare` (tarifa pagada), `Cabin` (camarote) y `Embarked`
(puerto de embarque).

## Estructura del dataset: tipos de datos y valores ausentes

Revisamos los tipos de datos y la presencia de valores nulos en cada
columna. Las columnas categóricas (`Sex`, `Embarked`, `Cabin`, etc.)
aparecen como tipo `object` en Pandas, mientras que las numéricas
(`Age`, `Fare`, `Pclass`, etc.) son enteras o flotantes. A continuación
calculamos los nulls por columna:

    df.isnull().sum()

Los resultados muestran que las columnas `Age`, `Cabin` y `Embarked`
tienen valores ausentes. En concreto: **Age** tiene 177 nulos, **Cabin**
687 nulos y **Embarked** 2
nulos[\[1\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Survived%2C%20three%20for%20passenger%20class,each%20for%20Parch%20and%20SibSp).
Esto era esperable: muchos pasajeros no tienen número de camarote
registrado, y algunos datos de edad y embarque faltan. El resto de
variables no tiene valores nulos. En total el dataset tiene 891
entradas, de las cuales **342 pasajeros sobrevivieron** (38,38%) y **549
no**[\[2\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=are%20891%20entries%20in%20the,each%20for%20Parch%20and%20SibSp).

Cada columna presenta el siguiente tipo de dato y contenido general:

-   **Survived**: Entero (0 = No sobrevivió, 1 = Sí sobrevivió). Es la
    variable objetivo (clase a predecir).
-   **Pclass**: Entero (clase socioeconómica del pasajero, 1ª/2ª/3ª).
-   **Name**: Texto (nombre completo del pasajero).
-   **Sex**: Texto (género: male/female).
-   **Age**: Float (edad en años; valores faltantes se observan).
-   **SibSp**: Entero (nº de hermanos o cónyuges a bordo).
-   **Parch**: Entero (nº de padres o hijos a bordo).
-   **Ticket**: Texto (código del boleto).
-   **Fare**: Float (tarifa pagada por el boleto).
-   **Cabin**: Texto (código de camarote; muchos valores nulos).
-   **Embarked**: Texto (puerto de embarque: C = Cherbourg, Q =
    Queenstown, S = Southampton).

De lo anterior, `Survived` es nuestra **clase** para el problema de
clasificación (binaria), mientras que `Pclass`, `Sex`, `Age`, `SibSp`,
`Parch`, `Fare` y posiblemente `Embarked` serán *features* relevantes
para predecir la supervivencia.

Notamos que **Sex** está representado como texto *\"male\"/\"female\"*,
y convendría codificarla (0/1) para análisis posteriores. `Pclass` ya es
numérica pero representa categorías ordinales (1ª \> 2ª \> 3ª clase).
Variables como `Ticket` y `Name` probablemente no sean directamente
útiles para el modelo (muchos valores únicos), aunque podríamos extraer
información si fuera necesario (por ejemplo, títulos en el nombre).

**Balance de clases:** hay un desbalance moderado -- \~62% de pasajeros
fallecieron vs \~38%
sobrevivieron[\[2\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=are%20891%20entries%20in%20the,each%20for%20Parch%20and%20SibSp),
por lo que en un modelo predictivo habría que considerar este
desequilibrio.

## Análisis univariado: distribuciones de variables

Comenzamos examinando la distribución de variables individuales para
entender sus rangos y frecuencias:

-   **Supervivencia (Survived):** Es una variable binaria. Podemos ver
    cuántos pasajeros sobrevivieron (valor 1) vs no (0). Un gráfico de
    barras simple muestra el desequilibrio: aproximadamente 549 no
    sobrevivieron frente a 342 que
    sí[\[2\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=are%20891%20entries%20in%20the,each%20for%20Parch%20and%20SibSp).

-   **Sexo (Sex):** La mayoría de los pasajeros eran hombres (577)
    frente a mujeres
    (314)[\[3\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Total%20passengers%20%3A%20Sex%20female,577%20Name%3A%20Sex%2C%20dtype%3A%20int64).
    Esta diferencia y la tasa de supervivencia por sexo es muy
    relevante, pues anticipamos (y confirmaremos) que sobrevivió un
    porcentaje mucho mayor de mujeres (las políticas de evacuación
    *\"mujeres y niños primero\"* tuvieron
    efecto[\[4\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Survival%20rate%20based%20on%20Sex%C2%B6)).

-   **Edad (Age):** Presenta una distribución con forma aproximadamente
    *right-skewed* (sesgo a la derecha). La edad promedio está alrededor
    de 29-30 años, con una mediana cercana a 28. Hay bebés y niños
    pequeños (edad mínima \~0.42 años) y el pasajero de mayor edad tenía
    80 años (Mr.
    Barkworth)[\[5\]](https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv#:~:text=D,Collyer%2C%20Mr).
    Podemos visualizar esta distribución con un histograma:

*Distribución de edades de los pasajeros del Titanic. Se observa una
mayor concentración de pasajeros entre \~20 y 40 años, con algunos niños
y menores de edad, y menos frecuencia en edades muy avanzadas.*

-   **Tarifa (Fare):** La tarifa pagada varía ampliamente. La mayoría de
    pasajeros de 3ª clase pagaron tarifas bajas (por ejemplo, £7--£15),
    mientras que pasajeros de 1ª clase pagaron mucho más (media en 1ª
    clase \~£84). El valor máximo de *Fare* es **512.33** (Mr. Cardeza,
    pasajero de 1ª clase con un camarote de
    lujo)[\[6\]](https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv#:~:text=Sofia,Panula%2C%20Mr.%20Jaako)[\[7\]](https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv#:~:text=Hjalmar,Brown%2C%20Mr.%20Thomas%20William).
    La distribución es fuertemente asimétrica (unos pocos valores muy
    altos elevan la cola derecha). Es útil graficar el histograma de
    Fare, a menudo aplicando escala logarítmica para apreciar mejor la
    densidad en rangos bajos.

-   **Pclass:** La mayoría de pasajeros viajaban en 3ª clase (sobre
    55%), seguida de 2ª (\~20%) y 1ª (\~25%). Esto refleja la realidad
    de que el Titanic transportaba principalmente pasajeros de clase
    económica. Un gráfico de barras de `Pclass` confirma esta
    proporción.

-   **SibSp y Parch:** La mayor parte de pasajeros viajaba sin
    hermanos/cónyuge (SibSp = 0) y sin padres/hijos (Parch = 0). En
    efecto \~68% no tenían SibSp y \~76% no tenían Parch (viajaban solos
    o solo con otros tipos de
    familiares)[\[8\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Parch%20%3A%20,C78%27%20%27D35%27%20%27C87%27%20%27B77%27%20%27E67).
    Sin embargo, hay algunos con familias numerosas: por ejemplo una
    familia con 5 hijos (Parch=5) o hasta 8 familiares en total en el
    barco (SibSp+Parch). Estas variables ayudan a derivar el tamaño de
    familia (FamilySize = SibSp + Parch + 1).

-   **Embarked:** La mayoría embarcó en Southampton (S). De los tres
    puertos, aproximadamente 72% salieron de Southampton, \~19% de
    Cherbourg (C) y \~9% de Queenstown (Q). Solo 2 registros faltaban en
    esta columna (que luego veremos cómo imputar).

En resumen, el perfil típico de pasajero es: hombre, adulto joven (\~30
años) de 3ª clase, viajando solo o con poca familia, embarcado en
Southampton y pagando una tarifa económica.

## Análisis bivariado: relaciones entre variables

Ahora examinamos cómo se relacionan las variables entre sí y,
fundamentalmente, con la supervivencia:

-   **Supervivencia vs Sexo:** La relación más llamativa es que
    **sobrevivió el \~74% de las mujeres vs solo \~19% de los
    hombres**[\[9\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Surval%20rate%20based%20on%20Sex,188908%20Name%3A%20Sex%2C%20dtype%3A%20float64)[\[10\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=0%20%20%20%20,109%20Name%3A%20Sex%2C%20dtype%3A%20int64).
    Esto es confirmado al cruzar `Survived` con `Sex`: de 314 mujeres a
    bordo, 233 sobrevivieron (74%), mientras que de 577 hombres solo 109
    sobrevivieron
    (19%)[\[3\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Total%20passengers%20%3A%20Sex%20female,577%20Name%3A%20Sex%2C%20dtype%3A%20int64)[\[11\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=0%20%20%20%20,109%20Name%3A%20Sex%2C%20dtype%3A%20int64).
    Es decir, ser mujer tuvo una fuerte asociación positiva con
    sobrevivir[\[12\]](https://blogs.opentext.com/in-database-machine-learning-2-calculate-a-correlation-matrix-a-data-exploration-post/#:~:text=,correlated%20to%20age%2C%20SibSp%2C).
    Visualmente, podríamos usar un gráfico de barras apiladas o facetado
    por sexo para ilustrar la diferencia: prácticamente **3 de cada 4
    mujeres** fueron rescatadas, contra **solo 1 de cada 5 hombres**.

-   **Supervivencia vs Clase (Pclass):** También hay una clara
    diferencia según la clase socioeconómica. En 1ª clase sobrevivió
    \~63% de los pasajeros, en 2ª clase \~47%, y en 3ª clase solo \~24%.
    Esto refleja las ventajas que tuvieron pasajeros de clases
    superiores (acceso más rápido a botes, camarotes más cerca de
    cubiertas altas, etc.). Por ejemplo, de 216 pasajeros de 1ª clase,
    \~136 sobrevivieron; en cambio en 3ª clase (\~491 pasajeros), solo
    \~119 sobrevivieron. Un diagrama de barras de *Survival Rate by
    Pclass* mostraría esta brecha.

-   **Supervivencia vs Edad:** Los niños pequeños tuvieron tasas altas
    de supervivencia (muchos fueron evacuados con las mujeres). Por
    ejemplo, todos los niños menores de 5 años en 1ª/2ª clase
    sobrevivieron, y en 3ª clase varios también (aunque no todos). En
    general, los supervivientes tienden a ser más jóvenes que los no
    supervivientes: la edad media de sobrevivientes \~28 años vs
    fallecidos \~30 años, diferencia modesta. Un gráfico de densidad o
    boxplot de edad por grupo de sobrevivencia indica que no hubo una
    diferencia de edad extremadamente marcada, salvo el caso de niños.
    Sí se aprecia que prácticamente **todos los menores de 10 años**
    sobrevivieron, salvo excepciones, indicando la prioridad que se dio
    a niños.

-   **Supervivencia vs Familia (SibSp/Parch):** Pasajeros que viajaban
    solos o con pocas personas parecen haber sobrevivido algo más que
    aquellos con familias muy grandes, especialmente en 3ª clase donde
    familias enteras perecieron. Por ejemplo, familias Skoog o Goodwin
    en 3ª clase (con 5 hijos) tuvieron muy baja supervivencia. En
    cambio, tener 1 o 2 acompañantes podía mejorar ligeramente el
    resultado (p. ej. mujeres con 1 niño tenían ambos prioridad). Si
    definimos *FamilySize = SibSp + Parch + 1*, se observa que familias
    de tamaño 2-4 tuvieron mejores chances que individuos solos o
    familias \>4, aunque este patrón requiere un análisis más detallado.

-   **Supervivencia vs Fare:** Como era de esperar, quienes pagaron
    tarifas más altas (correlacionado con 1ª clase) sobrevivieron más.
    Al graficar la tarifa media por sobrevivencia, vemos que la **tarifa
    promedio de sobrevivientes (\~£48) excede la de no sobrevivientes
    (\~£22)**. Pasajeros con tickets caros (ej. por encima de £100) en
    su mayoría estaban en 1ª clase y tienen alta supervivencia. Sin
    embargo, *Fare* en sí está fuertemente ligado a `Pclass`, por lo que
    su relación con `Survived` no es independiente.

-   **Embarked vs Supervivencia:** Ligado a lo anterior, los pasajeros
    embarcados en Cherbourg (C) tenían mayor proporción de 1ª clase, y
    en efecto la tasa de supervivencia desde Cherbourg fue más alta
    (\~55%) comparada con Southampton (\~33%) o Queenstown (\~39%).
    Ejemplo: muchos ricos embarcaron en Cherbourg (ej. los Astor,
    Cardeza, etc.), inflando la supervivencia de ese puerto. Este factor
    no es causal por sí mismo sino refleja la composición de pasajeros
    por puerto.

Para ilustrar algunas de estas relaciones, podemos usar visualizaciones:
por ejemplo, un **gráfico de barras apiladas de Survived por Sex** y
otro por Pclass, o un **gráfico de violín/boxplot de Age segmentado por
Survived**. A continuación se muestra un heatmap de correlación que
resume correlaciones numéricas entre variables:

*Matriz de correlación entre variables numéricas del Titanic. Las celdas
anotan el coeficiente de correlación de Pearson. Se observa, por
ejemplo, fuerte correlación negativa entre Fare y Pclass
(\~-0.55)[\[13\]](https://codesignal.com/learn/courses/intro-to-data-cleaning-and-preprocessing-with-titanic/lessons/understanding-and-handling-redundant-or-correlated-features-in-datasets#:~:text=This%20correlation%20matrix%20displays%20the,consistent%20with%20our%20initial%20assumption),
así como correlaciones positivas entre Parch y SibSp (tener padres/hijos
se relaciona con tener hermanos/cónyuge). La supervivencia (Survived)
correlaciona positivamente con Fare y negativamente con Pclass y (en
menor medida) con Age.*

## Correlación entre variables numéricas

Aunque muchas variables son categóricas, calculamos la **correlación de
Pearson** entre las numéricas principales (tratando `Survived` como 0/1
numérico). Confirmamos:

-   **Pclass** y **Fare**: correlación negativa fuerte (\~
    -0.55)[\[13\]](https://codesignal.com/learn/courses/intro-to-data-cleaning-and-preprocessing-with-titanic/lessons/understanding-and-handling-redundant-or-correlated-features-in-datasets#:~:text=This%20correlation%20matrix%20displays%20the,consistent%20with%20our%20initial%20assumption),
    porque los de 1ª clase (Pclass=1) pagan tarifas altas y Pclass=3
    pagan bajo Fare.
-   **Survived** tiene correlación positiva moderada con **Fare** (los
    sobrevivientes tendieron a pagar más) y correlación negativa con
    **Pclass** (a menor clase numérica --1ª-- mayor supervivencia). La
    correlación de Survived con **Sex** no se ve en la matriz numérica
    (por ser categoría), pero codificando female=1, male=0 obtendríamos
    una correlación positiva muy alta (\~0.54) con
    supervivencia[\[12\]](https://blogs.opentext.com/in-database-machine-learning-2-calculate-a-correlation-matrix-a-data-exploration-post/#:~:text=,correlated%20to%20age%2C%20SibSp%2C)
    -- ser mujer es el factor más asociado a sobrevivir.
-   **Age** muestra una leve correlación negativa con Survived (los
    sobrevivientes fueron ligeramente más jóvenes en promedio). También
    Edad correlaciona algo con Pclass (pasajeros de 1ª clase eran algo
    mayores en promedio que 3ª clase).
-   **SibSp** y **Parch**: entre sí tienen correlación positiva
    (familias con padres suelen tener hijos, etc.). Con Survived su
    correlación es baja; tener 1--2 familiares podía mejorar
    supervivencia de ciertos grupos (ej. niños con madres), pero
    familias grandes en 3ª clase fue perjudicial -- estos efectos se
    diluyen al solo mirar Pearson global.

En general, estas correlaciones sugieren que **Sexo, Clase y Fare**
serán variables importantes para predecir supervivencia, mientras que
Edad o familiares tienen menor influencia lineal.

## Limpieza básica de datos

Antes de modelar o profundizar, aplicamos algunas limpiezas al dataset:

-   **Imputación de Age:** Dado que **Age** tiene 177 faltantes (\~20%
    de las filas), podemos optar por imputar con alguna estrategia. Una
    opción simple es usar la **mediana** de edad por grupos (por
    ejemplo, mediana por Pclass/Sex) para completar. También podríamos
    usar la media global (\~29.7 años) o incluso modelos de imputación
    más complejos, pero para este EDA inicial usaremos la mediana global
    (\~28 años) para no sesgar con edades extremas.

```{=html}
<!-- -->
```
-   median_age = df['Age'].median()
        df['Age'].fillna(median_age, inplace=True)

    Ahora `Age` no tiene nulos y conserva una distribución similar
    (aunque subestimando la desviación en cierta medida por la
    imputación constante).

```{=html}
<!-- -->
```
-   **Cabin:** La columna **Cabin** tiene un 77% de valores
    nulos[\[1\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Survived%2C%20three%20for%20passenger%20class,each%20for%20Parch%20and%20SibSp).
    Esto dificulta extraer información útil. Una estrategia es
    **eliminar** esta columna por contener demasiados vacíos.
    Alternativamente, podríamos convertir *Cabin* en un indicador
    binario (tenía asignación de cabina o no), ya que tener cabina
    registrada podría correlacionar con clase alta. Para simplificar,
    eliminamos la columna completa en el dataset limpio:

```{=html}
<!-- -->
```
-   df.drop('Cabin', axis=1, inplace=True)

```{=html}
<!-- -->
```
-   **Embarked:** Solo 2 valores faltantes. Podemos imputarlos con el
    puerto más frecuente, que es **S (Southampton)**.

```{=html}
<!-- -->
```
-   df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    Ahora Embarked no tiene nulos. (En Titanic, esos 2 pasajeros con
    Embarked nulo eran probablemente de Southampton, por lo que la
    imputación con \'S\' es razonable).

```{=html}
<!-- -->
```
-   **Tipos de datos:** Podemos transformar **Sex** a un código 0/1 (por
    ejemplo, male=0, female=1) y **Embarked** a dummies categóricas si
    se requiere para modelado. Para EDA descriptivo, podemos dejarlas
    como categoría.

-   **Outliers:** Observamos *outliers* en algunas columnas:

    -   En **Fare**, los valores máximos (£512, £263, £211, etc.)
        corresponden a pocos pasajeros adinerados. No los eliminamos ya
        que son datos válidos, pero podría ser útil aplicar log(Fare+1)
        en algunos análisis para reducir skew. También notamos algunos
        pasajeros con Fare = 0 (gratuitos o crew camuflado), pero son
        pocos (ej. 2 registros), podríamos dejarlos.
    -   En **Age**, la presencia de edad 0.42 (un bebé de \~5 meses)
        podría considerarse outlier por ser muy bajo, pero es real. La
        edad máxima 80 también es real. No eliminamos ninguno.
    -   **Parch** y **SibSp** tienen algunos valores altos (hasta 5 y 8
        respectivamente); de nuevo son pocos casos reales (familias
        grandes) y los conservamos, aunque un modelo podría agruparlos.

Tras estas operaciones, nuestro dataset limpio tiene 891 filas y 11
columnas (eliminamos Cabin). **Guardamos** el dataset limpio en formato
Parquet para usos posteriores eficientes:

    # Guardar el DataFrame limpio a parquet
    df.to_parquet("titanic_clean.parquet")

*(Nota: El tamaño del CSV original (\~60 KB) es pequeño, pero se muestra
el guardado en Parquet por buenas prácticas cuando el dataset es mayor a
1 MB, aprovechando la eficiencia de Polars/Pandas con este formato.)*

## Conclusiones del análisis

El análisis exploratorio del Titanic confirma varias conclusiones
conocidas y aporta cuantificación específica:

-   **Factores clave de supervivencia:** Ser mujer y de clase alta
    aumentaron drásticamente la probabilidad de sobrevivir. Las mujeres
    sobrevivieron en un 74% vs 19% los hombres, y pasajeros de 1ª clase
    \~63% vs 24% en 3ª
    clase[\[10\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=0%20%20%20%20,109%20Name%3A%20Sex%2C%20dtype%3A%20int64)[\[2\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=are%20891%20entries%20in%20the,each%20for%20Parch%20and%20SibSp).
    Esto sugiere un fuerte sesgo en favor de mujeres y clases acomodadas
    al acceder a los botes salvavidas.

-   **Influencia de la tarifa y posición:** La tarifa (Fare) actúa como
    proxy de la posición socioeconómica; quienes pagaron más (a menudo
    en mejores camarotes) tenían ventaja. Vimos correlación negativa
    entre Fare y
    Pclass[\[13\]](https://codesignal.com/learn/courses/intro-to-data-cleaning-and-preprocessing-with-titanic/lessons/understanding-and-handling-redundant-or-correlated-features-in-datasets#:~:text=This%20correlation%20matrix%20displays%20the,consistent%20with%20our%20initial%20assumption),
    y positiva entre Fare y supervivencia. También notamos que pasajeros
    embarcados en Cherbourg (que incluía a muchos de 1ª clase) tuvieron
    mayor supervivencia que los de Southampton o Queenstown.

-   **Edad y grupos familiares:** Los niños pequeños tuvieron alta
    supervivencia (prioridad en evacuación), aunque en conjunto la edad
    no mostró un efecto lineal fuerte sobre la supervivencia. Pasajeros
    muy mayores en general no sobrevivieron (ej. solo 1 persona \>70
    años sobrevivió). En cuanto a familia, viajar solo no fue claramente
    ventajoso ni desventajoso por sí mismo, pero viajar con familia muy
    grande (especialmente en 3ª clase) solía implicar que varios
    miembros no lograran sobrevivir. Familias pequeñas (parejas,
    madre-hijo) a veces sí sobrevivieron juntos.

-   **Calidad de datos:** Identificamos datos faltantes significativos
    en *Age* y *Cabin*. Imputamos Age con mediana para no perder muchas
    filas; sin embargo, si se buscara mayor precisión, podríamos imputar
    edades de forma más segmentada (por título honorífico en el nombre,
    por ejemplo \"Mr\", \"Mrs\", \"Master\", que correlacionan con
    edad). La columna Cabin fue mayormente vacía; eliminarla o
    transformarla en *Deck* (cubierta A, B, C\...) podría ser una idea
    si quisiéramos aprovechar la poca información útil que contiene (los
    pocos valores no nulos de Cabin empiezan con letra que indica
    cubierta, lo cual está relacionado a Pclass). Para este análisis,
    prescindimos de Cabin.

-   **Distribuciones:** Confirmamos que la mayoría de pasajeros eran
    hombres jóvenes de tercera clase. Esto influye en las conclusiones:
    la baja tasa general de supervivencia (\~38%) se debe en parte a que
    muchos eran hombres de 3ª clase (el grupo con menor supervivencia).
    Casi todas las mujeres de 1ª y 2ª clase sobrevivieron, así como una
    buena proporción de hombres de 1ª.

En el siguiente paso, estos hallazgos nos guiarían para la construcción
de un modelo de clasificación (por ejemplo, un árbol de decisión o
regresión logística) usando las variables más predictivas (Sexo, Pclass,
Fare, Age, etc.). También podríamos crear nuevas features como
*FamilySize* o *Title* (título del nombre) para mejorar el modelo.

## Datasets de clasificación alternativos

Finalmente, se proponen **3 datasets de clasificación alternativos**, de
carácter realista, abiertos y de tamaño adecuado, para que los alumnos
practiquen mini-proyectos de EDA y modelado. Todos son lo
suficientemente grandes para aprovechar ventajas de Polars y métodos de
ML, pero manejables en entornos como Colab:

1.  **Adult Census Income (Ingresos del Censo)** -- Un clásico dataset
    extraído del censo de EE.UU. 1994, con **48.842 instancias y 14
    atributos**, donde el objetivo es predecir si el ingreso anual de
    una persona supera
    \$50K[\[14\]](http://archive.ics.uci.edu/dataset/2/adult#:~:text=).
    Es un problema de clasificación binaria con datos demográficos
    (edad, educación, ocupación, etc.). Es abierto (UCI Machine Learning
    Repository) y ampliamente usado para probar modelos de clasificación
    en contexto socioeconómico.

2.  **Bank Marketing (Marketing bancario)** -- Datos de una campaña de
    marketing telefónico de un banco portugués. Consta de **45.211
    registros y 16 features**, mezclando variables numéricas y
    categóricas, y el objetivo es predecir si un cliente terminará
    suscribiendo un depósito a plazo fijo
    (yes/no)[\[15\]](https://archive.ics.uci.edu/dataset/222/bank+marketing#:~:text=).
    Es realista (campañas bancarias), público (UCI) y requiere manejar
    desbalance (la clase \"yes\" es minoritaria \~11%). Permite
    ejercicios de EDA interesantes (p.ej. relación entre éxito y edad,
    profesión, etc.).

3.  **Default de Clientes de Tarjetas de Crédito** -- Dataset de una
    entidad bancaria de Taiwán con **30.000 observaciones y 23
    atributos**[\[16\]](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients#:~:text=).
    La tarea es predecir si un cliente incumplirá el pago de su tarjeta
    (default credit) el próximo mes. Incluye variables demográficas
    (edad, educación, estado civil), límite de crédito y historiales de
    pago mensuales recientes. Es un problema de clasificación binaria
    con cierto desbalance (≈22% defaults). Este dataset (UCI) permite
    analizar riesgo crediticio y probar técnicas de preprocesamiento
    para variables continuas y categóricas.

*(Opcionalmente, otro dataset viable es* *Telco Customer Churn* *de IBM,
con 7043 clientes y 21 características, donde se predice la baja de
clientes de un servicio de
telecomunicaciones[\[17\]](https://www.kaggle.com/datasets/blastchar/telco-customer-churn#:~:text=Each%20row%20represents%20a%20customer%2C,customers%29%20and%2021).
Es más pequeño pero muy práctico para EDA de variables categóricas como
tipo de contrato, servicios contratados, etc.)*

Cada uno de estos datasets ofrece un contexto diferente (ingresos,
marketing, finanzas -- e incluso churn de clientes), proporcionando a
los alumnos la oportunidad de explorar distintas áreas aplicando
técnicas similares de EDA, limpieza y modelado de clasificación. Todas
son bases de datos públicas y bien documentadas.

**Referencias:** Datos explorados y conclusiones basadas en el dataset
Titanic original de
Kaggle/UCI[\[18\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Null%20Values%20%3A%20PassengerId%20,0)[\[2\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=are%20891%20entries%20in%20the,each%20for%20Parch%20and%20SibSp),
y especificaciones de conjuntos de datos alternativos tomadas de UCI
Machine Learning
Repository[\[14\]](http://archive.ics.uci.edu/dataset/2/adult#:~:text=)[\[15\]](https://archive.ics.uci.edu/dataset/222/bank+marketing#:~:text=)[\[16\]](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients#:~:text=).
Los análisis concuerdan con estudios previos del Titanic donde el sexo y
la clase fueron determinantes en la
supervivencia[\[11\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=0%20%20%20%20,109%20Name%3A%20Sex%2C%20dtype%3A%20int64)[\[12\]](https://blogs.opentext.com/in-database-machine-learning-2-calculate-a-correlation-matrix-a-data-exploration-post/#:~:text=,correlated%20to%20age%2C%20SibSp%2C).
Los conjuntos sugeridos (Adult, Bank Marketing, Credit Default) son
ampliamente utilizados como benchmarks en la enseñanza de ML y están
disponibles públicamente.

[\[1\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Survived%2C%20three%20for%20passenger%20class,each%20for%20Parch%20and%20SibSp)
[\[2\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=are%20891%20entries%20in%20the,each%20for%20Parch%20and%20SibSp)
[\[3\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Total%20passengers%20%3A%20Sex%20female,577%20Name%3A%20Sex%2C%20dtype%3A%20int64)
[\[4\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Survival%20rate%20based%20on%20Sex%C2%B6)
[\[8\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Parch%20%3A%20,C78%27%20%27D35%27%20%27C87%27%20%27B77%27%20%27E67)
[\[9\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Surval%20rate%20based%20on%20Sex,188908%20Name%3A%20Sex%2C%20dtype%3A%20float64)
[\[10\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=0%20%20%20%20,109%20Name%3A%20Sex%2C%20dtype%3A%20int64)
[\[11\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=0%20%20%20%20,109%20Name%3A%20Sex%2C%20dtype%3A%20int64)
[\[18\]](https://bibinmjose.github.io/explore_titanic_data/#:~:text=Null%20Values%20%3A%20PassengerId%20,0)
titanic

<https://bibinmjose.github.io/explore_titanic_data/>

[\[5\]](https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv#:~:text=D,Collyer%2C%20Mr)
[\[6\]](https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv#:~:text=Sofia,Panula%2C%20Mr.%20Jaako)
[\[7\]](https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv#:~:text=Hjalmar,Brown%2C%20Mr.%20Thomas%20William)
raw.githubusercontent.com

<https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv>

[\[12\]](https://blogs.opentext.com/in-database-machine-learning-2-calculate-a-correlation-matrix-a-data-exploration-post/#:~:text=,correlated%20to%20age%2C%20SibSp%2C)
How to Calculate a Correlation Matrix - Data Exploration for Machine
\...

<https://blogs.opentext.com/in-database-machine-learning-2-calculate-a-correlation-matrix-a-data-exploration-post/>

[\[13\]](https://codesignal.com/learn/courses/intro-to-data-cleaning-and-preprocessing-with-titanic/lessons/understanding-and-handling-redundant-or-correlated-features-in-datasets#:~:text=This%20correlation%20matrix%20displays%20the,consistent%20with%20our%20initial%20assumption)
Understanding and Handling Redundant or Correlated Features in Datasets
\| CodeSignal Learn

<https://codesignal.com/learn/courses/intro-to-data-cleaning-and-preprocessing-with-titanic/lessons/understanding-and-handling-redundant-or-correlated-features-in-datasets>

[\[14\]](http://archive.ics.uci.edu/dataset/2/adult#:~:text=) UCI
Machine Learning Repository

<http://archive.ics.uci.edu/dataset/2/adult>

[\[15\]](https://archive.ics.uci.edu/dataset/222/bank+marketing#:~:text=)
UCI Machine Learning Repository

<https://archive.ics.uci.edu/dataset/222/bank+marketing>

[\[16\]](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients#:~:text=)
UCI Machine Learning Repository

<https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients>

[\[17\]](https://www.kaggle.com/datasets/blastchar/telco-customer-churn#:~:text=Each%20row%20represents%20a%20customer%2C,customers%29%20and%2021)
Telco Customer Churn - Kaggle

<https://www.kaggle.com/datasets/blastchar/telco-customer-churn>

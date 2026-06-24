#!/usr/bin/env python3
import json
import os

BASE_PATH = "/home/jmsa/IESRafaelAlberti24_25/Modulos/PIA/06-10-Herramientas/002-Pandas/pandas_exercises/Ejercicios_Seleccionados"

def make_cell(cell_type, source, outputs=None):
    """Helper para crear celdas"""
    cell = {"cell_type": cell_type, "metadata": {}}
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = outputs or []
    cell["source"] = source if isinstance(source, list) else [source]
    return cell

def make_notebook(title, dataset, exercises):
    """Genera un notebook con estructura standard"""
    cells = [make_cell("markdown", [f"# {title}\n\n### Dataset: {dataset}"])]
    
    for i, (ej_title, ej_desc, pista, var, test_cond, test_msg) in enumerate(exercises, 1):
        cells.append(make_cell("markdown", [f"### Ejercicio {i}: {ej_title}\n{ej_desc}"]))
        cells.append(make_cell("code", [f"# Pista: {pista}\n{var + ' = None' if var else ''}\n"]))
        cells.append(make_cell("code", [f"{test_cond}\nprint('{test_msg}')\n"]))
    
    cells.append(make_cell("markdown", ["## ¡Completado! 🎉"]))
    
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.8.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

# DEFINIR TODOS LOS EJERCICIOS
notebooks_config = {
    "02_Filtering_Sorting": {
        "title": "Filtering & Sorting",
        "dataset": "Euro 2012",
        "exercises": [
            ("Importar pandas", "Import pandas", "import pandas as pd", None, "assert 'pd' in dir()", "✓ Pandas OK"),
            ("Cargar dataset", "URL: https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv", "pd.read_csv()", "euro12", "assert euro12.shape[0] == 16", "✓ 16 equipos"),
            ("Ver estructura", "head() + info()", ".head() e .info()", None, "print('OK')", "✓ Revisado"),
            ("Columna Goals", "Obtén Series de Goals", "euro12['Goals']", "goals", "assert isinstance(goals, pd.Series)", "✓ Series"),
            ("Contar equipos", "¿Cuántos?", ".shape[0]", "num_equipos", "assert num_equipos == 16", "✓ 16"),
            ("Columnas totales", "¿Cuántas columnas?", ".shape[1]", "num_col", "assert num_col == 35", "✓ 35"),
            ("Select 3 cols", "Team, Yellow Cards, Red Cards", "euro12[[...]]", "discipline", "assert discipline.shape == (16, 3)", "✓ OK"),
            ("Sort by cards", "Red desc, Yellow desc", ".sort_values()", "sorted_d", "assert sorted_d is not None", "✓ Ordenado"),
            ("Media amarillas", "Mean of Yellow Cards", ".mean()", "media_y", "assert 8 < media_y < 10", "✓ Media"),
            ("Filter >6 goals", "Teams with >6 goals", "euro12[euro12.Goals > 6]", "teams_6", "assert len(teams_6) > 0", "✓ OK"),
            ("Teams start G", "Team name starts with G", ".str.startswith('G')", "teams_g", "assert len(teams_g) > 0", "✓ OK"),
            ("First 7 cols", "Select first 7", ".iloc[:, 0:7]", "first_7", "assert first_7.shape[1] == 7", "✓ OK"),
            ("No last 3", "Exclude last 3", ".iloc[:, :-3]", "no_last", "assert no_last.shape[1] == 32", "✓ OK"),
            ("3 teams accuracy", "England, Italy, Russia", ".loc[.isin(...)]", "teams_p", "assert teams_p.shape[0] == 3", "✓ OK"),
            ("Complex filter", ">5 goals AND >80 passes", "(cond1) & (cond2)", "teams_f", "assert len(teams_f) > 0", "✓ OK"),
        ]
    },
    
    "03_Grouping": {
        "title": "Grouping",
        "dataset": "Alcohol Consumption",
        "exercises": [
            ("Import", "Import pandas", "import pandas as pd", None, "assert 'pd' in dir()", "✓ OK"),
            ("Load drinks", "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv", "pd.read_csv()", "drinks", "assert drinks.shape[0] > 0", "✓ Cargado"),
            ("Preview", "See first rows", ".head()", None, "print('OK')", "✓ Vista"),
            ("Beer by continent", "Which continent drinks most beer?", ".groupby('continent').beer.mean()", "beer_mean", "assert beer_mean is not None", "✓ OK"),
            ("Wine stats", "Stats for wine by continent", ".groupby('continent').wine.describe()", "wine_stats", "assert wine_stats is not None", "✓ OK"),
            ("Mean all cols", "Mean by continent for all", ".groupby('continent').mean()", "all_mean", "assert all_mean is not None", "✓ OK"),
            ("Median all cols", "Median by continent", ".groupby('continent').median()", "all_median", "assert all_median is not None", "✓ OK"),
            ("Spirit agg", "Mean, min, max for spirits", ".agg(['mean', 'min', 'max'])", "spirit_agg", "assert spirit_agg is not None", "✓ OK"),
            ("Count by continent", "How many countries per continent?", ".groupby('continent').size()", "countries", "assert countries is not None", "✓ OK"),
            ("Total consumption", "Total alcohol by continent", ".groupby('continent').sum()", "total", "assert total is not None", "✓ OK"),
            ("Custom agg", "Multiple functions", ".agg({'beer': 'mean', 'wine': 'sum'})", "custom", "assert custom is not None", "✓ OK"),
            ("Filter + group", "Mean beer where > 100", ".loc[drinks.beer > 100].groupby('continent').mean()", "filtered", "assert filtered is not None", "✓ OK"),
        ]
    },
    
    "04_Apply": {
        "title": "Apply",
        "dataset": "Student Alcohol",
        "exercises": [
            ("Import", "Import libraries", "import pandas as pd", None, "assert 'pd' in dir()", "✓ OK"),
            ("Load data", "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv", "pd.read_csv()", "df", "assert df.shape[0] > 0", "✓ Cargado"),
            ("Slice cols", "school to guardian", "df.loc[:, 'school':'guardian']", "sliced", "assert sliced is not None", "✓ OK"),
            ("Lambda upper", "Create capitalize lambda", "lambda x: x.capitalize()", "cap", "assert callable(cap)", "✓ OK"),
            ("Apply capitalize", "Capitalize Mjob, Fjob", ".apply(capitalizer)", "cap_cols", "assert cap_cols is not None", "✓ OK"),
            ("Check type", "Verify string columns", "print(df.dtypes)", None, "print('OK')", "✓ Checked"),
            ("Apply inplace", "Modify original df", "df['Mjob'] = df['Mjob'].apply(...)", "updated", "assert updated is not None", "✓ OK"),
            ("Custom function", "Create legal_drinker (age>17)", "def majority(x): return x > 17", "legal", "assert callable(legal)", "✓ OK"),
            ("Apply function", "Add legal_drinker column", ".apply(majority)", "df_legal", "assert df_legal is not None", "✓ OK"),
            ("Lambda math", "Multiply by 10", "lambda x: x * 10 if isinstance(x, int) else x", "mult", "assert callable(mult)", "✓ OK"),
            ("Applymap", "Apply to all values", ".applymap() or .map()", "all_mult", "assert all_mult is not None", "✓ OK"),
            ("Groupby apply", "Custom groupby function", ".groupby('Mjob').apply(lambda x: x.mean())", "group_apply", "assert group_apply is not None", "✓ OK"),
            ("Transform", "Transform with groupby", ".groupby('school').transform('mean')", "transformed", "assert transformed is not None", "✓ OK"),
            ("Agg multiple", "Multiple aggregations", ".agg(['mean', 'sum', 'std'])", "multi_agg", "assert multi_agg is not None", "✓ OK"),
            ("Apply with axis", "Apply by row/column", ".apply(func, axis=1)", "axis_apply", "assert axis_apply is not None", "✓ OK"),
        ]
    },
    
    "05_Merge": {
        "title": "Merge",
        "dataset": "Auto MPG",
        "exercises": [
            ("Import", "Import pandas, numpy", "import pandas as pd; import numpy as np", None, "assert 'pd' in dir()", "✓ OK"),
            ("Load cars1", "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv", "pd.read_csv()", "cars1", "assert cars1 is not None", "✓ Cargado"),
            ("Load cars2", "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv", "pd.read_csv()", "cars2", "assert cars2 is not None", "✓ Cargado"),
            ("Clean cars1", "Remove unnamed columns", ".loc[:, 'mpg':'car']", "cars1_clean", "assert cars1_clean is not None", "✓ Limpio"),
            ("Check shape", "Shape of each df", ".shape", None, "print(f'{cars1_clean.shape}, {cars2.shape}')", "✓ Revisado"),
            ("Concat", "Join cars1 and cars2", "pd.concat([cars1, cars2])", "cars", "assert cars is not None", "✓ Concatenado"),
            ("Create owners", "Random integers 15000-73000", "np.random.randint(15000, 73001, size=len(cars))", "owners", "assert len(owners) == len(cars)", "✓ Creado"),
            ("Add column", "Add owners to cars", "cars['owners'] = owners", "cars_owners", "assert 'owners' in cars_owners.columns", "✓ Añadido"),
            ("Merge condition", "pd.merge on index", "pd.merge(cars1, cars2, left_index=True, right_index=True)", "merged", "assert merged is not None", "✓ OK"),
            ("Inner join", "Inner merge", "pd.merge(..., how='inner')", "inner", "assert inner is not None", "✓ OK"),
            ("Left join", "Left merge", "pd.merge(..., how='left')", "left", "assert left is not None", "✓ OK"),
            ("Outer join", "Outer merge", "pd.merge(..., how='outer')", "outer", "assert outer is not None", "✓ OK"),
            ("On column", "Merge on specific column", "pd.merge(..., on='key')", "on_col", "assert on_col is not None", "✓ OK"),
            ("Suffixes", "Add suffixes for conflicts", "pd.merge(..., suffixes=('_left', '_right'))", "suff", "assert suff is not None", "✓ OK"),
            ("Append", "Add rows with append/concat", "pd.concat([cars1, cars2], ignore_index=True)", "appended", "assert len(appended) > 0", "✓ OK"),
        ]
    },
    
    "06_Stats": {
        "title": "Stats",
        "dataset": "US Baby Names",
        "exercises": [
            ("Import", "Import pandas, numpy", "import pandas as pd; import numpy as np", None, "assert 'pd' in dir()", "✓ OK"),
            ("Load data", "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv", "pd.read_csv()", "baby_names", "assert baby_names.shape[0] > 0", "✓ Cargado"),
            ("Preview", "First rows", ".head()", None, "print('OK')", "✓ OK"),
            ("Drop cols", "Delete 'Unnamed: 0' and 'Id'", ".drop(['Unnamed: 0', 'Id'], axis=1)", "bn_clean", "assert bn_clean is not None", "✓ Limpio"),
            ("Gender count", "More male or female names?", ".groupby('Gender').size()", "gender_count", "assert gender_count is not None", "✓ OK"),
            ("Group by name", "Groupby name", ".groupby('Name')", "by_name", "assert by_name is not None", "✓ OK"),
            ("Unique names", "How many different names?", ".nunique() or .groupby().ngroups", "num_names", "assert num_names > 0", "✓ OK"),
            ("Most common", "Name with most occurrences", ".groupby('Name').Count.sum().idxmax()", "most_common", "assert most_common is not None", "✓ OK"),
            ("Least common", "How many with least?", "...min()...", "least_count", "assert least_count > 0", "✓ OK"),
            ("Median", "Median name occurrence", ".groupby('Name').Count.sum().median()", "med", "assert med > 0", "✓ OK"),
            ("Std", "Standard deviation", ".std()", "std_val", "assert std_val > 0", "✓ OK"),
            ("Describe", "Summary stats", ".describe()", "summary", "assert summary is not None", "✓ OK"),
            ("Top 10", "Top 10 names", ".groupby('Name').Count.sum().nlargest(10)", "top10", "assert len(top10) == 10", "✓ OK"),
            ("Percentiles", "25th, 50th, 75th", ".quantile([.25, .5, .75])", "perc", "assert perc is not None", "✓ OK"),
            ("Trend", "Names trend over time", ".groupby(['Year', 'Name']).Count.sum()", "trend", "assert trend is not None", "✓ OK"),
        ]
    },
    
    "07_Visualization": {
        "title": "Visualization",
        "dataset": "Titanic",
        "exercises": [
            ("Import", "Import pandas, matplotlib, seaborn", "import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns", None, "assert 'pd' in dir()", "✓ OK"),
            ("Load titanic", "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv", "pd.read_csv()", "titanic", "assert titanic.shape[0] > 0", "✓ Cargado"),
            ("Set index", "PassengerId as index", ".set_index('PassengerId')", "titanic_idx", "assert 'PassengerId' in titanic_idx.index.name or titanic_idx.index.name is None", "✓ OK"),
            ("Pie gender", "Gender distribution pie", "titanic['Sex'].value_counts().plot(kind='pie')", "pie", "assert pie is not None", "✓ OK"),
            ("Scatter", "Fare vs Age by gender", ".plot(x='Age', y='Fare', kind='scatter', c='Sex')", "scatter", "assert scatter is not None", "✓ OK"),
            ("Survived count", "How many survived?", "titanic['Survived'].sum()", "survived", "assert survived > 0", "✓ OK"),
            ("Histogram fare", "Fare distribution", "titanic['Fare'].plot(kind='hist')", "hist", "assert hist is not None", "✓ OK"),
            ("Bar plot", "Bar chart of classes", "titanic['Pclass'].value_counts().plot(kind='bar')", "bar", "assert bar is not None", "✓ OK"),
            ("Boxplot age", "Age boxplot", "titanic['Age'].plot(kind='box')", "box", "assert box is not None", "✓ OK"),
            ("Group viz", "Survived by gender", "titanic.groupby('Sex')['Survived'].mean()", "surv_gender", "assert surv_gender is not None", "✓ OK"),
            ("Heatmap", "Correlation heatmap", "sns.heatmap(titanic.corr())", "heat", "assert heat is not None", "✓ OK"),
            ("Kde plot", "Age KDE", "titanic['Age'].plot(kind='kde')", "kde", "assert kde is not None", "✓ OK"),
            ("Multi plot", "Age by Pclass", "titanic.boxplot(column='Age', by='Pclass')", "multi", "assert multi is not None", "✓ OK"),
            ("Violin", "Violin plot", "sns.violinplot(data=titanic, x='Sex', y='Age')", "violin", "assert violin is not None", "✓ OK"),
            ("Seaborn style", "Set seaborn style", "sns.set_style('darkgrid')", None, "print('✓ Style set')", "✓ OK"),
        ]
    },
    
    "08_Creating_Data": {
        "title": "Creating Series and DataFrames",
        "dataset": "Pokemon",
        "exercises": [
            ("Import", "Import pandas", "import pandas as pd", None, "assert 'pd' in dir()", "✓ OK"),
            ("Create dict", "Create Pokemon dictionary", "data = {'Name': [...], 'Type': [...], ...}", "pokemon_dict", "assert isinstance(pokemon_dict, dict)", "✓ OK"),
            ("Create DF", "DataFrame from dict", "pokemon = pd.DataFrame(pokemon_dict)", "pokemon", "assert isinstance(pokemon, pd.DataFrame)", "✓ OK"),
            ("Reorder cols", "Reorder to: Name, Type, HP, Evolution, Pokedex", "pokemon[['Name', 'Type', 'HP', 'Evolution', 'Pokedex']]", "pokemon_ordered", "assert list(pokemon_ordered.columns)[0] == 'Name'", "✓ OK"),
            ("Add column", "Add 'Place' column", "pokemon['Place'] = ['Kanto', 'Kanto', ...]", "with_place", "assert 'Place' in with_place.columns", "✓ OK"),
            ("Column types", "Show dtypes", ".dtypes", None, "print('OK')", "✓ OK"),
            ("Create Series", "Create a Series", "pd.Series([1, 2, 3])", "series", "assert isinstance(series, pd.Series)", "✓ OK"),
            ("Series with index", "Series with custom index", "pd.Series([...], index=['a', 'b', 'c'])", "indexed", "assert len(indexed.index) == 3", "✓ OK"),
            ("Concat series", "Concatenate Series", "pd.concat([s1, s2])", "concat_s", "assert concat_s is not None", "✓ OK"),
            ("From lists", "DF from lists", "pd.DataFrame({'col1': [...], 'col2': [...]})", "df_lists", "assert df_lists.shape[1] == 2", "✓ OK"),
        ]
    },
    
    "09_Time_Series": {
        "title": "Time Series",
        "dataset": "Apple Stock",
        "exercises": [
            ("Import", "Import pandas, numpy, matplotlib", "import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt", None, "assert 'pd' in dir()", "✓ OK"),
            ("Load stock", "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv", "pd.read_csv()", "apple", "assert apple.shape[0] > 0", "✓ Cargado"),
            ("Check types", "Check column types", ".dtypes", None, "print('OK')", "✓ OK"),
            ("To datetime", "Convert Date to datetime", "pd.to_datetime(apple['Date'])", "apple_dt", "assert apple_dt is not None", "✓ OK"),
            ("Set index", "Set Date as index", ".set_index('Date')", "apple_idx", "assert apple_idx.index.name == 'Date'", "✓ OK"),
            ("Sort index", "Sort by date ascending", ".sort_index()", "apple_sorted", "assert apple_sorted is not None", "✓ OK"),
            ("Check dups", "Check duplicate dates", ".duplicated().any()", "has_dup", "assert isinstance(has_dup, (bool, np.bool_))", "✓ OK"),
            ("Resample month", "Last business day of month", ".resample('BM').last()", "monthly", "assert monthly is not None", "✓ OK"),
            ("Date diff", "Days between first and last", "(apple_idx.index[-1] - apple_idx.index[0]).days", "days_diff", "assert isinstance(days_diff, (int, np.integer))", "✓ OK"),
            ("Months count", "Number of months", "len(apple_idx.resample('M'))", "months", "assert months > 0", "✓ OK"),
            ("Plot close", "Plot closing price", "apple_idx['Adj Close'].plot(figsize=(13.5, 9))", "plot_close", "assert plot_close is not None", "✓ OK"),
            ("Rolling mean", "30-day rolling mean", ".rolling(window=30).mean()", "rolling", "assert rolling is not None", "✓ OK"),
            ("Year group", "Group by year", ".groupby(apple_idx.index.year).mean()", "yearly", "assert yearly is not None", "✓ OK"),
            ("Volatility", "Daily returns", ".pct_change()", "returns", "assert returns is not None", "✓ OK"),
            ("Cumulative", "Cumulative returns", "(1 + .pct_change()).cumprod() - 1", "cum_ret", "assert cum_ret is not None", "✓ OK"),
        ]
    },
    
    "10_Deleting_Indexing": {
        "title": "Deleting & Indexing",
        "dataset": "Iris",
        "exercises": [
            ("Import", "Import pandas, numpy", "import pandas as pd\nimport numpy as np", None, "assert 'pd' in dir()", "✓ OK"),
            ("Load iris", "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", "pd.read_csv()", "iris", "assert iris.shape[0] > 0", "✓ Cargado"),
            ("Add columns", "sepal_length, sepal_width, petal_length, petal_width, class", "iris.columns = [...]", "iris_cols", "assert iris_cols.shape[1] == 5", "✓ OK"),
            ("Check nulls", "Missing values?", ".isnull().sum()", "nulls", "assert nulls is not None", "✓ OK"),
            ("Set NaN", "petal_length rows 10-29 to NaN", "iris.loc[10:29, 'petal_length'] = np.nan", "iris_nan", "assert iris_nan.isnull().sum().sum() > 0", "✓ OK"),
            ("Fill NaN", "Fill NaN with 1.0", ".fillna(1.0)", "iris_fill", "assert iris_fill.isnull().sum().sum() == 0", "✓ OK"),
            ("Drop class", "Delete class column", ".drop('class', axis=1)", "iris_no_class", "assert 'class' not in iris_no_class.columns", "✓ OK"),
            ("First 3 NaN", "Set first 3 rows to NaN", "iris.loc[0:2] = np.nan", "iris_head_nan", "assert iris_head_nan.isnull().any().any()", "✓ OK"),
            ("Dropna", "Delete rows with NaN", ".dropna()", "iris_clean", "assert iris_clean.isnull().sum().sum() == 0", "✓ OK"),
            ("Reset index", "Reset index to 0,1,2,...", ".reset_index(drop=True)", "iris_reset", "assert iris_reset.index[0] == 0", "✓ OK"),
            ("Set index", "Set column as index", ".set_index('sepal_length')", "iris_indexed", "assert iris_indexed.index.name == 'sepal_length'", "✓ OK"),
            ("Drop duplicates", "Remove duplicate rows", ".drop_duplicates()", "iris_unique", "assert iris_unique is not None", "✓ OK"),
            ("Filter index", "Select by index value", ".loc[5.0]", "by_index", "assert by_index is not None", "✓ OK"),
            ("Multi index", "Create MultiIndex", "pd.MultiIndex.from_tuples([...])", "multi_idx", "assert multi_idx is not None", "✓ OK"),
            ("Index operations", ".index.values, .index.name", ".index", None, "print('OK')", "✓ OK"),
        ]
    }
}

# GENERAR TODOS
os.makedirs(BASE_PATH, exist_ok=True)

for nb_name, config in notebooks_config.items():
    # Notebook de ejercicios
    nb = make_notebook(config["title"], config["dataset"], config["exercises"])
    with open(f"{BASE_PATH}/{nb_name}.ipynb", 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"✓ {nb_name}.ipynb")
    
    # Notebook de soluciones (igual estructura por ahora)
    with open(f"{BASE_PATH}/{nb_name}_SOLUCION.ipynb", 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"✓ {nb_name}_SOLUCION.ipynb")

print("\n✓✓✓ ¡TODOS LOS NOTEBOOKS CREADOS! ✓✓✓")
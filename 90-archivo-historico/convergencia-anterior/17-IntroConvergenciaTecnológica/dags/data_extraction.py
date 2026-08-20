import pandas as pd
from sklearn.datasets import load_iris

@task.external_python(task_id="external_python", python=PATH_TO_PYTHON_BINARY)
def extract_data():
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    target = pd.DataFrame(iris.target, columns=['target'])
    data.to_csv('/path/to/data/iris_data.csv', index=False)
    target.to_csv('/path/to/data/iris_target.csv', index=False)

    
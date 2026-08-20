import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

def validate_model():
    X_test = pd.read_csv('/path/to/data/iris_test_data.csv')
    y_test = pd.read_csv('/path/to/data/iris_test_target.csv')
    clf = joblib.load('/path/to/models/iris_model.joblib')
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    with open('/path/to/results/accuracy.txt', 'w') as f:
        f.write(str(accuracy))
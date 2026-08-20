import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    X_train = pd.read_csv('/path/to/data/iris_train_data.csv')
    y_train = pd.read_csv('/path/to/data/iris_train_target.csv')
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    joblib.dump(clf, '/path/to/models/iris_model.joblib')
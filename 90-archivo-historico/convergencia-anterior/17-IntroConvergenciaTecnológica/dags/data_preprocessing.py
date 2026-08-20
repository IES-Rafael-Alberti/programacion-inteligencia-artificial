import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data():
    data = pd.read_csv('/path/to/data/iris_data.csv')
    target = pd.read_csv('/path/to/data/iris_target.csv')
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    X_train_scaled.to_csv('/path/to/data/iris_train_data.csv', index=False)
    y_train.to_csv('/path/to/data/iris_train_target.csv', index=False)
    X_test_scaled.to_csv('/path/to/data/iris_test_data.csv', index=False)
    y_test.to_csv('/path/to/data/iris_test_target.csv', index=False)
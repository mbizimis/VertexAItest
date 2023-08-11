import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


gspath = 'gs://ai_repo/VertextAI_test'


if __name__ == '__main__':
    # read data
    X_train, X_test, y_train, y_test = [
        pd.read_json(f'{gspath}/{f}') for f in
        ['X_train.json', 'X_test.json', 'y_train.json', 'y_test.json']
    ]

    # create model
    model = linear_model.Ridge(alpha=0.5)
    model.fit(X_train, y_train)

    # eval model
    mse = mean_squared_error(y_pred=model.predict(X_test), y_true=y_test)

    # log experiment TODO: mlflow
    print(f'{mse=}')

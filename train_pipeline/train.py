import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


if __name__ == '__main__':
    # read data
    X_train, X_test, y_train, y_test = [np.load(f) for f in ['X_train.npy', 'X_test.npy', 'y_train.npy', 'y_test.npy']]

    # create model
    model = linear_model.Ridge(alpha=0.5)
    model.fit(X_train, y_train)

    # eval model
    mse = mean_squared_error(y_pred=model.predict(X_test), y_true=y_test)

    # log experiment TODO: mlflow
    print(f'{mse=}')

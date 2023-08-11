import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from data_pipeline.src.plots import analyze


if __name__ == '__main__':
    # read data
    df = pd.read_csv('../winequality-red.csv', sep=';')

    # analyze
    analyze(df)

    # train-test split
    X, y = df.iloc[:, :-1].values, df['quality'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # save data as output
    np.save('../X_train.npy', X_train)
    np.save('../X_test.npy', X_test)
    np.save('../y_train.npy', y_train)
    np.save('../y_test.npy', y_test)

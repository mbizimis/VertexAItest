import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from data_pipeline.src.plots import analyze


gspath = 'gs://ai_repo/VertextAI_test'


if __name__ == '__main__':
    # read data
    df = pd.read_csv(f'{gspath}/winequality-red.csv', sep=';')

    # analyze
    analyze(df, gspath=gspath)

    # train-test split
    X, y = df.iloc[:, :-1].values, df['quality'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # save data as output
    pd.DataFrame(X_train).to_json(f'{gspath}/X_train.json', orient='records')
    pd.DataFrame(X_test).to_json(f'{gspath}/X_test.json', orient='records')
    pd.DataFrame(y_train).to_json(f'{gspath}/y_train.json', orient='records')
    pd.DataFrame(y_test).to_json(f'{gspath}/y_test.json', orient='records')

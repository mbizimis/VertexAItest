import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import os
import joblib
from google.cloud import storage


gspath = 'gs://ai_repo/VertextAI_test'


if __name__ == '__main__':
    # TODO: for yaml config, have a local file changed and it should be uploaded on GCP path before every run to be read from there

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

    # Save model artifact to local filesystem (doesn't persist)
    filename = "dummy_linear_model.jlb"
    joblib.dump(model, filename)

    # Upload model artifact to Cloud Storage
    model_directory = os.environ['AIP_MODEL_DIR']
    storage_path = os.path.join(model_directory, filename)
    blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
    blob.upload_from_filename(filename)

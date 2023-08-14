from google.cloud import storage


def upload_file(oldfilepath: str, gspath: str, newfilename: str):
    """
    Uploads a generic file (e.g. that cant be saved with pandas) to GCP.
    """
    bucket_name, bucket_path = gspath.split('/')[2], '/'.join(gspath.split('/')[3:])
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(bucket_path + f'/{newfilename}')
    blob.upload_from_filename(oldfilepath, content_type='image/png')

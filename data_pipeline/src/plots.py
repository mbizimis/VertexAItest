import pandas as pd
import matplotlib.pyplot as plt

from data_pipeline.src.gcp_utils import upload_file


def analyze(df: pd.DataFrame, gspath: str, filename='fig.png'):
    plt.title('Quality histogram')
    df['quality'].hist()
    plt.savefig(filename, format='png')
    upload_file(filename, gspath=gspath, newfilename=filename)

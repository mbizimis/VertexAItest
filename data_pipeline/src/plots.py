import pandas as pd
import matplotlib.pyplot as plt


def analyze(df: pd.DataFrame):
    plt.title('Quality histogram')
    df['quality'].hist()
    plt.savefig('../fig.png')

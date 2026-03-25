import pandas as pd

def clean_data(df):
    df = df.dropna()
    df.columns = df.columns.str.lower()
    return df


def save_processed(df, path):
    df.to_csv(path, index=False

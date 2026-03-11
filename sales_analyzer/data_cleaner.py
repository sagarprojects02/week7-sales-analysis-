import pandas as pd

def clean_data(df):
    """
    Clean the dataset
    """

    # remove duplicates
    df = df.drop_duplicates()

    # handle missing values
    df = df.fillna(0)

    # convert date column
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    print("Data cleaned successfully")

    return df

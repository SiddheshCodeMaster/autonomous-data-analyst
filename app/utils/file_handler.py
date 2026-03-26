import pandas as pd


def read_csv(file):
    df = pd.read_csv(file)
    return df


def get_basic_summary(df):
    return {
        "columns": list(df.columns),
        "shape": df.shape,
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }

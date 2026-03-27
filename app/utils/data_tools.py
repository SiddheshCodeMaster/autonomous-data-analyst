import pandas as pd


def get_numeric_summary(df):
    return df.describe().to_dict()


def get_correlation(df):
    try:
        return df.corr(numeric_only=True).to_dict()
    except:
        return {}


def get_sample_data(df):
    return df.head(5).to_dict()


def get_column_info(df):
    return {"columns": list(df.columns), "dtypes": df.dtypes.astype(str).to_dict()}

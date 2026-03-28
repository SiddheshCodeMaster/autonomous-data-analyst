import pandas as pd


import pandas as pd


def load_file(file):
    import pandas as pd

    filename = file.name if hasattr(file, "name") else file

    if filename.endswith(".csv"):
        return pd.read_csv(file, encoding="utf-8", errors="ignore")

    elif filename.endswith((".xlsx", ".xls")):
        return pd.read_excel(file)

    else:
        raise ValueError("Unsupported file format")


def get_basic_summary(df):
    return {
        "columns": list(df.columns),
        "shape": df.shape,
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }

import pandas as pd


def load_file(file):

    # 🟢 CASE 1: FastAPI UploadFile
    if hasattr(file, "filename") and hasattr(file, "file"):
        filename = file.filename.lower()

        if not filename:
            raise ValueError("Filename is missing")

        if filename.endswith(".csv"):
            return pd.read_csv(file.file)

        elif filename.endswith((".xlsx", ".xls")):
            return pd.read_excel(file.file)

        else:
            raise ValueError("Unsupported file format")

    # 🟢 CASE 2: CLI (string path)
    elif isinstance(file, str):
        filename = file.lower()

        if filename.endswith(".csv"):
            return pd.read_csv(file)

        elif filename.endswith((".xlsx", ".xls")):
            return pd.read_excel(file)

        else:
            raise ValueError("Unsupported file format")

    # 🔴 EVERYTHING ELSE
    else:
        raise ValueError(f"Invalid file input type: {type(file)}")


def get_basic_summary(df):
    return {
        "columns": list(df.columns),
        "shape": df.shape,
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }

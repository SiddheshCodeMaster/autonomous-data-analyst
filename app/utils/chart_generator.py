import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import uuid


def generate_charts(df):
    charts = []

    numeric_df = df.select_dtypes(include=["number"])

    # ========================
    # 1. Correlation Heatmap
    # ========================
    if numeric_df.shape[1] >= 2:
        plt.figure(figsize=(6, 4))

        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

        path = os.path.join(os.getcwd(), f"heatmap_{uuid.uuid4().hex}.png")
        plt.savefig(path)
        plt.close()

        charts.append(path)

    # ========================
    # 2. Distribution Plot
    # ========================
    if len(numeric_df.columns) >= 1:
        col = numeric_df.columns[0]

        plt.figure()

        sns.histplot(numeric_df[col], kde=True)

        path = os.path.join(os.getcwd(), f"hist_{uuid.uuid4().hex}.png")
        plt.savefig(path)
        plt.close()

        charts.append(path)

    # ========================
    # 3. Bar Chart (Top Values)
    # ========================
    if len(numeric_df.columns) >= 1:
        col = numeric_df.columns[0]

        plt.figure()

        numeric_df[col].value_counts().head(10).plot(kind="bar")

        path = os.path.join(os.getcwd(), f"bar_{uuid.uuid4().hex}.png")
        plt.savefig(path)
        plt.close()

        charts.append(path)

    return charts

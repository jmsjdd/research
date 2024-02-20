import pandas as pd


def aggregate_index_from_constituents(df, list_of_periods):
    df_grouped = df.groupby("date").sum().reset_index()
    return df_grouped

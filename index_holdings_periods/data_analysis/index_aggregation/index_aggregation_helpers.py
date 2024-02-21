import pandas as pd


def aggregate_index_from_constituents(df):
    df_grouped = df.groupby("date").sum().reset_index()
    return df_grouped


def remove_missing_data(df, list_of_periods):
    # Filter rows where weight is not equal to 0
    filtered_df = df[df["weight"] != 0]

    # Find the minimum date
    min_date_row = filtered_df["date"].idxmin()

    for period in list_of_periods:
        col = f"fwd_weighted_return_mthly_{period}"
        period_min_index = min_date_row + period - 1
        df.loc[:, col] = df.loc[:, col].where(df.index >= period_min_index, 0)

    return df
    # print(df)

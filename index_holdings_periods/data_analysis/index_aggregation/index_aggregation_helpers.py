import pandas as pd


def aggregate_index_from_constituents(df):
    df_grouped = df.groupby("date").sum().reset_index()
    return df_grouped


def remove_missing_data(dataframe, list_of_periods, equal_start_dates=True):
    """
    bool is true if dates are to all start at the same point in time (so in line with the max holding period)
    """
    df = dataframe.copy()

    # Filter rows where weight is not equal to 0
    filtered_df = df[df["weight"] != 0]

    # Find the minimum date
    min_date_row = filtered_df["date"].idxmin()

    for period in list_of_periods:
        col = f"fwd_weighted_return_mthly_{period}"
        if not equal_start_dates:
            period_min_index = min_date_row + period - 1
        else:
            period_min_index = min_date_row + max(list_of_periods) - 1
        df.loc[:, col] = df.loc[:, col].where(df.index >= period_min_index, 0)

    if equal_start_dates:
        col = f"fwd_weighted_return_mthly_{max(list_of_periods)}"
        df = df[df[col] != 0]

    return df
    # print(df)

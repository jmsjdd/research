import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def cumulative_returns_from_constituents(
    data_frame, date_col_name, weight_col_name, return_col_name, portfolio_name
):
    """
    Calcs cumulative returns from constituents. Renames the cumulative returns column to the portfolio name.
    """

    # Calc weighted return
    data_frame["weighted_return"] = (
        data_frame[weight_col_name] * data_frame[return_col_name]
    )

    # Group by date
    df_grouped = (
        data_frame.groupby(date_col_name)["weighted_return"].sum().reset_index()
    )

    # Rename
    df_grouped.rename(columns={"weighted_return": return_col_name}, inplace=True)

    # Sort by date
    df_grouped = df_grouped.sort_values(by="date")

    # Calc cumulative return
    df_grouped[portfolio_name] = df_grouped["return"].cumsum()

    # Drop return col to keep data clean
    df_grouped.drop(columns=["return"], inplace=True)

    return df_grouped

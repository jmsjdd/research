import pandas as pd


def get_returns_for_periods(df, list_of_periods):
    # Sort the DataFrame by 'ID' and 'date'
    df.sort_values(by=["ID", "date"], inplace=True)

    # Calculate forward returns for each period
    for period in list_of_periods:
        forward_return_col = f"return_{period}"
        df[forward_return_col] = (
            df.groupby("ID")["price_t"].shift(-period) / df["price_t"] - 1
        )

    return df

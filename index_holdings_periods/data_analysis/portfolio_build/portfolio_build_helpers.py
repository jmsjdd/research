import pandas as pd


def weights_for_portfolios(df, list_of_periods):
    # Sort the DataFrame by ID and date
    df.sort_values(by=["ID", "date"], ascending=[True, False], inplace=True)

    # Iterate over each period in the list
    for period in list_of_periods:
        new_col = f"weight_{period}"

        # Calculate reverse rolling weights within each group
        df[new_col] = df.groupby("ID")["weight"].transform(
            lambda x: x[::-1].rolling(window=period, min_periods=1).sum() / period
        )


def weighted_return(df, list_of_periods):

    for period in list_of_periods:
        new_col = f"fwd_weighted_return_mthly_{period}"
        weight_col = f"weight_{period}"
        df[new_col] = df[weight_col] * df["fwd_return_mthly"]

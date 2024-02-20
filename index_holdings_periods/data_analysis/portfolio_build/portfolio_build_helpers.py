import pandas as pd


# def weights_for_portfolios(df, list_of_periods):
#     df.sort_values(by=["ID", "date"], ascending=[True, False], inplace=True)

#     for period in list_of_periods:
#         new_col = f"weight_{period}"
#         df[new_col] = 0
#         for row in range(0, len(df)):
#             for mth in range(0, period):
#                 mth = mth - 1
#                 if df.iloc[row]["ID"] == df.iloc[row + mth]["ID"]:
#                     df.loc[df.index[row], new_col] = (
#                         df.iloc[row + mth]["weight"] / period
#                     ) + df.loc[df.index[row], new_col]

#     print(df)


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

    return df

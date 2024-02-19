import pandas as pd
from datetime import datetime
from .data_loading import helper


def run(path_constituent_weights, path_constituent_pricing, periods_to_test):
    df_weights = helper.constituent_weights(path_constituent_weights)
    df_prices_initial = helper.constituent_pricing(path_constituent_pricing)
    df_prices = helper.get_returns_for_periods(df_prices_initial, periods_to_test)
    merged_df = pd.merge(df_weights, df_prices, on=["ID", "date"], how="left")
    merged_df.drop(columns=["return"], inplace=True)
    print(merged_df)

    # # Define the conversion function
    # datetime_to_excel_date = lambda dt: (dt - datetime(1899, 12, 30)).days

    # # Apply the conversion function to the 'Date' column
    # merged_df["date"] = merged_df["date"].apply(datetime_to_excel_date)

    # merged_df.to_excel(
    #     "C:\\Python\\research\\index_holdings_periods\\data\\output.xlsx", index=False
    # )


# TODO
"""
Merge pricing and weights
Spilt into helper file
Make manager file just call different functinos
"""

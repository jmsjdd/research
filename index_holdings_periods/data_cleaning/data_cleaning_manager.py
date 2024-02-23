from . import data_cleaning_helpers
import pandas as pd


def run(path_constituent_weights, path_constituent_pricing):
    df_weights = data_cleaning_helpers.constituent_weights(path_constituent_weights)
    print(df_weights)
    df_equal_weights = data_cleaning_helpers.calculate_equal_weights(df_weights)
    df_prices = data_cleaning_helpers.constituent_pricing(path_constituent_pricing)

    df_all = pd.merge(df_weights, df_prices, on=["date", "ID"], how="outer")
    df_all_equal_weights = pd.merge(
        df_equal_weights, df_prices, on=["date", "ID"], how="outer"
    )
    return df_weights, df_prices, df_all, df_all_equal_weights

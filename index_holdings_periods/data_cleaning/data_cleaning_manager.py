from . import data_cleaning_helpers
import pandas as pd


def run(path_constituent_weights, path_constituent_pricing):
    df_weights = data_cleaning_helpers.constituent_weights(path_constituent_weights)
    df_prices = data_cleaning_helpers.constituent_pricing(path_constituent_pricing)

    df_all = pd.merge(df_weights, df_prices, on=["date", "ID"], how="outer")

    return df_weights, df_prices, df_all

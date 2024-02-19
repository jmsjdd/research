import pandas as pd
from datetime import datetime
from .data_loading import helper


def run(path_constituent_weights, path_constituent_pricing):
    df_weights = helper.constituent_weights(path_constituent_weights)
    df_prices = helper.constituent_pricing(path_constituent_pricing)

    print(df_prices)


# TODO
"""
Merge pricing and weights
Spilt into helper file
Make manager file just call different functinos
"""

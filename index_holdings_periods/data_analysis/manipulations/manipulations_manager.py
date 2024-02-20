from . import manipulations_helpers


def full_index_constituents_data(df_weights, df_prices, list_of_periods):
    df_weights_all_periods = manipulations_helpers.weights_for_all_periods(
        df_weights, list_of_periods
    )
    print(df_weights_all_periods)
    df_returns = manipulations_helpers.get_returns_for_periods(
        df_prices, list_of_periods
    )
    df_returns_adj = manipulations_helpers.adj_returns_to_monthly(
        df_returns, list_of_periods
    )
    df = manipulations_helpers.merge(df_weights, df_returns_adj)
    manipulations_helpers.weighted_return(df, list_of_periods)
    manipulations_helpers.adj_weighted_return(df, list_of_periods)

    print("Full consituent ctrs calculated")
    return df


def index_returns(df, list_of_periods):
    df_grouped = manipulations_helpers.group_and_sum_intervals(df, list_of_periods)
    df_monthly_returns = manipulations_helpers.sum_different_periods(
        df_grouped, list_of_periods
    )
    df_cumulative_returns = manipulations_helpers.cumulative_returns(
        df_monthly_returns, list_of_periods
    )
    return df_cumulative_returns

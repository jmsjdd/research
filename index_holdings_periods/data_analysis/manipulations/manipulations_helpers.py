import pandas as pd
import numpy as np


def get_returns_for_periods(df, list_of_periods):
    # Sort the DataFrame by 'ID' and 'date'
    df.sort_values(by=["ID", "date"], inplace=True)

    # Calculate forward returns for each period and de-annualises returns to monthly
    for period in list_of_periods:
        forward_return_col = f"return_{period}"
        df[forward_return_col] = (
            df.groupby("ID")["price_t"].shift(-period) / df["price_t"] - 1
        )

    return df


def adj_returns_to_monthly(df, list_of_periods):
    # Sort the DataFrame by 'ID' and 'date'
    df.sort_values(by=["ID", "date"], inplace=True)

    # Calculate forward returns for each period and de-annualises returns to monthly
    for period in list_of_periods:
        return_col = f"return_{period}"
        adj_return_col = f"return_adj_{period}"
        df[adj_return_col] = (1 + df[return_col]) ** (1 / period) - 1

    return df


def merge(df_weights, df_prices):
    # Merge data
    merged_df = pd.merge(df_weights, df_prices, on=["ID", "date"], how="left")
    merged_df.drop(columns=["return"], inplace=True)

    return merged_df


def weighted_return(df, list_of_periods):
    for period in list_of_periods:
        df[f"weighted_return_{period}"] = df["weight"] * df[f"return_adj_{period}"]

    return df


def adj_weighted_return(df, list_of_periods):
    for period in list_of_periods:
        df[f"adj_weighted_return_{period}"] = df[f"weighted_return_{period}"] / period

    return df


def group_and_sum_intervals(
    df, list_of_periods, group_column="date", return_columns=None
):
    # Generate the list of columns to sum based on the list of periods
    return_columns = [f"adj_weighted_return_{interval}" for interval in list_of_periods]

    # Define the aggregation functions
    agg_funcs = {col: "sum" for col in return_columns}

    # Group by the specified column and apply the aggregation functions
    grouped_df = df.groupby(group_column).agg(agg_funcs).reset_index()

    return grouped_df


def sum_different_periods(df, list_of_periods):
    df = df.sort_values(by="date", ascending=True)  # Sort in ascending order by date

    for period in list_of_periods:
        old_col_name = f"adj_weighted_return_{period}"
        new_col_name = (
            f"rolling_sum_{period}"  # Update column name to reflect rolling sum
        )

        # Calculate the rolling sum using a vectorized operation
        df[new_col_name] = df[old_col_name].rolling(window=period, min_periods=1).sum()

        # Where the original column has 0 values, replace with NaN
        df.loc[df[old_col_name] == 0, new_col_name] = np.nan

    return df


def cumulative_returns(df, list_of_periods):
    df = df.sort_values(by="date", ascending=True)  # Sort in ascending order by date
    for period in list_of_periods:
        old_col_name = f"rolling_sum_{period}"
        new_col_name = f"{period} month rebalancing cumulation"
        df[new_col_name] = (1 + df[old_col_name]).cumprod() - 1

    return df


# def adj_returns(df, list_of_periods):


# TODO
"""
Get weight* return for each date
For 

 Returns are calculated following the methodology used by Hou, Xue and Zhang (2017). 
 For a holding period greater than one month, such as when rebalancing is annual, for 
 a given decile in each month, there are 12 sub-deciles, each of which is initiated in 
 the prior 12-month period. The average of the sub-decile one-month forward returns 
 at each month is then taken as the monthly return of that decile for that month. In 
 the three-yearly rebalancing case, because there are not 36 different sub-deciles until 
 1966, returns are only calculated from 1966-2016 which is why all analyses comparing the 
 monthly, annual and three yearly rebalancing periods cover the period 1966-2016 instead of 1963-2016.

"""

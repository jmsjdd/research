import pandas as pd


def monthly_constituent_returns(df):
    # Sort the DataFrame by 'ID' and 'date'
    df.sort_values(by=["ID", "date"], inplace=True)

    # Calculate forward returns for each period and de-annualises returns to monthly
    forward_return_col = f"fwd_return_mthly"
    df[forward_return_col] = df.groupby("ID")["price_t"].shift(-1) / df["price_t"] - 1
    # print(df)
    # df.to_excel(
    #     "C:\\Python\\research\\index_holdings_periods\\data\\output.xlsx", index=False
    # )
    return df


def cumulate_returns(df, list_of_periods):
    df = df.sort_values(by="date", ascending=True)  # Sort in ascending order by date

    for period in list_of_periods:
        old_col_name = f"fwd_weighted_return_mthly_{period}"
        new_col_name = f"{period} month rebalancing cumulation"
        df[new_col_name] = (1 + df[old_col_name]).cumprod() - 1

    return df

import pandas as pd


def weights_for_portfolios(df, list_of_periods):
    df.sort_values(by=["ID", "date"], ascending=[True, False], inplace=True)

    for period in list_of_periods:
        new_col = f"weight_{period}"
        df[new_col] = 0
        for row in range(0, len(df)):
            for mth in range(0, period):
                mth = mth - 1
                if df.iloc[row]["ID"] == df.iloc[row + mth]["ID"]:
                    df.loc[df.index[row], new_col] = (
                        df.iloc[row + mth]["weight"] / period
                    ) + df.loc[df.index[row], new_col]

    print(df)

from data_analysis.manipulations import manipulations_utils
import pandas as pd

def merge(df_weights, df_prices):
    # Merge data
    merged_df = pd.merge(df_weights, df_prices, on=["ID", "date"], how="left")
    merged_df.drop(columns=["return"], inplace=True)

    return merged_df


def weighted_return(df, list_of_periods):
    #will get weight*returns
    print('test')


def adj_returns(df, list_of_periods):



#TODO
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

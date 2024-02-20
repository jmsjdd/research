from . import portfolio_build_helpers


def run(df, list_of_periods):
    portfolio_build_helpers.weights_for_portfolios(df, list_of_periods)
    portfolio_build_helpers.weighted_return(df, list_of_periods)


"""
Get weight* return for each date
 Returns are calculated following the methodology used by Hou, Xue and Zhang (2017). 
 For a holding period greater than one month, such as when rebalancing is annual, for 
 a given decile in each month, there are 12 sub-deciles, each of which is initiated in 
 the prior 12-month period. The average of the sub-decile one-month forward returns 
 at each month is then taken as the monthly return of that decile for that month. In 
 the three-yearly rebalancing case, because there are not 36 different sub-deciles until 
 1966, returns are only calculated from 1966-2016 which is why all analyses comparing the 
 monthly, annual and three yearly rebalancing periods cover the period 1966-2016 instead of 1963-2016.

 
  Returns are calculated following the methodology used by Hou, Xue and Zhang (2017). 
 For a holding period greater than one month, such as when rebalancing is annual, there are 12 sub-deciles, each of which is initiated in 
 the prior 12-month period. The average of the sub-decile one-month forward returns 
 at each month is then taken as the monthly return of that decile for that month. In 
 the three-yearly rebalancing case, because there are not 36 different sub-deciles until 
 1966, returns are only calculated from 1966-2016 which is why all analyses comparing the 
 monthly, annual and three yearly rebalancing periods cover the period 1966-2016 instead of 1963-2016.
"""

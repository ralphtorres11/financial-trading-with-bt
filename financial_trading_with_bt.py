import pandas as pd
import matplotlib.pyplot as plt
import bt

# add the below if using jupyter notebook
%matplotlib inline

# download historical prices
bt_data = bt.get('goog, amzn, tsla',
                 start = '2020-6-1', 
                 end = '2020-12-1')
print(bt_data.head())

# define the strategy
bt_strategy = bt.Strategy('Trade_Weekly',
                          [bt.algos.RunWeekly(), # run weekly
                           bt.algos.SelectAll(), # use all data
                           bt.algos.WeighEqually(), # maintain equal weights
                           bt.algos.Rebalance()]) # rebalance

# create a backtest
bt_test = bt.Backtest(bt_strategy, bt_data)

# run the backtest
bt_res = bt.run(bt_test)

# get trade details
bt_res.get_transactions()

# plot the result
bt_res.plot(title = "Backtest result")

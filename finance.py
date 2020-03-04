import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame


start = datetime.datetime(2019, 1, 10)
end = datetime.datetime(2020, 1, 11)

dfcomp = web.DataReader(['AAPL', 'SBUX', 'GOOG', 'VZ', 'MSFT','STAG','WPG','UNP','FB','AXP'],'yahoo',start=start,end=end)['Adj Close']
dfcomp.tail(5)

dfcomp.to _csv (r'/Users/saul/Desktop/exportfinancesaul_dataframe.csv‘, index = None, header=True)



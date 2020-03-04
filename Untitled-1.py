import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame


start = datetime.datetime(2015, 1, 11)
end = datetime.datetime(2020, 1, 11)

#df = web.DataReader("VZ", 'yahoo', start, end)
#df.tail()

dfcomp = web.DataReader(['AAPL', 'SBUX', 'GOOG', 'VZ', 'MSFT','STAG','WPG','UNP','FB','AXP'],'yahoo',start=start,end=end)['Adj Close']
#dfcomp.tail()
dfcomp.to_csv(r'/Users/saul/Downloads/Finance3.csv',)
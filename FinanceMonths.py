import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame

#variables to set the start time to start pulling historical data from stocks and apprpiate index
start = datetime.datetime(2010, 1, 11)
end = datetime.datetime(2020, 3, 4)
#stocks that I am interersted in 
stocks = ['AAPL', 'SBUX', 'GOOG', 'VZ', 'MSFT','STAG','WPG','UNP','FB','AXP','SPY','VTI','VOO']
stocks1 = ['^DJI']
#data = web.get_data_yahoo(stocks,'01/01/2010',interval='m')['Adj Close']
#only want the Adj Close
data = web.get_data_yahoo(stocks1,start,interval='m')['Adj Close']

#data.head(50).mean()
#I want a CSV file that I can use for excel 
data.to_csv(r'/Users/saul/Documents/GitHub/Stock-Data/Finance11.csv',)

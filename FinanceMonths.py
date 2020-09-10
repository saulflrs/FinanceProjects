import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame

#variables to set the start time to start pulling historical data from stocks and apprpiate index
start = datetime.datetime(2001, 1, 11)
end = datetime.datetime(2020, 3, 12)
#stocks that I am interersted in 
stocks2 =["ALK" ,	"ADS" ,	"ALL" ,	"AAL" ,	"AMP" ,	"BK" ,	"BWA" ,	"COF" ,	"CPRI" ,	"CCL" ,	"CINF" ,	"C" ,	"CFG" ,	"CMA" ,	"COP" ,	"DAL" ,	"DFS" ,	"FITB" ,	"GPS" ,	"GM" ,	"HBI" ,	"HFC" ,	"HBAN" ,	"JCI" ,	"KSS" ,	"LNC" ,	"LYB" ,	"M" ,	"MPC" ,	"MET" ,	"MGM" ,	"MS" ,	"JWN" ,	"NLOK" ,	"NCLH" ,	"NRG" ,	"PFG" ,	"PRU" ,	"PVH" ,	"RF" ,	"RCL" ,	"SIVB" ,	"SYF" ,	"UAL" ,	"URI" ,	"UNM" ,	"VIAC" ,	"VNO" ,	"WRK" ,	"WHR" ,	"ZION" ,]
stocks = ['AAPL', 'SBUX', 'GOOG', 'VZ', 'MSFT','STAG','WPG','UNP','FB','AXP','SPY','VTI','VOO']
stocks1 = ['^DJI']
#data = web.get_data_yahoo(stocks,'01/01/2010',interval='m')['Adj Close']
#only want the Adj Close
data = web.get_data_yahoo(stocks2,start,interval='m')['Adj Close']

#data.head(50).mean()
#I want a CSV file that I can use for excel 
data.to_csv(r'/Users/saul/Documents/GitHub/Stock-Data/Finance21.csv',)


#https://stackoverflow.com/questions/54815864/downloading-a-companies-market-cap-from-yahoo
#the link above has info on other changes I can make with to the yahoo API

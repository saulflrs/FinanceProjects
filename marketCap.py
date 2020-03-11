#marketCap.py
#I want to download files to that give me overall marketcap of a stock

from pandas_datareader import data

tickers = ['AAPL','AMZN','TSLA','GOOG']
data.get_quote_yahoo(tickers)['marketCap']

data.head()


#https://stackoverflow.com/questions/54815864/downloading-a-companies-market-cap-from-yahoo
#the link above has info on other changes I can make with to the yahoo API
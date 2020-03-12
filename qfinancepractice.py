#quandl pull data for free using python 


import quandl
mydata = quandl.get("FRED/GDP")

print(mydata)

mydata.to_csv(r'/Users/saul/Documents/GitHub/Stock-Data/QuandlGDP001.csv',)
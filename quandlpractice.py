#quandl pull data for free using python 


import quandl
mydata = quandl.get("FRED/GDP")

print(mydata)

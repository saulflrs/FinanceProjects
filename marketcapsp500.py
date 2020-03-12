#s&p500 market cap pull from quandl

import quandl
quandl.ApiConfig.api_key = 'kjPrw_3wbz5LakWcmxi_'
import numpy as np
import pandas as pd
# Download financial data from Quandl/Sharadar
table = quandl.get_table('SHARADAR/SF1', paginate=True)
# Grab the most recent annual data ('MRY' denotes annual data)
stock_df = table[(table['calendardate'] == '2017-12-31 00:00:00') & (table['dimension']=='MRY')]


stock_df.to_csv(r'/Users/saul/Documents/GitHub/Stock-Data/QuandlMK501.csv',)
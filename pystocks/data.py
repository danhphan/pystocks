import pandas as pd
from pandas_datareader import data


def get_tickers(tickers, start_date, end_date):
    

df = data.get_data_yahoo("MSFT")

print(df.shape)



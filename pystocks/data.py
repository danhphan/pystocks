import pandas as pd
from pandas_datareader import data as pdr_data


def get_tickers(tickers, start_date, end_date):
    def get_data(ticker):
        return(pdr_data.get_data_yahoo(ticker, start=start_date, end=end_date))

    dfs = map(get_data, tickers)
    return pd.concat(dfs, keys=tickers, names=['Ticker', 'Date'])
df = pdr_data.get_data_yahoo("MSFT")

print(df.shape)



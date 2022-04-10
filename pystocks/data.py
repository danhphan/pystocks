import pandas as pd
from pandas_datareader import data as pdr_data
import datetime

def get_tickers(tickers, start_date, end_date):
    def get_data(ticker):
        return(pdr_data.get_data_yahoo(ticker, start=start_date, end=end_date))

    dfs = map(get_data, tickers)
    return pd.concat(dfs, keys=tickers, names=['Ticker', 'Date'])

startdate = datetime.datetime(2015,1,1)
enddate = datetime.datetime(2022,1,1)
tickers = ["FB", "AMZN", "AAPL", "NFLX", "GOOD"]
dfs = get_tickers(tickers, start_date=startdate, end_date=enddate)

dfs.to_csv("./data/tickers.csv")
print(dfs.shape)



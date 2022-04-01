import pandas as pd
import yfinance as yf


FinTech_tickers=pd.read_csv("FinTech_tickers_sample.csv")
print(FinTech_tickers)


def download_most_recent_price(ticker_new):
    data=yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers=ticker_new,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period="1d",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval="1d",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        #group_by='ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust=True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost=True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads=True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy=None
    )
    data=data.reset_index()
    data["Ticker_name"]=ticker_new
    data_new=pd.DataFrame({
        'Ticker':ticker_new,
        'Date':data["Date"],
        'Close_price':data["Close"]
    })
    return(data_new)

df_combined = pd.DataFrame()


for index, row in FinTech_tickers.iterrows():
    df_tempt=download_most_recent_price(row['Ticker'])
    df_combined=df_combined.append(df_tempt)
    print(df_combined)

df_combined.to_csv("FinTech_prices_sample.csv")





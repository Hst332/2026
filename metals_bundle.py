import yfinance as yf

def load_silver():
    df = yf.download("SI=F", start="2010-01-01", progress=False)
    return df

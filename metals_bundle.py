import yfinance as yf

def _load(symbol):
    df = yf.download(symbol, period="6mo", interval="1d", auto_adjust=True)
    df = df.dropna()
    return df

def load_gold():
    return _load("GC=F")      # Gold Futures

def load_silver():
    return _load("SI=F")      # Silver Futures

def load_gas():
    return _load("NG=F")      # Natural Gas

def load_copper():
    return _load("HG=F")      # Copper Futures

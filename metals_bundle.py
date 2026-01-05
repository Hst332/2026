import yfinance as yf
import pandas as pd

def _load(symbol, period="2y"):
    df = yf.download(symbol, period=period, progress=False)
    df = df[["Close"]].dropna()
    df["prob_up"] = 0.50  # placeholder (kommt aus deinem Modell)
    return df

def load_gold():
    return _load("GC=F")

def load_silver():
    return _load("SI=F")

def load_gas():
    return _load("NG=F")

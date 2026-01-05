import yfinance as yf
import pandas as pd

START_DATE = "2010-01-01"

def load_gold():
    df = yf.download("GC=F", start=START_DATE, progress=False)
    df = df.dropna()
    df["prob_up"] = df["Close"].pct_change().rolling(10).mean().fillna(0) + 0.5
    df["prob_up"] = df["prob_up"].clip(0, 1)
    return df

def load_silver():
    df = yf.download("SI=F", start=START_DATE, progress=False)
    df = df.dropna()
    df["prob_up"] = df["Close"].pct_change().rolling(10).mean().fillna(0) + 0.5
    df["prob_up"] = df["prob_up"].clip(0, 1)
    return df

def load_gas():
    df = yf.download("NG=F", start=START_DATE, progress=False)
    df = df.dropna()
    df["prob_up"] = df["Close"].pct_change().rolling(5).mean().fillna(0) + 0.5
    df["prob_up"] = df["prob_up"].clip(0, 1)
    return df

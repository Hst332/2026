import yfinance as yf
import pandas as pd

def load_gold():
    ticker = "GC=F"  # Gold Futures
    df = yf.download(ticker, period="60d", interval="1d")
    df["prob_up"] = 0.53  # Platzhalter für Forecast-Modelle
    df.index.name = "Date"
    return df

def load_silver():
    ticker = "SI=F"  # Silber Futures
    df = yf.download(ticker, period="60d", interval="1d")
    df["prob_up"] = 0.50
    df.index.name = "Date"
    return df

def load_gas():
    ticker = "NG=F"  # Natural Gas Futures
    df = yf.download(ticker, period="60d", interval="1d")
    df["prob_up"] = 0.56
    df.index.name = "Date"
    return df

def load_copper():
    ticker = "HG=F"  # Copper Futures
    df = yf.download(ticker, period="60d", interval="1d")
    df["prob_up"] = 0.535
    df.index.name = "Date"
    return df

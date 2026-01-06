# metals_bundle.py
import yfinance as yf
import pandas as pd

START_DATE = "2010-01-01"

def _load(symbol):
    df = yf.download(symbol, start=START_DATE, progress=False)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()
    return df


def load_gold():
    return _load("GC=F")          # Gold Futures


def load_silver():
    return _load("SI=F")          # Silver Futures


def load_gas():
    return _load("NG=F")          # Natural Gas


def load_copper():
    return _load("HG=F")          # Copper Futures

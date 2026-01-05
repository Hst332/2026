import pandas as pd

def load_gold():
    return pd.read_csv("gold_data.csv", index_col=0, parse_dates=True)

def load_silver():
    return pd.read_csv("silver_data.csv", index_col=0, parse_dates=True)

def load_gas():
    return pd.read_csv("gas_data.csv", index_col=0, parse_dates=True)

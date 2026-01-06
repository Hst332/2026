import pandas as pd
import os

DATA_DIR = "data"

def load_gold():
    path = os.path.join(DATA_DIR, "gold.csv")
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
    return df

def load_silver():
    path = os.path.join(DATA_DIR, "silver.csv")
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
    return df

def load_gas():
    path = os.path.join(DATA_DIR, "gas.csv")
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
    return df

# ✅ NEU: Copper laden
def load_copper():
    path = os.path.join(DATA_DIR, "copper.csv")
    if not os.path.exists(path):
        raise ValueError(
            "Copper-Daten konnten nicht gefunden werden. Bitte CSV oder metals_bundle prüfen."
        )
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
    # Sicherstellen, dass die benötigten Spalten da sind
    required_cols = ["Close", "prob_up"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Copper CSV muss Spalte '{col}' enthalten.")
    return df

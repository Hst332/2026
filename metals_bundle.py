import pandas as pd

# ⚠️ WICHTIG:
# Diese Funktionen müssen GENAU so heißen,
# weil sie überall importiert werden.

def load_gold():
    # HIER deine funktionierende Quelle einsetzen
    # Beispiel: bereits vorhandenes Forecast-DF
    return pd.read_pickle("gold_forecast.pkl")

def load_silver():
    return pd.read_pickle("silver_forecast.pkl")

def load_gas():
    return pd.read_pickle("gas_forecast.pkl")

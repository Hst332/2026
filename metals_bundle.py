# metals_bundle.py
# Zentrale Datenquelle – KEINE Files, KEIN I/O

from forecast_gold import df_gold
from forecast_silver import df_silver
from forecast_gas import df_gas


def load_gold():
    return df_gold.copy()


def load_silver():
    return df_silver.copy()


def load_gas():
    return df_gas.copy()

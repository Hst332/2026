from data_loader import load_asset
from model_core import model_score
from forecast_utils import forecast_trend, trade_signal


ASSETS = {
    "GOLD":   ("GC=F", "USD/oz"),
    "SILVER": ("SI=F", "USD/oz"),
    "GAS":    ("NG=F", "USD/MMBtu"),
    "COPPER": ("HG=F", "USD/lb"),
}


def forecast_asset(name, ticker, unit):
    df = load_asset(ticker)

    close = float(df["Close"].iloc[-1])
    score = model_score(df)

  return {
    "asset": name,
    "close": close,
    "score": score,
    "signal": signal,
    "f_1_5": forecast_trend(df, 5),
    "f_2_3": forecast_trend(df, 21),   # ← DAS FEHLTE
}



def run_all():
    results = []
    for name, (ticker, unit) in ASSETS.items():
        results.append(forecast_asset(name, ticker, unit))
    return results

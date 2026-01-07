import yfinance as yf
from datetime import datetime
from forecast_utils import model_score, forecast_trend, trade_signal


def copper_result():
    df = yf.download("HG=F", period="1y", interval="1d")

    close_lb = df["Close"].iloc[-1]          # USD / lb
    close_kg = close_lb * 2.20462            # USD / kg
    score = model_score(df)

    return {
        "asset": "COPPER",
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "close": f"{close_kg:.2f} USD/kg",
        "model_score": f"{score:.2%}",
        "signal": trade_signal(score),
        "f_short": forecast_trend(df, 5),
        "f_mid": forecast_trend(df, 21),
    }

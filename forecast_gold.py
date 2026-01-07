import yfinance as yf
from datetime import datetime
from forecast_utils import model_score, forecast_trend, trade_signal


def gold_result():
    df = yf.download("GC=F", period="1y", interval="1d")

    close = df["Close"].iloc[-1]
    score = model_score(df)

    return {
        "asset": "GOLD",
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/oz",
        "model_score": f"{score:.2%}",
        "signal": trade_signal(score),
        "f_short": forecast_trend(df, 5),
        "f_mid": forecast_trend(df, 21),
    }

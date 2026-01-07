import yfinance as yf
from forecast_utils import model_score, forecast_trend, trade_signal

def gold_result():
    df = yf.download("GC=F", period="2mo", interval="1d")
    close = float(df["Close"].iloc[-1])
    score = model_score(df)
    return {
        "asset": "GOLD",
        "date": df.index[-1].strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/oz",
        "model_score": f"{score:.2%}",
        "signal": trade_signal(score),
        "forecast_1_5d": forecast_trend(df, 5),
        "forecast_2_3w": forecast_trend(df, 21),
        "strategy_lines": [
            "0.53–0.55 → YES50",
            "≥ 0.55 → YES100",
            "No Short | Lev ≤ 5",
        ]
    }

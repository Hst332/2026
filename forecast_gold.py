import metals_bundle
from forecast_utils import model_score, forecast_trend

def gold_result():
    df = metals_bundle.load_gold()
    last = df.iloc[-1]

    close = float(df["Close"].iloc[-1])
    date = df.index[-1].strftime("%Y-%m-%d")
    
    score = model_score(df)
    
    return {
        "asset": "GOLD",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/oz",
        "model_score": f"{score:.2%}",
        "signal": "NO_TRADE",
        "forecast_1_5d": forecast_trend(df, 5),
        "forecast_2_3w": forecast_trend(df, 15),
        "strategy_lines": [
            "0.53–0.55 → YES50",
            "≥ 0.55 → YES100",
            "No Short | Lev ≤ 5",
        ],
    }

import metals_bundle
from forecast_utils import model_score, forecast_trend

def copper_result():
    df = metals_bundle.load_gold()
    last = df.iloc[-1]

    close = float(df["Close"].iloc[-1])
    date = df.index[-1].strftime("%Y-%m-%d")


    return {
        "asset": "COPPER",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f* 2.20462} USD/kg",
        "model_score": f"{score:.2%}",
        "signal": "NO_TRADE",
        "forecast_1_5d": forecast_trend(df, 5),
        "forecast_2_3w": forecast_trend(df, 20),
        "strategy_lines": [
            "Industrial metal | China driven",
            "Cycle & infrastructure sensitive",
            "Phase-2 momentum model",
        ],
    }

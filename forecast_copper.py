import metals_bundle
from forecast_utils import model_score, forecast_trend, trade_signal

def copper_result():
    df = metals_bundle.load_copper()
    last = df.iloc[[-1]]  # bewusst DataFrame, kein Series

    close = float(last["Close"].iloc[0])
    score = model_score(df)

    return {
        "asset": "COPPER",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{last['Close'] * 2.20462:.2f} USD/kg",
        "model_score": f"{score:.2%}",
        "signal": trade_signal(score),
        "forecast_1_5d": forecast_trend(df, 5),
        "forecast_2_3w": forecast_trend(df, 20),
        "strategy_lines": [
            "Industrial metal | China driven",
            "Cycle & infrastructure sensitive",
            "Phase-2 momentum model",
        ],
    }

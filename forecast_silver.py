from metals_bundle import load_silver
from forecast_utils import model_score, forecast_trend, trade_signal

def silver_result():
    df = load_silver()
    close = float(df["Close"].iloc[-1])
    score = model_score(df)

    return {
        "asset": "SILVER",
        "close": f"{close:.2f} USD/oz",
        "model_score": f"{score:.2%}",
        "signal": trade_signal(score),
        "f_short": forecast_trend(df, 5),
        "f_mid": forecast_trend(df, 21),
    }

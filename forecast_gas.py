from metals_bundle import load_gas
from forecast_utils import model_score, forecast_trend, trade_signal

def gas_result():
    df = load_gas()
    close = float(df["Close"].iloc[-1])
    score = model_score(df)

    return {
        "asset": "NATURAL GAS",
        "close": f"{close:.2f} USD/MMBtu",
        "model_score": f"{score:.2%}",
        "signal": trade_signal(score),
        "f_short": forecast_trend(df, 5),
        "f_mid": forecast_trend(df, 21),
    }

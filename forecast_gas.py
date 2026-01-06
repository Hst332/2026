import metals_bundle
from forecast_utils import model_score, forecast_trend, trade_signal

def gas_result():
    df = metals_bundle.load_gold()
    last = df.iloc[-1]

    close = float(last["Close"])
    score = model_score(df)

    return {
        "asset": "NATURAL GAS",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{last['Close']:.2f} USD/MMBtu",
        "model_score": f"{score:.2%}",
        "signal": trade_signal(score),
        "forecast_1_5d": forecast_trend(df, 5),
        "forecast_2_3w": forecast_trend(df, 20),
        "strategy_lines": [
            "≥ 56 % → LONG",
            "≤ 44 % → SHORT",
            "Lev ≤ 10 | SL −20 %",
        ],
    }

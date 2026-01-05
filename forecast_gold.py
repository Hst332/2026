import yfinance as yf
from forecast_writer import write_asset_row

def forecast_gold():
    df = yf.download("GC=F", period="6mo", progress=False)
    last = df.iloc[-1]

    close = float(last["Close"])
    prob_up = 0.5024  # ← kommt aus deinem Modell

    if prob_up >= 0.55:
        signal = "LONG"
        position = "100 %"
    elif prob_up >= 0.53:
        signal = "LONG"
        position = "50 %"
    else:
        signal = "NO_TRADE"
        position = "0 %"

    strategy = [
        "0.53–0.55 → 50 %",
        "≥ 0.55 → 100 %",
        "No Short | Lev ≤ 5"
    ]

    write_asset_row(
        asset="GOLD",
        date=last.name.strftime("%Y-%m-%d"),
        close=close,
        prob_up=prob_up,
        signal=signal,
        position=position,
        strategy_lines=strategy
    )

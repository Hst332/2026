import yfinance as yf
from forecast_writer import write_asset_row

def forecast_silver():
    df = yf.download("SI=F", period="6mo", progress=False)
    last = df.iloc[-1]

    close = float(last["Close"])
    prob_up = 0.5179  # Modellwert

    if prob_up >= 0.96:
        signal = "LONG"
        position = "100 %"
    else:
        signal = "NO_TRADE"
        position = "0 %"

    strategy = [
        "≥ 0.96 → LONG",
        "Long only",
        "Lev ≤ 15 | SL −20 %"
    ]

    write_asset_row(
        asset="SILVER",
        date=last.name.strftime("%Y-%m-%d"),
        close=close,
        prob_up=prob_up,
        signal=signal,
        position=position,
        strategy_lines=strategy
    )

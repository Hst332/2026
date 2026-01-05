from forecast_writer import write_asset_row

def forecast_gas(date, close, prob_up):
    if prob_up >= 0.56:
        signal = "LONG"
        position = "100 %"
    elif prob_up <= 0.44:
        signal = "SHORT"
        position = "100 %"
    else:
        signal = "NO_TRADE"
        position = "0 %"

    strategy = [
        "≥ 56 % → LONG",
        "≤ 44 % → SHORT",
        "Lev ≤ 10 | SL −20 %"
    ]

    write_asset_row(
        asset="NATURAL GAS",
        date=date,
        close=close,
        prob_up=prob_up,
        signal=signal,
        position=position,
        strategy_lines=strategy
    )

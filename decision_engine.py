def trade_decision(asset: str, prob_up: float):
    """
    Zentrale Handelslogik.
    MUSS im Backtest und im Daily Forecast identisch genutzt werden.
    """

    asset = asset.upper()

    # ---------------- GOLD ----------------
    if asset == "GOLD":
        if prob_up >= 0.55:
            return "LONG", "100%"
        elif prob_up >= 0.53:
            return "LONG", "50%"
        else:
            return "NO_TRADE", "-"

    # ---------------- SILVER ----------------
    if asset == "SILVER":
        if prob_up >= 0.96:
            return "LONG", "100%"
        else:
            return "NO_TRADE", "-"

    # ---------------- COPPER ----------------
    if asset == "COPPER":
        if prob_up >= 0.56:
            return "LONG", "100%"
        else:
            return "NO_TRADE", "-"

    # ---------------- NATURAL GAS ----------------
    if asset == "NATURAL GAS":
        if prob_up >= 0.56:
            return "LONG", "100%"
        elif prob_up <= 0.44:
            return "SHORT", "100%"
        else:
            return "NO_TRADE", "-"

    # ---------------- FALLBACK ----------------
    return "NO_TRADE", "-"

def decide_trade(asset, prob_up):
    asset = asset.upper()

    # NATURAL GAS (LONG + SHORT)
    if asset == "NATURAL GAS":
        if prob_up >= 0.56:
            return "LONG"
        elif prob_up <= 0.44:
            return "SHORT"
        else:
            return "NO_TRADE"

    # SILVER (LONG only)
    if asset == "SILVER":
        if prob_up >= 0.96:
            return "LONG"
        else:
            return "NO_TRADE"

    # GOLD (LONG only, abgestuft)
    if asset == "GOLD":
        if prob_up >= 0.55:
            return "LONG_FULL"
        elif prob_up >= 0.53:
            return "LONG_HALF"
        else:
            return "NO_TRADE"

    # COPPER (LONG only)
    if asset == "COPPER":
        if prob_up >= 0.56:
            return "LONG"
        else:
            return "NO_TRADE"

    return "NO_TRADE"

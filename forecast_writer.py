from datetime import datetime

def write_forecast_output(results, filename="forecast_output.txt"):
    """
    results: Liste von Dicts mit Schlüsseln:
      asset, prob_up
    """

    today = datetime.utcnow().strftime("%Y-%m-%d")

    lines = []
    lines.append(f"DATE: {today} (UTC)\n")
    lines.append("=" * 80)
    lines.append("DAILY TRADING FORECAST – EXECUTION FORMAT")
    lines.append("=" * 80 + "\n")

    lines.append(
        f"{'ASSET':<12}{'SIGNAL':<11}{'SIZE':<9}"
        f"{'PROB_UP':<10}{'ENTRY TYPE':<17}"
        f"{'HOLD':<12}{'RISK RULE'}"
    )
    lines.append("-" * 80)

    for r in results:
        asset = r["asset"]
        prob = float(r["prob_up"])

        # =========================
        # DECISION LOGIC (FINAL)
        # =========================

        signal = "NO TRADE"
        size = "–"
        entry = "–"
        hold = "–"
        risk = "–"

        if asset == "GOLD":
            if prob >= 0.55:
                signal = "LONG"
                size = "100%"
                entry = "Trend-Long"
                hold = "5–20d"
                risk = "SL optional"
            elif prob >= 0.53:
                signal = "LONG"
                size = "50%"
                entry = "Trend-Long"
                hold = "5–20d"
                risk = "SL optional"

        elif asset == "SILVER":
            if prob >= 0.96:
                signal = "LONG"
                size = "100%"
                entry = "High-Conviction"
                hold = "5–20d"
                risk = "SL −20%"

        elif asset == "COPPER":
            if prob >= 0.56:
                signal = "LONG"
                size = "100%"
                entry = "Cyclical Long"
                hold = "5–15d"
                risk = "SL −20%"

        elif asset == "NATURAL GAS":
            if prob >= 0.56:
                signal = "LONG"
                size = "100%"
                entry = "Trend"
                hold = "5–15d"
                risk = "SL −20%"
            elif prob <= 0.44:
                signal = "SHORT"
                size = "100%"
                entry = "Mean Reversion"
                hold = "5–15d"
                risk = "SL −20%"

        lines.append(
            f"{asset:<12}{signal:<11}{size:<9}"
            f"{prob:<10.2f}{entry:<17}"
            f"{hold:<12}{risk}"
        )

    lines.append("-" * 80 + "\n")

    # =========================
    # RULE BLOCK (STATIC)
    # =========================

    lines.append("=" * 80)
    lines.append("TRADING RULES (FINAL – BACKTEST VALIDATED)")
    lines.append("=" * 80 + "\n")

    lines.append(
        "GOLD\n"
        "- LONG only\n"
        "- Entry: prob_up ≥ 0.53\n"
        "- Size: 0.53–0.55 → 50% | ≥0.55 → 100%\n"
        "- Hold: 5–20 days | Leverage max 3–5\n\n"

        "SILVER\n"
        "- LONG only\n"
        "- Entry: prob_up ≥ 0.96\n"
        "- Trades/year ~12 | Leverage max 15\n"
        "- Stop-Loss: −20% hard\n\n"

        "COPPER\n"
        "- LONG only\n"
        "- Entry: prob_up ≥ 0.56 (optimal 0.56–0.60)\n"
        "- Leverage max 5–10 | Stop-Loss −20%\n\n"

        "NATURAL GAS\n"
        "- LONG  if prob_up ≥ 0.56\n"
        "- SHORT if prob_up ≤ 0.44\n"
        "- Hold: 5–15 days | Leverage max 10\n"
        "- Stop-Loss: −20% hard\n"
    )

    lines.append("=" * 80 + "\n")

    with open(filename, "w") as f:
        f.write("\n".join(lines))

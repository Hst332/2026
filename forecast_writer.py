from datetime import datetime

def write_forecast_output(results, filename="forecast_output.txt"):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M")

    with open(filename, "w") as f:
        f.write("=" * 90 + "\n")
        f.write("MARKET FORECAST – DAILY TRADE SHEET\n")
        f.write(f"Run time (UTC): {now}\n")
        f.write("=" * 90 + "\n\n")

        f.write(f"{'ASSET':<12}{'CLOSE':<13}{'SCORE':<8}{'SIGNAL':<11}{'1–5D':<8}{'2–3W':<8}\n")
        f.write("-" * 90 + "\n")

        for r in results:
            f.write(
                f"{r['asset']:<12}"
                f"{r['close']:<13}"
                f"{r['score']:<8}"
                f"{r['signal']:<11}"
                f"{r['f_1_5']:<8}"
                f"{r['f_2_3']:<8}\n"
            )

        f.write("-" * 90 + "\n\n")

        f.write("TRADE RULES (FINAL & BACKTEST-VALIDATED)\n")
        f.write("-" * 90 + "\n")
        f.write(
            "GOLD:\n"
            "- LONG only\n"
            "- Trade if prob_up ≥ 0.53\n"
            "- 0.53–0.55 → 50 % position size\n"
            "- ≥ 0.55 → 100 % position size\n"
            "- No short | Leverage max 3–5\n\n"

            "SILVER:\n"
            "- LONG only\n"
            "- Trade ONLY if prob_up ≥ 0.96\n"
            "- Below 0.96 → NO TRADE\n"
            "- Max leverage 15 | Hard SL −20 %\n\n"

            "NATURAL GAS:\n"
            "- LONG if prob_up ≥ 0.56\n"
            "- SHORT if prob_up ≤ 0.44\n"
            "- Else NO TRADE | Max lev 10 | SL −20 %\n\n"

            "COPPER:\n"
            "- LONG only\n"
            "- Trade if prob_up ≥ 0.56\n"
            "- Max lev 5–10 | Hard SL −20 %\n"
        )

        f.write("=" * 90 + "\n")

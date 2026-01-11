from datetime import datetime

def write_forecast_output(results, filename="forecast_output.txt"):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M")

    with open(filename, "w") as f:
        f.write("=" * 100 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {now}\n")
        f.write("=" * 100 + "\n")
        f.write(f"{'ASSET':<12}{'CLOSE':<13}{'SCORE':<8}{'SIGNAL':<12}{'1–5D':<7}{'2–3W'}\n")
        f.write("-" * 100 + "\n")

        for r in results:
            f.write(
                f"{r['asset']:<12}"
                f"{r['close']:.1f} {r['unit']:<6}"
                f"{r['score']:.3f}   "
                f"{r['signal']:<12}"
                f"{r['f_1_5']:<7}"
                f"{r['f_2_3']}\n"
            )

        f.write("-" * 100 + "\n\n")
        f.write("RULES (FINAL – BACKTEST VALIDATED)\n\n")

        f.write(
            "GOLD:\n"
            "• LONG only\n"
            "• prob_up ≥ 0.53 → LONG\n"
            "  0.53–0.55 → 50% position\n"
            "  ≥ 0.55    → 100% position\n"
            "• No Short | Leverage ≤ 5\n\n"

            "SILVER:\n"
            "• LONG only\n"
            "• prob_up ≥ 0.96 → LONG\n"
            "• Otherwise NO TRADE\n"
            "• Leverage ≤ 15 | Hard SL −20%\n\n"

            "NATURAL GAS:\n"
            "• prob_up ≥ 0.56 → LONG\n"
            "• prob_up ≤ 0.44 → SHORT\n"
            "• Otherwise NO TRADE\n"
            "• Leverage ≤ 10 | SL −20%\n\n"

            "COPPER:\n"
            "• LONG only\n"
            "• prob_up ≥ 0.56 → LONG\n"
            "• Industrial / China driven\n"
            "• Leverage ≤ 5–10 | SL −20%\n"
        )

        f.write("=" * 100 + "\n")

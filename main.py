from forecast_assets import run_all
from datetime import datetime

def main():
    results = run_all()

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    lines.append(f"Run time (UTC): {now}")
    lines.append("=" * 90)
    lines.append(f"{'ASSET':<10}{'CLOSE':<18}{'SCORE':<10}{'SIGNAL':<10}{'1–5D':<8}{'2–3W'}")
    lines.append("-" * 90)

    for r in results:
        line = (
            f"{r['asset']:<10}"
            f"{r['close']:<18}"
            f"{r['score']:<10}"
            f"{r['signal']:<10}"
            f"{r['f_1_5']:<8}"
            f"{r['f_2_3']}"
        )
        lines.append(line)

    output = "\n".join(lines)

    # 👉 WICHTIG: PRINT + DATEI
    print(output)

    with open("forecast_output.txt", "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()

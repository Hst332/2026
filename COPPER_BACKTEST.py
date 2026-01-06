import pandas as pd

# =========================
# CONFIG
# =========================
DATA_FILE = "copper_data.csv"

THRESHOLDS = [0.54, 0.55, 0.56, 0.58, 0.60, 0.62]

# =========================
# LOAD DATA
# =========================
def load_data():
    df = pd.read_csv(DATA_FILE, index_col=0, parse_dates=True)

    required_cols = {"Close", "prob_up", "Target"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required_cols}")

    df = df.dropna()
    return df


# =========================
# BACKTEST LOGIC
# =========================
def backtest(df, threshold):
    trades = 0
    wins = 0
    profit = 0

    for _, row in df.iterrows():
        prob = float(row["prob_up"])
        target = int(row["Target"])

        # LONG only
        if prob >= threshold:
            trades += 1
            if target == 1:
                wins += 1
                profit += 1
            else:
                profit -= 1

    accuracy = (wins / trades * 100) if trades > 0 else 0.0

    return {
        "TH": threshold,
        "Trades": trades,
        "Accuracy": accuracy,
        "Profit": profit,
    }


# =========================
# MAIN
# =========================
def main():
    print("[START] Copper backtest")

    df = load_data()

    results = []

    for th in THRESHOLDS:
        res = backtest(df, th)
        results.append(res)

        print(
            f"TH={res['TH']:.2f} | "
            f"Trades={res['Trades']} | "
            f"Accuracy={res['Accuracy']:.2f}% | "
            f"Profit={res['Profit']}"
        )

    # Save results
    out = pd.DataFrame(results)
    out.to_csv("copper_backtest_results.csv", index=False)

    print("\n[OK] copper_backtest_results.csv written")


# =========================
if __name__ == "__main__":
    main()

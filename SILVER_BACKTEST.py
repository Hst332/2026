#!/usr/bin/env python3
"""
SILVER BACKTEST
Automatischer Threshold-Test für Handelsentscheidungen
"""

# =======================
# IMPORTS
# =======================
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LogisticRegression

# =======================
# CONFIG
# =======================
SILVER_SYMBOL = "SI=F"
START_DATE = "2010-01-01"

# =======================
# LOAD SILVER PRICES
# =======================
def load_silver():
    df = yf.download(SILVER_SYMBOL, start=START_DATE, progress=False)
    if df.empty:
        return None
    df = df[["Close"]].rename(columns={"Close": "Close"})
    df.dropna(inplace=True)
    return df

# =======================
# BUILD FEATURES + TARGET
# =======================
def build_silver_features(df):
    df = df.copy()
    df["ret"] = df["Close"].pct_change()
    df["trend_5"] = df["Close"].pct_change(5)
    df["trend_20"] = df["Close"].pct_change(20)
    df["vol_10"] = df["ret"].rolling(10).std()
    df["Target"] = (df["ret"].shift(-1) > 0).astype(int)
    df.dropna(inplace=True)
    return df

# =======================
# TRAIN MODEL + PREDICT
# =======================
def train_silver_model(df):
    features = ["trend_5", "trend_20", "vol_10"]
    X = df[features]
    y = df["Target"]

    model = LogisticRegression(max_iter=200, class_weight="balanced")
    model.fit(X, y)

    df["prob_up"] = model.predict_proba(X)[:, 1]  # Wichtig für Backtest
    return df, model, features

# =======================
# BACKTEST
# =======================
def backtest(df, threshold):
    trades = []
    for i, row in df.iterrows():
        signal = None
        prob = float(row["prob_up"])
        if prob >= threshold:
            signal = 1  # LONG
        elif prob <= 1 - threshold:
            signal = -1  # SHORT
        else:
            continue

        # Profit: +1 für Treffer, -1 für Fehlsignal
        ret = 1 if (signal == 1 and row["Target"] == 1) or (signal == -1 and row["Target"] == 0) else -1
        trades.append(ret)

    trades = np.array(trades)
    if len(trades) == 0:
        return {"threshold": threshold, "accuracy": None, "profit": None, "n_trades": 0}

    accuracy = np.mean(trades > 0)
    profit = np.sum(trades)
    return {"threshold": threshold, "accuracy": accuracy, "profit": profit, "n_trades": len(trades)}

# =======================
# MAIN
# =======================
def main():
    print("[START] Silver backtest")

    # Lade Silberpreise
    df = load_silver()
    if df is None or len(df) == 0:
        print("[ERROR] No silver data loaded")
        return

    # Features + Target
    df = build_silver_features(df)

    # Modell + prob_up berechnen
    df, model, features = train_silver_model(df)

    # Backtest Thresholds
    thresholds = [0.52, 0.54, 0.56, 0.58]
    results = []

    for th in thresholds:
        res = backtest(df, th)
        results.append(res)

    # Ergebnisse anzeigen
    print("\n=== SILVER BACKTEST RESULTS ===")
    for r in results:
        print(
            f"TH={r['threshold']:.2f} | "
            f"Trades={r['n_trades']} | "
            f"Accuracy={r['accuracy'] if r['accuracy'] is not None else 0:.2%} | "
            f"Profit={r['profit'] if r['profit'] is not None else 0}"
        )

    # Ergebnisse speichern
    out = pd.DataFrame(results)
    out.to_csv("silver_backtest_results.csv", index=False)
    print("\n[OK] silver_backtest_results.csv written")

# =======================
# RUN
# =======================
if __name__ == "__main__":
    main()

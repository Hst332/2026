#!/usr/bin/env python3
"""
CODE A – SILVER FORECAST
COMEX Silver (SI=F)

ML-based, conservative, tradable
"""

# =======================
# IMPORTS
# =======================
import numpy as np
import pandas as pd
from datetime import datetime
import yfinance as yf

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score

# =======================
# CONFIG
# =======================
START_DATE = "2013-01-01"

SILVER_SYMBOL = "SI=F"
GOLD_SYMBOL = "GC=F"

UP_THRESHOLD = 0.56
DOWN_THRESHOLD = 0.44

# =======================
# DATA
# =======================
def load_prices():
    silver = yf.download(
        SILVER_SYMBOL,
        start=START_DATE,
        auto_adjust=True,
        progress=False,
    )

    gold = yf.download(
        GOLD_SYMBOL,
        start=START_DATE,
        auto_adjust=True,
        progress=False,
    )

    df = pd.DataFrame(index=silver.index)
    df["Silver"] = silver["Close"]
    df["Gold"] = gold["Close"]
    df.dropna(inplace=True)

    return df

# =======================
# FEATURES
# =======================
def build_features(df):
    df = df.copy()

    df["ret"] = df["Silver"].pct_change()
    df["trend_5"] = df["Silver"].pct_change(5)
    df["trend_20"] = df["Silver"].pct_change(20)
    df["vol_10"] = df["ret"].rolling(10).std()

    df["gold_ratio"] = df["Silver"] / df["Gold"]
    df["gold_ratio_trend"] = df["gold_ratio"].pct_change(10)

    df["Target"] = (df["ret"].shift(-1) > 0).astype(int)

    df.dropna(inplace=True)
    return df

# =======================
# MODEL
# =======================
def train_model(df):
    features = [
        "trend_5",
        "trend_20",
        "vol_10",
        "gold_ratio_trend",
    ]

    X = df[features]
    y = df["Target"]

    tscv = TimeSeriesSplit(n_splits=5)
    acc = []

    for tr, te in tscv.split(X):
        m = LogisticRegression(
            max_iter=200,
            class_weight="balanced"
        )
        m.fit(X.iloc[tr], y.iloc[tr])
        acc.append(
            accuracy_score(y.iloc[te], m.predict(X.iloc[te]))
        )

    model = LogisticRegression(
        max_iter=200,
        class_weight="balanced"
    )
    model.fit(X, y)

    return model, features, float(np.mean(acc)), float(np.std(acc))

# =======================
# RUN
# =======================
def forecast_silver():
    prices = load_prices()
    df = build_features(prices)

    model, features, cv_mean, cv_std = train_model(df)

    last = df.iloc[-1:]
    prob_up = model.predict_proba(last[features])[0][1]

    signal = (
        "UP" if prob_up >= UP_THRESHOLD
        else "DOWN" if prob_up <= DOWN_THRESHOLD
        else "NO_TRADE"
    )

    return {
        "market": "SILVER",
        "date": last.index[0].date().isoformat(),
        "close": float(prices.iloc[-1]["Silver"]),
        "prob_up": prob_up,
        "prob_down": 1.0 - prob_up,
        "signal": signal,
        "cv_mean": cv_mean,
        "cv_std": cv_std,
    }

import yfinance as yf
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def load_gold():
    df = yf.download("GC=F", start="2010-01-01", progress=False)
    df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()

    df["ret_1"] = df["Close"].pct_change()
    df["ret_5"] = df["Close"].pct_change(5)
    df["ma_10"] = df["Close"].rolling(10).mean()
    df["ma_50"] = df["Close"].rolling(50).mean()
    df["ma_ratio"] = df["ma_10"] / df["ma_50"] - 1
    df["vol_10"] = df["ret_1"].rolling(10).std()

    df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    df = df.dropna()

    # ===== MODEL =====
    features = ["ret_1", "ret_5", "ma_ratio", "vol_10"]
    X = df[features].values
    y = df["Target"].values

    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)

    model = LogisticRegression(
        max_iter=200,
        class_weight="balanced",
        solver="lbfgs"
    )
    model.fit(Xs, y)

    df["prob_up"] = model.predict_proba(Xs)[:, 1]

    return df

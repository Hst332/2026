import numpy as np

def model_score(df):
    returns = df["Close"].pct_change().dropna()
    mu = returns.tail(20).mean()
    score = 0.5 + np.tanh(mu * 15) / 2
    return float(df["prob_up"].iloc[-1])

def forecast_trend(df, window):
    r = df["Close"].pct_change().dropna().tail(window).mean()
    if r > 0.002:
        return "UP"
    if r < -0.002:
        return "DOWN"
    return "="

def trade_signal(score):
    if score >= 0.55:
        return "LONG"
    if score <= 0.45:
        return "SHORT"
    return "NO_TRADE"

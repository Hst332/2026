import numpy as np




def _close(df, idx):
return df["Close"].iloc[idx].item()




def model_score(df, lookback=21):
last = _close(df, -1)
past = _close(df, -lookback)


r = (last / past) - 1.0


score = 0.5 + np.tanh(r * 6) * 0.5
return float(np.clip(score, 0.0, 1.0))




def forecast_trend(df, days):
last = _close(df, -1)
past = _close(df, -days)


r = (last / past) - 1.0


if r > 0.01:
return "++"
elif r > 0.002:
return "+"
elif r < -0.01:
return "--"
elif r < -0.002:
return "-"
return "="




def trade_signal(score, long=0.55, short=0.45):
if score >= long:
return "LONG"
if score <= short:
return "SHORT"
return "NO_TRADE"

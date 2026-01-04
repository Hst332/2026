# --------- SILVER ---------
import pandas as pd
from datetime import datetime
import metals_bundle  # Funktion zum Laden der Silber-Daten

# Lade Silber-Daten
df = metals_bundle.load_silver()  # df muss 'Close' und 'prob_up' enthalten

# Letzter verfügbarer Tag
last_row = df.iloc[-1]
last_date = last_row.name.strftime("%Y-%m-%d")
close_price = last_row["Close"]
prob_up = last_row["prob_up"]

# Handelsstrategie Regeln
if prob_up >= 0.96:
    signal = "LONG"
    position_size = "100 % Positionsgröße"
elif prob_up >= 0.90:
    signal = "LONG (partial)"
    position_size = "50 % Positionsgröße"
else:
    signal = "NO_TRADE"
    position_size = "0 %"

# Ausgabe-Text zusammenstellen
output_text = (
    "--------- SILVER ---------\n"
    f"Data date : {last_date}\n"
    f"Close     : {close_price}\n"
    f"Prob UP   : {prob_up:.2f}%\n"
    "Handelsstrategie:\n"
    "prob_up ≥ 0.96 → LONG 100 % Positionsgröße\n"
    "0.90 ≤ prob_up < 0.96 → LONG 50 % Positionsgröße\n"
    "Alles darunter → kein Trade\n"
    "Kein Short, Max. Hebel 15, Stop-Loss -20 %\n"
    f"Signal    : {signal}\n"
    f"Positionsgröße : {position_size}\n"
)

# Ausgabe in Konsole
print(output_text)

# **In forecast_output.txt schreiben**
with open("forecast_output.txt", "a") as f:
    f.write(output_text + "\n")

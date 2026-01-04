# --------- SILVER ---------
import pandas as pd
from datetime import datetime
import metals_bundle  # Deine vorhandene Funktion zum Laden der Silber-Daten

# Lade Silber-Daten (funktioniert wie bisher)
df = metals_bundle.load_silver()  # df enthält 'Close' und 'prob_up'

# Letzter verfügbarer Tag
last_row = df.iloc[-1]
last_date = last_row.name.strftime("%Y-%m-%d")
close_price = last_row["Close"]
prob_up = last_row["prob_up"]

# Handelsstrategie Regeln (so wie du final definiert hast)
if prob_up >= 0.96:
    signal = "LONG"
    position_size = "100 % Positionsgröße"
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
    "Alles darunter → kein Trade\n"
    "Kein Short, Max. Hebel 15, Stop-Loss -20 %\n"
    f"Signal    : {signal}\n"
    f"Positionsgröße : {position_size}\n"
)

# Ausgabe in Konsole
print(output_text)

# In forecast_output.txt schreiben (anhängen)
with open("forecast_output.txt", "a") as f:
    f.write(output_text + "\n")

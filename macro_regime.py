def detect_macro_regime(gas, copper, gold):
    if gas["bull"] > 40 and copper["bull"] > 40:
        return "Reflation"
    if gas["bull"] > 40 and copper["bull"] < 30:
        return "Stagflation"
    if gas["bull"] < 30 and copper["bull"] < 30:
        return "Recession"
    if gold["bull"] > 40:
        return "Risk-Off"
    return "Transition"

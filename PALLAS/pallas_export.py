
import pandas as pd

def export_pallas_log(data, filename="PALLAS_Log.csv"):
    """
    Expects `data` as a list of dictionaries with keys:
    'Scene', 'Player Input', 'Ψ', 'SD', 'EW', 'RC', 'TC', 'CI'
    Calculates TMSᴩ and writes to a CSV file.
    """
    df = pd.DataFrame(data)
    df["TMSᴩ"] = (
        df["Ψ"] * 0.30 +
        df["SD"] * 0.15 +
        df["EW"] * 0.20 +
        df["RC"] * 0.15 +
        df["TC"] * 0.10 +
        df["CI"] * 0.10
    ).round(4)
    df.to_csv(filename, index=False)
    return filename

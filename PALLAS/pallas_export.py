import pandas as pd

def export_pallas_log(data, filename="PALLAS_Log.csv"):
    """
    Expects `data` as a list of dictionaries with keys:
    'Scene', 'Player Input', 'Ψ', 'SD', 'EW', 'RC', 'TC', 'CI',
    Optional Threadwalker fields:
    'Threadwalker Activated' (Yes/No)
    'Villager Pattern Assigned' (string)
    
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

    # Ensure optional Threadwalker fields exist
    if "Threadwalker Activated" not in df.columns:
        df["Threadwalker Activated"] = "No"
    if "Villager Pattern Assigned" not in df.columns:
        df["Villager Pattern Assigned"] = ""

    df.to_csv(filename, index=False)
    return filename

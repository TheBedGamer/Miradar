## Create a table containing PVP-related informations

# Library

import pandas as pd

# Function

def TrimData(ranking):
    raw = pd.read_csv(ranking)
    meta = raw[raw["Score"] >= 85]
    data = meta[["Pokemon", "Score", "Fast Move", "Charged Move 1", "Charged Move 2"]]
    data = data.reset_index(drop=True)
    data.insert(0, 'Rank', range(1, len(data) + 1))
    return data

labels = ["Great", "Ultra", "Master", "GreatMega", "UltraMega", "MasterMega"]

rankings = [TrimData("PvPoke/cp1500_all_overall_rankings.csv"), 
               TrimData("PvPoke/cp2500_all_overall_rankings.csv"), 
               TrimData("PvPoke/cp10000_all_overall_rankings.csv"), 
               TrimData("PvPoke/cp1500_mega_overall_rankings.csv"), 
               TrimData("PvPoke/cp2500_mega_overall_rankings.csv"), 
               TrimData("PvPoke/cp10000_mega_overall_rankings.csv")]

# Label the corresponding League

merged = pd.concat(
    [df.assign(League=label) for df, label in zip(rankings, labels)],
    ignore_index=True
)

league = merged.pop('League')
merged.insert(0, 'League', league)

# Export as .CSV

merged.to_csv("PvPoke/global_ranking.csv", index=False)
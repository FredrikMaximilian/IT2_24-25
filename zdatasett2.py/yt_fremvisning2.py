import pandas as pd

filnavn = "zytstats.csv"
df = pd.read_csv(filnavn, sep=",", encoding="utf-8", skiprows = 0)
land = df["Country"].value_counts().head(10)

"""
#Skriv ut 10 land med flest kanaler
print(land.to_string()) #Fjerner name og dtype
for land, telling in land.items():
    print(f'{land}: {telling}')
"""

for lander in land.keys():
    landinfo = df[df["Country"] == lander]
    df["subscribers"] = pd.to_numeric(df["subscribers"], errors="coerce")
    df["video views"] = pd.to_numeric(df["video views"], errors="coerce")
    abonnementer = landinfo["subscribers"].mean()
    visninger = landinfo["video views"].mean()
    print(f'{lander}: Abonnementer: {abonnementer:.0f}, visninger: {visninger:.0f}')
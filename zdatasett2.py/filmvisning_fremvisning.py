import pandas as pd

filnavn = "zfilmvisning.csv"
df = pd.read_csv(filnavn, sep=",", encoding="utf-8", skiprows = 0)

sjangre = df["Sjanger"].unique()
df["Besøkstall"] = pd.to_numeric(df["Besøkstall"], errors="coerce")

for sjang in sjangre:
    filminfo = df[df["Sjanger"] == sjang]
    besøkstall = filminfo["Besøkstall"].mean() #fucked
    print(f'{sjang}: Besøk: {round(besøkstall):,}')


land_telling = df["Land"].value_counts()
mest_land = land_telling.idxmax()
antall = land_telling.max()
print(f"Toppfilm oftest fra: {mest_land} ({antall} ganger)")


land_telling = df["Land"].value_counts()
mest_land = land_telling.index[0]  # Første land = flest forekomster
antall = land_telling.iloc[0]      # Antall ganger det forekommer
print(f"Toppfilm oftest fra: {mest_land} ({antall} ganger)")


from collections import Counter
landliste = df["Land"].dropna().tolist()
telling = Counter(landliste)
mest_land, antall = telling.most_common(1)[0]
print(f"Toppfilm oftest fra: {mest_land} ({antall} ganger)")

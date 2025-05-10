import pandas as pd

#Forenklet
'''
# Filnavn
filnavn = "Datasett_fodselstall.csv"

df = pd.read_csv(filnavn, sep="\t", encoding="latin1")
#df = pd.read_csv(filnavn, sep= None, engine="python", encoding="latin1")

# Gi enklere og mer praktiske kolonnenavn
df.columns = ["År", "Fødselstall", "Innflyttinger", "Utflyttinger"]

# Erstatt ".." med NaN og konverter alle relevante kolonner til tall
kolonner = ["År", "Fødselstall", "Innflyttinger", "Utflyttinger"]
df[kolonner] = df[kolonner].apply(pd.to_numeric, errors="coerce")

# Fjern rader der noen av kolonnene mangler tall
df = df.dropna(subset=kolonner)

# Konverter år tilbake til heltall hvis ønskelig
df["År"] = df["År"].astype(int)

#Legger til nettovekst
df["Netto folkevekst"] = df["Fødselstall"] + df["Innflyttinger"] - df["Utflyttinger"]

# Velg ønskede kolonner
#utvalg = df[["År", "Fødselstall", "Innflyttinger", "Utflyttinger"]]
utvalg = df[["År", "Fødselstall", "Innflyttinger", "Utflyttinger", "Netto folkevekst"]]

# Skriv ut siste 20 år i en enkel tabell
print("\nTABELL: Fødsler, innflyttinger og utflyttinger de siste 20 årene\n")
print(utvalg.tail(20).to_string(index=False))
'''

import pandas as pd

# Filnavn
filnavn = "zDatasett_fodselstall.csv"

# Les inn CSV-filen med riktig separator og koding
df = pd.read_csv(filnavn, sep="\t", encoding="latin1")

# Gi enkle kolonnenavn
df.columns = ["År", "Fødselstall", "Innflyttinger", "Utflyttinger"]

# Rens data: konverter til tall og håndter ".."
kolonner = ["År", "Fødselstall", "Innflyttinger", "Utflyttinger"]
df[kolonner] = df[kolonner].apply(pd.to_numeric, errors="coerce") #Gjør til tall, coerce gjør til NoN om ønskelig
df = df.dropna(subset=kolonner)
df["År"] = df["År"].astype(int)

# Beregn netto folkevekst
df["Netto folkevekst"] = df["Fødselstall"] + df["Innflyttinger"] - df["Utflyttinger"]

# Vis siste 20 rader i tabell
print("\nTABELL: Fødsler, innflyttinger, utflyttinger og netto folkevekst de siste 20 årene\n")
print(df.tail(20).to_string(index=False))

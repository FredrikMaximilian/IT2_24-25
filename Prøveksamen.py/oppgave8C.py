import numpy as np  # Importerer numpy for numeriske operasjoner
import matplotlib.pyplot as plt  # Importerer matplotlib for plotting

import pandas as pd
import matplotlib.pyplot as plt


filnavn = "innvandring_eksamen.csv"

df = pd.read_csv(filnavn, sep=";", encoding="utf-8", skiprows=1)

# Gi riktige kolonnenavn
df.columns = ["Landbakgrunn", "År", "Innvandrere og norskfødte med innvandrerforeldre"]

# Rens opp i spesialtegn og fjern ledende "ø" kun hvis den står først
df["Landbakgrunn"] = (
    df["Landbakgrunn"].str.replace("�", "ø"))

#print(alle_år)
totalår = df["År"].unique()
totalland = df["Landbakgrunn"].unique()

landinput = input(str("Skriv inn land: (A = Afrika, B = Asia, C = Nord-Am, D = Sør-Am, E = Euro, O = Osea) ")).capitalize().strip()
if landinput == "A":
    landinput = "Afrika"
elif landinput == "B":
    landinput = "Asia utenom Tyrkia"
elif landinput == "C":
    landinput = "Nord-, Sentral-Amerika og Karibia"
elif landinput == "D":
    landinput = "Sør-Amerika"
elif landinput == "E":
    landinput = "Europa og Tyrkia"
elif landinput == "O":
    landinput = "Oseania"
else:
    print("Skriv inn på nytt")


if landinput in totalland:
    infoliste = df[df["Landbakgrunn"] == landinput]["Innvandrere og norskfødte med innvandrerforeldre"].tolist()
else:
    print("Skriv på nytt")


plt.plot(totalår, infoliste)  # Plotter data
plt.title(f'{landinput}')  # Setter tittel
plt.xlabel("År")  # Setter x-akse etikett
plt.ylabel("Innvandrere")  # Setter y-akse etikett
plt.grid()  # Viser rutenett
plt.show()  # Viser grafen
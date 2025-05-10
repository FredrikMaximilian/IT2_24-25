import pandas as pd
import matplotlib.pyplot as plt

filnavn = "innvandring_eksamen.csv"
df = pd.read_csv(filnavn, sep=";", encoding="utf-8", skiprows=1)
df.columns = ["Landbakgrunn", "År", "Innvandrer"]
df["Landbakgrunn"] = df["Landbakgrunn"].str.replace("�", "ø")


årover20 = df[df["År"] >= 2020]
årover20 = årover20.sort_values(by = "År")
årkun25 = df[df["År"] == 2025].sort_values(by = "Innvandrer")

landliste = []
innvandrerliste = []

for land in årkun25["Landbakgrunn"]:
    landliste.append(land)
for verdi in årkun25["Innvandrer"]:
    innvandrerliste.append(verdi)

plt.barh(landliste, innvandrerliste)
plt.show()
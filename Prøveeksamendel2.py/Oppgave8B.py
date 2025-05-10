import pandas as pd
import matplotlib.pyplot as plt

filnavn = "innvandring_eksamen.csv"
df = pd.read_csv(filnavn, sep=";", encoding="utf-8", skiprows=1)
df.columns = ["Landbakgrunn", "År", "Innvandrer"]
df["Landbakgrunn"] = df["Landbakgrunn"].str.replace("�", "ø")


årover20 = df[df["År"] >= 2020]
#årover20 = årover20.sort_values(by = "År")

'''
årover20 = årover20.sort_values(by=["Landbakgrunn", "År"])
årover20["Endring"] = årover20.groupby("Landbakgrunn")["Innvandrer"].diff()
print(årover20)
'''

# Summerer antall innvandrere per år
total_per_år = årover20.groupby("År")["Innvandrer"].sum().reset_index()
# Legg til en kolonne for å vise endring fra året før
total_per_år["Endring"] = total_per_år["Innvandrer"].diff().fillna("0")
print(total_per_år)
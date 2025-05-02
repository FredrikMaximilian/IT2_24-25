import pandas as pd
import matplotlib.pyplot as plt


filnavn = "innvandring_eksamen.csv"

df = pd.read_csv(filnavn, sep=";", encoding="utf-8", skiprows=1)

# Gi riktige kolonnenavn
df.columns = ["Landbakgrunn", "År", "Innvandrere og norskfødte med innvandrerforeldre"]

# Rens opp i spesialtegn og fjern ledende "ø" kun hvis den står først
df["Landbakgrunn"] = (
    df["Landbakgrunn"].str.replace("�", "ø"))

alle_år = (df["År"].unique())
for år in alle_år:
    årdf = df[df["År"] == år]
    land = årdf["Landbakgrunn"].to_string(index = False)
    info = årdf["Innvandrere og norskfødte med innvandrerforeldre"]
    print(f'År: {år}, Land: {land}, Info: {info}')
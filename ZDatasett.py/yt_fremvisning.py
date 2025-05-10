import pandas as pd
import matplotlib.pyplot as plt


filnavn = "yt_statistikk.csv"
df = pd.read_csv(filnavn, sep=",", encoding="utf-8", skiprows=0)

#Print alle landene
#print(df["Country"].unique())

land_flestkanaler = df["Country"].value_counts().head(10)

"""
print("Gjennomsnittlig data for 10 landene med størst kanaler")
for land in land_flestkanaler.index:
    abonnementer = df[df["Country"] == land]["subscribers"].mean()
    videovisninger = df[df["Country"] == land]["video views"].mean()
    print(f'{land}: Visninger: {videovisninger:.0f}, Abonnementer: {abonnementer}')
"""

#Hvilket land har mest sette yt kanalen
visningsliste = df.sort_values("video views", ascending=False)
print(visningsliste["Youtuber"].iloc[0])

#Hvor mange unike kategorier finnes i datasettet
kategorier = df["category"].unique()
print(kategorier)

#Hvilke 5 kanaleer har flest abonnementer
abonnementliste = df.sort_values("subscribers", ascending=False)
#print(abonnementliste["Youtuber"].head(5))
for i in range(5):
    print(abonnementliste["Youtuber"].iloc[i])

#Finn gjennomsnittlig opplastninger per kanal
opplastninger = df["uploads"].mean()
print(opplastninger)

#Finn total/gjennomsnittlig videovisninger per amerikanske kanal
usa_df = df[df["Country"] == "United States"]
videovisningerUSA = usa_df["video views"]
total = videovisningerUSA.sum()
gjennomsnitt = videovisningerUSA.mean()
print(f'Total: {total:.0f}, Gjennomsnitt: {gjennomsnitt:.0f}')

#Landet med flest abonnementer
landabonnementliste = (df.groupby("Country")["subscribers"].sum().sort_values(ascending=False))
print(f'{landabonnementliste.index[0]} med {landabonnementliste[0]} abonnementer') #idxmax kan også brukes

#Finn kanal med mest inntekt
maks_rad = df[df["highest_monthly_earnings"] == df["highest_monthly_earnings"].max()]
navn = maks_rad["Youtuber"].values[0]
inntekt = maks_rad["highest_monthly_earnings"].values[0]
print(f"{navn} tjener mest per måned: ${inntekt:,.0f}")

#Tabell for alle land
alle_land = (df["Country"].unique())
for land in alle_land:
    antall_kanaler = len(df[df["Country"] == land])
    totalabonnement = df[df["Country"] == land]["subscribers"].sum()
    gjennomsnittabonnementer = df[df["Country"] == land]["subscribers"].mean()
    totalvisninger = df[df["Country"] == land]["video views"].sum()
    print(f'{land}= Kanaler:{antall_kanaler}, Abonnementer: {totalabonnement}, gjennomsnitt: {gjennomsnittabonnementer:.0f}, visninger: {totalvisninger:.0f}')

#print(df["Country"].value_counts()) #Printer land med antall ganger nevnt(kanaler)

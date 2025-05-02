import pandas as pd
import matplotlib.pyplot as plt


filnavn = "innvandring_eksamen.csv"

df = pd.read_csv(filnavn, sep=";", encoding="utf-8", skiprows=1)

# Gi riktige kolonnenavn
df.columns = ["Landbakgrunn", "År", "Innvandrere og norskfødte med innvandrerforeldre"]

# Rens opp i spesialtegn og fjern ledende "ø" kun hvis den står først
df["Landbakgrunn"] = (
    df["Landbakgrunn"].str.replace("�", "ø"))


underlik25= df[df["År"] <= 2025] #Alle år under/med 2025, trengte denne egentlig ikke, men greit å ha om man vil bytte til tidligere år senere
underlik20202025 = underlik25[underlik25["År"] >= 2020] #Filtrerer ut alt som ikke er over/lik 2020
#underlik20202025["Endring"] = underlik20202025["År"] noe her
underlik20202025 = underlik20202025.sort_values(by= "År") #Sorterer etter år
print(f'Tabell: {underlik20202025}')


#Deloppgave 2
år2025 = df[df["År"] == 2025].sort_values(by="Innvandrere og norskfødte med innvandrerforeldre", ascending= False) #Lager sortert liste med år

landliste2025 = []
infoliste2025 = []
#Legger til land/info i respektive lister
for land in år2025["Landbakgrunn"]:
    landliste2025.append(land) 
for info in år2025["Innvandrere og norskfødte med innvandrerforeldre"]:
    infoliste2025.append(info)

#Skriver ut
plt.figure(figsize=(12, 6))
plt.barh(landliste2025, infoliste2025)
plt.tight_layout()
plt.grid(axis = "x")
plt.show()



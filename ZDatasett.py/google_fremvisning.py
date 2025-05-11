import pandas as pd  # Importerer pandas-biblioteket for databehandling

# Last inn data
df = pd.read_csv("zgoogleplaystore.csv")  # Leser inn data fra CSV-filen "googleplaystore.csv" til en DataFrame

# Fjern rader med manglende verdier i nødvendige kolonner
df = df.dropna(subset=["Category", "Rating", "Installs"])  # Fjerner rader der "Category", "Rating" eller "Installs" har manglende verdier

# Behold bare rader hvor "Installs" faktisk er tall-lignende
df = df[df["Installs"].str.contains(r'^\d+[,\d]*\+$', regex=True)]  # Filtrerer rader der "Installs" matcher et tallformat som slutter med "+"

# Gjør om "Installs" til tall: fjern "+" og "," før konvertering
df["Installs"] = df["Installs"].str.replace("+", "", regex=False).str.replace(",", "").astype(int)  
# Fjerner "+" og "," fra "Installs"-kolonnen og konverterer verdiene til heltall

# De tre største kategoriene
topp_kategorier = df["Category"].value_counts().head(3).index.tolist()  
# Teller antall apper i hver kategori, henter de tre største kategoriene, og lagrer dem som en liste

# Filtrer til kun de tre største kategoriene
df_topp = df[df["Category"].isin(topp_kategorier)]  
# Filtrerer DataFrame til kun rader der "Category" er en av de tre største kategoriene

# Lag oversikten
oversikt = df_topp.groupby("Category").agg({  
    "App": "count",  # Teller antall apper i hver kategori
    "Rating": "mean",  # Beregner gjennomsnittlig rating for hver kategori
    "Installs": "mean"  # Beregner gjennomsnittlig antall installs for hver kategori
}).rename(columns={  
    "App": "Antall Apper",  # Gir nytt navn til kolonnen "App"
    "Rating": "Gjennomsnittlig Rating",  # Gir nytt navn til kolonnen "Rating"
    "Installs": "Gjennomsnittlige Installs"  # Gir nytt navn til kolonnen "Installs"
}).sort_values("Antall Apper", ascending=False)  
# Sorterer resultatet etter "Antall Apper" i synkende rekkefølge

print(oversikt)  # Skriver ut oversikten

for kategori in topp_kategorier:
    print(f'Kategori: {kategori}')
    #mest_populære = df[df["Category"] == kategori].sort_values("Installs", ascending = False).head(3) #Gir duplikater
    mest_populære = df[df["Category"] == kategori].drop_duplicates(subset = "App").sort_values("Installs", ascending = False).head(3)
    print(mest_populære[["App", "Installs", "Rating"]].to_string(index=False))
import pandas as pd  # Importerer pandas-biblioteket for databehandling

#1. Hva er gjennomsnittlig vurdering (rating) for apper i kategorien ART_AND_DESIGN?
#2. Hvor mange apper har over 1 million installs?
#3. Hva er navnet på appen med høyest rating i kategorien AUTO_AND_VEHICLES?
#4. Hvor mange apper er gratis?
#5. Hvilken app i kategorien ART_AND_DESIGN har flest anmeldelser (reviews)?
#6. Finn navnet på en app med nøyaktig 5.0 som Android minimumsversjon.
#7. Hvilken app er sist oppdatert (basert på "Last Updated")?
#8. Hvor mange apper har vurdering lavere enn 3.5?
#9. Hvilken app har minste størrelse (Size)?
#10. Hvor mange apper har "Teen" som Content Rating?

filnavn = "zgoogleplaystore.csv"
df = pd.read_csv(filnavn)

#1
artdesignkategori = df[df["Category"] == "ART_AND_DESIGN"]
avrgratingartdesign = artdesignkategori["Rating"].mean() #Kan bruke dropna() før mean mtp feil verdier
#print(artdesignkategori)
print(avrgratingartdesign)

#2
nedlastningerdf = df[df["Installs"].str.contains(r'^\d+[,\d]*\+$', regex=True)]
#nedlastningerdf["Installs"] = nedlastningerdf["Installs"].str.replace("+", "", regex=False).str.replace(",", "").astype(int) 
nedlastningerdf.loc[:, "Installs"] = nedlastningerdf["Installs"].str.replace("+", "", regex=False).str.replace(",", "").astype(int)

over_en_milly = nedlastningerdf[nedlastningerdf["Installs"] > 1_000_000]
antall = over_en_milly.shape[0] #shape gir tuppel av rader og kolonner. 
#print(over_en_milly.columns) Kan brukes til å se alle kolonnene
print(antall)

#3
autovehicles_kategori = df[df["Category"] == "AUTO_AND_VEHICLES"]
topp_rating_autovehicle = autovehicles_kategori.dropna(subset=["Rating"]).sort_values(by = "Rating", ascending=False).head(3)
print(topp_rating_autovehicle[["App", "Rating"]].to_string(index=False))


#4
gratiskategori = df[df["Price"] == "0"]
antall_gratis = gratiskategori.shape[0]
print(f'Antall gratis: {antall_gratis}')
#print(df["Price"].unique())

#5
# Funksjon for å konvertere tekst til tall
def konverter_reviews(verdi):
    verdi = str(verdi).replace(",", "").strip()
    if 'M' in verdi:
        return int(float(verdi.replace('M', '')) * 1_000_000)
    elif 'K' in verdi:
        return int(float(verdi.replace('K', '')) * 1_000)
    try:
        return int(verdi)
    except ValueError:
        return None  # Hvis det er noe annet tull
# Bruk funksjonen på Reviews-kolonnen
df["Reviews"] = df["Reviews"].apply(konverter_reviews)
# Filtrer for ART_AND_DESIGN
artdesignkategori = df[df["Category"] == "ART_AND_DESIGN"]
# Sorter etter antall reviews og vis topp 5
antallrating_artdesign = artdesignkategori.dropna(subset=["Reviews"]).sort_values(by="Reviews", ascending=False).head(5)
print(antallrating_artdesign[["App", "Reviews", "Rating"]].to_string(index=False))

#6
android5apps = df[df["Android Ver"] == "5.0 and up"]
print(android5apps["App"].head(5).to_string(index = False))

#7
# Sørg for at 'Last Updated' er i riktig datoformat
df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors="coerce")
# Finn raden med nyeste oppdateringsdato
sist_oppdatert_app = df.sort_values(by="Last Updated", ascending=False).iloc[0]
# Skriv ut app-navnet og datoen
print(f"Sist oppdatert app: {sist_oppdatert_app['App']}")
print(f"Oppdatert: {sist_oppdatert_app['Last Updated'].date()}")

#8
# Filtrer apper med rating lavere enn 3.5
lav_rating = df[df["Rating"] < 3.5]
# Tell hvor mange det er
antall_lav_rating = lav_rating.shape[0]
# Skriv ut svaret
print(f"Antall apper med vurdering lavere enn 3.5: {antall_lav_rating}")

#9
def konverter_size(size):
    size = str(size).strip()
    if 'M' in size:
        return float(size.replace('M', '')) * 1_000_000
    elif 'k' in size or 'K' in size:
        return float(size.replace('k', '').replace('K', '')) * 1_000
    elif size.lower() == 'varies with device':
        return None
    try:
        return float(size)
    except:
        return None

# Konverter kolonnen
df["Size_clean"] = df["Size"].apply(konverter_size)
# Finn raden med minste app-størrelse (ignorer nullverdier)
minste_app = df.dropna(subset=["Size_clean"]).sort_values(by="Size_clean", ascending=True).iloc[0]
# Skriv ut info
print(f"Minste app er: {minste_app['App']}")
print(f"Størrelse: {minste_app['Size']} ({minste_app['Size_clean']} bytes)")


#10
apper_teen = df[df["Content Rating"] == "Teen"].shape[0]
print(df[df["Content Rating"] == "Teen"][["App", "Rating", "Category"]].head(10).to_string(index=False))
print(apper_teen)

kategoriliste = (df["Category"].unique())
print(kategoriliste)
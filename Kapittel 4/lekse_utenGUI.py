import numpy as np  # Importerer numpy for numeriske operasjoner
import matplotlib.pyplot as plt  # Importerer matplotlib for plotting

filnavn = "leksedatasett.csv"  # Navnet på CSV-filen som inneholder data
årliste = []  # Liste for å lagre årstall
levendefødteliste = []  # Liste for å lagre antall levendefødte
innflytterliste = []  # Liste for å lagre antall innflyttere
utflytterliste = []  # Liste for å lagre antall utflyttere
nettoliste = []  # Liste for å lagre nettoverdier

with open(filnavn, encoding="utf-8") as fil:  # Åpner filen med UTF-8-koding
    next(fil)  # Hopper over første linje (header)
    for linje in fil:  # Itererer gjennom hver linje i filen
        info = linje.strip().split(",")  # Fjerner mellomrom og splitter linjen på komma
        år = int(info[0].strip('"'))  # Konverterer første kolonne (år) til heltall
        årliste.append(år)  # Legger til år i årliste

        try:
            levendefødteliste.append(int(info[1]))  # Forsøker å konvertere levendefødte til heltall
        except:
            levendefødteliste.append(np.nan)  # Hvis feil, legger til NaN (ikke et tall)
        
        try:
            innflytterliste.append(int(info[2]))  # Forsøker å konvertere innflyttere til heltall
        except:
            innflytterliste.append(np.nan)  # Hvis feil, legger til NaN
        
        try:
            utflytterliste.append(int(info[3]))  # Forsøker å konvertere utflyttere til heltall
        except:
            utflytterliste.append(np.nan)  # Hvis feil, legger til NaN

# Beregner nettoverdier basert på dataene
for i in range(len(årliste)):
    inn = innflytterliste[i]  # Henter antall innflyttere for året
    ut = utflytterliste[i]  # Henter antall utflyttere for året
    lefø = levendefødteliste[i]  # Henter antall levendefødte for året
    if not np.isnan(inn) and not np.isnan(ut) and not np.isnan(lefø):  # Sjekker om verdiene er gyldige
        netto = lefø + inn - ut  # Beregner nettoverdi
    else:
        netto = np.nan  # Setter nettoverdi til NaN hvis noen verdier mangler
    nettoliste.append(netto)  # Legger til nettoverdi i listen

# Henter brukerinput for første år
try:
    fra_år = int(input("Skriv inn første år (1945 ->): "))  # Leser inn første år
    if fra_år not in årliste:  # Sjekker om året finnes i datasettet
        raise ValueError("År ikke i datasett")  # Kaster feil hvis året ikke finnes
except ValueError as e:
    print(f'Ugyldig input: {e}')  # Skriver ut feilmelding
    exit()  # Avslutter programmet

# Henter brukerinput for siste år
try:
    til_år = int(input("Skriv inn første år (1945 ->): "))  # Leser inn siste år
    if til_år not in årliste:  # Sjekker om året finnes i datasettet
        raise ValueError("År ikke i datasett")  # Kaster feil hvis året ikke finnes
except ValueError as e:
    print(f'Ugyldig input: {e}')  # Skriver ut feilmelding
    exit()  # Avslutter programmet

# Sjekker om første år er lavere enn siste år
if fra_år > til_år:
    print("Første år må være lavere enn siste")  # Skriver ut feilmelding
    exit()  # Avslutter programmet

# Henter brukerinput for kategori
kategori = input("Hvilken kategori? (fødte, inn, ut, netto): ").lower()  # Leser inn kategori
gyldige_kategorier = ["fødte", "inn", "ut", "netto"]  # Definerer gyldige kategorier
if kategori not in gyldige_kategorier:  # Sjekker om kategorien er gyldig
    print("Ugyldig kategori")  # Skriver ut feilmelding
    exit()  # Avslutter programmet

# Finner start- og sluttindeks for årene
start_i = årliste.index(fra_år)  # Finner startindeks
slutt_i = årliste.index(til_år) + 1  # Finner sluttindeks

x_år = årliste[start_i: slutt_i]  # Henter utvalgte år

# Henter data basert på valgt kategori
if kategori == "fødte":
    yinfo = levendefødteliste[start_i: slutt_i]  # Henter data for levendefødte
    ynavn = "Levendefødte"  # Setter navn for grafen
elif kategori == "inn":
    yinfo = innflytterliste[start_i: slutt_i]  # Henter data for innflyttere
    ynavn = "Innflyttere"  # Setter navn for grafen
elif kategori == "ut":
    yinfo = utflytterliste[start_i: slutt_i]  # Henter data for utflyttere
    ynavn = "Utflyttere"  # Setter navn for grafen
elif kategori == "netto":
    yinfo = nettoliste[start_i: slutt_i]  # Henter data for nettoverdi
    ynavn = "Nettovekst"  # Setter navn for grafen
else:
    print("Ugyldig input")  # Skriver ut feilmelding
    yinfo = None  # Setter data til None

# Plotter grafen hvis data er tilgjengelig
if yinfo:
    plt.plot(x_år, yinfo)  # Plotter data
    plt.title(f'{ynavn} fra {fra_år} til {til_år}')  # Setter tittel
    plt.xlabel("År")  # Setter x-akse etikett
    plt.ylabel(kategori)  # Setter y-akse etikett
    plt.grid()  # Viser rutenett
    plt.show()  # Viser grafen
'''
#Oppgave 1, Skriv navn
Fredrik = {"Navn": "Fredrik", "Etternavn":"Lysnes-Steinbach", "Alder":"17"}
print(f'Navnet mitt er {Fredrik["Navn"]} {Fredrik["Etternavn"]} og jeg er {Fredrik["Alder"]} år gammel')
'''
'''
#Oppgave 2
Torsdag = {"Dato": "25.9", "Makstemp": "14", "Mintemp": "7"}
print(f'Dagens dato er {Torsdag["Dato"]}, makstemp og mintemp er henholdsvis {Torsdag["Makstemp"]} og {Torsdag["Mintemp"]} grader')
'''
'''
#Oppgave 4, kryptere tekst
krypter = {
    "a": "c", "b": "d", "c": "e", "d": "f", "e": "g", "f": "h", "g": "i",
    "h": "j", "i": "k", "j": "l", "k": "m", "l": "n", "m": "o", "n": "p",
    "o": "q", "p": "r", "q": "s", "r": "t", "s": "u", "t": "v", "u": "w",
    "v": "x", "w": "y", "x": "z", "y": "a", "z": "b", "ø": "a", "å": "b"
}

tekst = str(input("Skriv inn tekst: "))
tekst = tekst.lower()
krypterttekst = ""

for bokstav in tekst:  # Riktig måte å iterere gjennom hvert tegn
  #  if bokstav in krypter:
        krypterttekst += krypter[bokstav]
   # else:
    #    krypterttekst += bokstav  # Beholder tegn som ikke er i ordboka

print(krypterttekst)
'''
'''
land = {
    "Kina": 1_425_887_337,
    "India": 1_417_173_173,
    "USA": 331_893_745,
    "Indonesia": 276_361_783,
    "Pakistan": 240_485_658
}
sortert = sorted(land.keys())
for x in sortert:
    print(f'{x} har {land[x]} innbyggere')

flest = max(land, key=land.get)
færrest = min(land, key=land.get)
print(flest)
print(færrest)
'''
'''
#Oppgave 6, skriv ut vinnertid
sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]
print("For 200m:")
for i in sommer_ol:
    år = i["årstall"]
    seier200 = i["vinnertider"]["200 m"]
    print(f'I {år} var vinnertiden {seier200}')
print("\n For 400m:")
for i in sommer_ol:
    år = i["årstall"]
    seier400 = i["vinnertider"]["400 m"]
    print(f'I {år} var vinnertiden {seier400}')

print("\n")
vinnertider_2020 = next(i["vinnertider"] for i in sommer_ol if i["årstall"] == 2020)
print(f'Vinnertider i 2020: {vinnertider_2020}')
print(vinnertider_2020)
'''
'''
#Sluttoppgave 4. Lekse
# Lager en ordbok med informasjon om norske byer
norske_byer = {
    "Oslo": {
        "fylke": "Oslo",
        "innbyggertall": 693494,
        "grunnlagt": 1048
    },
    "Bergen": {
        "fylke": "Vestland",
        "innbyggertall": 286930,
        "grunnlagt": 1070
    },
    "Trondheim": {
        "fylke": "Trøndelag",
        "innbyggertall": 207595,
        "grunnlagt": 997
    },
    "Stavanger": {
        "fylke": "Rogaland",
        "innbyggertall": 144695,
        "grunnlagt": 1125
    }
}

for by, info in norske_byer.items(): #Går gjennom hvert bynavn (by) og tilhørende ordbok(info) i ordboken. 
    print(f"By: {by}") #Skrives ut byens navn
    for nøkkel, verdi in info.items(): #Vil gå gjennom alle byenes nøkkel-verdi-par
        print(f"{nøkkel.capitalize()}: {verdi}") #Printer ut nøkkelen med stor bokstav, oppfulgt av verdien
    print("-" * 30) #Printes for å gjøre mer oversiktlig
'''
'''
#Oppgave 1a
person = { "fornavn": "Fredrik", "etternavn": "Steinbach", "alder": "17år" }
for nøkkel, verdi in person.items():
    print(f'{nøkkel.capitalize()}: {verdi}')
#Oppgave 2a og b
onsdag = {"dato": "23.10.2024", "makstemp": "12 grader", "mintemp": "8 grader"}
for nøkkel, verdi in onsdag.items():
    print(f'{nøkkel.capitalize()}: {verdi}')
#Oppgave 3
ordbok = {"variabel": "Har som funksjon å ta vare på verdier i en kode",
          "datatype": "En form som en verdi kan ha, finnes integrer, string etc",
          "operator": "en element som kan gjøre noe med et annen element, gange/dele/plusse etc",
          "løkke": "En type kode som får den innskrevne biten til å gå i en løkke frem til den stoppes"}
for nøkkel, verdi in ordbok.items():
    print(f'{nøkkel.capitalize()}: {verdi}')
'''
'''
krypter = { "a": "c", "b": "d", "c": "e", "d": "f", "e": "g", "f": "h", "g": "i", "h": "j", "i": "k", "j": "l",
            "k": "m", "l": "n", "m": "o", "n": "p", "o": "q", "p": "r", "q": "s", "r": "t", "s": "u", "t": "v", 
            "u": "w", "v": "x", "w": "y", "x": "z", "y": "a", "z": "b" }

tekst = str(input("Skriv inn teksten du vil kryptere")).lower()

kryperttekst = ""
for bokstav in tekst:
    if bokstav in krypter:
        kryperttekst += krypter[bokstav]
    else: 
        kryperttekst += bokstav
print(kryperttekst)
'''
'''
land_innbyggere = {
    "Kina": 1400000000,   
    "India": 1390000000,  
    "USA": 333000000,     
    "Indonesia": 276000000, 
    "Pakistan": 240000000 }

flest_land = max(land_innbyggere, key=land_innbyggere.get)
flest_innbyggere = land_innbyggere[flest_land]
minst_land = min(land_innbyggere, key = land_innbyggere.get)
minst_innbyggere = land_innbyggere[minst_land]

for land in sorted(land_innbyggere.keys()):
    innbyggere = land_innbyggere[land]
    print(f'{land} har {innbyggere} innbyggere.')
print(f'{flest_land} har flest innbyggere med {flest_innbyggere}')
print(f'{minst_land} har flest innbyggere med {minst_innbyggere}')
'''
'''
sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]
liste200 = []
for ol in sommer_ol:
    aar = ol["årstall"]
    vinnertid200 = ol["vinnertider"]["200 m"]
    liste200.append(vinnertid200)
    print(f'I {aar} var vinnertidene for 200m {vinnertid200}')

print()

for ol in sommer_ol:
    aar = ol["årstall"]
    vinnertid400 = ol["vinnertider"]["400 m"]
    print(f'I {aar} var vinnertidene for 400m {vinnertid400}')
print()

vinnertider2020 = sommer_ol[4]["vinnertider"]
print("Resultatene under OL i 2020 var:")
for distanse, resultat in vinnertider2020.items():
    print(f'{distanse}: {resultat}')

minst = min(liste200)
maks = max(liste200)
print(f'Raskeste og tregeste resultatet for 200m var henholdsvis {maks} og {minst}.')
'''
'''
vinnerresultater = [
    {   "øvelse": "100 m", 
        "vinnertider": [
            { "årstall": 2004, "tid": 10.93 },
            { "årstall": 2008, "tid": 10.78 },
            { "årstall": 2012, "tid": 10.75 },
            { "årstall": 2016, "tid": 10.71 },
            { "årstall": 2020, "tid": 10.61 }
        ]  }, { 
        "øvelse": "200 m", 
        "vinnertider": [
            { "årstall": 2004, "tid": 22.06 },
            { "årstall": 2008, "tid": 21.74 },
            { "årstall": 2012, "tid": 21.88 },
            { "årstall": 2016, "tid": 21.78 },
            { "årstall": 2020, "tid": 21.53 }
        ]  },  { 
        "øvelse": "400 m", 
        "vinnertider": [
            { "årstall": 2004, "tid": 49.41 },
            { "årstall": 2008, "tid": 49.62 },
            { "årstall": 2012, "tid": 49.55 },
            { "årstall": 2016, "tid": 49.44 },
            { "årstall": 2020, "tid": 48.36 }
        ]  }]

for vinner in vinnerresultater:
    if vinner["øvelse"] == "400 m":
        print("Vinnertider for 400m er:")
        for tid in vinner["vinnertider"]:
            aar = tid["årstall"]
            vinnertid = tid["tid"]
            print(f'I {aar} var vinnertiden for 400 m: {vinnertid}')

vinnertider_2020 = []

# Itererer gjennom vinnerresultater
for vinner in vinnerresultater:
    for tid in vinner["vinnertider"]:
        if tid["årstall"] == 2020:  # Sjekker om årstallet er 2020
            vinnertider_2020.append({
                "øvelse": vinner["øvelse"],
                "tid": tid["tid"]  })
# Utskrift av vinnertider i 2020
print("Vinnertider i 2020:")
for resultat in vinnertider_2020:
    print(f'{resultat["øvelse"]}: {resultat["tid"]}')

liste200 = []
for vinner in vinnerresultater:
    if vinner["øvelse"] == "200 m":
        for tid in vinner["vinnertider"]:
            aar = tid["årstall"]
            vinnertid = tid["tid"]
            liste200.append(vinnertid)
maks = max(liste200)
minst = min(liste200)
print(f'Beste og dårligste 200m tiden var henholdsvis {minst} og {maks}.')
'''
#Sluttoppgave 2. Gjør tall om til teksttall
'''
tall_tekst = {
    1: "en",
    2: "to",
    3: "tre",
    4: "fire",
    5: "fem",
    6: "seks",
    7: "sju",
    8: "åtte",
    9: "ni",
    10: "ti"
}

for tall, tekst in tall_tekst.items():
    print(f'{tall}: {tekst.capitalize()}')

while True:
    bruker = input("Skriv inn et tall, eller 'exit' for å avslutte")
    if bruker.lower() == "exit":
        print("Du har avsluttet")
        break
    if bruker.isdigit():
        tall = int(bruker)
        if tall in tall_tekst:
            print(f'{tall} på norsk er: {tall_tekst[tall].title()}')
        else: 
            print("Du må skrive inn et tall mellom 1 og 10")
    else: 
        print("Du må skrive inn et tall")
'''
'''
#Oppgave 3. Skriv noe og tell bokstaver
tekst = str(input("Skriv noe: ")).lower()

bokstav_tekst = { 
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
    'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 
    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 
    'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'æ': 0, 'ø': 0, 
    'å': 0}

for bokstav in tekst:
    if bokstav in bokstav_tekst:
        bokstav_tekst[bokstav] += 1
for bokstav, antall in bokstav_tekst.items():
    if antall > 0: 
        print(f'{bokstav}: {antall}')
'''
'''
norske_byer = {
    "Oslo": {
        "fylke": "Oslo",
        "innbyggertall": 1_546_706,
        "areal_kv_km": 454,
        "etableringsår": 1048,
        "kjent_for": "Norges hovedstad, kultur og historie" },
    "Bergen": {
        "fylke": "Vestland",
        "innbyggertall": 283_929,
        "areal_kv_km": 465,
        "etableringsår": 1070,
        "kjent_for": "Bryggen, Fløyen, regn"  },
    "Stavanger": {
        "fylke": "Rogaland",
        "innbyggertall": 144_201,
        "areal_kv_km": 67.5,
        "etableringsår": 1125,
        "kjent_for": "Oljehovedstaden, Preikestolen"}}

for by, info in norske_byer.items():
    print(f'By: {by}')
    print(f' - Fylke: {info["fylke"]}')
    print(f' - Innbyggertall: {info["innbyggertall"]}')
    print(f' - Areal (km²): {info["areal_kv_km"]}')
    print(f' - Etableringsår: {info["etableringsår"]}')
    print(f' - Kjent for: {info["kjent_for"]}\n')
    '''

eliteserielag = [
  { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
  { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
  { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
  { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
  { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
  { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
  { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
  { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
  { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
  { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
  { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }
]
liste = []
for lag in eliteserielag:
    if lag["seriemesterskap"]:
        liste.append(lag)

print(liste)

#Oppgave 1
"""
person = {"fornavn": "Fredrik", "alder": 18, "søsken":4, "iste": "godt" }
person["søsken"] = 3
person["fødselsår"] = 2007
person.pop("iste")
print(person)
""""""
#Oppgave4
alfabet = "abcdefghijklmnopqrstuvwxyzæøå"
krypter = {}
for i, bokstav in enumerate(alfabet):
    krypter[bokstav] = alfabet[(i+2) % len(alfabet)]
#print(krypter)
tekst = "Hei, jeg heter Fredrik"
tekst = tekst.lower()
nytekst = ""
for j in tekst:
    if j in krypter:
        nytekst += krypter[j]
    else:
        nytekst += j
print(nytekst)
dekrypter = {}
gammeltekst = ""
for i, bokstav in enumerate(alfabet):
    dekrypter[bokstav] = alfabet[(i-2) % len(alfabet)]
for p in nytekst:
    if p in dekrypter:
        gammeltekst += dekrypter[p]
    else:
        gammeltekst += p
print(gammeltekst)
"""
#Oppgave 5
"""
innbyggere = {
    "India": 1430000000,
    "Kina": 1412000000,
    "USA": 339000000,
    "Indonesia": 277000000,
    "Pakistan": 241000000
}
for i in innbyggere.keys():
    print(i)
for i in innbyggere.values():
    print(i)
for i, j in innbyggere.items():
    print(f'{i} har {j} innbyggere')

sortert = sorted(innbyggere.keys())
for i in sortert:
    print([innbyggere[i]])

for land, antall in innbyggere.items():
    print(f'{land} har {antall} innbyggere')

flest = max(innbyggere, key = innbyggere.get)
minst = min(innbyggere, key = innbyggere.get)

print(f'\n{flest_innbyggere} har flest innbyggere. {faerrest_innbyggere} har færrest innbyggere.')
"""
"""
sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]

for ol in sommer_ol:
    år = ol["årstall"]
    vinnertid_200 = ol["vinnertider"]["200 m"]
    print((f"I {år} var vinnertiden på 200 m: {vinnertid_200}."))

for ol in sommer_ol:
    år = ol["årstall"]
    vinnertid_400 = ol["vinnertider"]["400 m"]
    print(år, vinnertid_400)

for ol in sommer_ol:
    if ol["årstall"] == 2020:
        vinnertider = ol["vinnertider"]
        print("Vinnertidene i 2020 er: ")
        for distanse, tid in vinnertider.items():
            print(f'{distanse}: {tid}')

beste_tid = float('inf')
dårligste_tid = 0
år_beste = None
år_dårligste = None

for ol in sommer_ol:
    tid = ol["vinnertider"]["200 m"]
    år = ol["årstall"]

    if tid < beste_tid:
        beste_tid = tid
        år_beste = år
    if tid > dårligste_tid:
        dårligste_tid = tid
        år_dårligste = år
    
print(f'Den beste vinnertiden er {beste_tid} som ble gjort i {år_beste}')
print(f'Den beste vinnertiden er {dårligste_tid} som ble gjort i {år_dårligste}')
"""
sommer_ol = [
    {
        "øvelse": "100 m",
        "vinnertider": {
            2004: 10.93,
            2008: 10.78,
            2012: 10.75,
            2016: 10.71,
            2020: 10.61   }  },
                {
        "øvelse": "200 m",
        "vinnertider": {
            2004: 22.06,
            2008: 21.74,
            2012: 21.88,
            2016: 21.78,
            2020: 21.53   }  },
    {
        "øvelse": "400 m",
        "vinnertider": {
            2004: 49.41,
            2008: 49.62,
            2012: 49.55,
            2016: 49.44,
            2020: 48.36
        } }]
"""
for øvelse in sommer_ol:
    if øvelse["øvelse"] == "400 m":
        print("Vinnertider for 400m:" )
        for år, tid in øvelse["vinnertider"].items():
            print(f'Vinnertiden for 400m i år {år} var {tid}')

for øvelse in sommer_ol:
    if 2020 in øvelse["vinnertider"]:
        tid2020 = øvelse["vinnertider"][2020]
        print(f"Vinnertiden for {øvelse['øvelse']} i 2020 var {tid2020} sekunder")
"""
"""
vinnertider = []
for øvelse in sommer_ol:
    if øvelse["øvelse"] == "200 m":
        for år, tid in øvelse["vinnertider"].items():
            print(f'Vinnertiden for 200m i år {år} var {tid}')
            vinnertider.append((år, tid))
           
rask = min([tid for år, tid in vinnertider])
treg = max([tid for år, tid in vinnertider])
for år, tid in vinnertider:
    if tid == rask:
        print(f'Raskeste tid på 200m var {tid} i {år}')
    if tid == treg:
        print(f'Tregeste tid på 200m var {tid} i {år}')
"""
"""
vaerdata = {
  "lat":59.97,"lon":10.78,"timezone":"Europe/Oslo","timezone_offset":7200,"daily": [
    { 
      "dt":1649329200,
      "sunrise":1649305463,
      "sunset":1649355199,
      "moonrise":1649311440,
      "moonset":1649295060,
      "moon_phase":0.19,
      "temp":{"day":277.51,"min":271.29,"max":277.51,"night":271.8,"eve":273.29,"morn":271.79},
      "feels_like":{"day":273.59,"night":265.92,"eve":268.02,"morn":269.78},
      "pressure":956,
      "humidity":46,
      "dew_point":267.62,
      "wind_speed":6.13,
      "wind_deg":19,
      "wind_gust":13.63,
      "weather":[{"id":601,"main":"Snow","description":"snow","icon":"13d"}],
      "clouds":100,"pop":0.89,"snow":1.65,"uvi":1.57
    },
    {
      "dt":1649415600,
      "sunrise":1649391683,
      "sunset":1649441745,
      "moonrise":1649400060,
      "moonset":1649385480,
      "moon_phase":0.22,
      "temp":{"day":274.79,"min":270.59,"max":275.91,"night":271.85,"eve":274.38,"morn":270.83},
      "feels_like":{"day":269.76,"night":268.08,"eve":270.43,"morn":264.98},
      "pressure":978,
      "humidity":47,
      "dew_point":264.4,
      "wind_speed":6.47,
      "wind_deg":17,
      "wind_gust":13.84,
      "weather":[{"id":601,"main":"Snow","description":"snow","icon":"13d"}],
      "clouds":100,"pop":0.93,"snow":3.25,"uvi":1.52
    },
    {
      "dt":1649502000,
      "sunrise":1649477903,
      "sunset":1649528291,
      "moonrise":1649490180,
      "moonset":1649474580,
      "moon_phase":0.25,
      "temp":{"day":279.69,"min":269.31,"max":280.16,"night":275.71,"eve":278.03,"morn":271.25},
      "feels_like":{"day":276.68,"night":272.13,"eve":275.54,"morn":268.85},
      "pressure":987,
      "humidity":33,
      "dew_point":264.45,
      "wind_speed":4.95,
      "wind_deg":309,
      "wind_gust":11.28,
      "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
      "clouds":99,"pop":0.07,"uvi":1.89
    },
    {
      "dt":1649588400,
      "sunrise":1649564124,
      "sunset":1649614838,
      "moonrise":1649581320,
      "moonset":1649562480,
      "moon_phase":0.28,
      "temp":{"day":280.52,"min":272.77,"max":280.52,"night":273.93,"eve":275.92,"morn":274.61},
      "feels_like":{"day":277.89,"night":273.93,"eve":274.78,"morn":272.43},
      "pressure":1007,
      "humidity":29,
      "dew_point":263.31,
      "wind_speed":4.52,
      "wind_deg":315,
      "wind_gust":12.53,
      "weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
      "clouds":6,"pop":0,"uvi":2.13
    },
    {
      "dt":1649674800,
      "sunrise":1649650345,
      "sunset":1649701385,
      "moonrise":1649673060,
      "moonset":1649649660,
      "moon_phase":0.32,
      "temp":{"day":280.61,"min":272.4,"max":280.61,"night":274.01,"eve":276.89,"morn":274.49},
      "feels_like":{"day":280.61,"night":272.1,"eve":275.3,"morn":273.14},
      "pressure":1021,
      "humidity":30,
      "dew_point":264,
      "wind_speed":1.78,
      "wind_deg":359,
      "wind_gust":2.4,
      "weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
      "clouds":4,"pop":0,"uvi":2.51
    },
    {
      "dt":1649761200,
      "sunrise":1649736566,
      "sunset":1649787932,
      "moonrise":1649764920,
      "moonset":1649736480,
      "moon_phase":0.35,
      "temp":{"day":281.89,"min":272.85,"max":282.59,"night":275.98,"eve":278.9,"morn":274.97},
      "feels_like":{"day":281.49,"night":275.98,"eve":278.9,"morn":274.97},
      "pressure":1027,
      "humidity":31,
      "dew_point":265.49,
      "wind_speed":1.39,
      "wind_deg":273,
      "wind_gust":1.67,
      "weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
      "clouds":41,"pop":0,"uvi":3
    },
    {
      "dt":1649847600,
      "sunrise":1649822788,
      "sunset":1649874479,
      "moonrise":1649856840,
      "moonset":1649823120,
      "moon_phase":0.38,
      "temp":{"day":281.97,"min":273.81,"max":281.97,"night":276.99,"eve":279.17,"morn":275.6},
      "feels_like":{"day":280.48,"night":276.99,"eve":277.99,"morn":275.6},
      "pressure":1028,
      "humidity":37,
      "dew_point":267.68,
      "wind_speed":2.98,
      "wind_deg":192,
      "wind_gust":3.87,
      "weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],
      "clouds":97,
      "pop":0.2,
      "snow":0.19,
      "uvi":3
    },
    {
      "dt":1649934000,
      "sunrise":1649909011,
      "sunset":1649961026,
      "moonrise":1649948700,
      "moonset":1649909700,
      "moon_phase":0.41,
      "temp":{"day":283.23,"min":276.18,"max":283.84,"night":276.63,"eve":279.32,"morn":276.9},
      "feels_like":{"day":281.36,"night":276.63,"eve":277.59,"morn":275.47},
      "pressure":1025,
      "humidity":41,
      "dew_point":270.19,
      "wind_speed":3.31,
      "wind_deg":199,
      "wind_gust":6.27,
      "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
      "clouds":83,
      "pop":0,
      "uvi":3
    }
  ]
}
import datetime as dt

for dag in vaerdata["daily"]:
    unixdato = dag["dt"]
    dato = dt.datetime.fromtimestamp(unixdato)
    temperatur = dag["temp"]["day"] - 273.15
    vær = dag["weather"][0]["description"]
    unix_soloppgang = dag["sunrise"]
    soloppgang = dt.datetime.fromtimestamp(unix_soloppgang)
    print(f'På {dato} er temperaturen {temperatur:.2f} og været er {vær} og soloppgang {soloppgang}')
"""
"""
#Sluttoppgave 2
ordbok = {1: "en", 2: "to", 3: "tre", 4: "fire", 5:"fem", 6: "seks", 7: "syv", 8: "åtte", 9: "ni", 10: "ti"}
for x in ordbok.keys():
    if x == 10:
        print(x,"|", ordbok[x].capitalize())
    else:
        print(x, " |", ordbok[x].capitalize())
""""""
#Sluttoppgave 3
tekst = "jeg heter Fredrik og .er atten år"
tekst = tekst.lower()
bokstavteller = {}
for bokstav in tekst:
    if bokstav != " " and bokstav != ".":
        if bokstav in bokstavteller:
            bokstavteller[bokstav] += 1
        else:
            bokstavteller[bokstav] = 1

sortert = sorted(bokstavteller.items())
for bokstav, antall in sortert:
    print(f'{bokstav}: {antall}')
""""""
byer = {
    "Oslo": {
        "fylke": "Oslo",
        "befolkning": 709037,
        "grunnlagt": 1048,
        "kjent_for": "hovedstad og operaen",
        "areal_km2": 454
    },
    "Bergen": {
        "fylke": "Vestland",
        "befolkning": 288000,
        "grunnlagt": 1070,
        "kjent_for": "Bryggen og regn",
        "areal_km2": 465
    },
    "Trondheim": {
        "fylke": "Trøndelag",
        "befolkning": 212660,
        "grunnlagt": 997,
        "kjent_for": "Nidarosdomen",
        "areal_km2": 342
    },
    "Stavanger": {
        "fylke": "Rogaland",
        "befolkning": 144699,
        "grunnlagt": 1125,
        "kjent_for": "oljebyen",
        "areal_km2": 71
    },
    "Tromsø": {
        "fylke": "Troms og Finnmark",
        "befolkning": 77900,
        "grunnlagt": 1794,
        "kjent_for": "nordlys og arktisk forskning",
        "areal_km2": 2521
    }
}

for sted, info in byer.items():
    print()
    print("-"* (len(sted)+3))
    print(sted)

    for nøkkel, verdi in info.items():
        print(f'{nøkkel.capitalize()}: {verdi}')
"""
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
"""
print("Lag som har vunnet minst ett seriemesterskap:")
print()
for team in eliteserielag:
    lag = team["lag"]
    seriemesterskap = team["seriemesterskap"]
    norgesmesterskap = team["norgesmesterskap"]
    if norgesmesterskap != [] and seriemesterskap != []:
        print(f'{lag} har vunnet minst en av hver')
        ost = True
    if seriemesterskap != []:
        print(f'{lag}: Seriemesterskap: {seriemesterskap}')
    if norgesmesterskap != []:
        print(f'{lag}: Norgesmesterskap: {norgesmesterskap}')
        if ost == True:
            print()
""""""
flest_serie = 0
flest_norges = 0
serielag_med_flest = ""
norgeslag_med_flest = ""
for team in eliteserielag:
    seriemesterskap = team["seriemesterskap"]
    norgesmesterskap = team["norgesmesterskap"]
    mengdeSeriemesterskap = len(seriemesterskap)
    mengdeNorgesmesterskap = len(norgesmesterskap)
    if mengdeSeriemesterskap > flest_serie:
            flest_serie = mengdeSeriemesterskap
            serielag_med_flest = team["lag"]
    if mengdeNorgesmesterskap > flest_norges:
          flest_norges = mengdeNorgesmesterskap
          norgeslag_med_flest = team["lag"]
print(f'{serielag_med_flest} har flest seiere i serieliga med {flest_serie}')
print(f'{norgeslag_med_flest} har flest seiere i Norgesliga med {flest_norges}')
"""
førsteårliste = []
sisteårliste = []
for team in eliteserielag:
    seriemesterskap = team["seriemesterskap"]
    if seriemesterskap:
        første_år = min(seriemesterskap)
        siste_år = max(seriemesterskap)
        førsteårliste.append((første_år, team["lag"]))
        sisteårliste.append((siste_år, team["lag"]))
førsteårliste.sort()
sisteårliste.sort() 
første_år, førstelag = førsteårliste[0]
siste_år, sistelag = sisteårliste[0]
print(f'{førstelag} vant for første gang i {første_år}')
print(f'{sistelag} vant for siste gang i {siste_år}')











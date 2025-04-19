#Oppgave 2 3
"""
filnavn = "mikkelrev.txt"

with open(filnavn, encoding = "utf-8") as fil:
    innhold = fil.read()
print(innhold)

#strip fjerner begge sider
#rstrip fjerner høyre
#lstrip fjerner venstre
tekstliste = []
with open(filnavn, encoding = "utf-8") as fil:
    for linje in fil:
        tekstliste.append(linje.rstrip())
print(tekstliste)
""""""
#Oppgave 3
class Rektangel:
    def __init__(self, lengde, bredde):
        self.lengde = lengde
        self.bredde = bredde

    def areal(self):
        return self.lengde * self.bredde
    
    def __str__(self):
        return(f'{self.lengde} og {self.bredde} gir {self.areal()}')
    
rektangler = []
rektangelfil = "rektangler.txt"

with open(rektangelfil) as fil:
    for linje in fil:
        sidekanter = linje.rstrip().split(",")

        lengde = int(sidekanter[0])
        bredde = int(sidekanter[1])

        rektangler.append(Rektangel(lengde, bredde))

for rektangel in rektangler:
    print(rektangel.areal())
""""""
#Oppgave 4
import numpy as np
import matplotlib.pyplot as plt

valgfil = "valgdeltagelse.txt"
årliste = []
deltagelseliste = []

with open(valgfil) as fil:
    for linje in fil:
        info = linje.strip().split(";")

        år = int(info[0])
        deltagelse = float(info[1].replace(",", "."))

        årliste.append(år)
        deltagelseliste.append(deltagelse)

plt.plot(årliste, deltagelseliste)
plt.show()
"""
#Oppgave 5
"""
tallfil = "tall.txt"
with open(tallfil) as fil:
    for linje in fil:
        info = linje.rstrip().split("-")
        talliste = [int(tall) for tall in info]
        total = sum(talliste)
        gjennomsnitt = total/len(talliste)
        tall_streng = " ".join(map(str, talliste))
        print(f'tall = {tall_streng}, total = {total}, gjennomsnitt = {gjennomsnitt}')
""""""
#Oppgave 6
    tekst = str(input("Skriv tekst: "))
    filnavn = "oppgave_6_tekstfil.txt"

    with open(filnavn, "a") as fil:
        fil.write(tekst + "\n")
""""""
#Oppgave 8
import csv
filnavn = "befolkning.csv"

with open(filnavn, encoding = "utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)

    for rad in filinnhold:
        print(rad)
"""
#Oppgave 11
"""
import csv
import matplotlib.pylab as plt
filnavn = "excel_aunivers_oppgave.csv"

spilliste = []
alderliste = []

with open(filnavn, encoding = "utf-8-sig") as fil:
    innhold = csv.reader(fil, delimiter=";")

    overskrifter = next(innhold)
    print(overskrifter)

    for rad in innhold:
        alder = rad[0].strip()
        if alder != "I alt":
            alderliste.append(alder)
            spilliste.append(int(rad[1]))

#plt.figure(figsize=(12, 5))
plt.bar(alderliste, spilliste)
plt.ylabel("Antall timer")
plt.xlabel("Aldersgrupper")
plt.grid(axis = "y")
plt.title("Timer spilling versus aldersgrupper")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()"""

#Oppgave 12
"""
import json

filnavn = "skandinavia.json"

with open(filnavn, encoding="utf-8") as fil:
    info = json.load(fil)

landene = [land["navn"] for land in info["land"]]
for land in info["land"]:
    if land["navn"] == "Danmark":
        print(land["byer"])
for land in info["land"]:
    navn = land["navn"]
    byer = ", ".join(land["byer"])
    print(f'{navn}: {byer}')

for land in info["land"]:
    if land["navn"] == "Danmark":
        byliste = land["byer"]
        byliste.append("AAAAA")
        byliste.append("BAAAA")
        byliste.sort()
        aindeks = byliste.index("AAAAA")
        bindeks = byliste.index("BAAAA")
        for i in range(aindeks+1, bindeks):
            print(byliste[i])

for land in info["land"]:
    if land["navn"] == "Danmark":
        for by in land["byer"]:
            if by.startswith("A"):
                print(by)
""""""
import json
import matplotlib.pyplot as plt
import numpy as np

filnavn = "lonnstabell.json"

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)
    data_formatert = json.dumps(data, indent=2)
    årstall = list(data["dataset"]["dimension"]["Tid"]["category"]["label"].values())
    lønner = data["dataset"]["value"]
    mannslønn = lønner[0:6]
    kvinnelønn = lønner[6:12]

fig, ax = plt.subplots()
x = np.arange(len(årstall))

ax.bar(x + 0.2, mannslønn, width = 0.4, label = "Menn")
ax.bar(x - 0.2, kvinnelønn, width = 0.4, label = "Kvinner", color = "pink")
ax.set_xticks(x, årstall)
plt.legend()
plt.grid(axis = "y")
plt.tight_layout()
plt.show()
""""""
plt.plot(årstall, mannslønn, color = "blue", label = "Menn")
plt.plot(årstall, kvinnelønn, color = "deeppink", label = "Damer")
plt.grid()
plt.xlabel("År")
plt.ylabel("Lønn")
plt.legend()
plt.tight_layout()
plt.show()
"""
#Sluttoppgave 1 Funker ikke
"""
filnavn = "ønskeliste.txt"
with open(filnavn, encoding="utf-8") as fil:
    info = fil.read()
    print(info)

with open(filnavn, "a", encoding="utf-8") as fil:
    while True:
        ønske = (input("Hva vil du ha?: "))
        prioritet = (input("Hvilken prioritet: "))
        if str(ønske) == "STOPP" or str(prioritet) == "STOPP":
            print("Liste stoppet")
            break
        else:
            fil.write(ønske + prioritet)
"""
import csv
import pandas as pd
filnavn = "fritidsboliger.csv"

with open(filnavn, encoding="utf-8") as fil:
    for linje in fil:
        print(linje)


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
"""
#Oppgave 6
while True:
    tekst = str(input("Skriv tekst: "))
    filnavn = "oppgave_6_tekstfil.txt"

    with open(filnavn, "a") as fil:
        fil.write(tekst + "\n")
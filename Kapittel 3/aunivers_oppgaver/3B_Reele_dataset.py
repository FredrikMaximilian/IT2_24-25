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
"""
#Oppgave 3
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
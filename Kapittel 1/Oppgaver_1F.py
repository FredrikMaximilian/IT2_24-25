'''
#Oppgave 1, tilfeldig hilsen
import random

def tilfeldighilsen():
    hilsener = ["Hei", "Hallo", "God dag"]
    hilsen = random.choice(hilsener)
    print(hilsen)

tilfeldighilsen()
'''
'''
#Endre på lister
tall = [1, 2, 3, 4, 5]

def endreFoerste(liste):
  liste[0] = "Hei"
  print(liste)

print(tall)
endreFoerste(tall)
print(tall)
'''
'''
#Potenisell energi
def potensiellEnergi(m, h, g=9.81):
  print(f"En gjenstand med massen {m} kg ved høyden {h} m har den potensielle energien {m*g*h:.2f} J (med g = {g})." )

potensiellEnergi(50, 10)

potensiellEnergi(50, 10, g=1.62)
potensiellEnergi(50, 10, 1.62)
'''
'''
#5, areal av kvadrat
def areal(side):
    return side**2

print(areal(2))
'''
'''
def arealRektangel(lengde, bredde):
  areal = lengde * bredde
  return areal
  '''
'''
def arealRektangel(lengde, bredde):
  return lengde * bredde

print(f"Arealet av et rektangel med sidelengder 8 og 4, er: {arealRektangel(8,4)}.")
'''
'''
#Bildebotek
import terninger as t

help(t.terning)
help(t.flereTerninger)

print(t.flereTerninger(4, 6))
'''
'''
#Global/lokal variabel
eksempel = "utenfor funksjon"  # en global variabel

def funksjon():
  eksempel = "inni funksjon"  # en lokal variabel 
  print(eksempel)             # skriver ut: inni funksjon

funksjon()
print(eksempel)  # skriver ut: utenfor funksjon
'''
'''
from random import choice
def tilfeldighilsen():
    hilsen = ["god morgen", "hei", "hallo"]
    valgt = choice(hilsen)
    print(valgt)
tilfeldighilsen()
'''
def sihei(navn):
    print("hei", navn)
sihei("Fredrik")

def areal(lengde, bredde):
    a = lengde*bredde
    print(a)

areal(4, 6)


#Oppgave 5-11
"""
def arealkvadrat(lengde, bredde):
    areal = lengde *bredde
    print(f'arealet er lik {areal}')

def arealsirkel(radius):
    areal = radius**2 * 3.14
    print(f'Arealet av en sirkel med radius {radius} er {areal}')

def byland(by, land):
    print(f'{by} er en by i {land}')

def minsttall(a, b):
    if a < b:
        print(a)
    elif b < a:
        print(b)
    else:
        print("a og b er lik")

def navneskilt(navn):
    print("-" * ((len(navn))+3))
    print(f'| {navn} |')
    print("-" * ((len(navn))+3))

ost = True
liste  = ["kaffekopp", 345, "bok om verdensrommet", ost, "liten robot"]
def visliste(listenavn):
    for indeks, bit in enumerate(listenavn): #Lar iterere oven liste og få både indeks og navn
        print(indeks, bit)

personer = {
    "Anna": 23,
    "Jonas": 31,
    "Mina": 27,
    "Elias": 19,
    "Sara": 31
}
def visordbok(ordboknavn):
    for navn, alder in ordboknavn.items():
        print(navn, alder)
""""""
#Oppgave 12-18
def trekantareal(høyde, grunnbredde):
    return 0.5*høyde*grunnbredde

def antallforekomster(tekst, bokstav):
    antall = 0
    for tegn in tekst:
        if tegn == bokstav:
            antall += 1
        else:
            antall = antall
    return antall


def tellantallord(tekst):
    ordliste = tekst.split()
    return len(ordliste)

def finnminst(a, b, c):
    return min(a, b, c)
def finnstørst(a, b, c):
    return max(a, b, c)
def finnminstogstørst(a, b, c):
    return(finnminst(a, b, c), finnstørst(a, b, c))

def sjekkomlike(a, b, c):
    if a == b and b == c:
        return True
    return False

def sjekkomulike(a, b, c):
    if sjekkomlike(a, b, c) == False:
        return True
    return False

liste = [1, 2, 4, 5, 7, 10]
def dobleliste(listenavn):
    doblet_liste = []
    for tall in listenavn:
        tall = 2*tall
        doblet_liste.append(tall)
    return(listenavn, doblet_liste)
"""      """
def arealRektangel(lengde, bredde):
    if isinstance(lengde, str) or isinstance(bredde, str):
        return("Lengde og/eller bredde kan ikke være tekst")
    elif lengde <= 0 or bredde <= 0:
        return("Lengde og/eller bredde kan ikke være 0 eller under")
    else:
        areal = lengde * bredde
        return(areal)

#Oppgave 19
help(sum)
help(arealRektangel)
""""""
import Biblotek_1F_Oppgave22 as bff
liste = [4, 1, 2, 5, "ord"]
print(bff.totalsum(liste))
print(bff.gjennomsnitt(liste))
print(bff.minst(liste))
print(bff.størst(liste))
"""
"""En lokal variabel ligger inni funksjonen og kan ikke tilkalles utenfor funksjonen. En global er alltid der."""
#Sluttoppgave 2
"""
def testalder(navn, alder):
    if alder < 30:
        print(f'Hei, {navn}, du er ung')
    else:
        print(f'Du er gammel, {navn}')
testalder("Janne", 29)
testalder("Per", 74)
""""""
#Sluttoppgave 3
tekst = "jegere"
def antalltegn(tekstnavn):
    total = 0
    for i in tekstnavn:
        total += 1
    return(total)

def midterste_tegn(tekstnavn):
    antall = antalltegn(tekstnavn)
    if antall % 2 != 0:
        midt = (antall//2)
        return(tekstnavn[midt])
    else:
        midt1 = antall//2-1
        midt2 = antall//2
        return(tekstnavn[midt1] + tekstnavn[midt2])
print(midterste_tegn(tekst))"""

tekst = "Regningere"
def sjekkpalindrom(tekstnavn):
    tekstnavn = tekstnavn.lower()
    rettliste = []
    omvendtliste = []
    for tegn in tekstnavn:
        rettliste.append(tegn)
    omvendtliste = rettliste.copy()
    omvendtliste.reverse()
    if rettliste == omvendtliste:
        return True
    return False

print(sjekkpalindrom(tekst))


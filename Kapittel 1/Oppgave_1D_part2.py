"""
#Opppgave 2
tall = [x for x in range(0, 51)]
print(tall)
oddetall = [(2*x+1)for x in range(0, 100)]
print(oddetall)
kvadrattall = [(x**2) for x in range(0, 21)]
print(kvadrattall)
kubikktall = [(x**3) for x in range(0, 16)]
print(kubikktall)
print(min(kubikktall))
print(max(kubikktall))
print(sum(kubikktall))
"""
"""
#append legger til bakerst i lista
#insert legger til fremst i lista
liste = []
liste.append(1)
liste.append(2)
liste.append(3)
liste.insert(2, "jeg")
print(liste)

tegneseriefigurer = ["Asterisk", "Obelix"]
tegneseriefigurer[0] = "Asterix"
#Setter ny verdi for første plass

if "Asterix" in tegneseriefigurer:
  print("Asterix er registrert")
#Kan sjekke om noe er med i liste slik

indeks = tegneseriefigurer.index("Asterix")
#Sjekker hvilken indeks første Asterix er 
#Kan sette tall foran for å bestemme hvor det skal starte
tegneseriefigurer.remove("Asterix")
#Fjerner første asterix

tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tall.pop(4)
#Kan bruke pop for å fjerne med indeks
#Uten indeks forsvinner -1
"""
"""
#Oppgave 7
liste = [x for x in range(0, 21)]
print(liste)
for i in range(10):
    liste.pop(i+1)
    i +=2
print(liste)
""""""
#Oppgave 8
tall = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
#if 3 in tall:
   # fjernindeks = tall.index(3)
    #tall.pop(fjernindeks)
while 3 in tall:
    tall.remove(3)
print(tall)
"""
"""
poeng = [87, 52, 34, 90, 23]
verdier = list(poeng)

verdier[2] = 68

print(poeng)
print(verdier)
#Lager en kopi av poengliste, kan ikke skrive poeng = verdier direkte
"""
"""
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(tall[3:6])
print(tall[:5])
print(tall[5:])
print(tall[-3:])
print(tall[:-1])
oddetall = tall[::2]
partall = tall[1::2]

tall = [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6] 
print(tall)        # Skriver ut: [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6]
tall.sort()        
print(tall)        # Skriver ut: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

tall = [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6] 
print(tall)        # Skriver ut: [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6]
tall.sort(reverse=True)
print(tall)        # Skriver ut: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

tall = [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6] 
print(tall)            # Skriver ut: [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6]
print(sorted(tall))    # Skriver ut: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(tall)            # Skriver ut: [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6]
"""
"""
#Oppgave 9
første = [2*x for x in range(11)]
print(første)
andre = [0 for x in range(10)]
print(andre)
tredje = []
for i in range(5):
    tredje.append(0)
    tredje.append(1)
print(tredje)
""""""
#Oppgave 10
byer = ["OSLOO", "Trondheim", "Bergen", "Stavaangir", "Kristiansand", "Drammen", "Tromsø"]
print(byer)
byer.remove("Stavaangir")
print(byer)
fjernoslo = byer.index("OSLOO")
byer.pop(fjernoslo)
print(byer)
byer.insert(0, "Oslo")
byer.insert(3, "Stavanger")
print(byer)"
""""""
#Oppgave 11
byer = ["OSLOO", "Trondheim", "Bergen", "Stavaangir", "Kristiansand", "Drammen", "Tromsø"]
byer[0] = "Oslo"
byer[3] = "Stavanger"
print(byer)""""""
#Oppgave 12
tall = [0, 1, 2, 0, 0, 3, 4, 5, 0, 0, 6, 0, 7, 0, 8, 0, 0, 0, 9, 10]
while 0 in tall:
    tall.remove(0)
print(tall)""""""
#Oppgave 13
navn = ["Anne", "Per", "Ole", "Anne", "Lise", "Ole", "Anne", "Per", "Anne", "Tor", "Ole"]
nyenavn = list(set(navn))
print(nyenavn)


# Bruk en løkke og en hjelpe-sett for å bevare rekkefølgen
unike_navn = []
sett_navn = set()

for n in navn:
    if n not in sett_navn:
        unike_navn.append(n)
        sett_navn.add(n)


print(unike_navn)""""""
#Oppgave 14
import random as r
liste = []
for i in range(1000):
    tall = r.randint(1, 100)
    liste.append(tall)
liste.append(17.42)
liste.append(81)
liste.sort()
print(liste)
print(liste[0])
print(liste[-1])
"""
"""
#Oppgave 16
tall = [2, 4, 6, 8, 10]
størst = tall[0]
for i in range(len(tall)):
    if tall[i] > størst:
        størst = tall[i]
print(størst)
print(min(tall))""""""
#Oppgave 17
liste = ["i", "jeg", "få", "oster", "chilly", "penerdfgfffffhjhhhh", "lengstemann"]
lengst = liste[0]
for i in liste:
    if len(i) > len(lengst):
        lengst = i
print(lengst)
""""""
#Oppgave 18
tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1]
total = 0
for i in tall:
    total += i
print(total)
gjennomsnitt = total/len(tall)
print(gjennomsnitt)
""""""
#Oppgave 19
tall = [1, 3, -2, 2, 5, -1, -7, 8, 5, 6, -4, 5]
antall = 0
negativ = []
for i in tall:
    if i < 0:
        antall += 1
        negativ.append(i)
print(antall)
print(negativ)
""""""
#Oppgave 20
tall = [3, 4, 1, 2, 5]

midlertidig3 = tall[0]
midlertidig4 = tall[1]
tall[0]=tall[2]
tall[1] = tall[3]
tall[2] = midlertidig3
tall[3] = midlertidig4
print(tall)""""""
#Oppgave 21
liste = []
while True:
    tall = input("Skriv inn et tall eller x for å avslutte: ")

    if tall.lower() == "x":
        print("Avbrutt")
        break
    try:
        tall = int(tall)
        liste.append(tall)
    except ValueError:
        print("Skriv inn et tall eller x")
    
if liste:
    print(liste)
    print(f'Minste tall er {min(liste)}')
    print(f'Største tall er {max(liste)}')
    print(f'Summen er {sum(liste)}')
else:
    print("Ingenting i lista")"""
"""
#OPpgave 22
navn = "Pål"
karakterer = [3, 4, 6, 6, 5, 4]
midlertidig = karakterer.copy()
midlertidig.pop(-1)

karaktertekst = ""
for i in range(len(karakterer)):
  if i > 0:
    karaktertekst += ", " 
  karaktertekst += str(karakterer[i])

print(f"{navn} fikk karakterene {karaktertekst}")

midlertidigtekst = ""
for i in range(len(midlertidig)):
  if i > 0:
    midlertidigtekst += ", "
  midlertidigtekst += str(karakterer[i])

midlertidigtekst += (f' og {str(karakterer[-1])}')
print(midlertidig)
print(midlertidigtekst)
"""
"""
#Oppgave 24a
rader = 5
kolonner = 5

tabell = [[0]*kolonner for _ in range(rader)]
for rad in tabell:
    print(rad)
""""""
#b
sjakkbrett = []
for r in range(8):
    rad = []
    for k in range(8):
        if (r+k) % 2 == 0:
            rad.append("H")
        else:
            rad.append("S")
    sjakkbrett.append(rad)

for rad in sjakkbrett:
    print(rad)"""
#c
# Lager en 5x5-liste med 0-er og 1-er i første og siste kolonne
"""
rader = 5
kolonner = 5
matrise = []

for r in range(rader):
    rad = []
    for k in range(kolonner):
        if k == 0 or k == kolonner - 1:  # Første eller siste kolonne
            rad.append(1)
        else:
            rad.append(0)
    matrise.append(rad)

# Skriver ut matrisen
for rad in matrise:
    print(rad)
    """"""
#Sluttoppgae 1
liste = [9, 8, 7, 6, 5, 4, 4, 3, 2, 1]

liste.pop()
liste.insert(0, 10)
liste.remove(4)
liste.append(1)
liste.reverse()
print(liste)
""""""
#Sluttoppgave 2
import random as r
partall = ""
oddetall = ""
partallsinndeks = ""

liste = []
for i in range(50):
    tall = r.randint(0, 100)
    liste.append(tall)
    if tall % 2 == 0:
        partall += str(tall) + " "
    else: 
        oddetall += str(tall) + " "

    
#for i in range(len(liste)):
  #  if i%2 == 0:
  #      print(liste[i])

print(liste)
print()
print(partall)
print()
print(oddetall)
print(partallsinndeks)
print()

for i in range(len(liste)):
    print(f'{liste[i]} ', end="")
""""""
#Sluttoppgave 3
liste = []
while len(liste) < 10:
    tall = input("Skriv inn et tall: ")

    try:
        tall = int(tall)
    except:
        print("Du må skrive inn et heltall")
        continue
    if tall in liste:
        print("Du må skrive inn et nytt tall")
    else:
        liste.append(tall)
        
print(liste)"""
"""
import random as r
n = 6
liste = []
for i in range(n):
    tall = r.randint(0, 100)
    tall = int(tall)
    liste.append(tall)
    
liste.sort()
print(liste)

if n % 2 != 0:
    n = n-1
    m = int(n/2)
    median = liste[m]
else:
    m = int(n/2)
    median = (liste[m] + liste[m-1])/2
print(f'Medianen er {median}')
"""

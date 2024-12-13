'''
#Oppgave 1
verdensdeler = ["Europa", "Afrika", "Nord-Amerika", "Sør-Amerika", "Asia","Oseania", "Antarktis"]
print(verdensdeler[0])
print(verdensdeler[3])
print(verdensdeler[-1])
'''
'''
#Oppgave 2
heltall = list(range(1, 51))
print(heltall)
'''
'''
#oppgave 3
oddetall = list(range(1, 200, 2))
print(oddetall)
'''
'''
#Oppgave 4
kvadrattall = [x**2 for x in range(1,20)]
print(kvadrattall)
'''
'''
#Oppgave 5
kubikktall = [x**3 for x in range(1, 15)]
print(kubikktall)
'''
'''
#Oppgave 7
heltall = []
for i in range(20):
    heltall.append(i)
print(heltall)

for j in range(0, 20, 2):
    heltall.remove(j)
print(heltall)
'''
'''
#Oppgave 8
liste = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
while 3 in liste:
    liste.remove(3)
print(liste)
'''
'''
#Oppgave 9, lag lister
liste = list(range(0, 21, 2))
print(liste)
liste2 = [0]*10
print(liste2)
liste3 = [0, 1] * 5
print(liste3)
'''
'''
#Oppgave 10
byer = ["OSLOO", "Trondheim", "Bergen", "Stavaangir", "Kristiansand", "Drammen", "Tromsø"]
print(byer)
byer.remove("Stavaangir")
print(byer)
indeks = byer.index("OSLOO")
print(indeks)
byer.pop(0)
print(byer)
byer.insert(0, "Oslo")
byer.insert(3, "Stavanger")
print(byer)
'''
'''
#Oppgave 11, omgjøre verdier direkte
byer = ["OSLOO", "Trondheim", "Bergen", "Stavaangir", "Kristiansand", "Drammen", "Tromsø"]
byer[3] = "Stavanger"
byer[0] = "Oslo"
print(byer)
'''
'''
#Oppgave 12, fjern 0
tall = [0, 1, 2, 0, 0, 3, 4, 5, 0, 0, 6, 0, 7, 0, 8, 0, 0, 0, 9, 10]
while 0 in tall:
    tall.remove(0)
print(tall)
'''
'''
#Oppgave 13, kun et navn i lista
navn = ["Anne", "Per", "Ole", "Anne", "Lise", "Ole", "Anne", "Per", "Anne", "Tor", "Ole"]
unikeNavn = list(set(navn))
print(unikeNavn)
'''
'''
#Oppgave 14, sorter tilfeldige tall mellom 0 og 100
import random as ra
liste = []
for i in range(0, 1000):
    a = ra.randint(0, 100)
    liste.append(a)

liste.sort()
print(liste)
minst = min(liste)
største = max(liste)
print(minst)
print(største)
'''
'''
#Oppgave 15
import random as ra
liste = [17, 42, 81]

for i in range(0, 1000):
    a = ra.randint(0, 100)
    liste.append(a)
liste.sort()
print(liste)
'''
'''
#Oppgave 16 Finn størst/minst verdi
liste = [4, 6, 2, 6, 89, 1]
størst = liste[0]
minst = liste[0]
for i in range(len(liste)):
    if liste[i] > størst:
        størst = liste[i]
for j in range(len(liste)):
    if liste[j] < minst:
        minst = liste[j]

print(minst)
print(størst)
'''
'''
#Oppgave 18 Sum og Gjennomsnitt
tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1]
total = sum(tall)
print(total)
gjennomsnitt = total/len(tall)
print(gjennomsnitt)
'''
'''
#Oppgave 19 Telle og liste negative verdier
tall = [1, 3, -2, 2, 5, -1, -7, 8, 5, 6, -4, 5]
total = 0
tliste = []
for i in range(len(tall)):
    if tall[i] < 0:
        tliste.append(tall[i])
        total = total + 1
        
print(total)
print(tliste)
'''
'''
#Oppgave 21
# Initialiser en tom liste for å lagre tallene
tall_liste = []

# Start en evig while-løkke
while True:
    # Be brukeren om å legge inn et tall eller 'x' for å avslutte
    bruker_input = input("Skriv inn et tall (eller 'x' for å avslutte): ")
    
    # Sjekk om brukeren vil avslutte
    if bruker_input.lower() == 'x':
        break
    
    # Forsøk å konvertere input til et tall
    try:
        tall = float(bruker_input)  # Bruk float for å støtte desimaltall
        tall_liste.append(tall)
    except ValueError:
        print("Ugyldig input, prøv igjen med et tall eller 'x' for å avslutte.")

# Hvis listen ikke er tom, skriv ut oversikten
if tall_liste:
    print("\nOversikt over de registrerte tallene:")
    print(tall_liste)
    print("Minste tall:", min(tall_liste))
    print("Største tall:", max(tall_liste))
    print("Summen av tallene:", sum(tall_liste))
else:
    print("Ingen tall ble registrert.")
'''
'''
#Oppgave 22 Legge til og
navn = "Pål"
karakterer = [3, 4, 6, 6, 5, 4]

karaktertekst = ""
for i in range(len(karakterer)-1):
  if i > 0:
    karaktertekst += ", " 
  karaktertekst += str(karakterer[i])

print(f"{navn} fikk karakterene {karaktertekst} og {karakterer[i+1]}")
'''
'''
rader = 4
kolonner = 5
tabell = []
for i in range(rader):
  rad = [0] * kolonner
  tabell.append(rad)
'''
#Oppgave 24a
'''
kolonner = 5
rader = 5
tabell = []
for i in range(rader):
    rad = [0] * kolonner
    tabell.append(rad)
for rad in tabell:
    print(rad)
'''
'''
#Oppgave 24b
rader = 8
kolonner = 8
tabell = []

for i in range(rader):
    rad = []
    for j in range(kolonner):
        if (i+j) % 2 == 0:
            rad.append("h")
        else:
            rad.append("s")
    tabell.append(rad)
for rad in tabell:
    print(rad)
'''
'''
#Oppgave 24C
kolonner = 5
rader = 5
tabell = []

tabell.append([1]*kolonner)
for i in range(rader-2):
    rad = [0] * kolonner
    tabell.append(rad)
tabell.append([1]*kolonner)
        
for rad in tabell:
    print(rad)
'''
'''
#Oppgave 25
import random as ra

rader = 10
kolonner = 10
tabell = []

for i in range(rader):
    rad = [False] * kolonner
    tabell.append(rad)


antallTrue = 5
for _ in range(antallTrue):
    tilfeldigRad = ra.randint(0, rader - 1)
    tilfeldigKolonne = ra.randint(0, kolonner - 1)

    while tabell[tilfeldigRad][tilfeldigKolonne] == True:
        tilfeldigRad = random.randint(0, rader - 1)
        tilfeldigKolonne = random.randint(0, kolonner - 1)

    tabell[tilfeldigRad][tilfeldigKolonne] = True

for rad in tabell:
    print(rad )
'''
'''
#Sluttoppgave 2
liste = []
n = 50
from random import randint
for i in range(n):
    tall = randint(0, 100)
    liste.append(tall)
print(liste)

partallListe = []
oddetallListe = []
for tall in range(n):
    if tall % 2 == 0:
     partallListe.append(tall)
    else:
     oddetallListe.append(tall)

print(partallListe)
print(oddetallListe)
'''
'''
#Sluttoppgave 3
liste = []
while len(liste) < 10:
    a = (input("Skriv inn et heltall: "))
    if a in liste:
        print("Skriv inn et annet tall: ")
    else: 
        liste.append(a)
print(liste)
'''
'''
for i in range(50):
    tall = ra.randint(1, 100)
    liste50.append(tall)
print(liste50)
'''
'''
import random

list_25 = random.sample(range(1, 101), 25)  # 25 tilfeldige tall mellom 1 og 100
list_50 = random.sample(range(1, 101), 50)  # 50 tilfeldige tall mellom 1 og 100

# Sorter begge listene
list_25_sorted = sorted(list_25)
list_50_sorted = sorted(list_50)

# Funksjon for å finne medianen
def find_median(lst):
    n = len(lst)
    if n % 2 == 1:  # Odde antall elementer
        return lst[n // 2]
    else:  # Partall elementer
        return (lst[n // 2 - 1] + lst[n // 2]) / 2

# Beregn medianer
median_25 = find_median(list_25_sorted)
median_50 = find_median(list_50_sorted)

# Vis resultatene
print("Sortert liste med 25 tall:", list_25_sorted)
print("Median av listen med 25 tall:", median_25)
print("Sortert liste med 50 tall:", list_50_sorted)
print("Median av listen med 50 tall:", median_50)
'''

'''
#Sluttoppgave 5. Lekse, lage bondesjakk

spillbrett = [[" " for _ in range(3)] for _ in range(3)] #Oppretter 3x3 spillbrett. 
#Indre listen lager rad med tre tomme strenger, ytre gjentar dette tre ganger for å lage rader. Hence 3x3 
def skriv_ut_spillbrett(): #Lager en funsjon som senere vil skrives ut på en lesbar måte
    for rad in spillbrett: #For løkke som går gjennom alle radene i "spillbrett"
        print(" | ".join(rad)) #Lager en tekststreng mellom hver del av lista (|), deretter skrives det ut
        print("-" * 9) #Printer 9 x - for hver rad. Gjør det mer oversiktlig

while True: #Starter en evig løkke, fortsetter til programmet er ferdig eller brukeren avslutter
    skriv_ut_spillbrett() #Bruker funksjonen ,vil gå i løkke til og legge til elementer til ferdig

    rad = int(input("Velg rad (0, 1 eller 2): ")) #Spør brukeren hvilken rad hen ønsker, definerer som heltall
    kolonne = int(input("Velg kolonne (0, 1 eller 2): ")) #Spør hvilken kolonne, definerer verdi som heltall
    symbol = input("Velg symbol ('x' eller 'o'): ").lower() #Velger mellom x og o. 
    #.lower brukes slik at programmet godtar X og O.   
    if spillbrett[rad][kolonne] != " ": #Dersom bestemt rad/kolonne er opptatt
        print("Dette feltet er allerede tatt! Prøv igjen.") #Printer følgende
        continue #Ber programmet fortsette dersom dette skjer
   
    spillbrett[rad][kolonne] = symbol #Oppdaterer spillbrettet etter valg. 
'''
'''
#Oppgave 4
y = [x**2 for x in range(1, 21)]
print(y)
'''
'''
#Oppgave 5
y = [x**3 for x in range(1, 16)]
print(y)
'''
'''
#Oppgave 7
liste = []
for i in range(20):
    liste.append(i)
print(liste)

for j in range(0, 20, 2):
    liste.remove(j)

print(liste)
'''
'''
#Oppgave 8, fjern 3 fra lista
liste = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
while 3 in liste:
    indeks = liste.index(3)
    liste.pop(indeks)

print(liste)
'''

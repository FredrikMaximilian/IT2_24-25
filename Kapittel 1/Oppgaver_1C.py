'''
#Oppgave 2a lekse
x = -100 #Definerer x som startverdi slik at programmet kan jobbe seg opp derifra

while x <= 100: #Så lenge x er mindre eller lik 100. Skriver lik fordi while løkken ellers ville droppet siste
    print(x, end=' ') #Priter ut x. Skriver "end=' '" for å skrive dem ut nærmere, slik at det er mer oversikt
    x = x + 2 #Gjør sånn at verdien x øker med 2 for hver runde i løkkaD
'''
'''
#Oppgave 2b Lekse
for i in range(73, -75, -2): #Går fra 73 til 75 i steg av 2. Siden 73 er oddetall, så vil alle tallene være det
    print(i, end=' ') # Printer ut i. end=' '  for å gjøre mer oversiktlig
'''
'''
#Oppgave 2c Lekse
import random as r #Importere slik at jeg kan genere tilfeldige verdier
t = 0 #Må definere t 
while t != 6: #Så lenge t er ulik 6, altså stopper løkken ved 6
    t = r.randint(1, 6) #Definerer t som en tilfeldig verdi mellom 1 og 6
    print(t) #Printer ut t, frem til t er 6
'''
'''
#Oppgave 3. Skriv én bokstav av gangen
tekst1 = "Fredrik" #Lager tekstvaribelen "Fredrik"
for i in tekst1: #Lager løkke som skriver ut 1 del av variablen til ferdig
    print(i) #Printer ut denne ene delen
'''
'''
#Oppgave 4 Samme som over, men med # mellom
tekst1 = "Fredrik"
for i in tekst1:
    print(i, end = "#")
'''
'''
#Oppgave 5 Skriv ut tekst med n
x = int(input("Skriv inn antall ganger"))
for i in range(x):
    n = x
print(f'Denne løkka har gjentatt seg {n} ganger')
'''
'''
#Oppgave 10 Kvadrattall under 100
x = 1
while x**2 <= 100:
    print(x**2)
    x = x+1
'''
'''
#Oppgave 12. Kaster terning for å få 12
import random as r
total = 0
c = 0
while total != 12:
    a = r.randint(1, 6)
    b = r.randint(1, 6)
    total = a + b
    c = c+1

print(f'Antall kast er {c}')
print(f'Terningene viser {a} og {b}')
'''
'''
#oppgave 15/16. Summene til 100
total = 0
i = 0
while i < 100:
    total = total + i
    i = i+1
print(total)
'''
'''
#Oppgave 19 Summer antall tall med selvvalgt verdi
a = int(input("Skriv inn hvor mange tall du vil summere: "))

total = 0
i = 0
while i < a:
    tall = int(input("Skriv inn et tall: ")) 
    total += tall  #Kan skrives som total + tall
    i = i + 1 
print("Summen av tallene er:", total)
'''
'''
#Oppgave 20 Sum og gjennomsnitt 1 til 100
sum_tall = 0

for tall in range(1, 101):
    sum_tall = sum_tall + tall  # Legger til tallet i summen

gjennomsnitt = sum_tall / 100

print("Summen av tallene fra 1 til 100 er:", sum_tall)
print("Gjennomsnittet av tallene fra 1 til 100 er:", gjennomsnitt)
'''
'''
#Oppgave 21
sum_tall = 0
for tall in range(50, 76):
    sum_tall = sum_tall + tall

gjennomsnitt = sum_tall/25

print("Summen av tallene fra 50 til 76 er:", sum_tall)
print("Gjennomsnittet av tallene fra 50 til 76 er:", gjennomsnitt)
'''
'''
#Oppgave 22 Gangetabell til 10
for i in range(1, 11):
  for j in range(1, 11):
    print(f"{(i * j):4}", end="")
  print("")
  '''
'''
#Oppgave 23
for i in range(10):
    print("#####")
'''
'''
#oppgave 24
while True:
    maanednr = input("Oppgi nummeret til måneden vi er i ")

    try:
        maanednr = int(maanednr)
        if maanednr < 1 or maanednr > 12:
            print("Du må oppgi et tall mellom 1 og 12.")
        else:
            print(f"Du skrev inn {maanednr}.")
            break
    except ValueError:
        print("Du må oppgi et gyldig tall.")
'''
'''
#Oppgave 25
while True:
    alder = input("Skriv inn alderen din ")
    
    try:
        alder = int(alder)
        if alder < 0:
            print("Du må oppgi et tall over null")
        else:
            print("Du skrev inn alderen din,", alder)
            break
    except ValueError:
        print("Du må oppgi et gyldig tall")
'''
'''
while True:
    snitt = input("Skriv inn et tall")

    try:
        snitt = float(snitt)
        if snitt in (1, 7):
            print("Snitt er lik", int.snitt)
            break
        elif 0 < snitt < 6.5:
            print("Snitt er lik", float(snitt))
        else:
            print("Du må skrive inn et realistisk tall")
    except ValueError:
        print("Du må skrive inn et tall")
'''
'''
#Sluttoppgave 2a
from random import randint
terning = 0
total = 0

while terning != 6:
    terning = randint(1, 6)
    total = total + 1
print(terning)
print(total)
'''
'''
#Sluttoppgave 2c
tekst = "Fredrik"

for bokstav in tekst:
    print(bokstav)
'''
'''
#Sluttoppgave 3a
a = int(input("Skriv inn et heltall"))
total = 0
for i in range(a+1):
    total = total + i
gjennomsnitt = total/a

print(total)
print(gjennomsnitt)
'''

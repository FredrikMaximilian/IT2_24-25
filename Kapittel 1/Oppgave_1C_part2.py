"""
#Oppgave 3
tekst = str(input("Skriv inn et tekst: "))
for i in range(len(tekst)):
    print(tekst[i])
print("")
for i in tekst:
    print(i)
"""
"""
#Oppgave 4, gjør på nytt
tekst = str(input("Skriv inn et tekst: "))
for i in tekst:
    print(i)
"""
"""
#oppgave7
x = 5
while x <= 30:
    print(x)
    x += 1
"""
"""
#Oppgave 10
x = 1
y = 0
while y < 100:
    print(y)
    y = x**2
    x += 1
"""
"""
#Oppgave 12
import random as r
total = 0
forsøk = 0
while total != 12:
    terning1 = r.randint(1, 6)
    terning2 = r.randint(1, 6)
    total = terning1 + terning2
    forsøk += 1
print(forsøk)
"""
"""
#Oppgave 14/15
total = 0
for i in range(1, 11):
    total += i
print(total)
"""
"""
#Oppgave 16
i = 0
total = 0
while i < 10:
    i += 1
    total += i
print(i)
print(total)
"""
"""
n = int(input("Skriv inn et tall: "))
total = (n*(n+1))/2
print(total)
""""""
total = 0
antall = int(input("Skriv antall:"))
for i in range(antall):
    tall = int(input("Skriv tall:"))
    total += tall
print(total)
""""""
#Oppgave 20
total = 0 
bunn = 50
topp = 75
delta = topp-bunn +1
for i in range(bunn, topp+1):
    total += i
    
print(total)
gjennomsnitt = total/delta
print(gjennomsnitt)
"""
"""
#Oppgave 22    
print(f" | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |")
print("____________________________________________")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{(i * j):4}", end="")
    print("")
"""""
"""""
#Oppgave 23
for i in range(3):
    for j in range(5):
        print("#")
"""
"""
#Oppgave 24
while True:
    månedsnummer =input("Skriv inn månedsnummer:")

    månedsnummer = int(månedsnummer)

    if månedsnummer >= 1 and månedsnummer <= 12:
        print(f'Du skrev inn {månedsnummer}')
        break
    else:
        print("Oppgi et tall mellom 1 og 12")
"""
"""
while True:
    alder = input("Skriv inn alderen din:")

    try:
        alder = int(alder)
        if alder >= 0 and alder <= 100:
            print(f'Alderen din er {alder}')
            break
        else:
            print("Du må skrive inn en reel alder")
    except:
        print("Du må skrive inn et tall")
"""""
"""
#Sluttoppgave 2a
for i in range(-100, 101, 2):
    print(i)

a = -100
while a <= 100:
    print(a)
    a = a+2"
""""""
tekst = "Jeg heter fredrik"
for i in tekst:
    print(i)
    """
"""
#Sluttoppgave 3
total = 0
tall = input("Skriv inn et tall")
try:
    tall = int(tall)
except:
    print("Du må skrive et tall")
for i in range(tall+1):
    total += i

gjennomsnitt = total/tall
print(f'Totalen er {total}')
print(f'Gjennomsnittet er {gjennomsnitt}')
"""
"""
total = 0
while True:
    tall = input("Skriv inn et tall: ")
    try:
        tall = int(tall)
    except:
        print("Du må skrive inn et tall")
        continue

    if tall > 10:
        tall_liste = list(range(tall+1))
        minst = min(tall_liste)
        størst = max(tall_liste)
        total = sum(tall_liste)
        gjennomsnitt = total/tall
        print(minst)
        print(størst)
        print(total)
        print(gjennomsnitt)
    else:
        print("Tallet må være over 10")
"""
"""
lengde = int(input("Skriv inn lengde"))
for i in range(lengde):
    print("#" * lengde)"
"""
"""
#Sluttoppgave 5
#Telle bokstaver
tekst = "jeg heter fredrik"
alfabet = "abcdefghijklmnopqrstuvwxyzæøå"

tekst = tekst.lower()

for bokstav in alfabet:
    antall = alfabet.count(bokstav)
    print(f'{bokstav}: {antall}')
"""
"""
#Sluttoppgave 6
tall = 97
while True:
    gjett = input("Gjett: ")
    try:
        gjett = int(gjett)

        if gjett == tall:
            print("Riktig tall")
            break
        elif gjett < tall:
            print("for lavt")
        else:
            print("For høyt")
    except:
        print("Du må skrive inn et tall")
"""

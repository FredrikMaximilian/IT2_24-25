'''
for i in range(10):
  print("hei")
'''
'''
a = int(input("Skriv inn antall"))
for i in range(a):
    print("hei")
'''
"""
while True:
    try:
      a = int(input("Skriv inn antall"))
      if 0<a<10:   
        break
      else:
        print("Tallet må være mellom 1 og 10")
    except ValueError:
      print("Du må skrive inn et heltall")
      
for i in range(a):
  print("hei")
"""
"""
import random as r
b = r.randint(1, 100)
while True:
    try:
        a = int(input("Gjett et tall"))
        if a == b:
            print("Riktig")
            break
        elif a < b:
            print("Tallet er for lavt")
        else:
            print("Tallet er for høyt")
    except ValueError:
        print("Du må skrive et heltall")
"""
'''
#Oppgave 4
t = []
while True: 
    try:
      a = input("Skriv noe: ")
      if a == "q":
        print("Riktig")
        break
      else:
        print("Ikke riktig")
        t.append(int(a))
    except:
      print("Noe gikk galt")
s = sum(t)
gjennomsnitt = (sum(t))/(len(t))
print(f'Summen av verdiene er {s}.')
print(f'Gjennomsnittet er {gjennomsnitt}')
'''
#Oppgave 5
'''
import random as r 
totalsum = 0
delsum = 0
navn = str(input("Skriv inn navnet ditt: "))
valg = str(input("Skriv inn K eller L: ")).strip().upper()
if valg == "K":
  try:
    while totalsum < 100:
      kast = r.randint(1, 6)
      print(kast)
      if kast <= 2:
        delsum = delsum + kast
      else:
        delsum = 0
    else:
      totalsum = totalsum
  except ValueError:
    print("Du må skrive inn K eller L")
print(delsum)
'''
'''
import random as r
totalsum = 0
omganger = 0
navn1 = str(input("Skriv navn til spiller 1"))

while totalsum < 50:
  delsum = 0
  omganger += 1


  while True:
    valg = str(input("Skriv K eller L")).strip().capitalize()
    if valg == "K":
      kast = r.randint(1, 6)
      print("Du kastet", kast)
      if kast >= 2:
        delsum += kast
        print(f'Din delsum er nå oppdatert til {delsum}')
      else:
        delsum = 0
        print("Uheldig, nå mistet du delsummen")
        break
    elif valg == "L":
      totalsum += delsum
      print(f'Du har nå lagret summen din på {totalsum}')
      break
    else:
      print("Nå har du skrevet noe feil")

print(f'Du brukte {omganger} på å vinne')
'''
'''
a = int(input("Skriv inn et tall"))
b = int(input("Skriv inn et tall"))
c = int(input("Skriv inn et tall"))

størst = 0
størst = a

if a < b:
  størst = b
  if b < c:
    størst = c
elif a < c:
  størst = c
else:
  størst = a
print(størst, "er det høyeste tallet.")
'''
'''
#Oppgave 5 kalkulator mellom F og C
a = int(input("Skriv inn temperaturtallet"))
b = str(input("Skriv inn F eller C")).strip().capitalize()

c = 0
if b == "F":
    c = (a-32)*(5/9)
    print(f'{a} grader Fahrenheit er lik {c:.5} grader Celius')
else: 
    c = (9/5)*a+32
    print(f'{a} grader Celsius er lik {c} grader Fahrenheit')
    '''

#Oppgave 3.2a
'''
x = -100
while x < 102:
    print(x)
    x = x+2
'''
''' b
x = 75
while x>-73:
    x = x-2
    print(x)
'''
''' c
import random as r
x = 0
while x != 6:
    x = r.randint(1,6)
    print(x)
'''
''' d
tekst = "Fredrik"
for bokstav in tekst:
    print(bokstav)
'''
#Oppgave 3.3 a
'''
a = int(input("Skriv inn et tall"))
x = 0
sum = 0
for i in range(a):
    x = x + 1
    sum += x
gjennomsnitt = sum/a
print("Summen er lik", sum)
print("Gjennomsnittet er lik", gjennomsnitt)
'''
'''b
a = 0
total = 0
omgang = 0
liste = []

while a < 10:
  a = int(input("Skriv inn et heltall"))
  total = total + a
  omgang = omgang + 1
  liste.append(a)

gjennomsnitt = total/omgang
minst = min(liste)
størst = max(liste)

print(f'Totalen er {total}')
print(f'Gjennomsnittet er {gjennomsnitt:.5}')
print(f'Minsteverdi er {minst}')
print(f'Størsteverdi er {størst}')
'''
''' c
import random as r
kast = 0
n = int(input("Skriv antall terningkast"))
total = 0

for i in range(n):
    kast = r.randint(1, 6)
    print(f'Kastet ble til {kast}')
    total = total + kast

gjennomsnitt = total/n

print(f'Antall kast var {n}')
print(f'Gjennomsnittet var {gjennomsnitt}')
'''
''' d
import random as r
kast = 0
kast2 = 0
n = int(input("Skriv antall terningkast"))
total = 0

for i in range(n):
    kast = r.randint(1, 6)
    kast2 = r.randint(1, 6)
    print(f'Kastet ble til {kast} og {kast2}')
    total = total + kast + kast2

gjennomsnitt = total/n

print(f'Antall dobbelkast var {n}')
print(f'Gjennomsnittet var {gjennomsnitt}')
'''
'''
#Oppgave 3.4
a = int(input("Skriv inn en sidelengde: "))
overside = 0
for i in range(a):
    overside = "#" * a
    print(overside)
'''
#Oppgave 3.5
'''
tekst = str(input("Skriv inn en tekst"))

alfabet = "abcdefghijklmnopqrstuvwxyzæøå"

forekomster = {bokstav: 0 for bokstav in alfabet}

for bokstav in tekst.lower():
    if bokstav in forekomster:
        forekomster[bokstav] += 1

for bokstav, antall in forekomster.items():
    print(f"{bokstav}: {antall}")

vanligste_bokstaver = sorted(forekomster.items(), key=lambda x: x[1], reverse=True)

print("\nVanligste bokstaver:")
for bokstav, antall in vanligste_bokstaver:
    if antall > 0:
        print(f"{bokstav}: {antall}")
'''
#Oppgave 3.6
'''
tall = int(input("Skriv inn tallet som skal gjettes: "))
forsøk = int(input("Skriv inn antall forsøk: "))
for i in range(forsøk):
    a = int(input("Skriv ditt gjett: "))
    if a == tall:
        print("Riktig, du har vunnet")
        break
    elif a < tall:
        print("Ditt gjett er for lavt")
    elif a > tall: 
        print("Tallet ditt er for høyt")
    else: 
      print("Du må skrive et heltall")
else: 
  print("Du har tapt")
'''

#Oppgave 3.7
'''
import random as r
liste = []
partall = []
oddetall = []
for i in range(50):
    tall = r.randint(1, 100)
    liste.append(tall)
    sortert = sorted(liste)
print("Sortert liste er", sortert)

for tall in sortert:
    if tall % 2 == 0:
        partall.append(tall)
    else:
        oddetall.append(tall)

print("Partall er", partall)
print("Oddetall er", oddetall)

omvendt = liste.reverse
print("Omvendt liste er", omvendt)

i = 1
for i in range(25):
    liste.pop(i)
    i = i + 2
print("Annenhver indeks liste er", liste)
'''
#Oppgave 4.3
'''
liste = []
while len(liste) < 10:
  try: 
    a = int(input("Skriv inn et tall: "))
    if a in liste:
        print("Tallet er allerede skrevet")
    else:
        liste.append(a)
  except ValueError:
    print("Du må skrive inn et heltall")
print("Lista ble nå", liste)
'''
#Oppgave 4.4
import random as r
liste = []
i = 0
#n = int(input("Skriv inn antall tall: "))
n = 4
for i in range(n):
    tall = r.randint(1, 100)
    liste.append(tall)
print(liste)

#(q) = n/2
#print(int(q))
'''
if (len(liste))%2 == 0: 
    for i in range(2 - 1):
        liste.pop(i)
        i = i+1
        median = 
print(liste)
''' o
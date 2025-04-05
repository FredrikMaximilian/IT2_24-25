#Oppgave1
"""
while True:
    tall = int(input("Skriv inn et tall: "))
    if tall == 0:
        print("Tallet er 0")
    elif tall < 0:
        print("Tallet er under 0")
    else:
        print("Tallet er over 0")
"""
"""
#Oppgave2
while True:
    tall = int(input("Skriv inn et tall: "))
    if tall < 0:
        if tall >= -9:
            print("Ensifret")
        elif tall >= -99 and tall < -9:
            print("tosifret")
        elif tall >= -999 and tall < -99:
            print("tresifret")
        elif tall >= -9999 and tall < -999:
            print("firesifret")
        else:
            print("Annet")
    if tall > 0:
        if tall <= 9:
            print("Ensifret")
        elif tall > 9 and tall <= 99:
            print("tosifret") 
        elif tall > 99 and tall <= 999:
            print("tresifret") 
        elif tall > 999 and tall <= 9999:
            print("firesifret") 
        else:
            print("annet")
"""
#Oppgave 3
"""
tall = int(input("Skriv inn et tall: "))
if tall <= 100 and tall >= 50:
    print("Tallet er mellom 50 og 100")
else:
    print("Tallet er noe annet")
"""
#Oppgave 5
"""
while True:
    tall = int(input("Skriv inn et tall: "))
    if tall > 0:
        if tall < 100:
            print("Tallet er over 0, men under 100")
        else:
            print("Tallet er over 0, og over 100")
    elif tall == 0:
        print("Tallet er 0")
    else:
        if tall < -100:
            print("Tallet er under 0, og under -100")
        else:
            print("Tallet er under 0, men over -100")
"""
"""
#Oppgave 9
talliste = []
for i in range(5):
    tall = float(input("skriv inn et tall: "))
    talliste.append(tall)
#if all(tall == talliste[0] for i in talliste):
    #print("Alle tallene er like")
#else:
   # print(Tallene er ulike, største tall er max(talliste))
tallike = True
for i in range(len(talliste)):
    if talliste[i] != talliste[0]:
        tallike = False
        break
if tallike == True:
    print("Tallene er like")
else:
    print("Det største tallet er", max(talliste))
"""
"""
#Oppgave 11
a = int(input("Skriv inn et tall: "))
b = int(input("Skriv inn et tall: "))
""" """
if a == 0 and b == 0:
    print("Begge er like 0")
elif a == 0 or b == 0:
    print("én av dem er 0")
else:
    print("Hverken av dem er 0")
    """
"""
if a is not 0 and b is not 0:
    print("h")
else:
    print("os")
"""
"""
#oppgave 13
a = int(input("Skriv inn et tall: "))
if a % 2 == 0:
    print("Tallet er partall")
else:
    print("Tallet er oddetall")
"""
"""
#Oppgave 2 sluttoppgave
tall = int(input("Skriv inn poengsom: "))
a, b, c, d, e, f, = [], [], [], [], [], []
a.append(20)
for i in range(20):
    a.append(i)
    b.append(21+i)
    c.append(41 +i)
    d.append(61+i)
for i in range(10):
    e.append(81+i)
    f.append(91+i)
if tall in a:
    print("Du får karakter 6")
#etcetc, er mer effektivt å bare skrive definisjonen på karakterene som krav i if/elif bestemmeren
"""
"""
#Oppgave 3 sluttoppgave
a = 1
b = 2
if a == 1:
    print("ost")
elif b == 2:
    print("ost")
else:
    print("Tallene er ulike")

tall = 4
if tall > 0:
    print("Tallet positivt")
elif tall % 2== 0:
    print("Tallet er partall")
else:
    print("Tallet er negativt og oddetall")
"""
"""
#Sluttoppgave 4
a = int(input("Skriv inn et tall"))
b = int(input("Skriv inn et tall"))
c = int(input("Skriv inn et tall"))
"""
"""
if a == b == c:
    print("Tallene er like")
else:
    print("Tallene er ulike")
"""
"""
"""
"""
if a % 2 == 0:
        print("Tallet er et partall")
else:
    print("Tallet er oddetall")
"""
"""
if a >= b and a >= c:
    størst = a
if b >= a and b >= c:
    størst = b
else:
    størst = c
print(størst)
"""
#Sluttoppgave 5
tall = float(input("Skriv inn et tall: "))
enhet = input("Skriv inn F eller C: ").capitalize()

if enhet == "F":
    c = (tall-32)*(5/9)
    print(f'Temperaturen i Celsius er {c:.1f}')
elif enhet == "C":
    f = (tall*(9/5))+32
    print(f'Temperaturen i Fahrenheit er {f:.1f}')
else:
    print("Prøv på nytt med F eller C")
     
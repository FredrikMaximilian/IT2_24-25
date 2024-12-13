#Oppgave 1 sjekk om over/under null
#tall = int(input("Skriv inn et tall"))
#if tall == 0:
#    print("Tallet er 0")
#elif tall < 0:
#    print("Tallet er under null")
#else:
#    print("Tallet er over null")


#Oppgave 2 Sjekk antall sifre
'''
tall = int(input("Skriv inn tallet ditt "))
if tall <= 0:
    print("Tallet er under 0")
    exit()

if 0 <= tall <= 9:
    print("Tallet er ensifret")
elif 10 <= tall <= 99:
    print("Tallet er tosifret.")
elif 100 <= tall <= 999:
    print("Tallet er tresifret.")
elif 1000 <= tall <= 9999:
    print("Tallet er firesifret.")
else:
    print("Tallet er mer enn firesifret")
'''
'''
#5 Ser om tall er +/- og deretter om den er over/under 100/-100
tall1 = int(input("Skriv inn tall1"))

if tall1 < 0:
    if tall1 < -100:
        print("Tallet er mindre enn -100")
    else: 
        print("Tallet er mer enn -100")
if tall1 > 0: 
    if tall1 < 100:
        print("Tallet er under 100")
    else:
        print("Tallet er over 100")
'''
'''
#Oppgave 11 Sjekk om variabler = 0
a = int(input("Skriv a")) #int for å gjøre 0 til heltall
b = int(input("Skriv b"))

if a == 0 and b == 0: #Må definere på begge sider
    print("Begge er lik null")
else:
    print("Veriablene er ikke lik 0")
'''
'''
#Oppgave 12 Sjekk om uik fra null
a = int(input("Skriv a")) 
b = int(input("Skriv b"))

if not(a == 0 and b == 0): 
    print("Begge er ikke lik null")
else:
    print("Veriablene er lik 0")
'''
'''
#Oppgave 13 Lag et program som sjekker om et tall er partall
a = int(input("Skriv inn et tall"))

if a%2 == 1:
    print("Ikke et partall")
else:
    print("Partall")
'''
'''
#Blandede oppgaver 4a
a = int(input("Skriv et tall")) #Skiver inn 1 av 3 verdier. Bruker int for å gjøre til heltall
b = int(input("Skriv et tall")) #Skiver inn 1 av 3 verdier. Bruker input for at brukeren kan bestemme 
c = int(input("Skriv et tall")) #Skiver inn 1 av 3 verdier

if a == b == c: #Om a er identisk til b og b er identisk til c
    print("Tallene er like") #Printer tallene er like dersom overfor stemmer
else: 
    print("Tallene er ulike") #Om noe annet stemmer (altså tallene er ikke like) så printer den følgende. 
'''
'''
#Blandede oppgaver 4b
a = int(input("Skriv et heltall")) #Lar brukeren legge til et tall, bruker int for å gjøre til heltall

if (a/2) % 1: #Dersom a/2 har en rest på 1, så vil a være et oddetall
    print("Heltallet er et oddetall") #Skriver følgende
else: #Dersom noe annet er tilfellet, altså det er ingen rest
    print("Heltallet er et partall") #Skriver følgende
'''
'''
#Blandede oppgaver 4C Skriver ut det største av tre tall
a = int(input("Skriv a")) #Skriver inn verdi og gjør om til heltall
minst = a #Definerer verdien minst som senere skal brukes, defineres som a inntil videre

b = int(input("Skriv et b")) #Skriv inn ny verdi og gjør om til heltall
if (b < minst): #Dersom b er mindre enn "minst"
    minst = b #Da defineres b som det minste, om if ikke stemmer, så forblir a minst

c = int(input("Skriv et c")) #Skriv inn ny verdi og gjør om til heltall
if (c < minst): #Om c er mindre enn "minst"
    minst = c #Definer c som "minst", om ikke forblir a/b som minst

print(f"Det minste tallet er {minst}") #Printer ut den verdien som nå er minst. 
'''

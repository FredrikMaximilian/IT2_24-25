#Oppgave 16 Tell antal bokstaver
#sitat = "Hello!"
#Antalltegn = len(sitat)
#print(Antalltegn)


#Oppgave 17 Gjør om til lowercase
#sitat = "HALLO!"
#sitat = sitat.lower()
#print(sitat)


#Oppgave 18 Gjør om teksten
#sitat = "Datamaskiner er ubrukelige. De kan bare gi oss svar."
#print((sitat[0:12] + " kan " + (sitat[40:52])))


#Oppgave 19 Lag variabler med tekst og verdi og få dem til å funke sammen
#fornavn = "Fredrik"
#etternavn = "Steinbach"
#telefonnummer = "41317212"
#print(fornavn, etternavn, "har telefonnummer", str(telefonnummer))


#Oppgave 20 Skriv ut tekst med ""
#print('Han sa "hei"') 


#Bruke input og int for å lage en kalkulator
#tall1 = input("Skriv et heltall ")
#tall1 = int(tall1) # Gjør om variabelen tall1 til et heltall (integer)
#tall2 = input("Skriv et heltall ")
#tall2 = int(tall2) # Gjør om variabelen tall2 til et heltall (integer)
#sum = tall1 + tall2
#print("Summen av tallene er", sum)


#Oppgave 22 Kalkulator for å finne summen av desimaltall
#tall1 = input("Skriv et desimaltall ")
#tall1 = float(tall1)
#tall2 = input("Skriv et til desimaltall ")
#tall2 = float(tall2)
#sum = tall1 + tall2
#print("Summen er", sum)


#Oppgave 23A Kalkulator som gjør liter om til desiliter
#tall1 = input("Skriv mengde i liter ")
#tall1 = float(tall1)
#tall2 = input("Skriv mengde i liter" )
#tall2 = float(tall2)
#sum = tall1 + tall2
#sum = int(sum)
#print("Antall desiliter er ", (sum*10))


#Oppgave 28 Formatering, Bruk fstrings for å skrive ut på spesiel måte
#navn = "Fredrik"
#alder = 17
#print(f"Navn:  {navn:>10}")
#print(f"Alder: {alder:>10}")

#Avslutningsoppgave 2 Beregn volum av en vannflaske til 0.5L
#import math as m
#r = 0.32
#h = 1
#kjegle = m.pi*r*r*(h/3)
#sylinder = m.pi*r*r*h
#kule = (2/3)*m.pi*r**3
#flaske = kjegle+sylinder+kule
#print(f"Volumet er, {flaske:.2f} liter")

#Avslutningsoppgave 3 Velg ut riktig måned
#maander = "JanFebMarAprMaiJunJulAugSepOktNovDes"
#nummer = int(input("Skriv inn månednummer: "))
#start_index = (nummer - 1) * 3  # Beregn startposisjonen for ønsket måned
#slutt_index = start_index + 3  # Sluttposisjon er 3 tegn frem
#print(maander[start_index:slutt_index])  # Hent og print måneden

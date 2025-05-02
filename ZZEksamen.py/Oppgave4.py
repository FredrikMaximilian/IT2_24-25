a = [ #Skriver inn listen
    [10, 15, 16],
    [40, 2, 12],
    [20, 6, 24], 
    [10, 13, 32]
]


talliste = [] #Definerer første talliste
filtrertliste = [] #Definerer en mer filtrert en

for bit in a: #For hver liste i listen a 
    for tall in bit: #for hvert tall i denne listen
        talliste.append(tall) #Legg til dette tallet i tallisten

for tall in talliste: #For hvert tall i tallisten (som nå kun består av tall og ikke lister)
    if tall >= 10 and tall <= 20 and tall%4 == 0: #Filtrerer basert på oppgave
        filtrertliste.append(tall) #Legger til de filtrerte verdiene i filtrertliste

total = 0 #setter total til 0
for tall in filtrertliste: #for hvert tall i filtrertliste
    total += tall #totalen øker for hver verdi av hvert tall

total2 = sum(filtrertliste) #Lagde også denne for å vise at det kan gjøres enklere. Gjør i praksis samme som total
gjennomsnitt = total/len(filtrertliste) #Gjennomsnittet er totalen delt på antall tall i filtrertliste

print(f'Gjennomsnittet av de filtrerte tallene er {int(gjennomsnitt)}')

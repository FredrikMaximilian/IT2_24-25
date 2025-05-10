a = [ #Skriver inn listen
    [10, 15, 16],
    [40, 2, 12],
    [20, 6, 24], 
    [10, 13, 32]
]

def beregnkolonne(d):
    a = [] #Lager 3 lister for hver av kolonnene
    b = []
    c = []
    liste = [] #Lager en liste som skal holde på abc
    gjennomsnittliste = [] #Lager en liste som skal holde på gjennomsnitt til abc

    for kolonne in d: #For hver kolonne i settet
        a.append(kolonne[0]) #Legger til hver av tallene i hver av kolonnene i egen liste
        b.append(kolonne[1])
        c.append(kolonne[2])
    liste.append(a) #Putter de i en felles liste
    liste.append(b)
    liste.append(c)
    for bit in liste: #For hver del (abc) i liste
        total = sum(bit) #Finn total
        gjennomsnitt = total/len(bit) #Dermed gjennomsnitt med lengden av lista
        gjennomsnittliste.append(gjennomsnitt) #Legger til i en liste for lik utskrift som tidligere
    return gjennomsnittliste
print(beregnkolonne(a))






    
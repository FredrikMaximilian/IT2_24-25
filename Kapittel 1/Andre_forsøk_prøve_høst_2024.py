
#oppgave 1a
liten = ["null","en","to","tre","fire","fem","seks","sju","åtte","ni","ti"] 

middels = ["elleve","tolv","tretten","fjorten","femten","seksten","sytten","atten","nitten"] 

stor = ["tjue","tretti","førti","femti","seksti","sytti","åtti","nitti","hundre"] 

storliste = []
i = 0
for j in range(len(stor)-1):
    for i in range(len(liten)-1):
        
        if i == 0:
            tall = stor[j] 
            storliste.append(tall)
        else:
            tall = stor[j]+liten[i] 
            storliste.append(tall)
            
storliste.append("hundre")

print(liten + middels + storliste)

'''
#Oppgave 1B

liten = ["null", "en", "to", "tre", "fire", "fem", "seks", "sju", "åtte", "ni", "ti"] 
middels = ["elleve", "tolv", "tretten", "fjorten", "femten", "seksten", "sytten", "atten", "nitten"] 
stor = ["tjue", "tretti", "førti", "femti", "seksti", "sytti", "åtti", "nitti", "hundre"]

# Oppretter en tom ordbok
tallord = {}

# Legger til tall fra 0 til 10 fra 'liten'
for i in range(len(liten)):
    tallord[liten[i]] = i

# Legger til tall fra 11 til 19 fra 'middels'
for i in range(len(middels)):
    tallord[middels[i]] = 11 + i

# Legger til tallene fra 20 til 99 ved å kombinere 'stor' og 'liten'
for j in range(len(stor)-1):  # Gå gjennom stor, minus "hundre"
    tallord[stor[j]] = (j + 2) * 10  # Legger til 20, 30, 40, osv.
    
    for i in range(1, len(liten)):  # Kombinerer med 'liten' for tallene fra 21 til 29 osv.
        tallord[stor[j] + liten[i]] = (j + 2) * 10 + i

# Legg til 'hundre' som 100
tallord["hundre"] = 100

# Skriver ut ordboken for å bekrefte resultatet
print(tallord)

'''


'''
#Oppgave c
a = (input("Skriv inn et heltall"))
b = (input("Skriv inn et heltall"))
tallord = ["null","en","to","tre","fire","fem","seks","sju","åtte","ni","ti"] 
tallord[a] = int(a)
tallord[b] = int(b)
   
a = int(a)
b = int(b)

#if a != (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, tallord):
#    print("Tallene må være mellom 0 og 10")

print(a*b)
'''





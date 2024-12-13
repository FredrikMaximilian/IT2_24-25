n = int(input("Skriv inn brettstørrelsen: ")) #Lar bruker bestemme størrelse på brettet
spillbrett = [[" " for _ in range(n)] for _ in range(n)] #Oppretter 3x3 spillbrett. 
#Indre listen lager rad med tre tomme strenger, ytre gjentar dette tre ganger for å lage rader. Hence 3x3 
def skriv_ut_spillbrett(): #Lager en funsjon som senere vil skrives ut på en lesbar måte
    for rad in spillbrett: #For løkke som går gjennom alle radene i "spillbrett"
        print(" | ".join(rad)) #Lager en tekststreng mellom hver del av lista (|), deretter skrives det ut
        print("-" * (4*n)) #Printer 9 x - for hver rad. Gjør det mer oversiktlig

while True: #Starter en evig løkke, fortsetter til programmet er ferdig eller brukeren avslutter
    skriv_ut_spillbrett() #Bruker funksjonen ,vil gå i løkke til og legge til elementer til ferdig


    rad = (input("Velg rad: ")) #Spør brukeren hvilken rad hen ønsker, definerer som heltall
    kolonne = (input("Velg kolonne: ")) #Spør hvilken kolonne, definerer verdi som heltall
    symbol = str(input("Velg symbol ('x' eller 'o'): ")).lower() #Velger mellom x og o. 
    #.lower brukes slik at programmet godtar X og O.   
    
    #Skal sjekke for om brukeren skriver inn annet enn x og o
    if symbol != "x" and symbol != "o": 
       print("Du må skrive inn x eller o")
       continue

    while True:
        if rad.isdigit():
            rad = int(rad)
            break
        else:
            print("Skriv gyldig rad-verdi")
            rad = (input("Velg rad: "))
    while True:
        if kolonne.isdigit():
            kolonne = int(kolonne)
            break
        else:
            print("Skriv gyldig kolonne-verdi")
            kolonne = (input("Velg kolonne: "))

    if 0 <= rad <= (n-1): #Sjekker om tall er innenfor brettstørrelse
        rad = rad
    else:
        print(f'Du må skrive tall mellom 0 og {n-1}')
        continue

    if 0 <= kolonne <= (n-1): #Sjekker om tall er innenfor brettstørrelse
        kolonne = kolonne
    else:
        print(f'Du må skrive tall mellom 0 og {n-1}')
        continue

    if spillbrett[rad][kolonne] != " ": #Dersom bestemt rad/kolonne er opptatt
        print("Dette feltet er allerede tatt, prøv igjen.") #Printer følgende
        continue #Ber programmet fortsette dersom dette skjer
   
    spillbrett[rad][kolonne] = symbol #Oppdaterer spillbrettet etter valg. 
#oppgave a


liten = ["null","en","to","tre","fire","fem","seks","sju","åtte","ni","ti"] 

middels = ["elleve","tolv","tretten","fjorten","femten","seksten","sytten","atten","nitten"] 

stor = ["tjue","tretti","førti","femti","seksti","sytti","åtti","nitti","hundre"] 

print(liten + middels)

j = 1
for i in range(10):
    for i in range(10):
        tall = (stor[j])+(liten[i+1]) #Noe som er galt her, usikker på hvordan jeg skal løse det
        print(tall)
    j = j + 1

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

'''
brett = [["_"]*8 for i in range(6)]
for i in brett:
    print(i)
'''
'''
brett = [["_"]*5 for i in range(5)] 
spiller = "X" 
trekkliste = [ [1,1], [2,2], [2,1], [3,1], [1,3], [2,1] ] 
for trekk in trekkliste:
    rad = trekk[0] 
    kolonne = trekk[1] 
    if brett[rad][kolonne] == "_": 
        brett[rad][kolonne] = spiller 
        if spiller == "X": 
            spiller = "O" 
        else: spiller = "X"
'''




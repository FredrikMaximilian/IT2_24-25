import numpy as np #Importerer funksjoner i python
import matplotlib.pyplot as plt

#Betingelser for array
xmin = -10
xmax = 10
antallPunkter = 100
xVerdier = np.linspace(xmin, xmax, antallPunkter) 

deltax = 1E-8#Definerer delta x som 10 opphøyd i -4

def f(x): #Definerer funksjon
    return x**3-8*x**2+4*x-14

def df(x): #Definerer den analytisk deriverte funksjonen
    return 3*x**2-16*x+4

def newtonFWD(a): #Definerer den fremoverderiverte
    return (f(a+deltax)-f(a))/deltax

def newtonSYM(a): #Definerer den symmetrisk deriverte
    return (f(a+deltax)-f(a-deltax))/(2*deltax)

print(f'Originalfunksjonen er: {f(2)}') #Printer de alle ut med x verdien satt til 2
print(f'Analytisk derivert er: {df(2)}')
print(f'Den numerisk deriverte med Newtons kvotient er: {newtonFWD(2)}')
print(f'Den numerisk deriverte med Newtons symmetriske kvotient er: {newtonSYM(2)}')
print()

yORG = f(xVerdier)
yANA = df(xVerdier)
yFWD = newtonFWD(xVerdier)
ySYM = newtonSYM(xVerdier)

#plt.plot(xVerdier, yORG, label = "Opprinnelig funksjon")
plt.plot(xVerdier, yANA, label = "Analytisk derivert")
#plt.plot(xVerdier, yFWD, label = "Fremoverderivert")
plt.plot(xVerdier, ySYM, label = "Symmetrisk derivert")

plt.legend()
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
dxTekst = str(deltax)
plt.title("Plot med dx = " + dxTekst)
plt.axhline(y = 0, color = "k")
plt.axvline(x = 0, color = "k")
plt.show()

diffAF = yANA - yFWD #Lager ny liste som er differansen mellom analytisk og fremoverderivert
diffAS = yANA - ySYM #Lager ny liste som er differansen mellom analytisk og symmetrisk derivert
feilAF = 0 #Setter avviket som 0 til å starte med
feilAS = 0 #Setter avviket som 0 til å starte med

for i in range(len(diffAF)): #For in range løkke som løper likt antall ganger som lengen i lista
    feilAF = feilAF + (abs(diffAF[i])) #Summerer opp differansen fra startsum 0
    feilAS = feilAS + (abs(diffAS[i]))

print(f'For delta-x lik {deltax}:')
print(f'Totalavviket mellom analytisk og fremoverderivert metode er {feilAF}')
print(f'Totalavviket mellom analytisk og symmertrisk derivert er {feilAS}')
print()

#Halveringsmetode for å finne første stasjonære punkt
a = -10
b = 10
nøyaktighet = 0.0001
m = (a + b)/2
while abs(newtonFWD(m)) >= nøyaktighet:
    if newtonFWD(a)*newtonFWD(m) < 0:
        b = m
    else: 
        a = m
    m = (a + b)/2
print(f'Det første stasjonære punktet er {m, f(m)}')

#Halveringsmetode for å finne andre stasjonære punkt
a2 = 3
b2 = 10
nøyaktighet2 = 0.0001
m2 = (a2 + b2)/2
while abs(newtonFWD(m2)) >= nøyaktighet2:
    if newtonFWD(a2)*newtonFWD(m2) < 0:
        b2 = m2
    else: 
        a2 = m2
    m2 = (a2 + b2)/2
print(f'Det andre stasjonære punktet er {m2, f(m2)}')
print()

def ddf(x): 
    return 6*x - 16

print(f"Den andrederiverte i det første stasjonære punktet (x = {m}): {ddf(m)}")
print(f"Den andrederiverte i det andre stasjonære punktet (x = {m2}): {ddf(m2)}")

if ddf(m) > 0:
    print("Det første stasjonære punktet er et bunnpunkt.")
elif ddf(m) < 0:
    print("Det første stasjonære punktet er et toppunkt.")
else:
    print("Det første stasjonære punktet er et terrassepunkt")

if ddf(m2) > 0:
    print("Det andre stasjonære punktet er et bunnpunkt.")
elif ddf(m2) < 0:
    print("Det andre stasjonære punktet er et toppunkt.")
else:
    print("Det første stasjonære punktet er et terrassepunkt")
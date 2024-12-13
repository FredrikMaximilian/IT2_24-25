import numpy as np #Importerer funksjoner i python
import matplotlib.pyplot as plt
import math as m

#Betingelser for array
xmin = -10
xmax = 10
antallPunkter = 100
xVerdier = np.linspace(xmin, xmax, antallPunkter) 

deltax = 1E-8#Definerer delta x som 10 opphøyd i -4

def f(x): #Definerer funksjon
    return x**2+x+1

#def df(x): #Definerer den analytisk deriverte funksjonen
#    return 3*x**2-16*x+4

def newtonFWD(a): #Definerer den fremoverderiverte
    return (f(a+deltax)-f(a))/deltax

def newtonSYM(a): #Definerer den symmetrisk deriverte
    return (f(a+deltax)-f(a-deltax))/(2*deltax)

print(f'Originalfunksjonen er: {f(1)}') #Printer de alle ut med x verdien satt til 2
#print(f'Analytisk derivert er: {df(2)}')
print(f'Den numerisk deriverte med Newtons kvotient er: {newtonFWD(1)}')
print(f'Den numerisk deriverte med Newtons symmetriske kvotient er: {newtonSYM(1)}')
print()

yORG = f(xVerdier)
#yANA = df(xVerdier)
yFWD = newtonFWD(xVerdier)
ySYM = newtonSYM(xVerdier)

plt.plot(xVerdier, yORG, label = "Opprinnelig funksjon")
#plt.plot(xVerdier, yANA, label = "Analytisk derivert")
plt.plot(xVerdier, yFWD, label = "Fremoverderivert")
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
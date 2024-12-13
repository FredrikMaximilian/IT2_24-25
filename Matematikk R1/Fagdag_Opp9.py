import numpy as np #Importerer funksjoner i python
import matplotlib.pyplot as plt


#Betingelser for array
xmin = -10
xmax = 10
antallPunkter = 100
xVerdier = np.linspace(xmin, xmax, antallPunkter) 

deltax = 1E-8#Definerer delta x som 10 opphøyd i -4

a = 1
b = 3
c = -1

def f(x): #Definerer funksjon
    return (a*(x**2))+(b*x)+c

def newtonSYM(a): #Definerer den symmetrisk deriverte
    return (f(a+deltax)-f(a-deltax))/(2*deltax)

print(f'Originalfunksjonen er: {f(2)}') #Printer de alle ut med x verdien satt til 2
print(f'Den numerisk deriverte med Newtons symmetriske kvotient er: {newtonSYM(2)}')
print()

yORG = f(xVerdier)
ySYM = newtonSYM(xVerdier)

plt.plot(xVerdier, yORG, label = "Opprinnelig funksjon")
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

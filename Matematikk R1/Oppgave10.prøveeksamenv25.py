import math #Importerer mattebibloteket

def f(x): #Definerer f(x)
    return (math.e)**(2*x)

dx = 0.0001 #Definerer delta x
a = -4 #Definerer x-verdien

derivert = (f(a + dx)-f(a))/dx #Definerer fremoverderivert-funksjon
symmetrisk = (f(a+dx) - f(a-dx))/(2*dx) #Definerer newtons-symmetriske-kvotient-funksjon

print(f'Den fremoverderiverte er lik {derivert}') #Printer ut fremoverderivert med desimaler
print(f'Med newtons symmetriske kvotient er den deriverte lik {symmetrisk}') #Printer ut symmetrisk kvotient med desimaler
print() #Printer mellomrom
print(f'En tilnærmingsverdi blir henholdsvis {derivert:.3f} og {symmetrisk:.3f}') #Printer tilnærmingsverdier
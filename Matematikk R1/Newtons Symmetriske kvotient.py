import math # Importerer sqrt funksjonen fra math biblioteket

def f(x):  # Definerer funksjonen vi vil derivere
    return (math.e)**(2*x) # Returnerer funksjonsverdien

def numerisk_derivert(a, delta_x):  # Definerer funksjonen for numerisk derivasjon
    return (f(a + delta_x) - f(a - delta_x)) / (2*delta_x)  # Beregner den numeriske deriverte

def eksakt_derivert(x):  # Definerer funksjonen for eksakt derivasjon
    return 2*(math.e)**(2*x)  # Returnerer den eksakte deriverte

print("f’(2) =", numerisk_derivert(2, 1E-8))  # Skriver ut den numeriske deriverte for x=2 med delta_x=1E-8
print(eksakt_derivert(2))  # Skriver ut den eksakte deriverte for x=2
print((eksakt_derivert(2)) - (numerisk_derivert(2, 1E-8)))  # Skriver ut differansen mellom eksakt og numerisk deriverte for x=2

for i in range(1, 17):  # Løkke som går fra 1 til 16
    print("f’(2) =", numerisk_derivert(3, 10**(-i)))  # Skriver ut den numeriske deriverte for x=2 med forskjellige delta_x verdier
from pylab import *
import math as m

def f(x):
  return m.e**(2*x)

x = linspace(-5, 7, 1000)
y = f(x)

plot(x, y, color = "b")
ylim(-20, 40)
axhline(y = 0, color = "k")
axvline(x = 0, color = "k")
xlabel("x")
ylabel("y")
grid()
show()

x1 = float(input("Skriv inn en x-verdi nær nullpunktet: "))
delta_x = 0.00001

def f_derivert(a):
  return (f(a + delta_x) - f(a)) / delta_x

def ny_x_verdi(x1):
  return x1 - (f(x1) / f_derivert(x1))

for i in range(10):
  x2 = ny_x_verdi(x1)
  #print("Et bedre forslag er gitt ved x =", round(x2, 4))
  x1 = x2

print("Med x =", x1, " er f(x) =", f(x1))

flyttall_løsning = x1

# Finn det største heltallet x0 som oppfyller ulikheten
x0 = int(flyttall_løsning)  # Konverter løsningen til heltall
while f(x0) >= 0:  # Sørg for at ulikheten er oppfylt
    x0 -= 1  # Gå bakover til ulikheten er sann

#Må legge inn ulikheten i funksjonen for å finne dette
print("Det største heltallet x0 slik at e^x0 + 2*x0 < 100 er:", x0)

def stigningstall_nullpunkt(f, x):
    return f_derivert(x)

print("Stigningstallet til nullpunktet er:", stigningstall_nullpunkt(f, x1))

'''
from pylab import *

delta_x = 1E-8

def f(x):
    return x**2 + 2*x

def derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x

x_verdier = linspace(- 5, 5, 100)
y_verdier = f(x_verdier)
dy_verdier = derivert(x_verdier)

plot(x_verdier, y_verdier)
plot(x_verdier, dy_verdier)
show()
'''
from math import sqrt
def f(x):	 	 	 	 	 	 # funksjonen vi vil derivere
 	 return x**3 + 2*x - 7

def numerisk_derivert(a, delta_x):  		 # numerisk derivasjon i a
    return (f(a + delta_x) - f(a - delta_x)) / (2*delta_x)

def eksakt_derivert(x):
       return 3*x**2+2


print("f’(2) =", numerisk_derivert(2, 1E-8))
print(eksakt_derivert(2))
print((eksakt_derivert(2))-(numerisk_derivert(2, 1E-8)))
'''
for i in range(1, 17):
   print("f’(2) =", derivert(2, 10**(-i)))
'''
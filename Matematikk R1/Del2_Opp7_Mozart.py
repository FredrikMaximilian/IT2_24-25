from math import sqrt

def f(x):
    return sqrt(3-x)

def areal(x):
    return (f(x))*(x)

delta_x = 1E-8

def der_areal(x):
    return (areal(x+delta_x)-areal(x))/delta_x 

x = 0
h = 0.01
while der_areal(x+h) > 0: 
    x = x + h

print(areal(x))
print(der_areal(x))
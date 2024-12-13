import math as matte

a = 0
b = 1
noyaktighet = 0.001

def f(x):
 return 5*matte.log(x**3 + 2) - 6

m = (a + b)/2

while abs(f(m)) >= noyaktighet:
    if f(a)*f(m) < 0:
     b = m
    else: 
     a = m

    m=(a+b)/2

print("Løsningen på likningen er tilnærmet lik", round(m, 4))
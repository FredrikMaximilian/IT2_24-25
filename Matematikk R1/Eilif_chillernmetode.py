def f(x):
    return x**3 - 2*x
 
dx = 1E-4
 
def symmetrisk_derivert(x):
    return (f(x+dx) - f(x-dx))/(2*dx)
 
def fremover_derivert(x):
    return (f(x+dx) - f(x))/dx
 
def bunnpunkt(f, x_start):
    while f(x_start) > f(x_start+dx):
        x_start += dx
    return print(f'Vi fant et bunnpunkt i x = {x_start:.2f}, her er f(x) = {f(x_start):.2f}.')
 
def toppunkt(f, x_start):
    while f(x_start) < f(x_start+dx):
        x_start += dx
    return print(f'Vi fant et toppunkt i x = {x_start:.2f}, her er f(x) = {f(x_start):.2f}.')
 
def deriverbarhet(x):
    if round(symmetrisk_derivert(x-dx), 3) == round(symmetrisk_derivert(x+dx), 3):
        return print(f'Funksjonen er deriverbar i x = {x}.')
    else:
        return print(f'Funksjonen er ikke deriverbar i x = {x}, fordi f({x}-dx) != f({x}+dx).')
 
def deriverbarhet_metode_2(x):
    if round(fremover_derivert(x-dx), 3) == round(fremover_derivert(x+dx), 3):
        return print(f'Funksjonen er deriverbar i x = {x}.')
    else:
        return print(f'Funksjonen er ikke deriverbar i x = {x}, fordi f({x}-dx) != f({x}+dx).')
 
bunnpunkt(f, 0)
 
 
def newtons_metode(f, f_derivert, x0, toleranse=1E-6, maks_iterasjoner=1000):
    x = x0
    for i in range(maks_iterasjoner):
        fx = f(x)
        fpx = f_derivert(x)
        if fpx == 0:
            print("Derivert er null, kan ikke fortsette.")
            return None
        x_ny = x - fx / fpx
        if abs(x_ny - x) < toleranse:
            return x_ny
        x = x_ny
    print("Maksimalt antall iterasjoner nådd.")
    return None
 
# Eksempel på bruk
def f_derivert(x):
    return 3*x**2 - 2
 
x_start = 1  # Startverdi for Newtons metode
nullpunkt = newtons_metode(f, f_derivert, x_start)
 
if nullpunkt is not None:
    print(f'En løsning er {nullpunkt:.4f}')
else:
    print('Fant ingen løsning.')
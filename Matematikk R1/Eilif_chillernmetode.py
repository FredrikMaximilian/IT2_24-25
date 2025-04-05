def f(x): 
    return x**3 - 2*x  # Definerer funksjonen f(x)

dx = 1E-4  # Setter en liten verdi for dx

def symmetrisk_derivert(x):
    return (f(x+dx) - f(x-dx))/(2*dx)  # Beregner symmetrisk derivert

def fremover_derivert(x):
    return (f(x+dx) - f(x))/dx  # Beregner fremoverderivert

def bunnpunkt(f, x_start):
    while f(x_start) > f(x_start+dx):  # Sjekker om funksjonsverdien synker
        x_start += dx  # Øker x_start med dx
    return print(f'Vi fant et bunnpunkt i x = {x_start:.2f}, her er f(x) = {f(x_start):.2f}.')  # Skriver ut bunnpunkt

def toppunkt(f, x_start):
    while f(x_start) < f(x_start+dx):  # Sjekker om funksjonsverdien øker
        x_start += dx  # Øker x_start med dx
    return print(f'Vi fant et toppunkt i x = {x_start:.2f}, her er f(x) = {f(x_start):.2f}.')  # Skriver ut toppunkt

def deriverbarhet(x):
    if round(symmetrisk_derivert(x-dx), 3) == round(symmetrisk_derivert(x+dx), 3):  # Sjekker om funksjonen er deriverbar
        return print(f'Funksjonen er deriverbar i x = {x}.')  # Skriver ut at funksjonen er deriverbar
    else:
        return print(f'Funksjonen er ikke deriverbar i x = {x}, fordi f({x}-dx) != f({x}+dx).')  # Skriver ut at funksjonen ikke er deriverbar

def deriverbarhet_metode_2(x):
    if round(fremover_derivert(x-dx), 3) == round(fremover_derivert(x+dx), 3):  # Sjekker om funksjonen er deriverbar med fremoverderivert
        return print(f'Funksjonen er deriverbar i x = {x}.')  # Skriver ut at funksjonen er deriverbar
    else:
        return print(f'Funksjonen er ikke deriverbar i x = {x}, fordi f({x}-dx) != f({x}+dx).')  # Skriver ut at funksjonen ikke er deriverbar

bunnpunkt(f, 0)  # Kaller funksjonen bunnpunkt med startverdi 0

def newtons_metode(f, f_derivert, x0, toleranse=1E-6, maks_iterasjoner=1000):
    x = x0  # Setter startverdi for x
    for i in range(maks_iterasjoner):  # Løkke for maks iterasjoner
        fx = f(x)  # Beregner funksjonsverdien
        fpx = f_derivert(x)  # Beregner den deriverte
        if fpx == 0:  # Sjekker om den deriverte er null
            print("Derivert er null, kan ikke fortsette.")  # Skriver ut feilmelding
            return None  # Returnerer None
        x_ny = x - fx / fpx  # Beregner ny x-verdi
        if abs(x_ny - x) < toleranse:  # Sjekker om forskjellen er mindre enn toleransen
            return x_ny  # Returnerer nullpunktet
        x = x_ny  # Oppdaterer x
    print("Maksimalt antall iterasjoner nådd.")  # Skriver ut feilmelding
    return None  # Returnerer None

def f_derivert(x):
    return 3*x**2 - 2  # Definerer den deriverte av funksjonen f(x)

x_start = 1  # Startverdi for Newtons metode
nullpunkt = newtons_metode(f, f_derivert, x_start)  # Kaller Newtons metode

if nullpunkt is not None:
    print(f'En løsning er {nullpunkt:.4f}')  # Skriver ut løsningen
else:
    print('Fant ingen løsning.')  # Skriver ut feilmelding
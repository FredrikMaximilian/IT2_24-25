def f(x): 
    return x**2+2*x-1  # Definerer funksjonen f(x)

dx = 1E-4  # Setter en liten verdi for dx


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
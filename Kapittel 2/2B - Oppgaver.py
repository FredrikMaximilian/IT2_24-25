"""
fahrenheit = float(input("Oppgi antall grader Fahrenheit: "))

if fahrenheit < -459.67:
    print("Temperaturen kan ikke være lavere enn det absolutte nullpunkt (-459.67°F).")
else:
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} grader Fahrenheit tilsvarer {celsius:.2f} grader Celsius.")
"""

def areal(lengde, bredde):
    if isinstance(lengde, str) or isinstance(bredde, str):
        return(-1)
    elif lengde <= 0 or bredde <= 0:
        return (-1)
    return lengde * bredde

# Liste over testverdier (lengde, bredde, forventet resultat)
testdata = [
    (4, 5, 20),       # gyldig
    (0, 5, -1),       # ugyldig: lengde er 0
    (-3, 2, -1),      # ugyldig: negativ lengde
    (3, "5", -1),     # ugyldig: bredde er en streng
    ("3", 5, -1),     # ugyldig: lengde er en streng
    (3.5, 2, 7.0),    # gyldig: flyttall
    ("lø", 2, -1),    # ugyldig: lengde er None
    (2, "os", -1),    # ugyldig: bredde er None
]

for i, (l, b, forventet) in enumerate(testdata, start=1):
    resultat = areal(l, b)
    print(f"Test {i}: areal({l}, {b}) = {resultat} → {'OK' if resultat == forventet else 'FEIL'}")

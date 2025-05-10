class DagsInfo:
    def __init__(self, ukedag, nedbør):
        self._ukedag = ukedag
        self.set_nedbør(nedbør)

    def get_ukedag(self):
        return self._ukedag

    def get_nedbør(self):
        return self._nedbør

    def set_nedbør(self, mm):
        if mm < 0:
            raise ValueError("Nedbør kan ikke være negativ.")
        self._nedbør = mm


class NedbørRegister:
    def __init__(self):
        self._dager = []
        self._ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]

    def registrer(self, mm):
        # Feilhåndtering
        if not isinstance(mm, (int, float)):
            raise TypeError("Nedbør må være et tall.")

        ukedag = self._ukedager[len(self._dager) % 7]
        dagsinfo = DagsInfo(ukedag, mm)
        self._dager.append(dagsinfo)

    def get_dager(self):
        return self._dager

    def total_nedbør(self):
        return sum(dag.get_nedbør() for dag in self._dager)

register = NedbørRegister()

# Eksempeldata (fra mandag og utover)
verdier = [12.3, 0.0, 5.5, 18.9, 7.2, 0.0, 3.1, 6.4]

for mm in verdier:
    register.registrer(mm)

# Skriv ut dag for dag
for dag in register.get_dager():
    print(f"{dag.get_ukedag()}: {dag.get_nedbør()} mm")

print(f"\nTotal nedbør: {register.total_nedbør()} mm")

"""
def test_nedbør_register():
    print("Starter test...")

    register = NedbørRegister()

    try:
        register.registrer(10.5)
        register.registrer(5.2)
        register.registrer(-3)  # Feil 1: Negativ verdi
    except ValueError as ve:
        print(f"FEIL OPPDAGET: {ve}")

    try:
        register.registrer("mye regn")  # Feil 2: Feil datatype
    except TypeError as te:
        print(f"FEIL OPPDAGET: {te}")

    # Normal registrering
    register.registrer(15)

    # Vis registrerte dager
    for dag in register.get_dager():
        print(f"{dag.get_ukedag()}: {dag.get_nedbør()} mm")

    # Vis total nedbør
    print(f"Total nedbør: {register.total_nedbør()} mm")

test_nedbør_register()


def set_nedbør(self, mm):
    if mm < 0:
        # Håndterer negativ verdi – kaster feil
        raise ValueError("Nedbør kan ikke være negativ.")

def registrer(self, mm):
    if not isinstance(mm, (int, float)):
        # Håndterer feil datatype – kaster feil
        raise TypeError("Nedbør må være et tall.")
"""
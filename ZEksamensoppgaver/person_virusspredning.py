import random


class Person:
    FRISK_UTEN_IMMUNITET = "frisk_uten_immunitet"
    SMITTET = "smittet"
    SYK = "syk"
    DOD = "dod"
    FRISK_MED_IMMUNITET = "frisk_med_immunitet"

    def __init__(self):
        self.tilstand = Person.FRISK_UTEN_IMMUNITET
        self.dager_smittet = 0
        self.dager_syk = 0

    def smitt(self):
        if self.tilstand == Person.FRISK_UTEN_IMMUNITET:
            self.tilstand = Person.SMITTET
            self.dager_smittet = 0

    def er_smittbar(self):
        return self.tilstand in [Person.SMITTET, Person.SYK]

    def kan_smittes(self):
        return self.tilstand == Person.FRISK_UTEN_IMMUNITET

    def er_i_live(self):
        return self.tilstand != Person.DOD
    
    def oppdater(self):
        if self.tilstand == Person.SMITTET:
            self.dager_smittet += 1
            if self.dager_smittet >= 3:
                self.tilstand = Person.SYK
                self.dager_syk = 0
        elif self.tilstand == Person.SYK:
            self.dager_syk += 1
            if random.random() < 0.01:
                self.tilstand = Person.DOD
            elif self.dager_syk >= 4:
                self.tilstand = Person.FRISK_MED_IMMUNITET



"""
antall_forsok = 10000
dodsfall = 0
for _ in range(antall_forsok):
    if rd.random() < 0.01:
        dodsfall += 1
print(f"Døde: {dodsfall} av {antall_forsok} ({(dodsfall / antall_forsok) * 100:.2f}%)")
"""

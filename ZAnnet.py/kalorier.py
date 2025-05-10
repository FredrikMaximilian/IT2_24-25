from datetime import datetime

class Maltid:
    def __init__(self, ukedag, type: str, kalorier: int, sunt: bool):
        self._ukedag = ukedag
        self.set_type(type)
        self.set_kalorier(kalorier)
        self.set_sunt(sunt)

    def get_ukedag(self):
        return self._ukedag
    
    def get_type(self):
        return self._type
    
    def get_kalorier(self):
        return self._kalorier
    
    def get_sunt(self):
        return self._sunt

    def set_type(self, maltidnavn):
        if isinstance(maltidnavn, (int, float)) or not maltidnavn:
            raise ValueError("Maltidnavn ma være en streng")
        self._type = maltidnavn

    def set_kalorier(self, kcal):
        if kcal < 0:
            raise ValueError("Kalorier kan ikke være negativt")
        self._kalorier = kcal

    def set_sunt(self, verdi):
        if not isinstance(verdi, bool):
            raise TypeError("Sunnhetsverdi må være True eller False")
        self._sunt = verdi


class Kaloridagbok:
    def __init__(self):
        self._maltid = []
        self._ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]

    def registrer_maltid(self, maltidsnavn, kcal, verdi):
        ukedag = self._ukedager[len(self._maltid) % 7]
        maltidinfo = Maltid(ukedag, maltidsnavn, kcal, verdi)
        self._maltid.append(maltidinfo)

    '''
    def registrer_3_maltider(self, maltidsnavn, kcal, verdi):
        # Finn hvor mange fulle dager som er registrert
        dagnummer = len(self._maltider) // 3  # én dag = 3 måltider
        ukedag = self._ukedager[dagnummer % 7]
        maltidinfo = Maltid(ukedag, maltidsnavn, kcal, verdi)
        self._maltider.append(maltidinfo)'''

    def total_kalorier(self):
        return sum(maltidsinfo.get_kalorier() for maltidsinfo in self._maltid)

    def snitt_kalorier(self):
        if not self._maltid:
            return 0
        return sum(maltidsinfo.get_kalorier() for maltidsinfo in self._maltid) / len(self._maltid)

    def antall_sunne_dager(self):
        return sum(1 for m in self._maltid if m.get_sunt())

    def mest_kalorier_dag(self):
        if not self._maltid:
            return None
        mest = max(self._maltid, key = lambda o: o.get_kalorier())
        return mest.get_ukedag()
    
    def skriv_ukeplan(self):
        for i, m in enumerate(self._maltider):
            print(f"{m.get_ukedag()} – {m.get_type()} ({m.get_kalorier()} kcal), sunt: {m.get_sunt()}")

# === Testprogram for Kaloridagbok ===

dagbok = Kaloridagbok()

# ✅ 1. Registrer 5 gyldige måltider
dagbok.registrer_maltid("Frokost", 350, True)
dagbok.registrer_maltid("Lunsj", 600, True)
dagbok.registrer_maltid("Middag", 900, False)
dagbok.registrer_maltid("Kveldsmat", 400, True)
dagbok.registrer_maltid("Snacks", 250, False)

#Tre måltider daglig
"""
dagbok.registrer_3_maltider("Frokost", 350, True)
dagbok.registrer_3_maltider("Lunsj", 600, True)
dagbok.registrer_3_maltider("Middag", 800, False)
dagbok.registrer_3_maltider("Frokost", 300, True)
dagbok.registrer_3_maltider("Lunsj", 650, False)
dagbok.registrer_3_maltider("Middag", 700, True)
dagbok.registrer_3_maltider("Kveldsmat", 200, True)
"""

# ✅ 2. Vis alle registrerte måltider
print("\n📘 Registrerte måltider:")
for m in dagbok._maltid:
    print(f"{m.get_ukedag()}: {m.get_type()} – {m.get_kalorier()} kcal, sunt: {m.get_sunt()}")

# ✅ 3. Total og snitt kalorier
print(f"\n🔥 Total kalorier: {dagbok.total_kalorier()} kcal")
print(f"📊 Snitt per dag: {dagbok.snitt_kalorier():.1f} kcal")

# ✅ 4. Antall sunne dager
print(f"✅ Antall sunne måltider: {dagbok.antall_sunne_dager()}")

# ✅ 5. Dag med mest kalorier
print(f"🏆 Dag med mest kalorier: {dagbok.mest_kalorier_dag()}")

# ❌ 6. Feil: negativt kaloriinntak
try:
    dagbok.registrer_maltid("Feilmat", -200, True)
except ValueError as e:
    print(f"\n❗ FEIL: {e}")

# ❌ 7. Feil: ugyldig type for 'sunt'
try:
    dagbok.registrer_maltid("Tekstilmat", 300, "ja")
except TypeError as e:
    print(f"❗ FEIL: {e}")
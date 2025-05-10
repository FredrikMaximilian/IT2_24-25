from datetime import datetime

class Entur:
    def __init__(self, dato, avstand: float, hoydemeter: int):
        self._dato = dato
        self.set_avstand(avstand)
        self.set_hoydemeter(hoydemeter)

    def get_dato(self):
        return self._dato
    
    def get_avstand(self):
        return self._avstand
    
    def get_hoydemeter(self):
        return self._hoydemeter
    
    def set_avstand(self, km):
        if km < 0:
            raise ValueError("Avstand kan ikke være negativ")
        self._avstand = km

    def set_hoydemeter(self, hm):
        if hm < 0:
            raise ValueError("Høydemeter kan ikke være negativt")
        self._hoydemeter = hm

class Dagbok:
    def __init__(self):
        self._turer = []

    def registrer(self, km, hm):
        dato = datetime.now().strftime("%Y-%m-%d")
        tur = Entur(dato, km, hm)
        self._turer.append(tur)

    def total_km(self):
        return sum(tur.get_avstand() for tur in self._turer)

    def snitt_hoydemeter(self):
        if not self._turer:
            return 0
        return sum(tur.get_hoydemeter() for tur in self._turer) / len(self._turer)

    def antall_turer(self):
        return len(self._turer)

# === Testprogram ===
dagbok = Dagbok()

# ✅ 1. Registrer tre gyldige turer
dagbok.registrer(7.5, 300)
dagbok.registrer(12.0, 450)
dagbok.registrer(9.2, 200)

# ✅ 2. Skriv ut resultater
print("Totalt antall km:", dagbok.total_km())
print("Snitt høydemeter per tur:", dagbok.snitt_hoydemeter())
print("Antall turer registrert:", dagbok.antall_turer())

# ❌ 3. Eksempel på FEIL – negativ km
try:
    dagbok.registrer(-5.0, 200)
except ValueError as e:
    print("FEIL:", e)

# ❌ 4. Eksempel på FEIL – negativ høydemeter
try:
    dagbok.registrer(6.0, -100)
except ValueError as e:
    print("FEIL:", e)

# ⚠️ 5. Eksempel på UNNTAK – ugyldig datoformat (manuelt)
try:
    tur = Entur("32-2024-04", 10.0, 200)  # gal dato
except Exception as e:
    print("UNNTAK:", e)
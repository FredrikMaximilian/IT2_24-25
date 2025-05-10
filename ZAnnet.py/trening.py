class Okt:
    def __init__(self, ukedag, okttype: str, intensitet: int, varighet: float):
        self._ukedag = ukedag
        self.set_okttype(okttype)
        self.set_intensitet(intensitet)
        self.set_varighet(varighet)

    def get_ukedag(self):
        return self._ukedag

    def get_okttype(self):
        return self._okttype

    def get_intensitet(self):
        return self._intensitet

    def get_varighet(self):
        return self._varighet
    
    def set_okttype(self, oktnavn):
        if isinstance(oktnavn, (int, float)) or not oktnavn:
            raise ValueError("Øktnavn må være en streng")
        self._okttype = oktnavn
    
    def set_intensitet(self, intensitetmengde):
        if intensitetmengde < 0 or intensitetmengde > 10:
            raise ValueError("Intensitetsmengden må være mellom 0 og 10")
        self._intensitet = intensitetmengde

    def set_varighet(self, tid):
        if tid < 0:
            raise ValueError("Tiden må være over 0")
        self._varighet = tid


class Treningsplan:
    def __init__(self):
        self._okter = []
        self._ukedager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]

    def legg_til_okt(self, oktnavn, intensitetsmengde, tid):
        ukedag = self._ukedager[len(self._okter) % 7]
        oktinfo = Okt(ukedag, oktnavn, intensitetsmengde, tid)
        self._okter.append(oktinfo)


    def total_tid(self):
        return sum(oktinfo.get_varighet() for oktinfo in self._okter)
    
    def tyngste_dag(self):
        if not self._okter:
            return None
        tyngst = max(self._okter, key=lambda o: o.get_intensitet())
        return tyngst.get_ukedag()
    
    def plan_for_uke(self):
        plan = []
        for o in self._okter:
            tekst = f"{o.get_ukedag()}: {o.get_okttype()} - intensitet {o.get_intensitet()}/10, {o.get_varighet()} min"
            plan.append(tekst)
        return plan

# === Testprogram for Treningsplan ===

plan = Treningsplan()

# ✅ 1. Registrer 5 økter
plan.legg_til_okt("Løping", 7, 45)
plan.legg_til_okt("Styrke", 9, 60)
plan.legg_til_okt("Yoga", 4, 30)
plan.legg_til_okt("Klatring", 8, 50)
plan.legg_til_okt("Hvile med tøying", 2, 20)

# ✅ 2. Vis hele planen dag for dag
print("\n📆 Plan for uka:")
for linje in plan.plan_for_uke():
    print(linje)

# ✅ 3. Skriv ut total treningstid
print(f"\n⏱️ Total treningstid: {plan.total_tid()} minutter")

# ✅ 4. Vis hvilken dag som hadde høyest intensitet
print(f"🔥 Tyngste dag: {plan.tyngste_dag()}")

# ❌ 5. Test på feil: negativ varighet
try:
    plan.legg_til_okt("Feiløkt", 5, -30)
except ValueError as e:
    print(f"\n❗ FEIL: {e}")

# ❌ 6. Test på feil: intensitet utenfor 1–10
try:
    plan.legg_til_okt("Altfor intens økt", 12, 40)
except ValueError as e:
    print(f"❗ FEIL: {e}")

try:
    plan.legg_til_okt(2, 5, 4)
except ValueError as e:
    print(f"❗ FEIL: {e}")

try:
    plan.legg_til_okt(None, 5, 4)
except ValueError as e:
    print(f"❗ FEIL: {e}")

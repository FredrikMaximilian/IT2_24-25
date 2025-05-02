class Bankkonto:
    def __init__(self, kontonummer: str, eier: str, saldo: float = 0.0):
        self.kontonummer = kontonummer
        self.eier = eier
        self.saldo = saldo

    def settInn(self, beløp: float) -> None:
        if beløp < 0:
            raise ValueError("Kan ikke sette inn negativt beløp.")
        self.saldo += beløp

    def taUt(self, beløp: float) -> None:
        if beløp < 0:
            raise ValueError("Kan ikke ta ut negativt beløp.")
        if beløp > self.saldo:
            raise RuntimeError("Ikke nok penger på konto.")
        self.saldo -= beløp

    def overførTil(self, annen_konto: 'Bankkonto', beløp: float) -> None:
        self.taUt(beløp)
        annen_konto.settInn(beløp)

    def hentSaldo(self) -> float:
        return self.saldo

def test_bankkonto():
    try:
        konto1 = Bankkonto("12345", "Ali", 1000)
        konto2 = Bankkonto("67890", "Emma", 500)

        # Test 1: Sett inn gyldig beløp
        konto1.settInn(500)
        assert konto1.hentSaldo() == 1500, "Feil: Saldo etter innskudd skal være 1500."

        # Test 2: Ta ut gyldig beløp
        konto1.taUt(300)
        assert konto1.hentSaldo() == 1200, "Feil: Saldo etter uttak skal være 1200."

        # Test 3: Overfør beløp til annen konto
        konto1.overførTil(konto2, 200)
        assert konto1.hentSaldo() == 1000, "Feil: Saldo etter overføring skal være 1000."
        assert konto2.hentSaldo() == 700, "Feil: Mottakende konto skal ha fått 200."

        # Test 4: Sett inn negativt beløp (forventet unntak)
        try:
            konto1.settInn(-100)
        except ValueError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 5: Ta ut mer enn saldo (forventet unntak)
        try:
            konto1.taUt(2000)
        except RuntimeError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 6: Overfør negativt beløp (forventet unntak)
        try:
            konto1.overførTil(konto2, -50)
        except ValueError as e:
            print(f"Forventet unntak fanget: {e}")

        print("Alle bankkonto-tester bestått!")

    except AssertionError as e:
        print(f"Test feilet: {e}")

# Kjør tester
test_bankkonto()

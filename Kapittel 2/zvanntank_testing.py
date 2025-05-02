class Vanntank:
    def __init__(self, maks_volum: float):
        self.maks_volum = maks_volum
        self.volum = 0.0  # Starter tom

    def fyllPå(self, liter: float) -> None:
        if liter < 0:
            raise ValueError("Kan ikke fylle på negativ mengde vann.")
        self.volum = min(self.volum + liter, self.maks_volum)

    def tappUt(self, liter: float) -> None:
        if liter < 0:
            raise ValueError("Kan ikke tappe ut negativ mengde vann.")
        if liter > self.volum:
            raise RuntimeError("Ikke nok vann i tanken.")
        self.volum -= liter

    def hentVolum(self) -> float:
        return self.volum

def test_vanntank():
    try:
        tank = Vanntank(200.0)  # Maks kapasitet er 200 liter

        # Test 1: Fyll på med 100 liter
        tank.fyllPå(100)
        assert tank.hentVolum() == 100, "Feil: Volum etter fylling skal være 100."

        # Test 2: Fyll på med mer enn maks kapasitet
        tank.fyllPå(150)
        assert tank.hentVolum() == 200, "Feil: Volum skal ikke overstige maks kapasitet."

        # Test 3: Tapp ut 50 liter
        tank.tappUt(50)
        assert tank.hentVolum() == 150, "Feil: Volum etter tapping skal være 150."

        # Test 4: Tapp ut for mye vann (forventet unntak)
        try:
            tank.tappUt(300)
        except RuntimeError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 5: Fyll på negativ verdi (forventet unntak)
        try:
            tank.fyllPå(-20)
        except ValueError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 6: Tapp ut negativ verdi (forventet unntak)
        try:
            tank.tappUt(-10)
        except ValueError as e:
            print(f"Forventet unntak fanget: {e}")

        print("Alle vanntank-tester bestått!")

    except AssertionError as e:
        print(f"Test feilet: {e}")

# Kjør tester
test_vanntank()

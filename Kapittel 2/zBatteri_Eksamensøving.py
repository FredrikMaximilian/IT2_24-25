class Batteri:
    def __init__(self, batteriID: str, energikapasitet: float):
        self.batteriID = batteriID
        self.energikapasitet = energikapasitet
        self.energinevå = 0.0  # Initial energinivå

    def ladOpp(self, energi: float) -> None:
        if energi < 0:
            raise ValueError("Energi som legges til kan ikke være negativ.")
        self.energinevå = min(self.energinevå + energi, self.energikapasitet)

    def brukEnergi(self, energi: float) -> None:
        if energi < 0:
            raise ValueError("Energi som brukes kan ikke være negativ.")
        if energi > self.energinevå:
            raise RuntimeError("Ikke nok energi tilgjengelig til å utføre handlingen.")
        self.energinevå -= energi

    def visEnerginivå(self) -> float:
        return self.energinevå
    

def test_batteri():
    try:
        # Oppretting av batteriobjekt
        batteri = Batteri("B001", 100.0)

        # Test 1: Lad opp med gyldig verdi
        batteri.ladOpp(50)
        assert batteri.visEnerginivå() == 50, "Feil: Energinivå etter oppladning er feil."

        # Test 2: Lad opp over kapasitet
        batteri.ladOpp(60)
        assert batteri.visEnerginivå() == 100, "Feil: Energinivå overstiger kapasitet."

        # Test 3: Bruk energi med gyldig verdi
        batteri.brukEnergi(30)
        assert batteri.visEnerginivå() == 70, "Feil: Energinivå etter bruk er feil."

        # Test 4: Bruk mer energi enn tilgjengelig (RuntimeError)
        try:
            batteri.brukEnergi(80)
        except RuntimeError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 5: Lad opp med negativ verdi (ValueError)
        try:
            batteri.ladOpp(-10)
        except ValueError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 6: Bruk negativ energi (ValueError)
        try:
            batteri.brukEnergi(-5)
        except ValueError as e:
            print(f"Forventet unntak fanget: {e}")

        print("Alle tester bestått!")
    except AssertionError as e:
        print(f"Test feilet: {e}")

# Kjør testprogrammet
test_batteri()

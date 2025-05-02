class Temperaturmåler:
    def __init__(self, målerID: str):
        self.målerID = målerID
        self.målinger = []

    def leggTilMåling(self, temp: float) -> None:
        if temp < -100 or temp > 100:
            raise ValueError("Ugyldig temperaturverdi.")
        self.målinger.append(temp)

    def hentGjennomsnitt(self) -> float:
        if not self.målinger:
            raise RuntimeError("Ingen målinger registrert.")
        return sum(self.målinger) / len(self.målinger)

    def hentMaks(self) -> float:
        if not self.målinger:
            raise RuntimeError("Ingen målinger registrert.")
        return max(self.målinger)

    def hentMin(self) -> float:
        if not self.målinger:
            raise RuntimeError("Ingen målinger registrert.")
        return min(self.målinger)

    def antallMålinger(self) -> int:
        return len(self.målinger)

def test_temperaturmåler():
    try:
        måler = Temperaturmåler("T-01")

        # Test 1: Legg til gyldige temperaturmålinger
        måler.leggTilMåling(20.5)
        måler.leggTilMåling(18.0)
        måler.leggTilMåling(22.5)
        assert måler.antallMålinger() == 3, "Feil: Antall målinger skal være 3."

        # Test 2: Hent gjennomsnitt
        gjennomsnitt = måler.hentGjennomsnitt()
        assert abs(gjennomsnitt - 20.3333) < 0.01, "Feil: Gjennomsnittet er feil."

        # Test 3: Hent maksimum
        assert måler.hentMaks() == 22.5, "Feil: Maks temperatur er feil."

        # Test 4: Hent minimum
        assert måler.hentMin() == 18.0, "Feil: Min temperatur er feil."

        # Test 5: Legg til ugyldig temperatur (for lav)
        try:
            måler.leggTilMåling(-150)
        except ValueError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 6: Hent snitt fra tom måler
        tom_måler = Temperaturmåler("T-02")
        try:
            tom_måler.hentGjennomsnitt()
        except RuntimeError as e:
            print(f"Forventet unntak fanget: {e}")

        print("Alle temperaturmåler-tester bestått!")

    except AssertionError as e:
        print(f"Test feilet: {e}")

# Kjør tester
test_temperaturmåler()

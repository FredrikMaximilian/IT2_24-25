class Temperaturmåler:
    def __init__(self, målerID: str):
        self.målerID = målerID
        self.målinger = []

    def leggTilMåling(self, temp: float) -> None:
        if temp < -100 or temp > 100:
            raise ValueError("Ugyldig temperaturverdi.")
        self.målinger.append(temp)

    def antallMålinger(self) -> int:
        return len(self.målinger)

class Dagsinfo(Temperaturmåler):
    def __init__(self, målerID):
        super().__init__(målerID)
        self.målinger = []
    
    def leggTilMåling(self, nedbør: float) -> None:
        if nedbør < 0  or nedbør > 250:
            raise ValueError("Ugyldig nedbørverdi.")
        self.målinger.append(nedbør)

    def hentDagens(self):
        if not self.målinger:
            raise RuntimeError("Ingen målinger registrert.")
        return (self.målinger)

    def antallMålinger(self) -> int:
        return len(self.målinger)
    
    def hentTotal(self) -> float:
        if not self.målinger:
            raise RuntimeError("Ingen målinger registrert.")
        return sum(self.målinger)

class Hentinfo(Dagsinfo):
    def __init__(self, målerID):
        super().__init__(målerID)
        ukedagliste = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
        dagensnedbør = self.hentDagens
        dag = self.dag
        return (f'{dag}: {målerID}: {dagensnedbør}')



def test_nedbørmåler():
    try:
        måler = Dagsinfo("Harald")

        # Test 1: Legg til gyldige temperaturmålinger
        måler.leggTilMåling(20.5)
        måler.leggTilMåling(18.0)
        måler.leggTilMåling(22.5)
        assert måler.antallMålinger() == 3, "Feil: Antall målinger skal være 3."

        
        total = måler.hentTotal()
        assert abs(total - 20.3333) < 0.01, "Feil: Gjennomsnittet er feil."

        try:
            måler.leggTilMåling(-150)
        except ValueError as e:
            print(f"Forventet unntak fanget: {e}")


        print("Alle nedbør-tester bestått!")

    except AssertionError as e:
        print(f"Test feilet: {e}")

# Kjør tester
test_nedbørmåler()

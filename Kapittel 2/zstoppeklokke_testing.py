class Stoppeklokke:
    def __init__(self):
        # Startetid og stoptid er None før klokken startes
        self.startetid = None
        self.stoptid = None
        self.går = False  # Stoppeklokken går ikke til å begynne med

    def start(self, tidspunkt: float) -> None:
        """
        Starter stoppeklokken. Krever at tidspunkt er gitt som float (f.eks. sekunder).
        """
        if self.går:
            raise RuntimeError("Stoppeklokken går allerede.")
        self.startetid = tidspunkt
        self.går = True

    def stopp(self, tidspunkt: float) -> None:
        """
        Stopper stoppeklokken og lagrer stoptid.
        """
        if not self.går:
            raise RuntimeError("Stoppeklokken er ikke startet.")
        self.stoptid = tidspunkt
        self.går = False

    def hentTid(self) -> float:
        """
        Returnerer tiden mellom start og stopp.
        """
        if self.startetid is None or self.stoptid is None:
            raise RuntimeError("Stoppeklokken er ikke startet og stoppet riktig.")
        return self.stoptid - self.startetid

    def nullstill(self) -> None:
        """
        Nullstiller stoppeklokken.
        """
        self.startetid = None
        self.stoptid = None
        self.går = False

def test_stoppeklokke():
    try:
        klokke = Stoppeklokke()

        # Test 1: Start og stopp normalt
        klokke.start(10.0)          # Start klokken ved 10 sekunder
        klokke.stopp(25.5)          # Stopp klokken ved 25.5 sekunder
        assert abs(klokke.hentTid() - 15.5) < 0.01, "Feil: Tid skal være 15.5 sekunder."

        # Test 2: Start på nytt etter nullstilling
        klokke.nullstill()
        klokke.start(100.0)
        klokke.stopp(108.2)
        assert abs(klokke.hentTid() - 8.2) < 0.01, "Feil: Tid skal være 8.2 sekunder."

        # Test 3: Stopp uten å starte først (forventet unntak)
        ny_klokke = Stoppeklokke()
        try:
            ny_klokke.stopp(50.0)
        except RuntimeError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 4: Start klokken to ganger uten å stoppe (forventet unntak)
        try:
            klokke.start(200.0)
        except RuntimeError as e:
            print(f"Forventet unntak fanget: {e}")

        # Test 5: Hent tid før stopp (forventet unntak)
        klokke2 = Stoppeklokke()
        klokke2.start(5.0)
        try:
            klokke2.hentTid()
        except RuntimeError as e:
            print(f"Forventet unntak fanget: {e}")

        print("Alle stoppeklokke-tester bestått!")

    except AssertionError as e:
        print(f"Test feilet: {e}")

# Kjør tester
test_stoppeklokke()

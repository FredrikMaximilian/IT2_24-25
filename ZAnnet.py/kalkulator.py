class Kalkulator:
    def __init__(self, førstetall, andretall):
        self.førstetall = førstetall
        self.andretall = andretall

    def addisjon(self):
        if not isinstance(self.førstetall, str) and not isinstance(self.andretall, str):
            return self.førstetall + self.andretall
        return ("Du må skrive inn to tall")
        
    def subtraksjon(self):
        if not isinstance(self.førstetall, str) and not isinstance(self.andretall, str):
            return self.førstetall - self.andretall
        return ("Du må skrive inn to tall")
    
    def multiplikasjon(self):
        if not isinstance(self.førstetall, str) and not isinstance(self.andretall, str):
            return self.førstetall * self.andretall
        return ("Du må skrive inn to tall")
    
    def divisjon(self):
        try:
            if not isinstance(self.førstetall, str) and not isinstance(self.andretall, str):
                return self.førstetall / self.andretall
            return ("Du må skrive inn to tall")
        except ZeroDivisionError:
            return "Kan ikke dele på null"
    
def test_kalkulator():
    print("Test 1: Vanlige tall")
    k1 = Kalkulator(10, 5)
    print("Addisjon:", k1.addisjon())        # 15
    print("Subtraksjon:", k1.subtraksjon())  # 5
    print("Multiplikasjon:", k1.multiplikasjon())  # 50
    print("Divisjon:", k1.divisjon())        # 2.0

    print("\nTest 2: Ugyldige verdier")
    k2 = Kalkulator("a", 5)
    print(k2.addisjon())  # Forvent feilmelding

    print("\nTest 3: Null i divisor")
    k3 = Kalkulator(10, 0)
    print(k3.divisjon())  # Forvent feilmelding eller håndtering

test_kalkulator()

"""viser avhengigheter"""
class Overklasse:
    def __init__(self):
        pass
 
class Avhengig:
    def __init__(self, assosiert):
        self.assosiert = assosiert
 
class Underklasse(Overklasse):
    def __init__(self, assosiert):
        self.assosiert = assosiert
        super.__init__()
    def metode(self, avhengig: Avhengig = None):
        print("Bruker avhengig klasse")
 
class Assosiert:
    def __init__(self):
        pass


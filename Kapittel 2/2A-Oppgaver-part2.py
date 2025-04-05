"""
#Oppgave 1
liste = [1, 2, 3]
ordbok = {"a": 1, "b": 2, "c": 3}

print(type(liste))
print(type(ordbok))
""""""
#Oppgave2
class Planet:
    def __init__ (self, navn, plassering, ringer = 0):
        self.navn = navn
        self.plassering = plassering
        self.ringer = ringer

merkur = Planet("Merkur", 1)
jupiter = Planet("Jupiter", 5, 4)
print(merkur.plassering)
print(jupiter.ringer)
print(jupiter.navn)"""
#Docstrings oppgave 3 5
'''
import math as m

class Planet:
  """
  Klasse for å lage planet-objekter.

  Parametre:
    navn (str): Planetens navn
    solavstand (float): Avstand fra sola i millioner km
    radius (float): Planetens radius i km
    antallRinger = 0 (int): Antall ringer rundt planeten
  """
  def __init__(self, navn, solavstand, radius, antallRinger = 0):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius
    self.antallRinger = antallRinger

  def overflate(self):
    return 4 * m.pi * (self.radius ** 2)
  
  def lystid(self):
    c = 300_000_000
    avstand_i_meter = self.solavstand * 1_000_000 * 1000
    return avstand_i_meter/c
  
  def visInfo(self):
    print(f'Planeten {self.navn} er {self.solavstand} millioner km fra sola, har radius lik {self.radius} og overflate {self.overflate()}')

# Lager planeten Jorda
jorda = Planet("Jorda", 149.6, 6371)
print(jorda.lystid())
print(jorda.overflate())
jorda.visInfo()''''''
#Oppgave 12
class Rektangel:
  """Klasse for å representere et rektangel"""
  def __init__(self, lengde, bredde):
    """Konstruktør"""
    self.lengde = lengde
    self.bredde = bredde
  
  def areal(self):
    """Metode for å beregne areal"""
    return self.lengde * self.bredde
  
  def visinfo(self):
    if self.lengde == self.bredde:
      print(f'Kvadrat med sidelengde {self.lengde} har areal {self.areal()}')
    else:
      print(f'Rektangel med lengde {self.lengde} og bredde {self.bredde} har areal {self.areal()}')
  
class Kvadrat(Rektangel):
  """Klasse for å representere et kvadrat"""
  def __init__(self, sidekant):
    super().__init__(sidekant, sidekant)

rektangel = Rektangel(2, 4)
kvadrat = Kvadrat(4)
rektangel.visinfo()
kvadrat.visinfo()'''
#Oppgave 13 14
'''
class Billett():
  def __init__(self):
      self.mva = 0.12
      self.pris = 20

  def beregnPris(self):
    return self.pris + (self.pris * self.mva)

class Barnebillett(Billett):
  def __init__(self):
      super().__init__()
      self.rabatt = 0.5
  
  def beregnPris(self):
      rabattpris = self.pris * self.rabatt
      return rabattpris + (rabattpris * self.mva)

class Vernepliktige(Billett):
    def __init__(self):
      super().__init__()
      self.rabatt = 0.1

    def beregnPris(self):
       rabattpris = self.pris * self.rabatt
       return rabattpris + (rabattpris * self.mva)

class Ukebillett(Billett):
   def __init__(self):
      super().__init__()
      self.pris = 7*self.pris
      self.rabatt = 0.8

   def beregnPris(self):
       return self.pris*self.rabatt
    
vanlig = Billett()
barn = Barnebillett()
verneplikt = Vernepliktige()
uke = Ukebillett()

print(vanlig.beregnPris())
print(barn.beregnPris())
print(verneplikt.beregnPris())
print(uke.beregnPris())'''
'''
class Rektangel:
  """Klasse for å representere et rektangel"""
  def __init__(self, lengde:int, bredde:int):
    """Konstruktør"""
    self.lengde = lengde
    self.bredde = bredde
  
  def areal(self):
    """Metode for å beregne areal"""
    return self.lengde * self.bredde

  def visInfo(self):
    """Skriver ut informasjon om et rektangel"""
    print(f"Rektangel med lengde {self.lengde} og bredde {self.bredde} har areal {self.areal()}")

class Kvadrat(Rektangel):
  """Klasse for å representere et kvadrat"""
  def __init__(self, sidekant:int):
    super().__init__(sidekant, sidekant)
  
  def visInfo(self):
    """Skriver ut informasjon om et kvadrat"""
    print(f"Kvadrat med sidelengde {self.lengde} har areal {self.areal()}")

kvadratliste = []
rektangelliste = []

kvadratliste.append(Kvadrat(1))
kvadratliste.append(Kvadrat(2))
kvadratliste.append(Kvadrat(3))
kvadratliste.append(Kvadrat(4))
kvadratliste.append(Kvadrat(5))
rektangelliste.append(Rektangel(1, 6))
rektangelliste.append(Rektangel(2, 2))
rektangelliste.append(Rektangel(3, 5))
rektangelliste.append(Rektangel(4, 1))
rektangelliste.append(Rektangel(5, 3))

for k in kvadratliste:
  k.visInfo()
for r in rektangelliste:
  r.visInfo()
"""
''''''
import math as m
class Planet:
  def __init__(self, navn, solavstand, radius, antallRinger = 0):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius
    self.antallRinger = antallRinger
    self.maaner = []
  
  def visInfo(self):
    print(f"Planeten {self.navn} har {self.antallRinger} ringer, er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")

  def leggTilMaane(self, maane):
    self.maaner.append(maane)

  def visMaanerOgForhold(self):
    if not self.maaner:
      print(f'{self.navn} har ingen måner')
    else:
      planetvolum = (4/3)*m.pi*self.radius**3
      print(f'Måner for {self.navn}:')
      for maane in self.maaner:
        maanevolum = maane.beregnVolum()
        forhold = maanevolum/planetvolum
        print(f' {maane.navn}: Volumforhold {forhold:.6f}')
  def __str__(self):
    return(f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")

class Maane:
  def __init__(self, navn, radius):
    self.navn = navn
    self.radius = radius

  def beregnVolum(self):
    volum = (4/3)*m.pi*self.radius**3
    return volum
"""
planeter = {}
planeter["Mars"] = Planet("Mars", 227.9, 3389.5)
planeter["Jupiter"] = Planet("Jupiter", 778.5, 69911, 4)
planeter["Saturn"] = Planet("Saturn", 1434000, 58232, 7)
"""
mars = Planet("Mars", 227.9, 3389.5)
print(mars)
'''
"""
for p in planeter.values():
  p.visInfo()

planeter["Mars"].visInfo()
jupiter = Planet("Jupiter", 778, 69911, antallRinger=4)
europa = Maane("Europa", 1560)
ganymedes = Maane("Ganymedes", 2634)
jupiter.leggTilMaane(europa)
jupiter.leggTilMaane(ganymedes)
jupiter.visInfo()
jupiter.visMaanerOgForhold()

mars = Planet("Mars", 228, 3390)
phobos = Maane("Phobos", 11.1)
deimos = Maane("Deimos", 6.2)
mars.leggTilMaane(phobos)
mars.leggTilMaane(deimos)
mars.visInfo()
mars.visMaanerOgForhold()
"""
'''
class Bankkonto:
    kontonummer = 0
    def __init__(self, eier, saldo):
        self.saldo = saldo
        self.eier = eier
        Bankkonto.kontonummer += 1
        self.kontonummer = Bankkonto.kontonummer

    def leggInnPenger(self, inntekt):
        self.saldo += inntekt
        return self.saldo
    
    def taUtPenger(self, utgift):
        self.saldo -= utgift
        return self.saldo
    
    def visInfo(self):
        print(f'{self.eier} har kontonummer {self.kontonummer} og saldo {self.saldo}')

class Sparekonto(Bankkonto):
    def __init__(self, eier, saldo, maksUttak = 3):
        super().__init__(eier, saldo)
        self.maksUttak = maksUttak
        self.antallUttak = 0

    def taUtPenger(self, beløp):
        if self.antallUttak >= self.maksUttak:
            print("Du kan ikke ta ut mer")
            return self.saldo
        if beløp > self.saldo:
            print("Ikke nok penger på konto")
            return self.saldo
        self.saldo -= beløp
        self.antallUttak += 1
        return self.saldo
    
    def visInfo(self):
        super().visInfo()
        print(f'uttak i år: {self.antallUttak}/{self.maksUttak}')

class BSUKonto(Bankkonto):
    def __init__(self, eier, saldo, maksUttak = 1):
        super().__init__(eier, saldo)
        self.maksUttak = maksUttak
        self.antallUttak = 0

    def TaUtAlt(self, beløp):
        if beløp != self.saldo:
            print("Du må ta ut alt på en gang")
            return
        elif self.antallUttak >= self.maksUttak:
            print(f'Du kan bare ta ut {self.maksUttak} ganger')
            return
        else:
            self.antallUttak += 1
            self.saldo = 0
            return self.saldo
'''        
"""
kim = Bankkonto("Kim", 100)
lucy = Bankkonto("Lucy", 1000)
kim.taUtPenger(30)
lucy.leggInnPenger(50)
lucy.visInfo()
kim.visInfo()""""""
# 🔍 Testeksempel
konto = BSUKonto("Sofie", 25000)
konto.visInfo()

print("\n🧪 Forsøk på å ta ut bare 10000:")
konto.TaUtAlt(10000)  # Feil beløp

print("\n🧪 Forsøk på å ta ut alt (25000):")
konto.TaUtAlt(25000)  # Riktig beløp

konto.visInfo()

print("\n🧪 Forsøk på å ta ut en gang til:")
konto.TaUtAlt(0)      # Skal ikke gå
"""
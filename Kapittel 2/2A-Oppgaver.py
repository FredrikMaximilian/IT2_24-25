'''
min_liste = [1, 2, 3]

min_ordbok = {
    "navn": "Fredrik",
    "alder": 20,}
liste_type = type(min_liste)
ordbok_type = type(min_ordbok)

print("Type av listen:", liste_type)
print("Type av ordboken:", ordbok_type)
'''
'''
#Oppgave 16 20 25
class Person:
    def __init__(self, fornavn, etternavn, fødselsår):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselsår

    def finnTrinn(self):
        nåværendeÅr = 2024
        alder = nåværendeÅr - self.fødselsår

        if alder == 16:
            return "VG1"
        if alder == 17:
            return "VG2"
        if alder == 18:
            return "VG3"
        else:
            return "Ukjent"
    
    def visInfo(self):
        print(f'{self.fornavn} {self.etternavn} er født i {self.fødselsår} og går i {self.finnTrinn()}')
        
class Lærer(Person):
    def __init__(self, fornavn, etternavn, fødselsår, fag = None, kontaktklasse=""):
        super().__init__(fornavn, etternavn, fødselsår)
        self.fag = fag if fag is not None else []
        self.kontaktklasse = kontaktklasse
    
    def sjekkfag(self, fagNavn):
        return fagNavn in self.fag
        
    def visInfo(self):
        fagliste = ", ".join(self.fag) if self.fag else "Ingen fag"
        kontaktinfo = f'Kontaktlærer for {self.kontaktklasse}' if self.kontaktklasse else "Ikke kontaktlærer"
        print(f'{self.fornavn} {self.etternavn} er født i {self.fødselsår}.')
        print(f'Kan undervise i: {fagliste}. {kontaktinfo}.')

class Skoleklasse:
    def __init__(self, navn, kontaktlærer):
        self.navn = navn
        self.kontaktlærer = kontaktlærer
        self.elever = []

    def angiKontaktlærer(self, nyLærer):
        print(f"Endrer kontaktlærer fra {self.kontaktlærer.fornavn} {self.kontaktlærer.etternavn} "
            f"til {nyLærer.fornavn} {nyLærer.etternavn}.")
        self.kontaktlærer = nyLærer
    
    def leggTilElev(self, person):
        self.elever.append(person)
        print(f'{person.fornavn} {person.etternavn} ble lagt til i klassen {self.navn}')
    
    def visKlasseliste(self):
            print(f"\n{'=' * 30}")
            print(f"Klasseliste for {self.navn}")
            print(f"Kontaktlærer: {self.kontaktlærer.fornavn} {self.kontaktlærer.etternavn}")
            print(f"{'=' * 30}")
            print(f"{'Nr.':<5}{'Navn':<20}{'Trinn':<10}")
            print(f"{'-' * 30}")
            for i, elev in enumerate(self.elever, start=1):
                print(f"{i:<5}{elev.fornavn} {elev.etternavn:<20}{elev.finnTrinn():<10}")
            print(f"{'=' * 30}")

#print(person1.fornavn, person1.etternavn, person1.fødselsår)
#print("Trinn:", person1.finnTrinn())
        
person1 = Person("Fredrik", "Lysnes", 2007)
person2 = Person("Ivo", "Tjessem", 2008)
person3 = Person("WenWei", "Ngo", 2009)
person4 = Person("Lucy", "Smith", 2007)
person5 = Person("Even", "Sandemose", 2007)
person6 = Person("Agathe", "Fleischer", 2006)
lærer1 = Lærer("Anders", "Pettersen", 1980, ["Matematikk", "Naturfag"], "1STF")
lærer2 = Lærer("Anne Kirsti", "Torbyen", 1985, ["Samfunnsfag"], "2STF")
lærer3 = Lærer("Rikke", "Larsen", 1990, ["Historie"], "2STF")
#person1.visInfo()
#person2.visInfo()
#person3.visInfo()
#lærer1.visInfo()
#lærer2.visInfo()
#print(lærer1.sjekkfag("Matematikk")) #Sjekker om lærere har visse fag
#print(lærer2.sjekkfag("Matematikk"))
print()

klasse1 = Skoleklasse("2STF", lærer1)
klasse1.angiKontaktlærer(lærer3)
klasse1.leggTilElev(person1)
klasse1.leggTilElev(person2)
klasse1.leggTilElev(person3)
klasse1.leggTilElev(person4)
klasse1.leggTilElev(person5)
klasse1.leggTilElev(person6)
print(f'Kontaktlæreren til {klasse1.navn} er nå {klasse1.kontaktlærer.fornavn} {klasse1.kontaktlærer.etternavn}')
print(f'Elever i klasse {klasse1.navn} er nå:')
for elev in klasse1.elever:
    print(f'{elev.fornavn} {elev.etternavn}')

klasse1.visKlasseliste()
'''
"""
class Planet:
  def __init__(self, navn, solavstand, radius):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius

merkur = Planet("Merkur", 57.9, 2440)  
venus = Planet("Venus", 108.2, 6052)
jorda = Planet("Jorda", 149.6, 6371)

print(f'Navnet til Merkur er {merkur.navn}.')
print(f'Radiusen til Venus er {venus.radius} km.')
print(f'Solavstanden til Jorda er {jorda.solavstand} millioner km.')
"""
#10
'''
"""
from datetime import datetime6

class Person:
    def __init__(self, navn, etternavn, fødselsår):
        self.navn = navn
        self.etternavn = etternavn
        self.fødselår = fødselsår
    
    def beregnAlder(self):
        """
        Beregner alder basert på fødselsår
        """
        gjeldeneÅr = datetime.now().year
        alder = gjeldeneÅr - self.fødselår
        return alder
    
    def visInfo(self):
        """
        Viser all informasjon om gitt person
        """
        alder = self.beregnAlder() 
        print(f'{self.navn}, {self.etternavn}, {self.fødselår}, {alder}')

person1 = Person("Eilif", "Kennedy", 2007)
person2 = Person("Fredrik", "Steinbach", 2007)
person3 = Person("Ivo", "Tjessem", 2007)
person1.visInfo()
person2.visInfo()
person3.visInfo()  
print(f'Alderen til {person1.navn} er {person1.beregnAlder()}')
print(f'Alderen til {person2.navn} er {person2.beregnAlder()}')
print(f'Alderen til {person3.navn} er {person3.beregnAlder()}')
"""
"""
#Oppgave 8 9
import math as m

class Planet:
    def __init__(self, navn, solavstand, radius):
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
    
    def volum(self):
     return (4/3)*m.pi*self.radius**3
    
    def overflate(self):
       return 4*m.pi*self.radius**2
    
    def soltid(self):
       return (self.solavstand*1000000)/300000
    
    def volumforhold(self, planet2):
        return self.volum()/planet2.volum()
    
    def visInfo(self):
       print(f'Planeten {self.navn} er {self.solavstand} millioner km unna sola, har radius {self.radius} km, overflatearealet er {self.overflate():,.3f} km^2, {self.volum():,.3f}.')

merkur = Planet("Merkur", 57.91, 2439.7)
venus = Planet("Venus", 108.2, 6051.8)
jorda = Planet("Jorda", 149.6, 6371)

merkur.visInfo()
venus.visInfo()
jorda.visInfo()
print()
print(f'Merkur sitt volum er {merkur.volum()}')
print(f'Venus sitt volum er {venus.volum()}')
print()
print(f'Merkur sin overflate er {merkur.overflate()}')
print(f'Venus sin overflate er {venus.overflate()}')
print()
print(f'Tiden det tar fra Sola til Merkur er {merkur.soltid():,.3f} sekunder')
print(f'Tiden det tar fra Sola til Venus er {venus.soltid():,.3f} sekunder')
print()
print(f'Volumforholdet mellom Merkur og Venus er {merkur.volumforhold(venus):,.3f}')
print(f'Volumforholdet mellom Venus og Merkur er {venus.volumforhold(merkur):,.3f}')
'''
'''
#Oppgave 11
import random as r
class Terning:
    def __init__(self, antallSider):
        self.antallSider = antallSider

    def trillTerning(self):
        return r.randint(1, self.antallSider)
    
terning1 = Terning(6)
print("Terning med", terning1.antallSider, "sider")
for i in range(10):
    print(f'kast {i+1}: {terning1.trillTerning()}')

terning2 = Terning(20)
print("Terning med", terning2.antallSider, "sider")
for i in range(10):
    print(f'Kast{i+1}: {terning2.trillTerning()}')
'''
"""
class Rektangel:
    def __init__(self, lengde, bredde):
        self.lengde = lengde
        self.bredde = bredde

    def areal(self):
        return self.lengde * self.bredde
    
    def visInfo(self):
        print(f'Et rektangel med lengde {self.lengde} og bredde {self.bredde} har areal {self.areal()}')
    
class Kvadrat(Rektangel):
    def __init__(self, sidekant):
        super().__init__(sidekant, sidekant)
    
    def visInfo(self):
        print(f'Et kvadrat med sidelengde {self.bredde} har areal {self.areal()}')

kvadrat1 = Kvadrat(2)
rektangel1 = Rektangel(2, 4)

print(kvadrat1.areal())
print(rektangel1.areal())
kvadrat1.visInfo()
rektangel1.visInfo()

kvadrater = []
rektangler = []

kvadrater.append(Kvadrat(2))
kvadrater.append(Kvadrat(4))
kvadrater.append(Kvadrat(5))

rektangler.append(Rektangel(2, 4))
rektangler.append(Rektangel(3, 5))
rektangler.append(Rektangel(4, 6))

for r in kvadrater:
    r.visInfo()
print()
for r in rektangler:
    r.visInfo()
"""
'''
class Rektangel:
    """Klasse for å representere rektangel"""
    def __init__(self, lengde, bredde):
        self.lengde = lengde
        self.bredde = bredde

    def areal(self):
        return self.lengde * self.bredde
    
    def visInfo(self):
        print(f'Rektangel: Lengde = {self.lengde}, Bredde = {self.bredde}, Areal = {self.areal()}')

class Kvadrat(Rektangel):
    """Klasse for å representere kvadrat"""
    def __init__(self, sidekant):
        super().__init__(sidekant, sidekant)

    def visInfo(self):
        print(f'Kvadrat: Sidekant = {self.lengde}, Areal = {self.areal()}')

kvadrat1 = Kvadrat(2)
rektangel1 = Rektangel(3, 5)

kvadrat1.visInfo()
rektangel1.visInfo()
'''
'''
class Billett():
    def __init__(self):
        self.mva = 0.12
        self.pris = 20
    
    def beregnPris(self):
        return self.pris + (self.pris*self.mva)

class Barnebillett(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.5
    
    def beregnPris(self):
        return super().beregnPris() * self.rabatt

class Vernepliktig(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.1
    
    def beregnPris(self):
        return super().beregnPris() * self.rabatt
    
class Ukesbillett(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.8
        self.antallDager = 7

    def beregnPris(self):
        return super().beregnPris() * self.antallDager * self.rabatt

voksenbillett = Billett()
barnebillett = Barnebillett()
vernepliktig = Vernepliktig()
ukesbillett = Ukesbillett()

print(voksenbillett.beregnPris())
print(barnebillett.beregnPris())
print(f'{vernepliktig.beregnPris():.2f}')
print(ukesbillett.beregnPris())
'''
"""
import random as r
class Terning:
    def __init__(self, antallSider):
        self.antallSider = antallSider

    def trillTerning(self):
        return r.randint(1, self.antallSider)
    
terning1 = Terning(6)
print("Terning med", terning1.antallSider, "sider:")
for i in range(5):
    print(f'kast {i+1}: {terning1.trillTerning()}')


terning2 = Terning(20)
print("Terning med", terning2.antallSider, "sider")
for i in range(10):
    print(f'Kast{i+1}: {terning2.trillTerning()}')


class Jukseterning(Terning):
    def __init__(self, antallSider):
        super().__init__(antallSider)

        def trillTerning(self):
            vekting = [i for i in range(1, self.antallSider + 1)] + [self.antallSider] * 2
            return r.choice(vekting)
        
jukseterning1 = Jukseterning(6)
print("Jukseterning med", jukseterning1.antallSider, "sider:")
for i in range(5):
    print(f'kast{i+1}: {jukseterning1.trillTerning()}')
"""
"""
import math as m

class Måner:
    def __init__(self, navn, radius):
        self.navn = navn
        self.radius = radius

    def beregnVolum(self):
        return (4 / 3) * m.pi * self.radius**3

class Planet:
    def __init__(self, navn, solavstand, radius, antallRinger=0):
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        self.antallRinger = antallRinger
        self.måner = []
    
    def __str__(self):
        return(f'Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km.')

    def visInfo(self):
        print(f"Planeten {self.navn} har {self.antallRinger} ringer, er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")
        if self.måner:
             print(f"{self.navn} har følgende måner:")
             for måne in self.måner:
                  print(f"- {måne.navn} med radius {måne.radius} km og volum {måne.beregnVolum():.2f} km³.")
        else:
            print(f'Planeten {self.navn} har ingen måner.')

    def leggTilMåne(self, måne):
        self.måner.append(måne)

    def visMånerMedForhold(self):
        if not self.måner:
            print(f'Planeten {self.navn} har ingen måner')
            return
        planetVolum = (4 / 3) * m.pi * self.radius**3
        print(f'{self.navn} har følgende måner med volumforhold:')
        for måne in self.måner:
            måneVolum = måne.beregnVolum()
            forhold = måneVolum/planetVolum
            print(f'{måne.navn}: Forhold til planetens volum = {forhold:.6f}')

# Lager en dictionary for å holde Planet-objekter
planeter = {
    "Mars": Planet("Mars", 227.9, 3389.5, 2),
    "Jupiter": Planet("Jupiter", 778.5, 69911, 4),
    "Saturn": Planet("Saturn", 1434, 58232, 7),
    "Jorda": Planet("Jorda", 149.6, 6378)
}
Jorda = Planet("Jorda", 149.6, 6378)
planeter["Jorda"].leggTilMåne(Måner("Månen", 1737))
planeter["Jupiter"].leggTilMåne(Måner("Europa", 1561))
planeter["Jupiter"].leggTilMåne(Måner("Ganymedes", 2634))
planeter["Mars"].leggTilMåne(Måner("Phobos", 11))
planeter["Mars"].leggTilMåne(Måner("Deimos", 6.2))

# Itererer over planetene og viser informasjon
for planet in planeter.values():
    planet.visInfo()
    print()
print("VOLUMFORHOLD")
print()
for planet in planeter.values():
    planet.visMånerMedForhold()
    print()

#planetnavn = str(input("Skriv inn planeten din")).capitalize()
#if planetnavn in planeter:
#    planeter[planetnavn].visInfo()
#else:
#    print("Planeten er dessverre ikke i lista")
print(Jorda)
planeter["Jorda"].visInfo()
"""
"""
#Oppgave 21
class Bankkonto:
    banknummer = 0
    def __init__(self, eier, saldo):
        self.eier = eier
        self.saldo = saldo
        Bankkonto.banknummer = Bankkonto.banknummer + 1
        self.banknummer = Bankkonto.banknummer

    def visInfo(self):
        print(f'{self.eier} har en saldo på {self.saldo} og kontonummer {self.banknummer}')

    def settInnPenger(self, beløp):
        if beløp <= 0:
            print(f'Du kan ikke sette inn et negativt beløp, {beløp}')
        else:
            self.saldo += beløp
            print(f'Saldoen til {self.eier} har blitt oppdatert fra {self.saldo-beløp} til {self.saldo}')

class Sparekonto(Bankkonto):
    def __init__(self, eier, saldo, maksUttak=2):
        super().__init__(eier, saldo)
        self.maksUttak = maksUttak
        self.uttakTell = 0

    def taUtPenger(self, beløp):
        if self.uttakTell >= self.maksUttak:
            print(f'Uttak mislyktes, du har brukt opp dine {self.maksUttak} årlige uttak')
        elif beløp > self.saldo:
            print(f'Uttak mislyktes, saldoen er for lav ({self.saldo})')
        else:
            self.saldo = self.saldo - beløp
            self.uttakTell + 1
            print(f'Saldoen til {self.eier} har blitt oppdatert fra {(self.saldo)+beløp} til {self.saldo}')

class BSUKonto(Bankkonto):
    def __init__(self, eier, saldo, maksUttak=1):
        super().__init__(eier, saldo)
        self.maksUttak = maksUttak
        self.uttakTell = 0
    
    def taUtPenger(self, beløp):
        if self.uttakTell >= self.maksUttak:
            print(f'Uttak mislyktes, du har brukt opp dine {self.maksUttak} årlige uttak')
        elif beløp != self.saldo:
            print(f'Uttak mislyktes, uttaket må være likt saldoen')
        else:
            self.saldo = self.saldo - beløp
            print(f'BSU-konten til {self.eier} har blitt tømt fra {(self.saldo)+beløp} til {self.saldo}')
            self.uttakTell += 1

person1 = Bankkonto("Fredrik Lysnes", 300)
person2 = Bankkonto("Simon", 500)
person3 = Sparekonto("Victoria", 1000)
person4 = BSUKonto("Vilma", 500)

person1.visInfo()
person2.visInfo()
print()
person1.settInnPenger(300)
person2.settInnPenger(-400)
print()
person1.visInfo()
person2.visInfo()
person3.taUtPenger(300)
person3.taUtPenger(200)
person3.taUtPenger(100)
person4.taUtPenger(500)
person4.taUtPenger(0)
"""
'''
class Person:
    def __init__(self, fornavn, etternavn, fødselsår):
        self.__fornavn = fornavn
        self.__etternavn = etternavn
        self.__fødselsår = fødselsår

    def finnTrinn(self):
        nåværendeÅr = 2024
        alder = nåværendeÅr - self.__fødselsår

        if alder == 16:
            return "VG1"
        if alder == 17:
            return "VG2"
        if alder == 18:
            return "VG3"
        else:
            return "Ukjent"
    """
    def visInfo(self):
        print(f'{self.__fornavn} {self.__etternavn} er født i {self.__fødselsår} og går i {self.finnTrinn()}')
"""
    def __str__(self):
        return (f'{self.__fornavn} {self.__etternavn} er født i {self.__fødselsår} og går i {self.finnTrinn()}')

    # Getter-metoder
    def hentFornavn(self):
        return self.__fornavn

    def hentEtternavn(self):
        return self.__etternavn

    def hentFødselsår(self):
        return self.__fødselsår


class Lærer(Person):
    def __init__(self, fornavn, etternavn, fødselsår, fag=None, kontaktklasse=""):
        super().__init__(fornavn, etternavn, fødselsår)
        self.__fag = fag if fag is not None else []
        self.__kontaktklasse = kontaktklasse

    def sjekkfag(self, fagNavn):
        return fagNavn in self.__fag
    """
    def visInfo(self):
        fagliste = ", ".join(self.__fag) if self.__fag else "Ingen fag"
        kontaktinfo = f'Kontaktlærer for {self.__kontaktklasse}' if self.__kontaktklasse else "Ikke kontaktlærer"
        print(f'{self.hentFornavn()} {self.hentEtternavn()} er født i {self.hentFødselsår()}.')
        print(f'Kan undervise i: {fagliste}. {kontaktinfo}.')
"""
    def __str__(self):
        fagliste = ", ".join(self.__fag) if self.__fag else "Ingen fag"
        kontaktinfo = f'Kontaktlærer for {self.__kontaktklasse}' if self.__kontaktklasse else "Ikke kontaktlærer"
        return (f'{self.hentFornavn()} {self.hentEtternavn()} er født i {self.hentFødselsår()}.'
            f' Kan undervise i: {fagliste}. {kontaktinfo}.')

    # Getter-metoder
    def hentFag(self):
        return self.__fag

    def hentKontaktklasse(self):
        return self.__kontaktklasse


class Skoleklasse:
    def __init__(self, navn, kontaktlærer):
        self.__navn = navn
        self.__kontaktlærer = kontaktlærer
        self.__elever = []

    def angiKontaktlærer(self, nyLærer):
        print(f"Endrer kontaktlærer fra {self.__kontaktlærer.hentFornavn()} {self.__kontaktlærer.hentEtternavn()} "
              f"til {nyLærer.hentFornavn()} {nyLærer.hentEtternavn()}.")
        self.__kontaktlærer = nyLærer

    def leggTilElev(self, person):
        self.__elever.append(person)
        print(f'{person.hentFornavn()} {person.hentEtternavn()} ble lagt til i klassen {self.__navn}')

    def visKlasseliste(self):
        print(f"\n{'=' * 30}")
        print(f"Klasseliste for {self.__navn}")
        print(f"Kontaktlærer: {self.__kontaktlærer.hentFornavn()} {self.__kontaktlærer.hentEtternavn()}")
        print(f"{'=' * 30}")
        print(f"{'Nr.':<5}{'Navn':<20}{'Trinn':<10}")
        print(f"{'-' * 30}")
        for i, elev in enumerate(self.__elever, start=1):
            print(f"{i:<5}{elev.hentFornavn()} {elev.hentEtternavn():<20}{elev.finnTrinn():<10}")
        print(f"{'=' * 30}")

person1 = Person("Fredrik", "Lysnes", 2007)
person2 = Person("Ivo", "Tjessem", 2008)
lærer1 = Lærer("Anne", "Torbyen", 1985, ["Matematikk"], "2STF")

klasse1 = Skoleklasse("2STF", lærer1)
klasse1.leggTilElev(person1)
klasse1.leggTilElev(person2)
#print(person2.navn)

# Vise klasseliste
klasse1.visKlasseliste()
print(person1)
print(lærer1)
'''
#Sluttoppgave
class Mangekant:
    def __init__(self, antallSider):
        self.antallSider = antallSider
        self.sideLengder = []

    def registrerSideLengder(self):
        for i in range(self.antallSider):
            sideLengde = float(input(f'Skriv inn sidelengden til side {i+1}: '))
            self.sideLengder.append(sideLengde)
        
    def omkrets(self):
        return sum(self.sideLengder)

    def __str__(self):
        return f'Mangekanten har {self.antallSider} sider, sidelengde {self.sideLengder} og omkrets {self.omkrets()}'
    
class Rektangel(Mangekant):
    def __init__(self, lengde, bredde):
        super().__init__(4)
        self.lengde = lengde
        self.bredde = bredde
        self.sideLengder = [lengde, lengde, bredde, bredde]
        
    def areal(self):
        return self.lengde*self.bredde
    
    def omkrets(self):
        return sum(self.sideLengder)
    
    def __str__(self):
        return (f'Rektangelet har lengde {self.lengde}, bredde {self.bredde}, omkrets {self.omkrets()} og areal {self.areal()}')
    
class Kvadrat(Rektangel):
    def __init__(self, sidelengde):
        super().__init__(sidelengde, sidelengde)
        self.sidelengde = sidelengde
      #  self.sideLengder = [sidelengde, sidelengde, sidelengde, sidelengde]

    def areal(self):
        return self.sidelengde**2
    
   # def omkrets(self):
    #    return sum(self.sideLengder)
    
    def __str__(self):
        return (f'Et kvadrat med sidelengde {self.sidelengde} har omkrets {self.omkrets()} og areal {self.areal()}')


trekant = Mangekant(3)
firkant = Mangekant(4)
femkant = Mangekant(5)

#trekant.registrerSideLengder()
#firkant.registrerSideLengder()
#femkant.registrerSideLengder()
#print(trekant)
#print(firkant)
#print(femkant)

rektangler = [
    Rektangel(2, 3),
    Rektangel(3, 4),
    Rektangel(4, 5),
    Rektangel(5, 6)
]

kvadrater = [
    Kvadrat(2), 
    Kvadrat(3), 
    Kvadrat(4), 
    Kvadrat(5)
]

print("Rektangler:")
for rektangel in rektangler:
    print(rektangel)

print()
print("Kvadrater:")
for kvadrat in kvadrater:
    print(kvadrat)

class Trekant(Mangekant):
    def __init__(self, a, b, c):
        super().__init__(3)
        self.sideLengder = [a, b, c]
        self.a = a
        self.b = b
        self.c = c
    
    def omkrets(self):
        return sum(self.sideLengder)
    
    def __str__(self):
        return (f'Trekanten har sidene a={self.a}, b={self.b}, c={self.c}, omkrets={self.omkrets():.2f} ')
    
trekanter = [
    Trekant(4, 4.2, 5),
    Trekant(5, 5.6, 5.6),
    Trekant(4, 4, 4),
    Trekant(4, 6, 7),
    Trekant(3, 6.2, 6.2)
]
print("Trekanter:")
for trekant in trekanter:
    print(trekant)
    
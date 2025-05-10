import pygame as pg  # Importerer pygame for å lage grafisk grensesnitt
import math  # Importerer math for matematiske operasjoner (ikke brukt i denne filen)
from person_virusspredning import Person  # Importerer Person-klassen fra en ekstern fil
import random  # Importerer random for å generere tilfeldige tall

# Konstantene
ANTALL_RUTER = 20  # Antall ruter i hver rad og kolonne
RUTE_STR = 20  # Størrelsen på hver rute i piksler

# Farger for de ulike tilstandene til en person
FARGER = {
    Person.FRISK_UTEN_IMMUNITET: (200, 200, 200),  # Grå for frisk uten immunitet
    Person.SMITTET: (255, 182, 193),  # Rosa for smittet
    Person.SYK: (255, 0, 0),  # Rød for syk
    Person.DOD: (0, 0, 0),  # Svart for død
    Person.FRISK_MED_IMMUNITET: (100, 100, 100)  # Mørk grå for frisk med immunitet
}

# Ekstra farger
SVART = (0, 0, 0)  # Svart farge
HVIT = (255, 255, 255)  # Hvit farge
GRAA = (150, 150, 150)  # Grå farge

# Initialiserer pygame
pg.init()
vindu = pg.display.set_mode((ANTALL_RUTER * RUTE_STR, ANTALL_RUTER * RUTE_STR))  # Oppretter et vindu med riktig størrelse
pg.display.set_caption("Virus-simulering")  # Setter tittelen på vinduet

# Klasse for hver rute i rutenettet
class Rute:
    def __init__(self, rad, kolonne, person):
        self.rad = rad  # Raden til ruten
        self.kolonne = kolonne  # Kolonnen til ruten
        self.person = person  # Personen som befinner seg i ruten

    def tegn(self, vindu):
        x = self.rad * RUTE_STR  # Beregner x-posisjonen til ruten
        y = self.kolonne * RUTE_STR  # Beregner y-posisjonen til ruten
        farge = FARGER[self.person.tilstand]  # Henter fargen basert på personens tilstand
        pg.draw.rect(vindu, farge, (x, y, RUTE_STR, RUTE_STR))  # Tegner ruten med riktig farge
        pg.draw.rect(vindu, GRAA, (x, y, RUTE_STR, RUTE_STR), width=1)  # Tegner kantlinjen rundt ruten

        # Tegner mønstre basert på personens tilstand
        if self.person.tilstand == Person.SMITTET:
            pg.draw.line(vindu, SVART, (x, y), (x + RUTE_STR, y + RUTE_STR), 2)  # Diagonal linje for smittet
        elif self.person.tilstand == Person.SYK:
            pg.draw.line(vindu, HVIT, (x, y), (x + RUTE_STR, y + RUTE_STR), 2)  # Diagonal linje for syk
        elif self.person.tilstand == Person.FRISK_MED_IMMUNITET:
            pg.draw.circle(vindu, SVART, (x + RUTE_STR // 2, y + RUTE_STR // 2), 3)  # Sirkel for frisk med immunitet
        elif self.person.tilstand == Person.DOD:
            pg.draw.circle(vindu, HVIT, (x + RUTE_STR // 2, y + RUTE_STR // 2), 3)  # Sirkel for død

# Klasse for populasjonen
class Populasjon:
    def __init__(self, antall_ruter):  # Initialiserer populasjonen med antall ruter
        self.antall_ruter = antall_ruter  # Antall ruter i populasjonen
        self.ruter = [[None for _ in range(antall_ruter)] for _ in range(antall_ruter)]  # Lager en 2D-liste for ruter
        for i in range(antall_ruter):  # Itererer gjennom alle rader
            for j in range(antall_ruter):  # Itererer gjennom alle kolonner
                person = Person()  # Oppretter en ny person
                self.ruter[i][j] = Rute(i, j, person)  # Oppretter en ny rute med en person

        self.starttilstand()  # Setter starttilstanden for viruset

    def starttilstand(self):
        midt = self.antall_ruter // 2  # Finner midten av rutenettet
        self.ruter[midt][midt].person.tilstand = Person.SYK  # Setter personen i midten til "SYK"
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Itererer over naboene (opp, ned, venstre, høyre)
            nabo = self.ruter[midt + dx][midt + dy].person  # Henter naboen til midten
            nabo.tilstand = Person.SMITTET  # Setter naboens tilstand til "SMITTET"
            nabo.dager_smittet = 0  # Initialiserer antall dager smittet til 0

    def hent_naboer(self, rad, kol):
        naboer = []  # Oppretter en liste for å lagre naboene
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Itererer over mulige naboer (opp, ned, venstre, høyre)
            ny_rad, ny_kol = rad + dx, kol + dy  # Beregner naboens rad og kolonne
            if 0 <= ny_rad < self.antall_ruter and 0 <= ny_kol < self.antall_ruter:  # Sjekker om naboen er innenfor rutenettet
                naboer.append(self.ruter[ny_rad][ny_kol].person)  # Legger til naboen i listen
        return naboer  # Returnerer listen over naboer

    def oppdater(self):
        for i in range(self.antall_ruter):  # Itererer over alle rader i rutenettet
            for j in range(self.antall_ruter):  # Itererer over alle kolonner i rutenettet
                self.ruter[i][j].person.oppdater()  # Oppdaterer tilstanden til personen i hver rute

        nye_smittede = []  # Oppretter en liste for å lagre nye smittede personer

        for i in range(self.antall_ruter):  # Itererer over alle rader i rutenettet
            for j in range(self.antall_ruter):  # Itererer over alle kolonner i rutenettet
                person = self.ruter[i][j].person  # Henter personen i den aktuelle ruten
                if person.er_smittbar():  # Sjekker om personen kan bli smittet
                    for nabo in self.hent_naboer(i, j):  # Itererer over alle naboene til personen
                        if nabo.kan_smittes() and random.random() < 0.3:  # Sjekker om naboen kan smitte og om det skjer med 30% sannsynlighet
                            nye_smittede.append(nabo)  # Legger til naboen i listen over nye smittede
        for person in nye_smittede:  # Itererer over alle nye smittede
            person.smitt()  # Setter tilstanden til "SMITTET"

    def tegn(self, vindu):
        for i in range(self.antall_ruter):  # Itererer over alle rader i rutenettet
            for j in range(self.antall_ruter):  # Itererer over alle kolonner i rutenettet
                self.ruter[i][j].tegn(vindu)  # Tegner hver rute

# Hovedløkken
populasjon = Populasjon(ANTALL_RUTER)  # Oppretter en populasjon med gitt antall ruter
klokke = pg.time.Clock()  # Oppretter en klokke for å kontrollere oppdateringsfrekvensen
paused = False  # Variabel for å holde styr på om simuleringen er satt på pause
første_frame = True  # Variabel for å håndtere første frame
dagsteller = 0  # Teller antall dager i simuleringen
font = pg.font.SysFont("Arial", 36)  # Oppretter en font for å vise tekst

while True:  # Evig løkke for simuleringen
    for event in pg.event.get():  # Henter alle hendelser
        if event.type == pg.QUIT:  # Sjekker om brukeren lukker vinduet
            pg.quit()  # Avslutter pygame
            exit()  # Avslutter programmet
        if event.type == pg.KEYDOWN:  # Sjekker om en tast er trykket
            if event.key == pg.K_SPACE:  # Sjekker om mellomromstasten er trykket
                paused = not paused  # Bytter mellom pause og spill

    if not paused and not første_frame:  # Oppdaterer kun hvis simuleringen ikke er på pause
        populasjon.oppdater()  # Oppdaterer populasjonen
        dagsteller += 1  # Øker dagstelleren

    første_frame = False  # Setter første frame til False etter første iterasjon

    vindu.fill(HVIT)  # Fyller vinduet med hvit bakgrunn
    populasjon.tegn(vindu)  # Tegner populasjonen
    dagstekst = font.render((f'Dager: {dagsteller}'), True, (0, 0, 0))  # Lager tekst for antall dager
    vindu.blit(dagstekst, (10, 10))  # Tegner teksten på vinduet

    pg.display.flip()  # Oppdaterer skjermen
    klokke.tick(2)  # Setter oppdateringsfrekvensen til 1 oppdatering per sekund

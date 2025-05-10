import pygame as pg
import random

# Grunnkonstanter
ANTALL_RUTER = 20
RUTE_STR = 20
BREDDE = ANTALL_RUTER * RUTE_STR
HOYDE = ANTALL_RUTER * RUTE_STR

# Farger
FARGER = {
    "tom": (200, 200, 200),
    "hare": (150, 255, 150),
    "rev": (255, 150, 150),
    "død": (50, 50, 50)
}

# Init Pygame
pg.init()
vindu = pg.display.set_mode((BREDDE, HOYDE))
pg.display.set_caption("Økosystem – Rev og Hare")
klokke = pg.time.Clock()

class Dyr:
    def __init__(self, art):
        self.art = art            # "hare" eller "rev"
        self.energi = 10 if art == "rev" else 0
        self.alder = 0
        self.har_formert = False  # Hindrer flere formeringer per runde

    def oppdater(self):
        self.alder += 1
        self.har_formert = False
        if self.art == "rev":
            self.energi -= 1
            if self.energi <= 0:
                self.art = "død"

class Rute:
    def __init__(self, rad, kolonne):
        self.rad = rad
        self.kolonne = kolonne
        self.dyr = None

    def tegn(self, vindu):
        x = self.kolonne * RUTE_STR
        y = self.rad * RUTE_STR
        art = "tom" if self.dyr is None else self.dyr.art
        pg.draw.rect(vindu, FARGER[art], (x, y, RUTE_STR, RUTE_STR))
        pg.draw.rect(vindu, (100, 100, 100), (x, y, RUTE_STR, RUTE_STR), width=1)

# Rutenett
rutenett = [[Rute(i, j) for j in range(ANTALL_RUTER)] for i in range(ANTALL_RUTER)]

# Startpopulasjon
for i in range(ANTALL_RUTER):
    for j in range(ANTALL_RUTER):
        rand = random.random()
        if rand < 0.05:
            rutenett[i][j].dyr = Dyr("rev")
        elif rand < 0.25:
            rutenett[i][j].dyr = Dyr("hare")

# Hjelpefunksjon: gyldige naboer
def hent_naboer(i, j):
    naboer = []
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        ny_i, ny_j = i + dx, j + dy
        if 0 <= ny_i < ANTALL_RUTER and 0 <= ny_j < ANTALL_RUTER:
            naboer.append((ny_i, ny_j))
    return naboer

# Hovedløkke
kjør = True
while kjør:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjør = False

    # Først: oppdater alle dyr
    for rad in rutenett:
        for rute in rad:
            if rute.dyr:
                rute.dyr.oppdater()

    # Flytt og spis
    nye_rutenett = [[Rute(i, j) for j in range(ANTALL_RUTER)] for i in range(ANTALL_RUTER)]

    for i in range(ANTALL_RUTER):
        for j in range(ANTALL_RUTER):
            rute = rutenett[i][j]
            dyr = rute.dyr
            if dyr is None or dyr.art == "død":
                continue

            mulige = hent_naboer(i, j)
            random.shuffle(mulige)

            flyttet = False
            for ny_i, ny_j in mulige:
                mål = nye_rutenett[ny_i][ny_j]
                # Rev spiser hare
                if dyr.art == "rev":
                    opprinnelig = rutenett[ny_i][ny_j]
                    if opprinnelig.dyr and opprinnelig.dyr.art == "hare":
                        dyr.energi += 5
                        mål.dyr = dyr
                        flyttet = True
                        break
                # Flytt til tom celle
                if mål.dyr is None:
                    mål.dyr = dyr
                    flyttet = True
                    break

            if not flyttet:
                nye_rutenett[i][j].dyr = dyr  # Dyr står stille

    # Former harer og rever
    for i in range(ANTALL_RUTER):
        for j in range(ANTALL_RUTER):
            rute = nye_rutenett[i][j]
            dyr = rute.dyr
            if not dyr or dyr.har_formert:
                continue
            naboer = hent_naboer(i, j)
            for ny_i, ny_j in naboer:
                nabo_rute = nye_rutenett[ny_i][ny_j]
                hvis_tom = nabo_rute.dyr is None
                if dyr.art == "hare" and hvis_tom and dyr.alder > 3:
                    nabo_rute.dyr = Dyr("hare")
                    dyr.har_formert = True
                    break
                elif dyr.art == "rev" and hvis_tom and dyr.energi > 10:
                    nabo_rute.dyr = Dyr("rev")
                    dyr.har_formert = True
                    dyr.energi -= 5  # Formeringskostnad
                    break

    # Tegn rutenett
    vindu.fill((255, 255, 255))
    for rad in nye_rutenett:
        for rute in rad:
            rute.tegn(vindu)

    rutenett = nye_rutenett  # Oppdater til ny verden

    pg.display.flip()
    klokke.tick(4)  # Juster hastighet

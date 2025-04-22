import pygame as pg
import random

# Konstanter
ANTALL_RUTER = 30             # Rutenett-størrelse
RUTE_STR = 20                 # Pikselstørrelse per rute
BREDDE = ANTALL_RUTER * RUTE_STR
HOYDE = ANTALL_RUTER * RUTE_STR

# Farger for tilstander
FARGER = {
    "tom": (200, 200, 200),
    "tre": (34, 139, 34),
    "brann": (255, 0, 0),
    "brent": (50, 50, 50),
    "vann": (0, 0, 255),
    "stein": (100, 100, 100)
}

# Vindretning (sør)
VIND = (1, 0)  # Vind blåser sørover

# Initialiserer pygame
pg.init()
vindu = pg.display.set_mode((BREDDE, HOYDE))
pg.display.set_caption("Brannsimulering med vind og terreng")
klokke = pg.time.Clock()

# Klasse for rute i rutenettet
class Rute:
    def __init__(self, rad, kol):
        self.rad = rad
        self.kol = kol
        self.tilstand = "tre"
        self.neste_tilstand = "tre"

    def tegn(self, vindu):
        x = self.kol * RUTE_STR
        y = self.rad * RUTE_STR
        farge = FARGER[self.tilstand]
        pg.draw.rect(vindu, farge, (x, y, RUTE_STR, RUTE_STR))
        pg.draw.rect(vindu, (80, 80, 80), (x, y, RUTE_STR, RUTE_STR), width=1)

# Lager rutenett med overvekt av trær
def lag_rutenett():
    nett = [[Rute(i, j) for j in range(ANTALL_RUTER)] for i in range(ANTALL_RUTER)]
    for rad in nett:
        for rute in rad:
            r = random.random()
            if r < 0.03:
                rute.tilstand = "vann"
            elif r < 0.06:
                rute.tilstand = "stein"
            else:
                rute.tilstand = "tre"
    return nett

# Henter opp/ned/venstre/høyre naboer
def hent_naboer(i, j):
    naboer = []
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        ny_i, ny_j = i + dx, j + dy
        if 0 <= ny_i < ANTALL_RUTER and 0 <= ny_j < ANTALL_RUTER:
            naboer.append((ny_i, ny_j))
    return naboer

# Lager første rutenett
rutenett = lag_rutenett()

# Sørger for at midten er et tre og tenner det på
midt = ANTALL_RUTER // 2
rutenett[midt][midt].tilstand = "tre"
rutenett[midt][midt].tilstand = "brann"

# Hovedløkke
kjør = True
while kjør:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjør = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            kol = x // RUTE_STR
            rad = y // RUTE_STR
            valgt = rutenett[rad][kol]
            if valgt.tilstand == "tre":
                valgt.tilstand = "brann"
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                rutenett = lag_rutenett()
                midt = ANTALL_RUTER // 2
                rutenett[midt][midt].tilstand = "tre"
                rutenett[midt][midt].tilstand = "brann"

    # Brannlogikk: bestem neste tilstand
    for i in range(ANTALL_RUTER):
        for j in range(ANTALL_RUTER):
            rute = rutenett[i][j]
            if rute.tilstand == "brann":
                rute.neste_tilstand = "brent"
                for ny_i, ny_j in hent_naboer(i, j):
                    nabo = rutenett[ny_i][ny_j]
                    if nabo.tilstand == "tre":
                        dx, dy = ny_i - i, ny_j - j
                        vind_bonus = 0.2 if (dx, dy) == VIND else 0
                        if random.random() < 0.5 + vind_bonus:  # Økt sjanse
                            nabo.neste_tilstand = "brann"
            elif rute.tilstand in ["tre", "vann", "stein"]:
                rute.neste_tilstand = rute.tilstand
            else:
                rute.neste_tilstand = "brent"

    # Overfører neste tilstand
    for rad in rutenett:
        for rute in rad:
            rute.tilstand = rute.neste_tilstand

    # Tegner hele rutenettet
    vindu.fill((255, 255, 255))
    for rad in rutenett:
        for rute in rad:
            rute.tegn(vindu)

    pg.display.flip()
    klokke.tick(5)

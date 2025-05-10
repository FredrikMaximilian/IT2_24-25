import pygame as pg
import numpy as np
import math

from pg_meny import Knapp
from pg_meny import MENYFARGE, HOVERFARGE

# Ruteinfo
ANTALL_RUTER = 20
RUTE_STR = 20

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRAA = (70, 70, 70)

# Meny
MENY_XSTART = ANTALL_RUTER * RUTE_STR
MENY_YSTART = 20
MENY_BREDDE = 200
MENY_YAVSTAND = 60

# Vindu
VINDU_BREDDE = ANTALL_RUTER * RUTE_STR + MENY_BREDDE
VINDU_HOYDE = ANTALL_RUTER * RUTE_STR
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.init()

class Rute:
    def __init__(self, rad, kolonne):
        self.rad = rad
        self.kolonne = kolonne
        self.levende = False
        self.nesteStatus = False
        self.farge = HVIT

    def oppdater(self):
        self.levende = self.nesteStatus

    def byttTilstand(self):
        self.levende = not self.levende

    def tegn(self, vindu):
        self.farge = SVART if self.levende else HVIT
        pg.draw.rect(vindu, self.farge, (self.rad*RUTE_STR, self.kolonne*RUTE_STR, RUTE_STR, RUTE_STR))
        pg.draw.rect(vindu, GRAA, (self.rad*RUTE_STR, self.kolonne*RUTE_STR, RUTE_STR, RUTE_STR), width=1)

class Rutenett:
    def __init__(self):
        self.ruter = [[Rute(i, j) for j in range(ANTALL_RUTER)] for i in range(ANTALL_RUTER)]

    def oppdater(self):
        for i in range(ANTALL_RUTER):
            for j in range(ANTALL_RUTER):
                self.ruter[i][j].nesteStatus = self.ruter[i][j].levende

        for i in range(ANTALL_RUTER):
            for j in range(ANTALL_RUTER):
                naboer = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if not (x == 0 and y == 0):
                            if 0 <= i + x < ANTALL_RUTER and 0 <= j + y < ANTALL_RUTER:
                                if self.ruter[i+x][j+y].levende:
                                    naboer += 1
                if naboer <= 1 or naboer > 3:
                    self.ruter[i][j].nesteStatus = False
                elif naboer == 3:
                    self.ruter[i][j].nesteStatus = True

        for i in range(ANTALL_RUTER):
            for j in range(ANTALL_RUTER):
                self.ruter[i][j].oppdater()

class Glidebryter:
    def __init__(self, x, y, bredde, min_verdi, max_verdi, start_verdi):
        self.x = x
        self.y = y
        self.bredde = bredde
        self.min_verdi = min_verdi
        self.max_verdi = max_verdi
        self.verdi = start_verdi
        self.knapp_x = x + int((max_verdi - start_verdi) / (max_verdi - min_verdi) * bredde)
        #self.knapp_x = x + int((start_verdi - min_verdi) / (max_verdi - min_verdi) * bredde)
        self.hoyde = 20
        self.knapp_bredde = 10
        self.rektangel = pg.Rect(x, y, bredde, self.hoyde)
        self.knapp_rekt = pg.Rect(self.knapp_x, y - 5, self.knapp_bredde, self.hoyde + 10)
        self.aktiv = False

    def tegn(self, vindu):
        # Stang
        pg.draw.rect(vindu, GRAA, self.rektangel)
        # Glideknapp
        self.knapp_rekt.x = self.knapp_x
        pg.draw.rect(vindu, SVART, self.knapp_rekt)

        # Tekst (viser nåværende verdi) (Ekstra)
        tekst = FONT.render(f"{self.verdi} ms", True, (0, 0, 0))
        vindu.blit(tekst, (self.x, self.y + 25))


    def oppdater(self, mus_x):
        self.knapp_x = max(self.x, min(mus_x, self.x + self.bredde))
        #self.verdi = int(self.min_verdi + (self.knapp_x - self.x) / self.bredde * (self.max_verdi - self.min_verdi)) #Motsatt side
        self.verdi = int(self.max_verdi - (self.knapp_x - self.x) / self.bredde * (self.max_verdi - self.min_verdi))


def tilfeldig_start():
    for i in range(ANTALL_RUTER):
        for j in range(ANTALL_RUTER):
            rutenett.ruter[i][j].levende = False
            if np.random.randint(0, 3) == 1:
                rutenett.ruter[i][j].byttTilstand()

def museklikk(pos):
    global pauset  # ← dette er det som manglet
    x, y = pos
    if x < ANTALL_RUTER * RUTE_STR and y < ANTALL_RUTER * RUTE_STR:
        rutenett.ruter[x // RUTE_STR][y // RUTE_STR].byttTilstand()
    else:
        for knapp in meny:
            if knapp.rektangel.collidepoint(pos):
                if knapp.tekst == "Omstart":
                    for rad in rutenett.ruter:
                        for rute in rad:
                            rute.levende = False
                elif knapp.tekst == "Tilfeldig start":
                    tilfeldig_start()
                elif knapp.tekst == "Start" or knapp.tekst == "Pause":
                    pauset = not pauset
                    knapp.tekst = "Pause" if not pauset else "Start"

rutenett = Rutenett()
tilfeldig_start()

meny = [
    Knapp(MENY_XSTART + 20, MENY_YSTART, "Omstart"),
    Knapp(MENY_XSTART + 20, MENY_YSTART + MENY_YAVSTAND, "Tilfeldig start"),
    Knapp(MENY_XSTART + 20, MENY_YSTART + 2*MENY_YAVSTAND, "Start")
]

glidebryter = Glidebryter(MENY_XSTART + 20, MENY_YSTART + 3*MENY_YAVSTAND, 150, 10, 1000, 200)

pauset = True
klokke = pg.time.Clock()
tid_siden_sist_oppdatering = 0

fortsett = True
FONT = pg.font.SysFont("Arial", 20)
while fortsett:
    dt = klokke.tick(60)  # dt = antall millisekunder siden forrige frame
    tid_siden_sist_oppdatering += dt

    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            museklikk(pg.mouse.get_pos())
            if glidebryter.knapp_rekt.collidepoint(pg.mouse.get_pos()):
                glidebryter.aktiv = True
        elif event.type == pg.MOUSEBUTTONUP:
            glidebryter.aktiv = False
        elif event.type == pg.MOUSEMOTION and glidebryter.aktiv:
            glidebryter.oppdater(pg.mouse.get_pos()[0])

    # Bare oppdater rutenett hvis ikke pauset OG det har gått lang nok tid
    if not pauset and tid_siden_sist_oppdatering > glidebryter.verdi:
        rutenett.oppdater()
        tid_siden_sist_oppdatering = 0

    VINDU.fill(HVIT)
    for rad in rutenett.ruter:
        for rute in rad:
            rute.tegn(VINDU)

    musPos = pg.mouse.get_pos()
    for m in meny:
        m.tegn(VINDU, HOVERFARGE if m.rektangel.collidepoint(musPos) else MENYFARGE)

    glidebryter.tegn(VINDU)
    pg.display.flip()

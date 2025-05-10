import pygame as pg
import random

# Init
pg.init()

# Konstantene
ANTALL_RUTER = 30
RUTE_STR = 20
BREDDE = ANTALL_RUTER * RUTE_STR
HOYDE = ANTALL_RUTER * RUTE_STR

# Farger for celletilstander
FARGER = {
    "tom": (180, 180, 180),
    "celle_0": (173, 216, 230),  # lyseblå
    "celle_1": (100, 149, 237),  # blå
    "celle_2": (25, 25, 112),    # mørkeblå
    "død": (0, 0, 0)
}

# Regler
ALDER_FOR_REPRODUKSJON = 3
ALDER_FOR_MUTASJON = 5
MAKS_ALDER = 12
MUTASJONSSJANSE = 0.1

# Setup vindu
vindu = pg.display.set_mode((BREDDE, HOYDE))
pg.display.set_caption("Cellemutasjonssimulering")
klokke = pg.time.Clock()

# Celleklasse
class Celle:
    def __init__(self):
        self.alder = 0
        self.mutasjonsnivå = 0  # 0 = minst mutert, 2 = maks
        self.død = False

    def oppdater(self):
        if self.død:
            return
        self.alder += 1
        if self.alder >= MAKS_ALDER:
            self.død = True
        elif self.alder >= ALDER_FOR_MUTASJON and random.random() < MUTASJONSSJANSE:
            if self.mutasjonsnivå < 2:
                self.mutasjonsnivå += 1

    def farge(self):
        if self.død:
            return FARGER["død"]
        return FARGER[f"celle_{self.mutasjonsnivå}"]

# Rute i rutenettet
class Rute:
    def __init__(self, rad, kol):
        self.rad = rad
        self.kol = kol
        self.celle = None

    def tegn(self, vindu):
        x = self.kol * RUTE_STR
        y = self.rad * RUTE_STR
        if self.celle:
            farge = self.celle.farge()
        else:
            farge = FARGER["tom"]
        pg.draw.rect(vindu, farge, (x, y, RUTE_STR, RUTE_STR))
        pg.draw.rect(vindu, (100, 100, 100), (x, y, RUTE_STR, RUTE_STR), width=1)

# Oppretter rutenett
rutenett = [[Rute(i, j) for j in range(ANTALL_RUTER)] for i in range(ANTALL_RUTER)]

# Hjelpefunksjon for naboer
def hent_naboer(i, j):
    naboer = []
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        ny_i, ny_j = i + dx, j + dy
        if 0 <= ny_i < ANTALL_RUTER and 0 <= ny_j < ANTALL_RUTER:
            naboer.append(rutenett[ny_i][ny_j])
    return naboer

# Hovedløkke
pause = False
kjør = True
while kjør:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjør = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            kol = x // RUTE_STR
            rad = y // RUTE_STR
            rute = rutenett[rad][kol]
            if not rute.celle:
                rute.celle = Celle()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pause = not pause
            elif event.key == pg.K_c:
                for rad in rutenett:
                    for rute in rad:
                        rute.celle = None

    if not pause:
        nye_celler = []

        # Oppdater og planlegg formering
        for i in range(ANTALL_RUTER):
            for j in range(ANTALL_RUTER):
                rute = rutenett[i][j]
                if rute.celle:
                    rute.celle.oppdater()

                    if not rute.celle.død and rute.celle.alder >= ALDER_FOR_REPRODUKSJON:
                        naboer = hent_naboer(i, j)
                        for nabo in naboer:
                            if not nabo.celle:
                                nye_celler.append(nabo)

        # Legg til nye celler
        for rute in nye_celler:
            rute.celle = Celle()

    # Tegn rutenett
    vindu.fill((255, 255, 255))
    for rad in rutenett:
        for rute in rad:
            rute.tegn(vindu)
    pg.display.flip()

    klokke.tick(4)  # Juster hastighet her

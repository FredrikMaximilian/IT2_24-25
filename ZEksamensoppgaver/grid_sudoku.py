import pygame as pg
import random
import copy

# Pygame setup
pg.init()
BREDDE = 540
HOYDE = 600
vindu = pg.display.set_mode((BREDDE, HOYDE))
pg.display.set_caption("Sudoku")
FONT = pg.font.SysFont("Arial", 30)
LITEN_FONT = pg.font.SysFont("Arial", 20)

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
BLA = (50, 50, 255)
GRAA = (200, 200, 200)
GRØNN = (0, 150, 0)
RØD = (200, 0, 0)

# Rute
class Rute:
    def __init__(self, verdi, rad, kol, fast):
        self.verdi = verdi
        self.rad = rad
        self.kol = kol
        self.fast = fast
        self.valgt = False

    def tegn(self, vindu):
        x = self.kol * 60
        y = self.rad * 60
        if self.valgt:
            pg.draw.rect(vindu, GRAA, (x, y, 60, 60))
        if self.verdi != 0:
            farge = SVART if self.fast else BLA
            tekst = FONT.render(str(self.verdi), True, farge)
            vindu.blit(tekst, (x + 20, y + 15))

# Brett
class Brett:
    def __init__(self, rutenett):
        self.ruter = [[Rute(rutenett[i][j], i, j, rutenett[i][j] != 0) for j in range(9)] for i in range(9)]
        self.valgt = None
        self.original = copy.deepcopy(rutenett)

    def tegn(self, vindu):
        for rad in self.ruter:
            for rute in rad:
                rute.tegn(vindu)
        # Rutenett-linjer
        for i in range(10):
            bredde = 4 if i % 3 == 0 else 1
            pg.draw.line(vindu, SVART, (0, i * 60), (540, i * 60), bredde)
            pg.draw.line(vindu, SVART, (i * 60, 0), (i * 60, 540), bredde)

    def velg(self, pos):
        x, y = pos
        kol = x // 60
        rad = y // 60
        if 0 <= rad < 9 and 0 <= kol < 9:
            self.valgt = (rad, kol)
            for r in self.ruter:
                for rute in r:
                    rute.valgt = False
            self.ruter[rad][kol].valgt = True

    def sett_inn(self, tall):
        if self.valgt:
            rad, kol = self.valgt
            rute = self.ruter[rad][kol]
            if not rute.fast:
                rute.verdi = tall

    def slett(self):
        if self.valgt:
            rad, kol = self.valgt
            rute = self.ruter[rad][kol]
            if not rute.fast:
                rute.verdi = 0

    def hent_brett(self):
        return [[self.ruter[i][j].verdi for j in range(9)] for i in range(9)]

    def gyldig(self, tall, rad, kol):
        for i in range(9):
            if self.ruter[rad][i].verdi == tall and i != kol:
                return False
            if self.ruter[i][kol].verdi == tall and i != rad:
                return False
        start_i = (rad // 3) * 3
        start_j = (kol // 3) * 3
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                if self.ruter[i][j].verdi == tall and (i, j) != (rad, kol):
                    return False
        return True

    def full(self):
        for rad in self.ruter:
            for rute in rad:
                if rute.verdi == 0:
                    return False
        return True

    def korrekt(self):
        brett = self.hent_brett()
        for i in range(9):
            for j in range(9):
                verdi = brett[i][j]
                if verdi == 0 or not self.gyldig(verdi, i, j):
                    return False
        return True

    def løs(self):
        brett = self.hent_brett()
        self._løs_helper(brett)
        for i in range(9):
            for j in range(9):
                self.ruter[i][j].verdi = brett[i][j]

    def _løs_helper(self, brett):
        for i in range(9):
            for j in range(9):
                if brett[i][j] == 0:
                    for tall in range(1, 10):
                        if self._gyldig_brett(brett, tall, i, j):
                            brett[i][j] = tall
                            if self._løs_helper(brett):
                                return True
                            brett[i][j] = 0
                    return False
        return True

    def _gyldig_brett(self, brett, tall, rad, kol):
        for i in range(9):
            if brett[rad][i] == tall and i != kol:
                return False
            if brett[i][kol] == tall and i != rad:
                return False
        start_i = (rad // 3) * 3
        start_j = (kol // 3) * 3
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                if brett[i][j] == tall and (i, j) != (rad, kol):
                    return False
        return True

# Sudoku-generator
def lag_full_løsning():
    brett = [[0]*9 for _ in range(9)]
    def fyll():
        for i in range(9):
            for j in range(9):
                if brett[i][j] == 0:
                    tall = list(range(1, 10))
                    random.shuffle(tall)
                    for t in tall:
                        if gyldig(brett, t, i, j):
                            brett[i][j] = t
                            if fyll():
                                return True
                            brett[i][j] = 0
                    return False
        return True
    def gyldig(brett, tall, rad, kol):
        for i in range(9):
            if brett[rad][i] == tall or brett[i][kol] == tall:
                return False
        start_i = (rad // 3) * 3
        start_j = (kol // 3) * 3
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                if brett[i][j] == tall:
                    return False
        return True
    fyll()
    return brett

def lag_puslespill(fullt_brett, tomme=40):
    brett = copy.deepcopy(fullt_brett)
    fjernet = 0
    while fjernet < tomme:
        i, j = random.randint(0,8), random.randint(0,8)
        if brett[i][j] != 0:
            brett[i][j] = 0
            fjernet += 1
    return brett

# Init
full_løsning = lag_full_løsning()
puslespill = lag_puslespill(full_løsning, tomme=50)
brett = Brett(puslespill)

# Hovedløkke
kjør = True
pause = False
while kjør:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjør = False
        elif event.type == pg.MOUSEBUTTONDOWN and not pause:
            brett.velg(pg.mouse.get_pos())
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                full_løsning = lag_full_løsning()
                puslespill = lag_puslespill(full_løsning)
                brett = Brett(puslespill)
            elif event.key == pg.K_SPACE:
                pause = not pause
            elif event.key == pg.K_RETURN:
                brett.løs()
            elif event.key == pg.K_BACKSPACE:
                brett.slett()
            elif event.unicode in "123456789":
                brett.sett_inn(int(event.unicode))

    # Tegn
    vindu.fill(HVIT)
    brett.tegn(vindu)
    if pause:
        txt = FONT.render("PAUSET", True, RØD)
        vindu.blit(txt, (10, 555))
    elif brett.full():
        if brett.korrekt():
            txt = FONT.render("Løsning er korrekt!", True, GRØNN)
        else:
            txt = FONT.render("Noe er feil...", True, RØD)
        vindu.blit(txt, (10, 555))
    else:
        instruks = LITEN_FONT.render("R: restart | ENTER: løs | SPACE: pause | BACKSPACE: slett", True, SVART)
        vindu.blit(instruks, (10, 565))

    pg.display.flip()

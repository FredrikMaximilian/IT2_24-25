import pygame as pg
import random as r
import math as m

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
ROD = (255, 0, 0)
GUL = (255, 255, 0)
GRONN = (0, 255, 0)
BLA = (0, 0, 255)
GRAA = (150, 150, 150)

VINDU_BREDDE, VINDU_HOYDE = 400, 400

class Plass:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.pasientplass = False
        self.gulvplass = True
        self.lege_paa_plass = False
        self.restutisjon = r.randint(1, 100)
        self.helse = 0.1
        self.kunnskaps_farger = ["white", "yellow", "orange", "green", "blue", "purple", "brown"]

    def tegn(self, vindu, lengde):
        if self.gulvplass:
            pg.draw.rect(vindu, "lightyellow", (self.x, self.y, lengde, lengde))
            pg.draw.rect(vindu, "black", (self.x, self.y, lengde, lengde), 1)
        if self.pasientplass:
            pg.draw.rect(vindu, f'gray{self.restutisjon}', (self.x, self.y, lengde, lengde))
            pg.draw.rect(vindu, "black", (self.x, self.y, lengde, lengde), 1)
            pg.draw.circle(vindu, self.kunnskaps_farger[m.floor(self.helse)], ((self.x + lengde / 2), (self.y + lengde / 2)), lengde / 3)
        if self.lege_paa_plass:
            pg.draw.rect(vindu, "lightyellow", (self.x, self.y, lengde, lengde))
            pg.draw.circle(vindu, "brown", ((self.x + lengde / 2), (self.y + lengde / 2)), lengde / 3)
            pg.draw.rect(vindu, "black", (self.x, self.y, lengde, lengde), 1)

class Rom:
    def __init__(self, vindu: pg.surface):
        self.vindu = vindu
        self.kolonner = 10
        self.rader = 10
        self.lengde = VINDU_BREDDE // self.kolonner
        self.rom = [[Plass(i * self.lengde, j * self.lengde) for j in range(self.rader)] for i in range(self.kolonner)]

    def start(self):
        for i in range(self.rader):
            for j in range(self.kolonner):
                if i == 0 and j == 0:
                    self.rom[j][i].lege_paa_plass = True
                if i in [1, 2, 4, 5, 7, 8] and j in [2, 3, 6, 7]:
                    self.rom[j][i].pasientplass = True

    def tegn_sykehus(self):
        for i in range(self.rader):
            for j in range(self.kolonner):
                self.rom[j][i].tegn(self.vindu, self.lengde)

    def lege_naer(self):
        for i in range(self.rader):
            for j in range(self.kolonner):
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x != 0 and y != 0:
                            continue
                        if (0 <= i + x < self.rader) and (0 <= j + y < self.kolonner):
                            if self.rom[j + y][i + x].lege_paa_plass and self.rom[j][i].pasientplass:
                                self.rom[j][i].helse += 0.6

    def flytt_lege(self):
        for i in range(self.rader):
            for j in range(self.kolonner):
                if self.rom[j][i].lege_paa_plass:
                    self.rom[j][i].lege_paa_plass = False
        x = [0, 1, 4, 5, 8, 9]
        y = [0, 3, 6, 9]
        x_en = r.choice(x)
        y_en = r.choice(y)
        self.rom[x_en][y_en].lege_paa_plass = True

    def oppdater_helse(self):
        for i in range(self.rader):
            for j in range(self.kolonner):
                plass = self.rom[j][i]
                if plass.pasientplass:
                    if r.randint(1, 100) <= plass.restutisjon:
                        firepasienter = []
                        for x in [-1, 0, 1]:
                            for y in [-1, 0, 1]:
                                if abs(x) + abs(y) == 1:
                                    nabo_x, nabo_y = j + x, i + y
                                    if 0 <= nabo_x < self.kolonner and 0 <= nabo_y < self.rader:
                                        nabo_plass = self.rom[nabo_x][nabo_y]
                                        if nabo_plass.pasientplass:
                                            firepasienter.append(nabo_plass.helse)
                        gjennomsnitt_helse = sum(firepasienter) / len(firepasienter) if firepasienter else 0
                        helseoekning = 0.05 * gjennomsnitt_helse + 0.2
                        plass.helse = min(plass.helse + helseoekning, 6.9)

    def avsluttspill(self):
        for i in range(self.rader):
            for j in range(self.kolonner):
                plass = self.rom[j][i]
                if plass.lege_paa_plass:
                    plass.lege_paa_plass = False
                    pg.draw.circle(self.vindu, "white", ((plass.x + self.lengde / 2), (plass.y + self.lengde / 2)), self.lengde / 3)
        total_helse = 0
        antall_elever = 0
        for i in range(self.rader):
            for j in range(self.kolonner):
                plass = self.rom[j][i]
                if plass.pasientplass:
                    total_helse += plass.helse
                    antall_elever += 1
        gjennomsnitt_helse = total_helse / antall_elever if antall_elever > 0 else 0
        font = pg.font.SysFont("Arial", 14)
        tekst = font.render(f"Gj.snitt helse: {gjennomsnitt_helse:.2f}", True, SVART)
        tekst_rect = tekst.get_rect(center=(VINDU_BREDDE // 2, VINDU_HOYDE - 10))
        self.vindu.blit(tekst, tekst_rect)

# === Init og hovedløkke ===
pg.init()
vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
pg.display.set_caption("Sykehussimulering")
font = pg.font.SysFont("Arial", 16)

sykehuset = Rom(vindu)
sykehuset.start()

fortsett = True
pause = False
tallet = 0

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pause = not pause

    sykehuset.tegn_sykehus()
    pause_tekst = "Trykk SPACE for å fortsette" if pause else "Trykk SPACE for å pause"
    tekst_surface = font.render(pause_tekst, True, SVART)
    vindu.blit(tekst_surface, (10, VINDU_HOYDE - 30))

    if not pause and tallet <= 70 * 90:
        if tallet % 70 == 0 and tallet != 0:
            sykehuset.flytt_lege()
            sykehuset.lege_naer()
            sykehuset.oppdater_helse()

    if tallet == 70 * 90:
        sykehuset.avsluttspill()
        pause = True  # 🔧 NYTT: stopp simulering, men hold vinduet åpent

    if not pause and tallet < 70 * 90:
        tallet += 1

    pg.display.flip()

pg.quit()

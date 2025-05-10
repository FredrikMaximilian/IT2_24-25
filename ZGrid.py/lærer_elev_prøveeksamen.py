import pygame
import sys
import random

# --- Innstillinger ---
rader, kolonner = 16, 8
cellestørrelse = 40
bredde = kolonner * cellestørrelse
høyde = rader * cellestørrelse
FPS = 10
MINUTTER_TOTALT = 90

# --- Farger ---
BAKGRUNN = (245, 222, 179)  # Lys beige
BORDGRÅ = (60, 60, 60)
LÆRERFARGE = (139, 69, 19)
FERDIGFARGE = (255, 255, 255)
KUNNSKAPSFARGER = [
    (255, 255, 255),  # 0
    (255, 255, 0),    # 1
    (255, 165, 0),    # 2
    (0, 255, 0),      # 3
    (0, 0, 255),      # 4
    (128, 0, 128),    # 5
    (165, 42, 42)     # 6
]

# --- Bordplassering ---
sitteplasser = [
    (1, 1), (1, 2), (2, 1), (2, 2), (5, 1), (5, 2), (6, 1), (6, 2),
    (9, 1), (9, 2), (10, 1), (10, 2), (13, 1), (13, 2), (14, 1), (14, 2),
    (1, 5), (1, 6), (2, 5), (2, 6), (5, 5), (5, 6), (6, 5), (6, 6),
    (9, 5), (9, 6), (10, 5), (10, 6), (13, 5), (13, 6), (14, 5), (14, 6)
]

firerbord = [
    [(1,1), (1,2), (2,1), (2,2)],
    [(5,1), (5,2), (6,1), (6,2)],
    [(9,1), (9,2), (10,1), (10,2)],
    [(13,1), (13,2), (14,1), (14,2)],
    [(1,5), (1,6), (2,5), (2,6)],
    [(5,5), (5,6), (6,5), (6,6)],
    [(9,5), (9,6), (10,5), (10,6)],
    [(13,5), (13,6), (14,5), (14,6)],
]

# --- Klasser ---
class Elev:
    def __init__(self):
        self.kunnskap = 0.0
        self.drivkraft = random.randint(0, 33)
        self.økning = 0.0

    def kunnskapsfarge(self):
        nivå = min(int(self.kunnskap), 6)
        return KUNNSKAPSFARGER[nivå]

class Plass:
      def __init__(self, rad, kol):
        self.rad = rad
        self.kol = kol
        self.er_bord = (rad, kol) in sitteplasser
        self.laerer = False
        self.elev = Elev() if self.er_bord else None

      def tegn(self, skjerm, ferdig=False):
         x = self.kol * cellestørrelse
         y = self.rad * cellestørrelse
         pygame.draw.rect(skjerm, BAKGRUNN, (x, y, cellestørrelse, cellestørrelse))

         if self.er_bord:
            # Fargen til bord basert på drivkraft
            gråverdi = int((self.elev.drivkraft / 33) * 255)
            gråfarge = (gråverdi, gråverdi, gråverdi)
            pygame.draw.rect(skjerm, gråfarge, (x, y, cellestørrelse, cellestørrelse))

            # Elevsirkel basert på kunnskapsnivå
            farge = self.elev.kunnskapsfarge()
            pygame.draw.circle(skjerm, farge, (x + cellestørrelse//2, y + cellestørrelse//2), 10)

         else:
            if self.laerer:
                  farge = FERDIGFARGE if ferdig else LÆRERFARGE
                  pygame.draw.circle(skjerm, farge, (x + cellestørrelse//2, y + cellestørrelse//2), 10)


class Klasserom:
    def __init__(self):
        self.plasser = [[Plass(r, k) for k in range(kolonner)] for r in range(rader)]
        self.laererpos = (0, 0)
        self.plasser[0][0].laerer = True
        self.minutt = 0

    def tegn(self, skjerm, ferdig=False):
        for rad in self.plasser:
            for plass in rad:
                plass.tegn(skjerm, ferdig)

    def rundt(self, rad, kol):
        nabolag = []
        for dr in [-1, 0, 1]:
            for dk in [-1, 0, 1]:
                if dr == 0 and dk == 0:
                    continue
                r, k = rad + dr, kol + dk
                if 0 <= r < rader and 0 <= k < kolonner:
                    nabolag.append((r, k))
        return nabolag

    def flytt_lærer(self):
        gulvplasser = [(r, k) for r in range(rader) for k in range(kolonner) if not self.plasser[r][k].er_bord]
        nypos = random.choice(gulvplasser)
        gammel = self.laererpos
        self.plasser[gammel[0]][gammel[1]].laerer = False
        self.laererpos = nypos
        self.plasser[nypos[0]][nypos[1]].laerer = True

    def oppdater_kunnskap(self):
        # 1. Lærer flytter
        self.flytt_lærer()
        lr, lk = self.laererpos
        nabolag = self.rundt(lr, lk)
        elever_nær = [self.plasser[r][k].elev for (r, k) in nabolag if self.plasser[r][k].er_bord]

        for elev in elever_nær[:2]:
            if elev.kunnskap < 6.0:
                elev.økning = 0.3
            else:
                elev.økning = 0.0

        # 2. Samarbeid på bord
        for bord in firerbord:
            elever = [self.plasser[r][k].elev for (r, k) in bord]
            gjennomsnitt = sum(e.kunnskap for e in elever) / 4
            for elev in elever:
                if elev.kunnskap >= 6.0:
                    elev.økning = 0.0
                elif elev not in elever_nær:
                    if random.random() < elev.drivkraft / 100:
                        elev.økning = 0.05 * gjennomsnitt + 0.2
                    else:
                        elev.økning = 0.0

        # 3. Oppdater
        for rad in self.plasser:
            for plass in rad:
                if plass.er_bord:
                    elev = plass.elev
                    if elev.kunnskap < 6.0:
                        elev.kunnskap = min(elev.kunnskap + elev.økning, 6.9)

# --- Kjøring ---
pygame.init()
skjerm = pygame.display.set_mode((bredde, høyde))
pygame.display.set_caption("Oppg 9")
klokke = pygame.time.Clock()
klasserom = Klasserom()
ferdig = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    skjerm.fill(BAKGRUNN)

    if klasserom.minutt < MINUTTER_TOTALT:
        klasserom.oppdater_kunnskap()
        klasserom.minutt += 1
    elif not ferdig:
        ferdig = True
        # Kalkuler snitt
        elever = [plass.elev for rad in klasserom.plasser for plass in rad if plass.er_bord]
        snitt = sum(e.kunnskap for e in elever) / len(elever)
        snitt_text = f"Gjennomsnittlig kunnskap: {snitt:.2f}"
        font = pygame.font.SysFont(None, 28)
        tekst = font.render(snitt_text, True, (0, 0, 0))
        skjerm.blit(tekst, (10, høyde - 30))

    klasserom.tegn(skjerm, ferdig)
    pygame.display.flip()
    klokke.tick(FPS)

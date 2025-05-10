import pygame as pg
import random

# Pygame-oppsett
pg.init()
BREDDE, HOYDE = 800, 200
vindu = pg.display.set_mode((BREDDE, HOYDE))
pg.display.set_caption("Trafikksimulering")
klokke = pg.time.Clock()

# Farger
HVIT = (255, 255, 255)
GRÅ = (180, 180, 180)
RØD = (200, 0, 0)
GRØNN = (0, 180, 0)
BILFARGER = [(0, 0, 255), (255, 165, 0), (128, 0, 128), (0, 128, 128)]

# Konstanter
BIL_BREDDE = 40
BIL_HOYDE = 20
VEI_Y = HOYDE // 2 - BIL_HOYDE // 2
HASTIGHET = 2
ANTALL_BILER = 5
LYS_POSISJON = 600
LYS_INTERVALL = 120  # antall frames før skifte

# Klasse for biler
class Bil:
    def __init__(self, x):
        self.x = x
        self.farge = random.choice(BILFARGER)
        self.stoppet = False
    """
    def flytt(self, biler_foran, lys):
        # Hvis bilen er utenfor skjermen – start på nytt
        if self.x > BREDDE:
            self.x = -BIL_BREDDE

        # Sjekk avstand til bil foran
        for bil in biler_foran:
            if bil.x > self.x and bil.x - self.x < BIL_BREDDE + 5:
                self.stoppet = True
                return

        # Sjekk avstand til trafikklys
        if self.x + BIL_BREDDE >= LYS_POSISJON - 5 and not lys.er_grønt():
            self.stoppet = True
            return

        # Hvis ingen hindringer – kjør
        self.stoppet = False
        self.x += HASTIGHET"""
        
    def flytt(self, biler_foran, lys):
        if self.x > BREDDE:
            self.x = -BIL_BREDDE

        # Sjekk bil foran
        for bil in biler_foran:
            if bil.x > self.x and bil.x - self.x < BIL_BREDDE + 5:
                self.stoppet = True
                return

        # Sjekk trafikklys – kun hvis ingen bil er foran deg
        if not biler_foran:
            if self.x + BIL_BREDDE >= LYS_POSISJON - 5 and not lys.er_grønt():
                self.stoppet = True
                return

        # Hvis ingen hindringer – kjør
        self.stoppet = False
        self.x += HASTIGHET


    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, (self.x, VEI_Y, BIL_BREDDE, BIL_HOYDE))

# Klasse for trafikklys
class Trafikklys:
    def __init__(self, x):
        self.x = x
        self.ramme = pg.Rect(x, VEI_Y - 40, 20, 60)
        self.rødt = True
        self.teller = 0

    def oppdater(self):
        self.teller += 1
        if self.teller >= LYS_INTERVALL:
            self.rødt = not self.rødt
            self.teller = 0

    def tegn(self, vindu):
        pg.draw.rect(vindu, GRÅ, self.ramme)
        if self.rødt:
            pg.draw.circle(vindu, RØD, (self.x + 10, VEI_Y - 25), 8)
        else:
            pg.draw.circle(vindu, GRØNN, (self.x + 10, VEI_Y - 10), 8)

    def er_grønt(self):
        return not self.rødt

# Opprett biler og trafikklys
biler = [Bil(x * -100) for x in range(ANTALL_BILER)]  # Plasser dem med mellomrom
lys = Trafikklys(LYS_POSISJON)

# Simuleringsstatus
pause = False

# Hovedløkke
kjør = True
while kjør:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjør = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pause = not pause

    if not pause:
        lys.oppdater()
        for i, bil in enumerate(biler):
            biler_foran = biler[:i]
            bil.flytt(biler_foran, lys)

    # Tegn alt
    vindu.fill(HVIT)
    pg.draw.rect(vindu, GRÅ, (0, VEI_Y, BREDDE, BIL_HOYDE))  # Vei
    lys.tegn(vindu)
    for bil in biler:
        bil.tegn(vindu)

    pg.display.flip()
    klokke.tick(60)

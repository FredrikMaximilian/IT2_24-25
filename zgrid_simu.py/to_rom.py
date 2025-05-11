import pygame as pg
import sys

# --- Konfigurasjon ---
SKJERM_BREDDE, SKJERM_HOYDE = 640, 480
FPS = 60
SPILLER_FART = 20

# Farger (R, G, B)
HVIT            = (255, 255, 255)
ROM1_FARGE      = (100, 149, 237)  # lys blå
ROM2_FARGE      = (34, 139, 34)    # skogsgrønn
DOR_FARGE       = (139, 69, 19)    # brun
SKATT_FARGE     = (255, 215, 0)    # gull
FELLE_FARGE     = (255, 0, 0)      # rød
SPILLER_FARGE   = (200, 200, 200)  # lys grå

pg.init()
skjerm = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HOYDE))
pg.display.set_caption("Skattejakt i forlatt ruin")
ur = pg.time.Clock()
font = pg.font.SysFont(None, 24)

# --- Klasser ---
class Spiller:
    """
    Representerer spilleren (arkeologen).
    Flytter seg med piltastene og kolliderer med objekter.
    """
    def __init__(self, pos):
        self.rekt = pg.Rect(pos[0], pos[1], 32, 32)
        self.fart = SPILLER_FART
        self.vx = 0
        self.vy = 0

    def behandle_inndata(self):
        """Leser tastetrykk og oppdaterer hastighet"""
        taster = pg.key.get_pressed()
        self.vx, self.vy = 0, 0
        if taster[pg.K_LEFT]:  self.vx = -self.fart
        if taster[pg.K_RIGHT]: self.vx =  self.fart
        if taster[pg.K_UP]:    self.vy = -self.fart
        if taster[pg.K_DOWN]:  self.vy =  self.fart

    def oppdater(self):
        """Oppdaterer posisjon og hindrer at spilleren går utenfor skjermen"""
        self.rekt.x += self.vx
        self.rekt.y += self.vy
        self.rekt.clamp_ip(skjerm.get_rect())

    def tegn(self, overflate):
        """Tegner spilleren som en firkant"""
        pg.draw.rect(overflate, SPILLER_FARGE, self.rekt)

class Rom:
    """
    Representerer et rom i eventyrspillet.
    Har bakgrunnsfarge, en dør, skatter og feller.
    """
    def __init__(self, bakgrunn, dor_rekt, dor_mal, start_pos):
        self.bakgrunnsfarge = bakgrunn
        self.dor_rekt       = dor_rekt       # pg.Rect for døren
        self.dor_mal        = dor_mal        # indeks til målet rom
        self.start_pos      = start_pos      # hvor spiller spawner
        self.skatter        = []             # liste av pg.Rect
        self.feller         = []             # liste av pg.Rect

    def tegn(self, overflate):
        """Tegner rommet: bakgrunn, dør, skatter og feller"""
        overflate.fill(self.bakgrunnsfarge)
        pg.draw.rect(overflate, DOR_FARGE, self.dor_rekt)
        for skatt in self.skatter:
            pg.draw.rect(overflate, SKATT_FARGE, skatt)
        for felle in self.feller:
            pg.draw.rect(overflate, FELLE_FARGE, felle)

# --- Opprett rommene ---
rom1 = Rom(
    bakgrunn = ROM1_FARGE,
    dor_rekt  = pg.Rect(620, 200, 20, 80),
    dor_mal   = 1,
    start_pos = (550, 220)
)
rom2 = Rom(
    bakgrunn = ROM2_FARGE,
    dor_rekt  = pg.Rect(0, 200, 20, 80),
    dor_mal   = 2,
    start_pos = (50, 220)
)
rom_start = Rom(
    bakgrunn = ROM1_FARGE,
    dor_rekt  = pg.Rect(620, 200, 20, 80),
    dor_mal   = 1,
    start_pos = (50, 220)
)



# Legger til skatter og feller i hvert rom
rom_start.skatter = [pg.Rect(300, 100, 20, 20)]
rom_start.feller  = [pg.Rect(400, 300, 20, 20)]
rom1.skatter = [pg.Rect(300, 100, 20, 20)]
rom1.feller  = [pg.Rect(400, 300, 20, 20)]
rom2.skatter = [pg.Rect(300, 100, 50, 20)]
rom2.feller  = [pg.Rect(400, 300, 30, 20)]

rommer = [rom_start, rom1, rom2]
aktuelt_rom = rommer[0]
spiller = Spiller(rom_start.start_pos)

poeng = 0

# --- Hovedløkke ---
kjører = True
game_over = False
while kjører:
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            kjører = False

    # Inndata og bevegelse
    spiller.behandle_inndata()
    spiller.oppdater()

    # Kollisjon med dør: bytt rom og plasser spiller
    
    if spiller.rekt.colliderect(aktuelt_rom.dor_rekt):
        if aktuelt_rom == rommer[0]:
            aktuelt_rom = rommer[2]
        elif aktuelt_rom == rommer[2]:
            aktuelt_rom = rommer[1]
        elif aktuelt_rom == rommer[1]:
            aktuelt_rom = rommer[2]
        spiller.rekt.topleft = aktuelt_rom.start_pos



    # Kollisjon med felle: død
    for felle in aktuelt_rom.feller:
        if spiller.rekt.colliderect(felle):
            game_over = True

    # Kollisjon med skatt: øk poeng og fjern skatt
    for skatt in aktuelt_rom.skatter[:]:
        if spiller.rekt.colliderect(skatt):
            aktuelt_rom.skatter.remove(skatt)
            poeng += 1

    # Tegn alt
    aktuelt_rom.tegn(skjerm)
    spiller.tegn(skjerm)

    # UI: viser poeng og instruksjoner
    poeng_tekst = font.render(f"Poeng: {poeng}", True, HVIT)
    skjerm.blit(poeng_tekst, (10, 10))
    instruksjon = font.render("Piler: beveg    Gå gjennom dør    Unngå feller", True, HVIT)
    skjerm.blit(instruksjon, (10, SKJERM_HOYDE - 30))

    
    if game_over:
        font = pg.font.SysFont("Arial", 40)
        tekst = font.render("Game Over", True, (255, 0, 0))
        skjerm.blit(tekst, (SKJERM_BREDDE//2 - tekst.get_width()//2, SKJERM_HOYDE//2 - tekst.get_height()//2))
        pg.display.flip()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

    pg.display.flip()
    ur.tick(FPS)

pg.quit()
sys.exit()
import pygame as pg
import sys
import random

# --- Konfigurasjon ---
SKJERM_BREDDE, SKJERM_HOYDE = 640, 480
FPS = 60
SPILLER_FART = 20  # piksler per oppdatering

# Farger (R, G, B)
HVIT           = (255, 255, 255)
ROM_FARGER     = [(100, 149, 237), (34, 139, 34), (210, 180, 140), (181, 101, 29)]
DOR_FARGE      = (139, 69, 19)
SKATT_FARGE    = (255, 215, 0)
FELLE_FARGE    = (255, 0, 0)
SPILLER_FARGE  = (200, 200, 200)
ROM1_FARGE = (255, 255, 255)

pg.init()
skjerm = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HOYDE))
pg.display.set_caption("Skattejakt i forlatte ruiner")
ur = pg.time.Clock()
font = pg.font.SysFont(None, 24)
font_store = pg.font.SysFont(None, 48)

# --- Klasser ---
class Spiller:
    def __init__(self, pos):
        x, y = pos
        self.rekt = pg.Rect(x, y, 32, 32)
        self.fart = SPILLER_FART
        self.vx = 0
        self.vy = 0

    def behandle_inndata(self):
        taster = pg.key.get_pressed()
        self.vx, self.vy = 0, 0
        if taster[pg.K_LEFT]:   self.vx = -self.fart
        if taster[pg.K_RIGHT]:  self.vx =  self.fart
        if taster[pg.K_UP]:     self.vy = -self.fart
        if taster[pg.K_DOWN]:   self.vy =  self.fart

    def oppdater(self):
        self.rekt.x += self.vx
        self.rekt.y += self.vy
        self.rekt.clamp_ip(skjerm.get_rect())

    def tegn(self, overflate):
        pg.draw.rect(overflate, SPILLER_FARGE, self.rekt)

class Rom:
    def __init__(self, bakgrunnsfarge, venstre_dor, hoyre_dor, spawn_from_left, spawn_from_right):
        self.bakgrunnsfarge = bakgrunnsfarge
        self.venstre_dor = venstre_dor     # pygame.Rect for dør på venstre
        self.hoyre_dor = hoyre_dor         # pygame.Rect for dør på høyre
        # start_pos dictionaries for hvilken side spilleren kom fra
        self.spawn_from = {
            'left': spawn_from_left,
            'right': spawn_from_right
        }
        self.skatter = []
        self.feller = []

    def tegn(self, overflate):
        overflate.fill(self.bakgrunnsfarge)
        # Tegn dører
        pg.draw.rect(overflate, DOR_FARGE, self.venstre_dor)
        pg.draw.rect(overflate, DOR_FARGE, self.hoyre_dor)
        # Tegn skatter og feller
        for skatt in self.skatter:
            pg.draw.rect(overflate, SKATT_FARGE, skatt)
        for felle in self.feller:
            pg.draw.rect(overflate, FELLE_FARGE, felle)

# --- Funksjon for å opprette nye rom ---
def nytt_rom(idx):
    # Velg bakgrunnsfarge tilfeldig
    bg = random.choice(ROM_FARGER)
    # Dør-parametre
    door_w, door_h = 20, 80
    door_y = (SKJERM_HOYDE - door_h) // 2
    # Venstre dør
    venstre_dor = pg.Rect(0, door_y, door_w, door_h)
    spawn_from_left = (venstre_dor.right + 20, door_y + door_h//2 - 16)
    # Høyre dør
    hoyre_dor = pg.Rect(SKJERM_BREDDE - door_w, door_y, door_w, door_h)
    spawn_from_right = (hoyre_dor.left - 20 - 32, door_y + door_h//2 - 16)
    # Lag rom
    rom = Rom(bg, venstre_dor, hoyre_dor, spawn_from_left, spawn_from_right)
    # Fyll med skatter
    for _ in range(random.randint(1, 3)):
        x = random.randint(100, SKJERM_BREDDE - 120)
        y = random.randint(50, SKJERM_HOYDE - 100)
        rom.skatter.append(pg.Rect(x, y, 20, 20))
    # Fyll med feller
    for _ in range(random.randint(1, 2)):
        x = random.randint(100, SKJERM_BREDDE - 120)
        y = random.randint(50, SKJERM_HOYDE - 100)
        rom.feller.append(pg.Rect(x, y, 20, 20))
    return rom

# --- Initialisering ---
rommer = {}
rommer[0] = nytt_rom(0)
current_index = 0
current_room = rommer[0]
# Startspilleren i rom 0, kom fra venstre (ingen, men vi bruk spawn_from['left'])
spiller = Spiller(current_room.spawn_from['left'])
poeng = 0
game_over = False

# --- Spilløkke ---
while True:
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if not game_over:
        # Input og bevegelse
        spiller.behandle_inndata()
        spiller.oppdater()

        # Dør-kollisjon
        if spiller.rekt.colliderect(current_room.venstre_dor):
            side = 'left'
        elif spiller.rekt.colliderect(current_room.hoyre_dor):
            side = 'right'
        else:
            side = None

        if side:
            # Bestem neste indeks
            if side == 'left':
                next_index = current_index - 1

            else:
                next_index = current_index + 1
            # Opprett rom om nødvendig
            if next_index not in rommer:
                rommer[next_index] = nytt_rom(next_index)
                print(next_index)
            # Bytt variabler
            current_index = next_index
            current_room = rommer[current_index]
            # Spawn spiller på motsatt side
            oppside = 'right' if side == 'left' else 'left'
            spiller.rekt.topleft = current_room.spawn_from[oppside]

        # Felle-kollisjon
        #for felle in current_room.feller:
            #if spiller.rekt.colliderect(felle):
            #    game_over = True

        # Skatt-kollisjon
        for skatt in current_room.skatter[:]:
            if spiller.rekt.colliderect(skatt):
                current_room.skatter.remove(skatt)
                poeng += 1

    # Tegn alt
    current_room.tegn(skjerm)
    spiller.tegn(skjerm)

    # UI: poeng og instruksjoner
    tekst_poeng = font.render(f"Poeng: {poeng}", True, HVIT)
    skjerm.blit(tekst_poeng, (10, 10))
    instr = font.render("Piler: beveg   Gå gjennom dør   Unngå feller", True, HVIT)
    skjerm.blit(instr, (10, SKJERM_HOYDE - 30))

    # Game over
    if game_over:
        go_tekst = font_store.render("GAME OVER", True, (255, 0, 0))
        skjerm.blit(go_tekst, (SKJERM_BREDDE//2 - go_tekst.get_width()//2,
                               SKJERM_HOYDE//2 - go_tekst.get_height()//2))

    pg.display.flip()
    ur.tick(FPS)
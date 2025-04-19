import pygame
import sys
import random as rd

# Konstanter
bredde, høyde = 500, 500
rader, kolonner = 9, 9
cellestørrelse = bredde // kolonner
palett_høyde = 50

antall_ruter = rader * kolonner
antall_miner = 10
trygge_miner_trykket = 0

# farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRÅ = (200, 200, 200)
TRYKKEGRÅ = "slategray"
RØD = (255, 0, 0)
BLÅ = (0, 0, 255)

fargetall = {
    1: (0, 0, 255),       # blå
    2: (0, 128, 0),       # grønn
    3: (255, 0, 0),       # rød
    4: (0, 0, 128),       # mørk blå
    5: (139, 69, 19),     # brun
    6: (0, 255, 255),     # cyan
    7: (0, 0, 0),         # svart
    8: (128, 128, 128)    # grå
}

# Initialiser pygame
pygame.init()
skjerm = pygame.display.set_mode((bredde, høyde))
pygame.display.set_caption("Minesveiper")
game_over = False

class Rute:
    def __init__(self):
      self.har_mine = False
      self.trykket = False
      self.første = False
    
    def farge(self):
        if self.trykket:
          if self.har_mine:
            if self.første:
               return RØD
            return SVART
          else:
             return TRYKKEGRÅ
        return HVIT
    
    def tell_nabo_miner(self, rad, kol, brett):
        antall = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                ny_rad = rad + dx
                ny_kol = kol + dy
                if 0 <= ny_rad < rader and 0 <= ny_kol < kolonner:
                    if brett[ny_rad][ny_kol].har_mine:
                        antall += 1
        return antall

brett = [[Rute() for _ in range(kolonner)] for _ in range(rader)]

alle_posisjoner = [(r, k) for r in range(rader) for k in range(kolonner)]
mine_posisjoner = rd.sample(alle_posisjoner, antall_miner)

for r, k in mine_posisjoner:
   brett[r][k].har_mine = True

# Funksjon for å tegne opp brettet
def tegnBrett():
    for rad in range(rader):
        for kol in range(kolonner):
            rute = brett[rad][kol]
            farge = rute.farge()
            pygame.draw.rect(skjerm, farge, (kol * cellestørrelse, rad * cellestørrelse, cellestørrelse, cellestørrelse))
            pygame.draw.rect(skjerm, GRÅ, (kol * cellestørrelse, rad * cellestørrelse, cellestørrelse, cellestørrelse), 1)

            #tegn tall
            if rute.trykket and not rute.har_mine:
                antall = rute.tell_nabo_miner(rad, kol, brett)
                if antall > 0:
                    font = pygame.font.SysFont("Arial", 24)
                    farge_tall = fargetall.get(antall, SVART)
                    tekst = font.render(str(antall), True, farge_tall)
                    tekst_rect = tekst.get_rect(center=(kol * cellestørrelse + cellestørrelse // 2,
                                                        rad * cellestørrelse + cellestørrelse // 2))
                    skjerm.blit(tekst, tekst_rect)


fortsett = True
seier = False

while fortsett:
  if game_over:
    fortsett = False
    continue

  for hendelse in pygame.event.get():
    if hendelse.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    elif hendelse.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        rad, kol = y // cellestørrelse, x // cellestørrelse
        if not brett[rad][kol].trykket:
            brett[rad][kol].trykket = True

        if not brett[rad][kol].har_mine:
            trygge_miner_trykket += 1

            if trygge_miner_trykket == antall_ruter-antall_miner:
                seier = True
                fortsett = False
                brett[rad][kol].første = True
                for r, k in mine_posisjoner:
                    brett[r][k].trykket = True

        else:
            game_over = True
            brett[rad][kol].første = True
            for r, k in mine_posisjoner:
                brett[r][k].trykket = True


  skjerm.fill(HVIT)
  tegnBrett()
  


  if seier:
        font = pygame.font.SysFont("Arial", 40)
        tekst = font.render("Seier", True, (0, 255, 255))
        skjerm.blit(tekst, (bredde//2 - tekst.get_width()//2, høyde//2 - tekst.get_height()//2))
        pygame.display.flip()
              
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

  if game_over:
        font = pygame.font.SysFont("Arial", 40)
        tekst = font.render("Game Over", True, (0, 255, 255))
        skjerm.blit(tekst, (bredde//2 - tekst.get_width()//2, høyde//2 - tekst.get_height()//2))
        pygame.display.flip()
              
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

  pygame.display.flip()
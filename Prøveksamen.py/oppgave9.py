import pygame
import sys
import random as rd

# Konstanter
bredde, høyde = 500, 700
rader, kolonner = 16, 8
cellestørrelse = 40
palett_høyde = 600

antall_ruter = rader * kolonner

# farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRÅ = (200, 200, 200)
TRYKKEGRÅ = "slategray"
RØD = (255, 0, 0)
BLÅ = (0, 0, 255)

en = "white"
to = "yellow"
tre = "orange"
fire = "green"
fem = "blue"
seks = "lilla"
syv = "brun"

sitteplasser = [(1, 1), (1, 2), (2, 1), (2, 2), (5, 1), (5, 2), (6, 1), (6, 2), (9, 1), (9, 2), (10, 1), (10, 2),
 (13, 1), (13, 2), (14, 1), (14, 2), (1, 5), (1, 6), (2, 5), (2, 6), (5, 5), (5, 6), (6, 5), (6, 6), 
 (9, 5), (9, 6), (10, 5), (10, 6), (13, 5), (13, 6), (14, 5), (14, 6)]

alle_posisjoner = [(r, k) for r in range(rader) for k in range(kolonner)]
gulvplasser = []
for posisjon in alle_posisjoner:
   if posisjon not in sitteplasser:
      gulvplasser.append(posisjon)

class Elev:
    def __init__(self, kunnskap: float, ):
        self.kunnskap = kunnskap
        self.posisjon = sitteplasser
    
    def drivkraft(self):
       drivkraft = rd.randint(0, 33)
       return drivkraft
    
    def fargePåBord(self):
       gråfarge = self.drivkraft * 7
       farge = (gråfarge, gråfarge, gråfarge)
       return farge
    
    def fargePåElev(self):
       if self.kunnskap < 0.9:
          return en
       if self.kunnskap < 1.9:
          return to
       if self.kunnskap < 2.9:
          return tre
       if self.kunnskap < 3.9:
          return fire
       if self.kunnskap < 4.9:
          return fem
       if self.kunnskap < 5.9:
          return seks
       if self.kunnskap > 5.9:
          return syv
       
    def tegnElev(self):
       self.radius = 10
       self.vindusobjekt = skjerm
       self.x = self.rad * cellestørrelse  # Beregner x-posisjonen til ruten
       self.y = self.kolonne * cellestørrelse  # Beregner y-posisjonen til ruten
       elevsirkel = pygame.draw.circle(self.vinduobjekt, self.fargePåElev, (self.x, self.y), self.radius)
       return elevsirkel

class Lærer:
    def __init__(self):
      self.posisjon = gulvplasser
      self.farge = "brown"
    
    def tegnLærer(self):
       self.x = self.posisjon[0]
       self.y = self.posisjon[1]

    def startposisjon(self):
       self.x = 0
       self.y = 0


# Initialiser pygame
pygame.init()
skjerm = pygame.display.set_mode((bredde, høyde))
pygame.display.set_caption("Klasserom")


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
    
def genererElev():
    global sitteplasser
    elevliste = []
    for i in range(24):
        radius = rd.randint(10, 15)
        xfart = 0
        yfart = 0
        kunnskap = 0
        x, y = sitteplasser
        elev = Elev(x, y, radius, kunnskap, skjerm, xfart, yfart)
        elevliste.append(elev)
    return elevliste

brett = [[Rute() for _ in range(kolonner)] for _ in range(rader)]


for r, k in sitteplasser:
   brett[r][k].er_elev = True

# Funksjon for å tegne opp brettet
def tegnBrett():
    for rad in range(rader):
        for kol in range(kolonner):
            rute = brett[rad][kol]
            farge = rute.farge()
            pygame.draw.rect(skjerm, farge, (kol * cellestørrelse, rad * cellestørrelse, cellestørrelse, cellestørrelse))
            pygame.draw.rect(skjerm, GRÅ, (kol * cellestørrelse, rad * cellestørrelse, cellestørrelse, cellestørrelse), 1)


fortsett = True
seier = False

while fortsett:

  for hendelse in pygame.event.get():
    if hendelse.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    else:
        for r, k in sitteplasser:
                brett[r][k].trykket = True


  skjerm.fill(HVIT)
  tegnBrett()
  
  pygame.display.flip()
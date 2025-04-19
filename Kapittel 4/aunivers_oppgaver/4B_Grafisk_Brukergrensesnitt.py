###Museklikk og musepekerens posisjon
##Fargetrykk med viskelær og markør
"""
import pygame
import sys

# Konstanter
bredde, høyde = 800, 600
rader, kolonner = 20, 20
cellestørrelse = bredde // kolonner
palett_høyde = 50

# farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRÅ = (200, 200, 200)
farger = [
  (255, 0, 0),   # Rød
  (0, 255, 0),   # Grønn
  (0, 0, 255),   # Blå
  (60, 60, 60), # Gul
  (255, 165, 0), # Oransje
  (0, 255, 255), # Cyan
  (255, 0, 255)  # Magenta
]

# Initialiser pygame
pygame.init()

# Setter opp skjermen
skjerm = pygame.display.set_mode((bredde, høyde))
pygame.display.set_caption("Tegnebrett")

# Lager en todimensjonal liste som representerer brettet, 
# der hver rute har fargen hvit
brett = [[HVIT for k in range(kolonner)] for r in range(rader)]

# Valgt farge
valgtFarge = HVIT

# Funksjon for å tegne opp brettet
def tegnBrett():
  for rad in range(rader):
    for kol in range(kolonner):
      pygame.draw.rect(skjerm, brett[rad][kol], (kol * cellestørrelse, rad * cellestørrelse, cellestørrelse, cellestørrelse))
      pygame.draw.rect(skjerm, GRÅ, (kol * cellestørrelse, rad * cellestørrelse, cellestørrelse, cellestørrelse), 1)

# Funksjon for å tegne opp fargepaletten
def tegnPalett():
  for i in range(len(farger)):
    pygame.draw.rect(skjerm, farger[i], (i * cellestørrelse, høyde - palett_høyde, cellestørrelse, palett_høyde))
    pygame.draw.rect(skjerm, GRÅ, (i * cellestørrelse, høyde - palett_høyde, cellestørrelse, palett_høyde), 1)

    if valgtFarge == farger[i]:
      pygame.draw.rect(skjerm, SVART, (i * cellestørrelse, høyde - palett_høyde, cellestørrelse, palett_høyde), 3)



def tegnViskelær():
  pygame.draw.rect(skjerm, HVIT, ((kolonner-1) * cellestørrelse, høyde - palett_høyde, cellestørrelse, palett_høyde))
  pygame.draw.rect(skjerm, SVART, ((kolonner-1) * cellestørrelse, høyde - palett_høyde, cellestørrelse, palett_høyde), 2)

  if valgtFarge == HVIT:
    pygame.draw.rect(skjerm, (255, 0, 0), ((kolonner-1) * cellestørrelse, høyde - palett_høyde, cellestørrelse, palett_høyde), 3)

  # Tegn en liten 'E' for "Eraser"
  font = pygame.font.SysFont(None, 24)
  tekst = font.render('E', True, SVART)
  tekst_rect = tekst.get_rect(center=((kolonner-1) * cellestørrelse + cellestørrelse//2, høyde - palett_høyde//2))
  skjerm.blit(tekst, tekst_rect)

while True:
  for hendelse in pygame.event.get():
    if hendelse.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    elif hendelse.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
      if y >= høyde - palett_høyde:
        indeks = x // cellestørrelse
        if indeks < len(farger):
          valgtFarge = farger[indeks]
        elif indeks == kolonner - 1:
          valgtFarge = HVIT
      else:
        rad, kol = y // cellestørrelse, x // cellestørrelse
        brett[rad][kol] = valgtFarge

  skjerm.fill(HVIT)

  tegnBrett()
  tegnPalett()
  tegnViskelær()
  pygame.display.flip()
"""

##Forskjellige knapper
'''
import pygame as pg
from pg_meny import Knapp
from pg_meny import MENYFARGE, HOVERFARGE

# Farge
BAKGRUNNSFARGE = (255, 255, 255)

# Definerer et vindu
VINDU_BREDDE = 600
VINDU_HOYDE = 400

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = 400
MENY_YSTART = 20
MENY_YAVSTAND = 60  # y-avstand for hver knapp

VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Initialiserer/starter pygame
pg.init()

# Funksjon som håndterer museklikk
def museklikk(posisjon):
    global BAKGRUNNSFARGE
    for m in meny:
        if m.rektangel.collidepoint(posisjon):
            print(f"Klikket på: {m.tekst}")
            if m.tekst == "Første knapp":
                BAKGRUNNSFARGE = ((255, 0, 0))
            elif m.tekst == "Andre knapp":
                BAKGRUNNSFARGE = ((0, 255, 0))
            elif m.tekst == "Tredje knapp":
                BAKGRUNNSFARGE = ((255, 255,  255))
                

# En liste med menyelementer
meny = []

# Lager en knapp
meny.append(Knapp(MENY_XSTART, MENY_YSTART, "Første knapp"))
meny.append(Knapp(MENY_XSTART, MENY_YSTART + MENY_YAVSTAND, "Andre knapp"))
meny.append(Knapp(MENY_XSTART, MENY_YSTART + 2 * MENY_YAVSTAND, "Tredje knapp"))

# Gjenta helt til brukeren lukker vinduet
fortsett = True

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        if event.type == pg.MOUSEBUTTONDOWN:
            museklikk(event.pos)

    VINDU.fill(BAKGRUNNSFARGE)
    muspos = pg.mouse.get_pos()

    for m in meny:
        if m.rektangel.collidepoint(muspos):
            m.tegn(VINDU, HOVERFARGE)
        else:
            m.tegn(VINDU, MENYFARGE)

    pg.display.flip()

pg.quit()
'''"""
##Nedtrekksliste
import pygame as pg
from pg_meny import Knapp, Nedtrekksliste
from pg_meny import MENYFARGE, HOVERFARGE

# Farger
BAKGRUNNSFARGE = (255, 255, 255)

# Definerer et vindu
VINDU_BREDDE = 600
VINDU_HOYDE = 400

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = 400
MENY_YSTART = 20
MENY_YAVSTAND = 60  # y-avstand for hver knapp

VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Initialiserer/starter pygame
pg.init()

# Funksjon som håndterer museklikk
def museklikk(posisjon):
    for m in meny:
        # Hvis listen er aktiv så vises alternativene. Klikk utenfor deaktiverer listen.
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.visAlternativer(posisjon)

        elif m.rektangel.collidepoint(posisjon):
            print(f"Klikket på: {m.tekst}")
            if isinstance(m, Nedtrekksliste):
                m.visAlternativer(posisjon)

# En liste med menyelementer
meny = []
andremeny = []

# Lager en nedtrekksliste
meny.append(
    Nedtrekksliste(
        MENY_XSTART, MENY_YSTART, ["Gjøk", "Sisik", "Trost", "Stær"]
    )
)

# Gjenta helt til brukeren lukker vinduet
fortsett = True

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        if event.type == pg.MOUSEBUTTONDOWN:
            museklikk(event.pos)

    VINDU.fill(BAKGRUNNSFARGE)
    muspos = pg.mouse.get_pos()

#Førstemeny
    for m in meny:
        if m.rektangel.collidepoint(muspos):
            m.tegn(VINDU, HOVERFARGE)
        else:
            m.tegn(VINDU, MENYFARGE)

    # Tegn de aktive nedtrekkslistene (som viser sine alternativer)
    for m in meny:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.tegn(VINDU, HOVERFARGE)
"""

##To/flere menyer
"""
import pygame as pg
from pg_meny import Knapp, Nedtrekksliste
from pg_meny import MENYFARGE, HOVERFARGE

BAKGRUNNSFARGE = (255, 255, 255)

# Vindusstørrelse
VINDU_BREDDE = 600
VINDU_HOYDE = 400

# Initialiserer Pygame og vinduet
pg.init()
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# En felles liste med alle menyer
alle_menyer = []

# Legger til ulike nedtrekkslister
alle_menyer.append(Nedtrekksliste(400, 20, ["Gjøk", "Sisik", "Trost", "Stær"]))       # Fugleliste
alle_menyer.append(Nedtrekksliste(300, 100, ["Laks", "Ørret", "Sild", "Makrell"]))   # Fiskeliste

  # Funksjon for å håndtere museklikk
def museklikk(posisjon):
    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.visAlternativer(posisjon)
        elif m.rektangel.collidepoint(posisjon):
            print(f"Klikket på: {m.tekst}")
            if isinstance(m, Nedtrekksliste):
                m.visAlternativer(posisjon)

# Hovedløkke
fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            museklikk(event.pos)

    VINDU.fill(BAKGRUNNSFARGE)
    muspos = pg.mouse.get_pos()

    # Tegner menyer med hover-effekt
    for m in alle_menyer:
        if m.rektangel.collidepoint(muspos):
            m.tegn(VINDU, HOVERFARGE)
        else:
            m.tegn(VINDU, MENYFARGE)

    # Tegner nedtrekksalternativer hvis aktiv
    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.tegn(VINDU, HOVERFARGE)

    pg.display.flip()
""""""
##Sirkel basert på info

import pygame as pg
from pg_meny import Knapp, Nedtrekksliste
from pg_meny import MENYFARGE, HOVERFARGE

BAKGRUNNSFARGE = (255, 255, 255)
FARGER = {"Rød": (255, 0, 0),
          "Blå": (0, 0, 255),
          "Grønn": (0, 255, 0), 
          "Gul": (255, 255, 0)}

STØRRELSER = {"Liten": 30, 
              "Middels": 60, 
              "Stor": 90}

# Vindusstørrelse
VINDU_BREDDE = 600
VINDU_HOYDE = 400

# Initialiserer Pygame og vinduet
pg.init()
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Sirkel basert på info")

# En felles liste med alle menyer
alle_menyer = []

# Legger til ulike nedtrekkslister
alle_menyer.append(Nedtrekksliste(400, 20, ["Rød",  "Blå", "Gul", "Grønn"]))       # Fugleliste
alle_menyer.append(Nedtrekksliste(300, 100, ["Liten", "Middels", "Stor"]))   # Fiskeliste

  # Funksjon for å håndtere museklikk
def museklikk(posisjon):
    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.visAlternativer(posisjon)
        elif m.rektangel.collidepoint(posisjon):
            print(f"Klikket på: {m.tekst}")
            if isinstance(m, Nedtrekksliste):
                m.visAlternativer(posisjon)

# Hovedløkke
fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            museklikk(event.pos)

    VINDU.fill(BAKGRUNNSFARGE)
    muspos = pg.mouse.get_pos()

    # Tegner menyer med hover-effekt
    for m in alle_menyer:
        if m.rektangel.collidepoint(muspos):
            m.tegn(VINDU, HOVERFARGE)
        else:
            m.tegn(VINDU, MENYFARGE)

    # Tegner nedtrekksalternativer hvis aktiv
    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.tegn(VINDU, HOVERFARGE)

    farge_valgt = alle_menyer[0].valgt
    størrelse_valgt = alle_menyer[1].valgt

    if farge_valgt and størrelse_valgt:
        farge = FARGER.get(farge_valgt, (0, 0, 0))
        radius = STØRRELSER.get(størrelse_valgt, 40)
        pg.draw.circle(VINDU, farge, (100, 100), radius)


    pg.display.flip()
pg.quit()
"""



##Game of life

import pygame as pg
import numpy as np
import math

from pg_meny import Knapp
from pg_meny import MENYFARGE, HOVERFARGE

# Ruteinfo
ANTALL_RUTER = 20 # antall ruter i bredden og høyden (20 x 20)
RUTE_STR = 20     # rutenes bredde og høyde

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
GRAA = (70, 70, 70)

# Farge
BAKGRUNNSFARGE = (255, 255, 255)

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = ANTALL_RUTER * RUTE_STR
MENY_YSTART = 20
MENY_BREDDE = 200
MENY_YAVSTAND = 60  # y-avstand for hver knapp

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = ANTALL_RUTER * RUTE_STR + MENY_BREDDE
VINDU_HOYDE  = ANTALL_RUTER * RUTE_STR
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Initialiserer/starter pygame
pg.init()


class Rutenett:
  """Klasse for å representere et rutenett"""
  def __init__(self):
    """Konstruktør"""
    self.ruter = [[0]*ANTALL_RUTER for i in range(ANTALL_RUTER)]

  def oppdater(self):
    # Resetter neste status
    for i in range(ANTALL_RUTER):
      for j in range(ANTALL_RUTER):
        self.ruter[i][j].nesteStatus = self.ruter[i][j].levende

    # Først alle cellene, angi ny status
    for i in range(ANTALL_RUTER):
      for j in range(ANTALL_RUTER):
        # Nå er vi inne på rute i,j. Da kan vi telle antall naboer
        antall_naboer = 0
        # Går gjennom plassene rundt ruta vår
        for x in [-1, 0, 1]:
          for y in [-1, 0, 1]:
            # Vi må ikke telle med ruta selv
            if not (x == 0 and y == 0):
              # Vi må bare ta med ruter innenfor brettet
              if (i+x >= 0 and i+x < ANTALL_RUTER) and (j+y >= 0 and j+y < ANTALL_RUTER):
                if self.ruter[i+x][j+y].levende:
                  antall_naboer += 1

        # Oppdaterer rutenett-kopien
        if antall_naboer <= 1:
          self.ruter[i][j].nesteStatus = False
        elif antall_naboer == 3:
          self.ruter[i][j].nesteStatus = True
        elif antall_naboer > 3:
          self.ruter[i][j].nesteStatus = False

    # Deretter endre status for alle
    for i in range(ANTALL_RUTER):
      for j in range(ANTALL_RUTER):
        self.ruter[i][j].oppdater()

class Rute:
  """Klasse for å representere en rute"""
  def __init__(self, rad, kolonne):
    self.rad = rad
    self.kolonne = kolonne
    self.levende = False
    self.nesteStatus = False
    self.farge = HVIT

  def oppdater(self):
    """ Metode for å oppdatere rutens status til neste status """
    self.levende = self.nesteStatus

  def byttTilstand(self):
    """Metode for å gjøre levende celle død og omvendt"""
    self.levende = not self.levende

  def tegn(self, vindu):
    """Metode for å tegne opp en celle i rutenettet"""
    if self.levende:
      self.farge = SVART
    else:
      self.farge = HVIT
    # Tegner selve ruten
    pg.draw.rect(vindu, self.farge, (self.rad*RUTE_STR, self.kolonne*RUTE_STR, RUTE_STR, RUTE_STR))
    # Tegner på en kantlinje rundt ruten
    pg.draw.rect(vindu, GRAA, (self.rad*RUTE_STR, self.kolonne*RUTE_STR, RUTE_STR, RUTE_STR), width=1)

# Funksjon som håndterer museklikk
def museklikk(posisjon):
  xkoordinat = posisjon[0]
  ykoordinat = posisjon[1]

  # Hva ble klikket på?
  # En rute
  if (xkoordinat >= 0 and xkoordinat <= ANTALL_RUTER*RUTE_STR) and (ykoordinat >= 0 and ykoordinat <= ANTALL_RUTER*RUTE_STR):
    x = math.floor(xkoordinat/RUTE_STR)
    y = math.floor(ykoordinat/RUTE_STR)
    rutenett.ruter[x][y].byttTilstand()
  else: # Noe annet (kanskje en knapp)
    for m in meny:
      if m.rektangel.collidepoint(posisjon):
        if m.tekst == "Omstart":
          for i in range(ANTALL_RUTER):
            for j in range(ANTALL_RUTER):
              rutenett.ruter[i][j].levende = False
        if m.tekst == "Neste":  
          rutenett.oppdater()

meny = [] # liste med knapper

# Lager en omstartsknapp
meny.append(Knapp(MENY_XSTART + 20, MENY_YSTART, "Omstart"))

# Lager en nesteknapp
meny.append(Knapp(MENY_XSTART + 20, MENY_YSTART + MENY_YAVSTAND, "Neste"))

# Lager et rutenett
rutenett = Rutenett()

# Lager rutene
for i in range(ANTALL_RUTER):
  for j in range(ANTALL_RUTER):
    rutenett.ruter[i][j] = Rute(i,j)

    # Trekker tilfeldig ett av tallene 0, 1 eller 2
    tilfeldig = np.random.randint(0,3)
    # Angir cellen som levende hvis tallet er 1 (1/3)
    if tilfeldig == 1:
      rutenett.ruter[i][j].byttTilstand()

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

  # Sjekker om brukeren har lukket vinduet eller klikket med mus
  for event in pg.event.get():
    if event.type == pg.QUIT:
      fortsett = False

    if event.type == pg.MOUSEBUTTONDOWN:
      museklikk(pg.mouse.get_pos())

  # Oppdaterer innholdet
  VINDU.fill(HVIT)

  # Tegner opp alle ruter som døde (hvite) eller levende (svarte) celler
  for i in range(ANTALL_RUTER):
    for j in range(ANTALL_RUTER):
      rutenett.ruter[i][j].tegn(VINDU)

  # Tegner knappene
  musPos = pg.mouse.get_pos()
  for m in meny:
    # Endre farge hvis musen er over knappen (hover)
    if m.rektangel.collidepoint(musPos):
      m.tegn(VINDU, HOVERFARGE)
    else:
      m.tegn(VINDU, MENYFARGE)

  pg.display.flip()



##Nedtrekkslister
'''
import pygame as pg
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

from pg_meny import Knapp, Nedtrekksliste
from pg_meny import MENYFARGE, HOVERFARGE

# Sett Matplotlib til ikke-interaktiv modus med 'Agg' som backend
matplotlib.use('Agg')

# Farger
BAKGRUNNSFARGE = (255, 255, 255)
MORK_GRA = (169, 169, 169)
LYS_GRA = (211, 211, 211)
BLA = (0, 120, 215)

# Definerer et vindu
VINDU_BREDDE = 800
VINDU_HOYDE = 600

# Definerer menyfeltet til høyre i vinduet
MENY_XSTART = 600
MENY_YSTART = 20
MENY_YAVSTAND = 60  # y-avstand for hvert element

VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Initialiserer/starter pygame
pg.init()

# Data
stortingsrepresentanter = [
  { "årstall": 2021, "representanter": {"AP": 48, "FrP": 21, "H": 36, "KrF": 3, "MDG": 3, "R": 8, "Sp": 28, "SV": 13, "V": 8, "PF": 1} },
  { "årstall": 2017, "representanter": {"AP": 49, "FrP": 27, "H": 45, "KrF": 8, "MDG": 1, "R": 1, "Sp": 19, "SV": 11, "V": 8, "PF": 0} }
]

# Funksjon som konverterer PyGame-farge (0-255) til Matplotlib-farge (0-1)
def pygameTilMatplotlibFarge(pygame_farge):
  return tuple([x / 255 for x in pygame_farge])

# Funksjon tegner opp valgt diagram for valgt årstall
def tegnMatplotlibDiagram(aarstall, diagramtype):
  # Tabell
  if diagramtype == "Tabell":
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig, axs = plt.subplots(1, 1)

    merkelapper = []
    antall = []

    # Henter aktuelle data
    for rep in stortingsrepresentanter:
      aar = rep["årstall"]

      if aar == int(aarstall):
        for parti in rep["representanter"]:
          merkelapper.append(parti)
          antall.append(rep["representanter"][parti])

    axs.axis('off')

    data = [antall, antall]

    # Juster fontstørrelse, cellepolstring, kantfarge og kanttykkelse
    tabell = axs.table(cellText=data, colLabels=merkelapper, loc="top", cellLoc="center")
    tabell.auto_set_font_size(False)
    tabell.set_fontsize(16)
    tabell.scale(1, 2)  # Øk høyden på cellene

    # Juster kantene for å gjøre det mer leselig
    for key, celle in tabell.get_celld().items():
      celle.set_edgecolor("black")
      celle.set_linewidth(2)
      celle.set_text_props(ha="center", va="center")
  
  # Søylediagram
  elif diagramtype == "Søyle":
    fig, ax = plt.subplots()
    barWidth = 0.35
    
    merkelapper = []
    antall = []

    # Henter aktuelle data
    for rep in stortingsrepresentanter:
      aar = rep["årstall"]

      if aar == int(aarstall):
        for parti in rep["representanter"]:
          merkelapper.append(parti)
          antall.append(rep["representanter"][parti])
    
    x = np.arange(len(merkelapper))
    y = antall
    ax.bar(x, y, barWidth, color=[pygameTilMatplotlibFarge(BLA), pygameTilMatplotlibFarge(MORK_GRA)])
    ax.set_xticks(x)
    ax.set_xticklabels(merkelapper)
    ax.set_ylim(0, max(antall) + 20)

  # Sektordiagram
  elif diagramtype == "Sektor":        
    merkelapper = []
    antall = []

    # Henter aktuelle data
    for rep in stortingsrepresentanter:
      aar = rep["årstall"]

      if aar == int(aarstall):
        for parti in rep["representanter"]:
          merkelapper.append(parti)
          antall.append(rep["representanter"][parti])

    plt.rcParams["figure.figsize"] = [5.00, 5.00]
    plt.rcParams["figure.autolayout"] = True
    fig, axs = plt.subplots(1, 1)
    plt.pie(antall, labels=merkelapper, textprops={"fontsize": 14})

  # Lagre diagrammet som en bildebuffer
  buf = BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)
  plt.close(fig)
  bilde = pg.image.load(buf)

  # Skalerer bildet til å passe til vinduet.
  bilde = pg.transform.scale(bilde, (MENY_XSTART, VINDU_HOYDE))
  return bilde

# En liste med menyelementer
meny = []

# To nedtrekkslister
meny.append(
  Nedtrekksliste(
    MENY_XSTART, MENY_YSTART, ["2017", "2021"]
  )
)

meny.append(
  Nedtrekksliste(
    MENY_XSTART, MENY_YSTART + MENY_YAVSTAND, ["Tabell","Søyle","Sektor"]
  )
)

# OK-knapp
meny.append(Knapp(MENY_XSTART, MENY_YSTART + 2*MENY_YAVSTAND, "OK"))

# Funksjon som håndterer museklikk
def museklikk(posisjon):
  global diagramBilde

  for m in meny:
    # Hvis listen er aktiv så vises alternativene. Klikk utenfor deaktiverer listen.
    if isinstance(m, Nedtrekksliste) and m.aktiv:
      m.visAlternativer(posisjon)

    elif m.rektangel.collidepoint(posisjon):
      if isinstance(m, Nedtrekksliste):
        m.visAlternativer(posisjon)
      elif m.tekst == "OK":
        # Oppdater diagrammet basert på de valgte alternativene
        diagramBilde = tegnMatplotlibDiagram(meny[0].tekst, meny[1].tekst)

diagramBilde = None

# Gjenta helt til brukeren lukker vinduet
while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
    if event.type == pg.MOUSEBUTTONDOWN:
      museklikk(event.pos)

  VINDU.fill(BAKGRUNNSFARGE)
  musPos = pg.mouse.get_pos()

  for m in meny:
    if m.rektangel.collidepoint(musPos):
      m.tegn(VINDU, HOVERFARGE)
    else:
      m.tegn(VINDU, MENYFARGE)

  # Tegn diagrammet hvis det finnes
  if diagramBilde:
    VINDU.blit(diagramBilde, (0, 0), pg.Rect(0, 0, MENY_XSTART+200, VINDU_HOYDE+100))

  # Tegn de aktive nedtrekkslistene (som viser sine alternativer)
  for m in meny:
    if isinstance(m, Nedtrekksliste) and m.aktiv:
      m.tegn(VINDU, MENYFARGE)

  pg.display.flip()
'''
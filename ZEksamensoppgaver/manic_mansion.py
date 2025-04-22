import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m
import random as rd

gap = 100
spillermedsaufart = 0.07
vanligspillerfart = 0.14
poeng_total = 0

# Initialiserer/starter pygame
pg.init()
spillet_er_over = False

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

font = pg.font.SysFont("Arial", 36)
class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.radius = radius
    self.farge = farge
    self.total = 0
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
  
  def finnAvstand(self, annenBall):
    """Metode for å finne avstanden til en annen ball"""
    xAvstand2 = (self.x - annenBall.x)**2  # x-avstand i andre
    yAvstand2 = (self.y - annenBall.y)**2  # y-avstand i andre
    sentrumsavstand = m.sqrt(xAvstand2 + yAvstand2)
    radiuser = self.radius + annenBall.radius
    avstand = sentrumsavstand - radiuser
    return avstand


class Hinder(Ball):
  """Klasse for å representere et hinder"""
  def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.xFart = xFart
    self.yFart = yFart

  def flytt(self):

    """Metode for å flytte hinderet"""
    # Sjekker om hinderet er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 100) or ((self.x + self.radius) >= self.vindusobjekt.get_width()-100):
      self.xFart = -self.xFart
    # Sjekker om hinderet er utenfor øvre/nedre kant
    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.yFart = -self.yFart
    # Flytter hinderet
    self.x += self.xFart
    self.y += self.yFart


class Spiller(Ball):
  """Klasse for å representere en spiller"""
  def __init__(self, x, y, radius, farge, vindusobjekt, fart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.fart = fart
    self.igang = True


  def flytt_med_kollisjon(self, taster, hindringer):
    original_x = self.x
    original_y = self.y

    # Opp
    if taster[K_UP]:
        self.y -= self.fart
        if self.y - self.radius < 0 or self.treffer_hindring(hindringer):
            self.y = original_y

    # Ned
    if taster[K_DOWN]:
        self.y += self.fart
        if self.y + self.radius > self.vindusobjekt.get_height() or self.treffer_hindring(hindringer):
            self.y = original_y

    # Venstre
    if taster[K_LEFT]:
        self.x -= self.fart
        if self.x - self.radius < 0 or self.treffer_hindring(hindringer):
            self.x = original_x

    # Høyre
    if taster[K_RIGHT]:
        self.x += self.fart
        if self.x + self.radius > self.vindusobjekt.get_width() or self.treffer_hindring(hindringer):
            self.x = original_x


  def treffer_hindring(self, hindringer):
    for h in hindringer:
        if self.finnAvstand(h) <= 0:
            return True
    return False


class Sau(Ball):
    def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
        super().__init__(x, y, radius, farge, vindusobjekt)
        self.xFart = xFart
        self.yFart = yFart
        self.bæres = False
        self.reddet = False

    def flytt(self):
        """Metode for å flytte sauen"""
        # Sjekker om hinderet er utenfor høyre/venstre kant
        self.x += self.xFart
        self.y += self.yFart

        if ((self.x - self.radius) <= (self.vindusobjekt.get_width())-gap) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.xFart = -self.xFart
        # Sjekker om hinderet er utenfor øvre/nedre kant
        if (self.y - self.radius) <= 0 or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart
            # Flytter hinderet
            self.x += self.xFart
            self.y += self.yFart

    def fjern(self):
       self.y = -400
       self.x = 200
       self.xfart = 0
       self.yfart = 0

   
def generer_spøkelse(antall, radius, farge):
    """Genererer spøkelseliste"""
    spøkelseliste = []
    spacing = VINDU_BREDDE // antall
    for i in range(antall):
        x = rd.randint(gap + radius//2 + 50, vindu.get_width()-gap-radius//2 - 50)
        y = rd.randint(radius//2 + 50, vindu.get_height()-radius//2 - 50)
        xfart = rd.uniform(-0.1, 0.1)
        yfart = rd.uniform(-0.03, 0.03)
        spøkelse = Hinder(x, y, radius, farge, vindu, xfart, yfart)
        spøkelseliste.append(spøkelse)
    return spøkelseliste
      
def generer_sau(antall, radius, farge):
    """Genererer spøkelseliste"""
    sauliste = []
    spacing = VINDU_BREDDE // antall
    for i in range(antall):
        x = rd.randint(vindu.get_width()-gap+radius, vindu.get_width() -radius)
        y = rd.randint(radius + 50, vindu.get_height()-radius - 50)
        xfart = rd.uniform(-0.1, 0.1)
        yfart = rd.uniform(-0.1, 0.1)
        sau = Sau(x, y, radius, farge, vindu, xfart, yfart)
        sauliste.append(sau)
    return sauliste

def generer_hindring(antall, farge):
    hinderliste = []
    for i in range(antall):
        radius = rd.randint(10, 15)
        xfart = 0
        yfart = 0
        x = rd.randint(gap + radius//2 + 50, vindu.get_width()-gap-radius//2 - 50)
        y = rd.randint(radius//2 + 50, vindu.get_height()-radius//2 - 50)
        hinder = Hinder(x, y, radius, farge, vindu, xfart, yfart)
        hinderliste.append(hinder)
    return hinderliste


# Lager et Spiller-objekt
spiller = Spiller(50, 200, 20, (0, 0, 0), vindu, vanligspillerfart)
spøkelseliste = generer_spøkelse(1, 30, "red")
sauliste = generer_sau(3, 25, "white")
hinderliste = generer_hindring(3, "blue")

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))
    pg.draw.line(vindu, "black", (100, 0), (100, 500), 3) 
    pg.draw.line(vindu, "black", (400, 0), (400, 500), 3) 

    # Tegner og flytter spiller og hinder
    if spiller.igang: 
        spiller.flytt_med_kollisjon(trykkede_taster, hinderliste)
        for hinder in spøkelseliste:
            hinder.flytt()
        for sau in sauliste:
            sau.flytt()

    spiller.tegn()
    for sau in sauliste:
        if sau.bæres == False and sau.reddet == False:
            sau.tegn()
    for spøkelse in spøkelseliste:
        spøkelse.tegn()

    # Sjekker avstanden mellom spiller og hinder
    for spøkelse in spøkelseliste:
        if spiller.finnAvstand(spøkelse) <= 0 and not spillet_er_over:
            print("Spillet er over")
            spiller.igang = False  
            spillet_er_over = True

    for hindring in hinderliste:
       hindring.tegn()
    

    for sau in sauliste:
            if spiller.finnAvstand(sau) <= 0 and not sau.bæres and not sau.reddet:
                if any(s.bæres for s in sauliste):  # Hvis spiller allerede bærer en annen sau
                    spiller.igang = False
                    spillet_er_over = True
            if sau.bæres and spiller.x <= 100:
                sau.reddet = True
                sau.bæres = False
                spiller.farge = ((0, 0, 0))
                spiller.fart = vanligspillerfart
                sau.fjern()
                poeng_total += 1
                nysau = generer_sau(1, 25, "white")[0]
                sauliste.append(nysau)
                nyspøkelse = generer_spøkelse(1, 30, "red")[0]
                spøkelseliste.append(nyspøkelse)
                nyhinder = generer_hindring(1, "blue" )
                hinderliste.extend(nyhinder)


            if spiller.finnAvstand(sau) <= 0 and not spillet_er_over:
                sau.bæres = True
                spiller.farge = "grey"
                spiller.fart = spillermedsaufart  

    poengtekst = font.render((f'Poeng: {poeng_total}'), True, (255, 0, 0))
    vindu.blit(poengtekst ,(380, 6))

    if spillet_er_over:
      tekst = font.render("Spillet er over", True, (255, 0, 0))
      vindu.blit(tekst, (150, 150))
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
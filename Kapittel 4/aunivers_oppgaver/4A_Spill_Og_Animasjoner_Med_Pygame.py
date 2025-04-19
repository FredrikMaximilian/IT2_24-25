import pygame as pg
###STILLESTÅENDE OBJEKTER
"""
# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

print(type(vindu))

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen hvit
    vindu.fill((255, 255, 255))

    # Tegner en sirkel
    pg.draw.circle(vindu, (255, 0, 0), (100, 250), 50)
    # Tegner et rektangel #Navn på vindu, farge, lengde fra venstrekant på vindu (måles fra venstre topphjørne), lengde fra topp, bredde, lengde. 
    pg.draw.rect(vindu, (0, 255, 0), (400, 400, 70, 90))
    # Tegner en ellipse
    pg.draw.ellipse(vindu, (0, 0, 255), (300, 250, 90, 60))
    # Tegner en linje
    pg.draw.line(vindu, (200, 0, 200), (400, 100), (420, 400), 5)

    # Lager en tekst i form av et bilde og legger til bildet i vinduet
    bilde = font.render("Heisann!", True, (50, 50, 50))
    vindu.blit(bilde, (400, 20))

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
""""""
pg.init()
vindubredde = 600
vindulengde = 600
vindu = pg.display.set_mode([vindubredde, vindulengde])
#print(type(vindu))

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((255, 255, 255))

    pg.draw.rect(vindu, (0, 32, 91), (0, 270, 600, 60))
    pg.draw.rect(vindu, (0, 32, 91), (215, 0, 60, 600))
    pg.draw.rect(vindu, (186, 12, 47), (0, 0, 200 , 250))
    pg.draw.rect(vindu, (186, 12, 47), (0, 350, 200 , 250))
    pg.draw.rect(vindu, (186, 12, 47), (290, 0, 400 , 250))
    pg.draw.rect(vindu, (186, 12, 47), (290, 350, 400 , 250))

    pg.display.flip()
pg.quit()
""""""
import random as rd
pg.init()
vindubredde = 500
vindulengde = 500
vindu = pg.display.set_mode([vindubredde, vindulengde])
vindu.fill((255, 255, 255))

def tegnsirkel(vindu, lengde, bredde):
    radius = rd.randint(10, 100)
    x = rd.randint(radius, bredde - radius)
    y = rd.randint(radius, lengde - radius)
    farge = (
        rd.randint(0, 255), 
        rd.randint(0, 255), 
        rd.randint(0, 255))
    pg.draw.circle(vindu, farge, (x, y), radius)

for _ in range(50):
    tegnsirkel(vindu, vindulengde, vindubredde)

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    pg.display.flip()
pg.quit()
""""""
import random as rd
import pygame as pg

pg.init()
vindubredde = 500
vindulengde = 500
vindu = pg.display.set_mode([vindubredde, vindulengde])
vindu.fill((255, 255, 255))

class Sirkel:
    def __init__(self, vindu):
        self.radius = rd.randint(10, 100)
        vindubredde, vindulengde = vindu.get_size()
        self.x = rd.randint(self.radius, vindubredde - self.radius)
        self.y = rd.randint(self.radius, vindulengde - self.radius)
        self.farge = (        
            rd.randint(0, 255), 
            rd.randint(0, 255), 
            rd.randint(0, 255))

    def tegn(self, vindu):
        pg.draw.circle(vindu, self.farge, (self.x, self.y), self.radius)
    
sirkelliste = [Sirkel(vindu) for i in range(50)]

for sirkel in sirkelliste:
    sirkel.tegn(vindu)

pg.display.flip()

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    pg.display.flip()
pg.quit()
"""

###ENKEL ANIMASJON

import math as m
import pygame as pg
# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

bakgrunnsbilde = pg.image.load("kaex.jpg")
bakgrunnsbilde = pg.transform.scale(bakgrunnsbilde, (VINDU_BREDDE, VINDU_HOYDE))

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, xfart, yfart, radius, vindusobjekt, farge):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.xfart = xfart
    self.yfart = yfart
    self.radius = radius
    self.vindusobjekt = vindusobjekt
    self.farge = farge

  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.xfart = -self.xfart

    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
        self.yfart = -self.yfart
    self.y += self.yfart
    self.x += self.xfart

def finnavstand(obj1, obj2):
    xAvstand2 = (obj1.x - obj2.x)**2  # x-avstand i andre
    yAvstand2 = (obj1.y - obj2.y)**2  # y-avstand i andre
    avstand = m.sqrt(xAvstand2 + yAvstand2)
    return avstand
  
def sjekkkollisjon(ball, ball2):
    avstand = finnavstand(ball, ball2)
    return avstand <= (ball.radius + ball2.radius)

def byttfart(ball1, ball2):
   ball1.xfart, ball2.xfart = ball2.xfart, ball1.xfart
   ball1.yfart, ball2.yfart = ball2.yfart, ball1.yfart

def sprettbeggeveier(ball1, ball2):
   ball1.xfart *= -1
   ball1.yfart *= -1
   ball2.xfart *= -1
   ball2.yfart *= -1

def sett_bakgrunn(vindu, bilde):
    vindu.blit(bilde, (0, 0))

# Lager et Ball-objekt
#ball = Ball(250, 250, 0.2, 0.3,  20, vindu, (255, 69, 0))
#ball2 = Ball(300, 300, 0.3, 0.2, 30, vindu, "pink")
balliste =  baller = [
    Ball(250, 250, 0.2, 0.3,  20, vindu, (255, 69, 0)), 
    Ball(150, 300, 0.15, 0.1, 30, vindu, "pink"),
    Ball(100, 100, 0.1, 0.1, 15, vindu, (255, 0, 0)),   # rød, liten
    Ball(200, 150, 0.15, 0.1, 25, vindu, (0, 255, 0)),   # grønn, medium
    Ball(300, 250, -0.2, 0.3, 29, vindu, (0, 0, 255)),  # blå, stor
    Ball(400, 100, -0.3, -0.1, 20, vindu, (255, 255, 0)),  # gul
    Ball(250, 300, 0.1, -0.2, 25, vindu, (255, 0, 255))   # lilla
]

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    #vindu.fill((135, 206, 235))
    sett_bakgrunn(vindu, bakgrunnsbilde)

    # Tegner og flytter ballen
    for ball in balliste:
        ball.tegn()
        ball.flytt()
    
#Funksjon for å få baller til å sprette fra hverandre
    for i in range(len(balliste)):
       for j in range(i+1, len(balliste)):
          ball1 = balliste[i]
          ball2 = balliste[j]
          if sjekkkollisjon(ball1, ball2):
            if ball1.radius == ball2.radius:
                byttfart(ball1, ball2)
            else:
               sprettbeggeveier(ball1, ball2)

#Funksjon for å spise mindre baller
    '''
    baller_som_skal_fjernes = []
    for i in range(len(balliste)):
        for j in range(i + 1, len(balliste)):
            ball1 = balliste[i]
            ball2 = balliste[j]
            if sjekkkollisjon(ball1, ball2):
                if ball1.radius > ball2.radius:
                    ball1.radius += int(ball2.radius * 0.3)
                    baller_som_skal_fjernes.append(ball2)
                elif ball2.radius > ball1.radius:
                    ball2.radius += int(ball1.radius * 0.3)
                    baller_som_skal_fjernes.append(ball1)
    # Fjern baller som har blitt spist
    for ball in baller_som_skal_fjernes:
        if ball in balliste: 
            balliste.remove(ball)  '''

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()
# Avslutter pygame
pg.quit()


###BEVEGELSE STYRT AV TASTATURET

##Bytte farge basert på pil
"""
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
      if event.type == pg.QUIT:
        fortsett = False

    # Henter en liste med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen
    if trykkede_taster[K_UP]:
      vindu.fill((0, 255, 255))
    if trykkede_taster[K_DOWN]:
      vindu.fill((255, 255, 0))
    if trykkede_taster[K_LEFT]:
      vindu.fill((255, 0, 255))
    if trykkede_taster[K_RIGHT]:
      vindu.fill((0, 0, 255))

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
"""

##Flytte på 
'''
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart = fart
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

  def flytt(self, taster):
    """Metode for å flytte ballen"""
    if taster[K_UP]:
      self.y -= self.fart
    if taster[K_DOWN]:
      self.y += self.fart
    if taster[K_LEFT]:
      self.x -= self.fart
    if taster[K_RIGHT]:
      self.x += self.fart

# Lager et Ball-objekt
ball = Ball(200, 200, 0.1, 20, (255, 69, 0), vindu)

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

    # Tegner og flytter ballene
    ball.tegn()
    ball.flytt(trykkede_taster)

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()'''
##Spretter rundt
'''
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m

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
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.xFart = -self.xFart
      spiller.total += 1
    # Sjekker om hinderet er utenfor øvre/nedre kant
    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.yFart = -self.yFart
      spiller.total += 1
    # Flytter hinderet
    self.x += self.xFart
    self.y += self.yFart


class Spiller(Ball):
  """Klasse for å representere en spiller"""
  def __init__(self, x, y, radius, farge, vindusobjekt, fart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.fart = fart
    self.igang = True

  def flytt(self, taster):
    global spillet_er_over
    """Metode for å flytte spilleren"""
    if taster[K_UP]:
      if self.y - self.radius >= 0:
        self.y -= self.fart
    if taster[K_DOWN]:
      if self.y + self.radius <= self.vindusobjekt.get_height():
        self.y += self.fart
    if taster[K_LEFT]:
      self.x -= self.fart
    if taster[K_RIGHT]:
      self.x += self.fart
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
    #Spillet stopper når man treffer høyre/venstre vegg
      spillet_er_over = True
      spiller.igang = False
      

# Lager et Spiller-objekt
spiller = Spiller(50, 200, 20, (0, 0, 0), vindu, 0.1)
# Lager et Hinder-objekt
#hinder = Hinder(150, 250, 20, (0, 0, 255), vindu, 0.08, 0.12)
hinderliste = [
    Hinder(150, 250, 20, (0, 0, 255), vindu, 0.08, 0.12),
    Hinder(300, 100, 15, (255, 0, 0), vindu, -0.07, 0.1),
    Hinder(100, 400, 25, (0, 255, 0), vindu, 0.1, -0.09),
    Hinder(400, 200, 18, (255, 255, 0), vindu, -0.06, 0.08),
    Hinder(250, 150, 22, (255, 0, 255), vindu, 0.09, -0.1)
]

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

    # Tegner og flytter spiller og hinder
    if spiller.igang: 
        spiller.flytt(trykkede_taster)
        for hinder in hinderliste:
            hinder. ()

    spiller.tegn()
    for hinder in hinderliste:
        hinder.tegn()

    # Sjekker avstanden mellom spiller og hinder
    for hinder in hinderliste:
        if spiller.finnAvstand(hinder) <= 0 and not spillet_er_over:
            print("Spillet er over")
            spiller.igang = False  
            spillet_er_over = True

    if spillet_er_over:
      tekst = font.render("Spillet er over", True, (255, 0, 0))
      vindu.blit(tekst, (150, 150))
      poengtekst = font.render((f'Du fikk {spiller.total} poeng'), True, (255, 0, 0))
      vindu.blit(poengtekst ,(150, 100))
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()'''
'''
##Endrer side
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m

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
    if ((self.x + self.radius) <= 0):
       self.x = self.vindusobjekt.get_width()
       spiller.total += 1
    if ((self.x - self.radius) >= self.vindusobjekt.get_width()):
      self.x = 0
      spiller.total += 1
    # Sjekker om hinderet er utenfor øvre/nedre kant
    if ((self.y + self.radius) <= 0): 
       self.y = self.vindusobjekt.get_height()
       spiller.total += 1
    if ((self.y - self.radius) >= self.vindusobjekt.get_height()):
      self.y = 0
      spiller.total += 1

    # Flytter hinderet
    self.x += self.xFart
    self.y += self.yFart


class Spiller(Ball):
  """Klasse for å representere en spiller"""
  def __init__(self, x, y, radius, farge, vindusobjekt, fart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.fart = fart
    self.igang = True

  def flytt(self, taster):
    global spillet_er_over
    """Metode for å flytte spilleren"""
    if taster[K_UP]:
      if self.y + self.radius >= 0:
        self.y -= self.fart
      else:
         self.y = self.vindusobjekt.get_height()

    if taster[K_DOWN]:
      if self.y - self.radius <= self.vindusobjekt.get_height():
        self.y += self.fart
      else: 
         self.y = 0

    if taster[K_LEFT]:
      if self.x + self.radius >= 0:
        self.x -= self.fart
      else:
        self.x = self.vindusobjekt.get_width()

    if taster[K_RIGHT]:
      if self.x - self.radius <= self.vindusobjekt.get_width():
        self.x += self.fart
      else:
        self.x = 0
      

# Lager et Spiller-objekt
spiller = Spiller(200, 200, 20, (0, 0, 0), vindu, 0.2)

hinderliste = [
    Hinder(150, 250, 20, (0, 0, 255), vindu, 0.08, 0.12),
    Hinder(300, 100, 15, (255, 0, 0), vindu, -0.07, 0.1),
    Hinder(100, 400, 25, (0, 255, 0), vindu, 0.1, -0.09),
    #Hinder(400, 200, 18, (255, 255, 0), vindu, -0.06, 0.08),
    #Hinder(250, 150, 22, (255, 0, 255), vindu, 0.09, -0.1)
]

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

    # Tegner og flytter spiller og hinder
    if spiller.igang: 
        spiller.flytt(trykkede_taster)
        for hinder in hinderliste:
            hinder.flytt()

    spiller.tegn()
    for hinder in hinderliste:
        hinder.tegn()

    # Sjekker avstanden mellom spiller og hinder
    for hinder in hinderliste:
        if spiller.finnAvstand(hinder) <= 0 and not spillet_er_over:
            print("Spillet er over")
            spiller.igang = False  
            spillet_er_over = True

    if spillet_er_over:
      tekst = font.render("Spillet er over", True, (255, 0, 0))
      vindu.blit(tekst, (150, 150))
      poengtekst = font.render((f'Du fikk {spiller.total} poeng'), True, (255, 0, 0))
      vindu.blit(poengtekst ,(150, 100))
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()'''
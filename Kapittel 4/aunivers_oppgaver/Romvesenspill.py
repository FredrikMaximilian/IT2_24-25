import pygame as pg
from pygame.locals import (K_LEFT, K_RIGHT, K_UP)
import math as m
import random as rd

pg.init()

vindubredde = 500
vindulengde = 500
vindu = pg.display.set_mode([vindubredde, vindulengde])

#BILDE
bakgrunnsbilde = pg.image.load("space_invaders_bakgrunn.jpg")
bakgrunnsbilde = pg.transform.scale(bakgrunnsbilde, (vindubredde, vindulengde))

class Skudd:
    def __init__(self, x, y, lengde, bredde, farge, vinduobjekt, fart = 2):
        """Klasse for å håndtere skudd"""
        self.x = x
        self.y = y
        self.lengde = lengde
        self.bredde = bredde
        self.farge = farge
        self.vinduobjekt = vinduobjekt
        self.fart = fart
        self.radius = max(self.lengde, self.bredde)/2 #Setter radius for ca-verdi av størrelse

    def tegn(self):
        """Tegner skuddet"""
        pg.draw.rect(self.vinduobjekt, self.farge, (self.x, self.y, self.lengde, self.bredde))

    def flytt(self):
        """Flytter skuddet oppover"""
        self.y -= self.fart

class Figur:
    def __init__(self, x, y, radius, farge, vinduobjekt):
        """Klasse for å håndtere figurer"""
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vinduobjekt = vinduobjekt

    def tegn(self):
        """Tegner figuren"""
        pg.draw.circle(self.vinduobjekt, self.farge, (self.x, self.y), self.radius)

    def finnAvstand(self, annenBall):
        """Finner avstanden mellom to figurer"""
        xAvstand2 = (self.x - annenBall.x)**2  # x-avstand i andre
        yAvstand2 = (self.y - annenBall.y)**2  # y-avstand i andre
        sentrumsavstand = m.sqrt(xAvstand2 + yAvstand2)
        radiuser = self.radius + annenBall.radius
        avstand = sentrumsavstand - radiuser
        return avstand
    
    def sjekkkollisjon(self, annenfigur):
        """Sjekker om to figurer kolliderer"""
        avstand = m.hypot(self.x - annenfigur.x, self.y - annenfigur.y)
        return avstand <= (self.radius + annenfigur.radius)

    def sjekkhelse(self, annenfigur):
        """Sjekker om figuren har helse"""
        total = 0
        if self.sjekkkollisjon(annenfigur):
            total += 1


class Spiller(Figur):
    def __init__(self, x, y, radius, farge, vinduobjekt, xfart, yfart):
        """Spiller-klasse som arver fra Figur-klassen."""
        super().__init__(x, y, radius, farge, vinduobjekt)
        self.xfart = xfart
        self.yfart = yfart
        self.igang = True

    def flytt(self, taster):
        """Flytter spilleren basert på tastetrykk."""
        if taster[K_LEFT]:
            if self.x - self.radius >= 0:
                self.x -= self.xfart
        if taster[K_RIGHT]:
            if self.x + self.radius <= self.vinduobjekt.get_width():
                self.x += self.xfart

    def skyt(self, taster):
        """Skaper et skudd når spilleren trykker på opp-tasten."""
        if taster[K_UP]:
            skudd_x = self.x - 2
            skudd_y = self.y - self.radius - 10
            rakettskudd = Skudd(skudd_x, skudd_y, 4, 16, (0, 0, 0), vindu)
            return rakettskudd
        

class Vesen(Figur):
    def __init__(self, x, y, radius, farge, vinduobjekt, fart, lever = True):
        """Romvesen-klasse som arver fra Figur-klassen."""
        super().__init__(x, y, radius, farge, vinduobjekt)
        self.fart = fart
        self.lever = lever
        self.helse = max(1, round(self.radius/6)) # helse avhenger av radius

    def flytt(self): # flytter romvesenet nedover
        """Flytter romvesenet nedover."""
        self.y += self.fart

    def håndterskudd(self, skudd): 
        """Håndterer skudd fra spiller"""
        if self.sjekkkollisjon(skudd):
            self.helse -= 1

    @property
    def helse(self):
        """Hente helse"""
        return self._helse

    @helse.setter
    def helse(self, ny_helse):
        """Setter helse og sjekker om den er død"""
        self._helse = max(0, ny_helse)  # Sørger for at helse aldri er negativ
        if self._helse == 0:
            self.død()

    def død(self):
        """Håndterer død av romvesen"""
        print("død")
        self.lever = False


def generer_pulje(antall, radius, farge):
    """Genererer en pulje av romvesener"""
    vesener = []
    spacing = vindubredde // antall
    for i in range(antall):
        x = spacing * i + spacing // 2
        y = rd.randint(-100, -50)
        fart = max(0.03, 5 - radius / 6)
        romvesen = Vesen(x, y, radius, farge, vindu, fart)
        vesener.append(romvesen)
    return vesener


rakett = Spiller(250, 465, 20, (0, 0, 0), vindu, 0.2, 0.2) # Spiller-klasse
#romvesen = Vesen(200, 0, 30, "pink", vindu, 0.02) # Romvesen-klasse
romvesener = generer_pulje(5, 30, "red") # Genererer romvesener, første for å starte


aktivt_skudd = None
fortsett = True
game_over = False


while fortsett:
    if game_over:
        fortsett = False
        continue

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.blit(bakgrunnsbilde, (0, 0)) # Tegner bakgrunnsbilde, kan fjernes om du vil ha hvit bakgrunn
    #vindu.fill((255, 255, 255)) # Fyller vinduet med hvit bakgrunn, kan tas inn om ønskelig

    trykkede_taster = pg.key.get_pressed() # Henter tastetrykkene
    pg.draw.rect(vindu, "black", (0, 500-int(rakett.radius)-40, 500, 3)) # Tegner treshold for rakett


    for romvesen in romvesener:
        if romvesen.lever:
            romvesen.tegn()

            if romvesen.y + romvesen.radius >= 500 - int(rakett.radius) - 40: # Sjekker om romvesenet har nådd treshold
                game_over = True

        if not romvesen.lever: #Spawner romvesen langt unna når død
            romvesen.x = 1000
            romvesen.y = -200

        if rakett.igang:
            romvesen.flytt()

    if rakett.igang:
        rakett.flytt(trykkede_taster)
        rakett.tegn()

        nytt_skudd = rakett.skyt(trykkede_taster)
        if nytt_skudd and aktivt_skudd is None:  # Kun ett skudd om gangen
            aktivt_skudd = nytt_skudd

        # Oppdater og tegn skudd hvis det finnes
        if aktivt_skudd:
            aktivt_skudd.flytt()
            aktivt_skudd.tegn()

            for romvesen in romvesener:
                if romvesen.y + romvesen.radius >= 500 - int(rakett.radius) - 40: # Sjekker om romvesenet har nådd treshold
                    game_over = True

                if romvesen.lever and romvesen.sjekkkollisjon(aktivt_skudd): ## Sjekker om skuddet treffer romvesenet
                    romvesen.håndterskudd(aktivt_skudd) ## Håndterer skudd
                    print("Treff")
                    aktivt_skudd = None
                    break

                # Fjern skudd når det forlater skjermen
            if aktivt_skudd and aktivt_skudd.y < 0: ## Sjekker om skuddet er utenfor skjermen
                aktivt_skudd = None ## Fjerner skuddet når det er utenfor skjermen

    if not any(vesen.lever for vesen in romvesener): # Sjekker om alle romvesener er døde
        valg = rd.randint(1, 3) # Velger tilfeldig romvesen
        if valg == 1:
            #RØD
            romvesener = generer_pulje(5, 30, "red") 
            for romvesen in romvesener:
                romvesen.fart = 0.05
                romvesen.helse = 10
        elif valg == 2:
            #BLÅ
            romvesener = generer_pulje(7, 20, "blue") #
            for romvesen in romvesener:
                romvesen.fart = 0.03
                romvesen.helse = 7
        elif valg == 3:
            #GRØNN
            romvesener = generer_pulje(8, 15, "green") # små og raske
            for romvesen in romvesener:
                romvesen.fart = 0.06
                romvesen.helse = 3

    pg.display.flip()

    if game_over:
        font = pg.font.SysFont("Arial", 40)
        tekst = font.render("Game Over", True, (255, 0, 0))
        vindu.blit(tekst, (vindubredde//2 - tekst.get_width()//2, vindulengde//2 - tekst.get_height()//2))
        pg.display.flip()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

pg.quit()

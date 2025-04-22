# Disse klassene er laget av Aksel Nissen Hellerud

import pygame as pg

# Farger
TEKSTFARGE = (255, 255, 255)
MENYFARGE = (0, 0, 255)
HOVERFARGE = (100, 100, 150)

# Nedtrekksmeny
NEDTREKKS_BREDDE, NEDTREKKS_HOYDE = 200, 50

# Menyfelt
# MENYFELT_START = 400
# MENYFELT_BREDDE = 200

# Initialiserer/starter pygame
pg.init()

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Tahoma", 16)

alle_knapper = []

class Knapp:
    instanser = []
    """Klasse for å representere en knapp"""
    def __init__(self, xPosisjon, yPosisjon, tekst):
        Knapp.instanser.append(self)
        alle_knapper.append(self)
        self.xPosisjon = xPosisjon
        self.yPosisjon = yPosisjon
        self.bredde = 100
        self.hoyde = 40
        self.tekst = tekst
        self.rect = pg.Rect(
            self.xPosisjon, self.yPosisjon, self.bredde, self.hoyde
        )

    def tegn(self, vindu, farge):
        pg.draw.rect(vindu, farge, self.rect, border_radius=int(round(self.bredde/2, 0)))
        pg.draw.rect(vindu, (0, 0, 0), self.rect, border_radius=int(round(self.bredde/2, 0)), width = 2)
        tekst = font.render(self.tekst, True, TEKSTFARGE)
        tekstRamme = tekst.get_rect(center=self.rect.center)
        vindu.blit(tekst, tekstRamme.topleft)

class Nedtrekksliste:
    instanser = []
    def __init__(self, xPosisjon, yPosisjon, alternativer, overskrift, bredde):
        alle_knapper.append(self)
        Nedtrekksliste.instanser.append(self)
        self.xPosisjon = xPosisjon
        self.yPosisjon = yPosisjon
        self.alternativer = alternativer
        self.aktiv = False
        self.overskrift = overskrift
        self.tekst = alternativer[0]
        self.bredde = bredde
        self.hoyde = 40
        self.rect = pg.Rect(
            self.xPosisjon, self.yPosisjon, self.bredde + 10, self.hoyde
        )
    def lengsteTekst(self):
        # Returnerer lengden til det lengste alternativet
        lengst = 0
        for alternativ in self.alternativer:
            if len(alternativ) > lengst:
                lengst = len(alternativ) + 3    # Legger til litt pga forskyvning
        return lengst

    def tegn(self, vindu, farge, pos = None):
        pg.draw.rect(vindu, farge, self.rect)
        rekt = self.rect
        tekst = font.render(self.tekst, True, TEKSTFARGE)
        overskrift = font.render(self.overskrift, True, (0, 0, 0))
        tekstRamme = tekst.get_rect(center=self.rect.center)
        tekstRamme.left = rekt.left + 10 # Venstrejusterer teksten
        tekstRamme.centery = rekt.centery  # Sentraliserer teksten vertikalt
        vindu.blit(tekst, tekstRamme.topleft)
        vindu.blit(overskrift, (tekstRamme.x, tekstRamme.y-40))

        if self.aktiv:
            i = 0
            for alternativ in self.alternativer:
                rekt = self.alternativRamme(i)
                pg.draw.rect(vindu, HOVERFARGE, rekt)

                if pos != None:
                    if rekt.collidepoint(pos):
                        pg.draw.rect(vindu, (HOVERFARGE[0] - 20, HOVERFARGE[1] - 20, HOVERFARGE[2] - 20), rekt)

                tekst = font.render(alternativ, True, TEKSTFARGE)
                tekstRamme = tekst.get_rect(center=rekt.center)
                tekstRamme.left = rekt.left + 10 # Venstrejusterer teksten
                tekstRamme.centery = rekt.centery  # Sentraliserer teksten vertikalt
                vindu.blit(tekst, tekstRamme.topleft)
                i += 1

    def alternativRamme(self, i):
        return pg.Rect(
            self.xPosisjon + 10,
            self.yPosisjon + (i + 1) * self.hoyde,
            self.bredde,
            self.hoyde
        )

    def visAlternativer(self, pos):
        if pos == None:
            return
        elif self.rect.collidepoint(pos):
            self.aktiv = not self.aktiv
        elif self.aktiv:
            i = 0
            while i < len(self.alternativer):
                if self.alternativRamme(i).collidepoint(pos):
                    self.tekst = self.alternativer[i]
                    self.aktiv = False
                    break
                i += 1
        else:
            self.aktiv = False
        
                    # Klikk utenfor alternativer deaktiverer nedtrekkslisten

class Input_felt:
    
    instanser = []
    PADDING = 10
    def __init__(self, x, y, beskrivelse, overskrift):
        alle_knapper.append(self)
        self.innhold = beskrivelse
        self.x = x
        self.y = y
        self.overskrift = overskrift
        self.aktiv = False
        self.bredde = 150
        self.tekst = font.render(self.innhold, True, (255, 255, 255))
        self.rect = self.tekst.get_rect()
        Input_felt.instanser.append(self)

    def aktiver(self, pos):
        if pos != None: 
            if self.rect.collidepoint(pos):
                self.aktiv = True
            else: 
                self.aktiv = False

    def tegn(self, vindu, farge, events):
        keys = []

        self.farge = farge 

        for event in events:
            if event.type == pg.KEYDOWN:       
                keys.append(pg.key.name(event.key))
    
        if self.aktiv:
            if keys != None:
                for key in keys:
                    if key == "backspace":
                        if self.innhold[len(self.innhold)-1] != " ":
                            self.innhold = self.innhold[:-1]
                        else: 
                            pass
                    elif key.isnumeric(): 
                        self.innhold += key
                    else:
                        if key == "return":
                            self.aktiv = False
                        pass
        self.tekst = font.render(self.innhold, True, (255, 255, 255))
        overskrift = font.render(self.overskrift, True, (0, 0, 0))
        self.rect = pg.Rect(self.x - Input_felt.PADDING, self.y - Input_felt.PADDING, self.bredde, self.tekst.get_height() + 2 * Input_felt.PADDING)
        pg.draw.rect(vindu, farge, self.rect)

        if self.aktiv:
            pg.draw.rect(vindu, (0, 0, 0), self.rect, width=2, border_radius = 4)

        vindu.blit(self.tekst, (self.x, self.y))
        vindu.blit(overskrift, (self.x, self.y - 40))

    @property
    def verdi(self):
        return self.innhold[self.innhold.index(":")+1:]
    
class Slider:

    instanser = []

    def __init__(self, x, y, start_range, end_range, overskrift, nøyaktighet):

        self.x = x
        self.y = y
        self.start_range = start_range
        self.end_range = end_range
        self.verdi = (self.start_range+self.end_range)/2
        self.overskrift = overskrift
        self.lengde = 130
        self.midtpunkt = x + int(round(self.lengde / 2, 0))
        self.slider_x = self.midtpunkt
        self.høyde = 7
        self.nøyaktighet = nøyaktighet
        Slider.instanser.append(self)

    def tegn(self, vindu, farge):

        self.vindu = vindu
        self.farge = farge
        self.rect = pg.Rect(self.x, self.y, self.lengde, self.høyde)
        pg.draw.rect(vindu, farge, self.rect, border_radius=5)
        self.tekst = font.render(self.overskrift, True, (0, 0, 0), None)
        self.tall_tekst = font.render(f"{self.verdi}", True, (0, 0, 0), None)
        self.tekst_rect = self.tekst.get_rect(center = (self.midtpunkt, self.y - 20))
        self.tall_rect = self.tall_tekst.get_rect(center = (self.midtpunkt, self.y + 25))
        vindu.blit(self.tall_tekst, self.tall_rect.topleft)
        vindu.blit(self.tekst, self.tekst_rect.topleft)
    
    def oppdater_slider(self, events):

        for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    mus_x, mus_y = pg.mouse.get_pos()
                    if self.rect.collidepoint((mus_x, mus_y)):
                        self.slider_x = mus_x

        self.slider_sirkel(self.slider_x)
        self.verdi = round((self.slider_x-self.x)/self.lengde*self.end_range, self.nøyaktighet)

    def slider_sirkel(self, x):          
        pg.draw.circle(self.vindu, (self.farge[0] - 30, self.farge[1] - 30, self.farge[2] - 30), (x, self.y+4), 8)


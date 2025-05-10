import pygame as pg

# Farger
TEKSTFARGE = (255, 255, 255)
MENYFARGE = (0, 0, 255)
HOVERFARGE = (0, 150, 255)

# Initialiserer pygame
pg.init()

# Skrifttype
font = pg.font.SysFont("Tahoma", 24)


class Knapp:
    """Klasse for å representere en knapp"""
    def __init__(self, xPosisjon, yPosisjon, tekst):
        self.xPosisjon = xPosisjon
        self.yPosisjon = yPosisjon
        self.bredde = len(tekst) * 14 + 20
        self.hoyde = 40
        self.tekst = tekst
        self.rektangel = pg.Rect(
            self.xPosisjon, self.yPosisjon, self.bredde, self.hoyde
        )

    def tegn(self, vindu, farge):
        pg.draw.rect(vindu, farge, self.rektangel)
        tekst = font.render(self.tekst, True, TEKSTFARGE)
        tekstRamme = tekst.get_rect(center=self.rektangel.center)
        vindu.blit(tekst, tekstRamme.topleft)


class Nedtrekksliste:
    def __init__(self, xPosisjon, yPosisjon, alternativer):
        self.xPosisjon = xPosisjon
        self.yPosisjon = yPosisjon
        self.alternativer = alternativer
        self.aktiv = False
        self.tekst = alternativer[0]
        self.valgt = None
        self.bredde = self.lengsteTekst() * 14
        self.hoyde = 40
        self.rektangel = pg.Rect(
            self.xPosisjon, self.yPosisjon, self.bredde + 10, self.hoyde
        )
        self.scroll_offset = 0
        self.max_visible = 5

    def lengsteTekst(self):
        lengst = 0
        for alternativ in self.alternativer:
            if len(alternativ) > lengst:
                lengst = len(alternativ) + 3
        return lengst

    def tegn(self, vindu, farge):
        # Tegn valgt element (hovedmeny)
        pg.draw.rect(vindu, farge, self.rektangel)
        tekst = font.render(self.tekst, True, TEKSTFARGE)
        tekstRamme = tekst.get_rect(center=self.rektangel.center)
        tekstRamme.left = self.rektangel.left + 10
        tekstRamme.centery = self.rektangel.centery
        vindu.blit(tekst, tekstRamme.topleft)

        # Tegn alternativer hvis menyen er aktiv
        if self.aktiv:
            start = self.scroll_offset
            slutt = min(len(self.alternativer), start + self.max_visible)
            for vis_i, i in enumerate(range(start, slutt)):
                alternativ = self.alternativer[i]
                rekt = self.alternativRamme(vis_i)
                pg.draw.rect(vindu, HOVERFARGE, rekt)
                tekst = font.render(alternativ, True, TEKSTFARGE)
                tekstRamme = tekst.get_rect(center=rekt.center)
                tekstRamme.left = rekt.left + 10
                tekstRamme.centery = rekt.centery
                vindu.blit(tekst, tekstRamme.topleft)

    def alternativRamme(self, vis_i):
        return pg.Rect(
            self.xPosisjon + 10,
            self.yPosisjon + (vis_i + 1) * self.hoyde,
            self.bredde,
            self.hoyde
        )

    def visAlternativer(self, pos):
        if self.rektangel.collidepoint(pos):
            self.aktiv = not self.aktiv
        elif self.aktiv:
            start = self.scroll_offset
            slutt = min(len(self.alternativer), start + self.max_visible)
            for vis_i, i in enumerate(range(start, slutt)):
                rekt = self.alternativRamme(vis_i)
                if rekt.collidepoint(pos):
                    self.tekst = self.alternativer[i]
                    self.valgt = self.alternativer[i]
                    print(f"Valgt alternativ: {self.tekst}")
                    self.aktiv = False
                    break
        else:
            self.aktiv = False

    def scroll(self, retning):
        if self.aktiv:
            self.scroll_offset += retning
            maks_offset = max(0, len(self.alternativer) - self.max_visible)
            self.scroll_offset = max(0, min(self.scroll_offset, maks_offset))

import pandas as pd 
import numpy as np
import pygame as pg
from graf_knapp_klasser import *
from GUI_funksjoner import *
from fil_klasser import Fil_reader

fil = "Datasett_fodselstall.csv"
datasett = Fil_reader(fil)

class GUI_plotter: 
    """
    Klasse for å plotte grafer i pygame med GUI
    """

    def kjør(self):
        """
        Starter fremvisningen
        """

        # Pygame setup

        BREDDE, HØYDE = 800, 600
        vindu = pg.display.set_mode((BREDDE, HØYDE))

        # Estetiske verdier 

        TOPP_MARGIN = 40
        MENYFARGE = (50, 50, 100)
        HOVERFARGE = (30, 30, 90)
        font = pg.font.SysFont("tahoma", 25)

        # Alle objekter lages

        velg_y_meny = Nedtrekksliste(30, TOPP_MARGIN, datasett.rader[1:], "Y-akseverdi", 150)
        velg_type_meny = Nedtrekksliste(220, TOPP_MARGIN, ["Linje", "Bar", "Sektor"], "Type graf", 150) #Endre til riktige alternativer
        vis_knapp = Knapp(BREDDE - 130, TOPP_MARGIN, "Vis graf")
        input = Input_felt(BREDDE - 300, TOPP_MARGIN, "År: ", "Skriv år")

        graf_overflate = None #Dette er hva som skal bli en pygame-surface og vises når man trykker vis graf

        # Spilloop 

        run = True

        while run:

            # Eventhåndtering og plotting 

            events = pg.event.get()
            pos = pg.mouse.get_pos()
            for event in events:

                if event.type == pg.QUIT:
                    run = False

                if event.type == pg.MOUSEBUTTONDOWN:

                    pos = pg.mouse.get_pos()
                    
                    for knapp in Nedtrekksliste.instanser:
                        knapp.visAlternativer(pos)

                    for knapp in Input_felt.instanser:
                            knapp.aktiver(pos)

                    if vis_knapp.rect.collidepoint(pos): #Plotter

                        datasett.df = datasett.df.dropna(subset = velg_y_meny.tekst)
                        x_verdier = datasett.df["År"]
                        y_verdier = datasett.df[velg_y_meny.tekst]
                        type = velg_type_meny.tekst
                    
                        graf_overflate = plott_graf(x_verdier, y_verdier, type, (7, 5), "År", velg_y_meny.tekst)

            # Herfra tegnes alt 

            vindu.fill((255, 255, 255))

            info_tekst = font.render('Trykk "Vis graf" for å se', True, (200, 200, 200))
            info_tekst_rect = info_tekst.get_rect(center = (BREDDE / 2, HØYDE / 2))
            vindu.blit(info_tekst, info_tekst_rect)

            # Viser figuren i vinduet
            if graf_overflate != None:
                vindu.blit(graf_overflate, (60, 115))

            pg.draw.line(vindu, (175, 175, 175), (0, 95), (BREDDE, 95), 1)

            #Tegner knapper

            for knapp in alle_knapper:
                if knapp.rect.collidepoint(pos):
                    if isinstance(knapp, Input_felt):
                        knapp.tegn(vindu, HOVERFARGE, events)
                    elif isinstance(knapp, Nedtrekksliste):
                        knapp.tegn(vindu, HOVERFARGE, pos)
                    elif knapp == vis_knapp:
                        knapp.tegn(vindu, (70, 70, 90))
                    else: 
                        knapp.tegn(vindu, HOVERFARGE)
                else:
                    if isinstance(knapp, Input_felt):
                        knapp.tegn(vindu, MENYFARGE, events)
                    elif isinstance(knapp, Nedtrekksliste):
                        knapp.tegn(vindu, MENYFARGE, pos)
                    elif knapp == vis_knapp:
                        knapp.tegn(vindu, (90, 90, 130))
                    else:
                        knapp.tegn(vindu, MENYFARGE)

            pg.display.flip()

import pygame as pg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pg_meny_scroll import Knapp, Nedtrekksliste
from pg_meny_scroll import MENYFARGE, HOVERFARGE

# --- Avkrysningsboks-klasse ---
class Avkrysningsboks:
    def __init__(self, x, y, tekst):
        self.tekst = tekst
        self.rektangel = pg.Rect(x, y, 20, 20)
        self.farge = (0, 0, 0)
        self.avkrysset = False
        self.font = pg.font.SysFont("Tahoma", 20)
        self.tekstoverflate = self.font.render(tekst, True, (0, 0, 0))
        self.tekst_pos = (x + 30, y - 2)

    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, self.rektangel, 2)
        if self.avkrysset:
            pg.draw.line(vindu, self.farge, self.rektangel.topleft, self.rektangel.bottomright, 2)
            pg.draw.line(vindu, self.farge, self.rektangel.topright, self.rektangel.bottomleft, 2)
        vindu.blit(self.tekstoverflate, self.tekst_pos)

    def trykk(self, pos):
        if self.rektangel.collidepoint(pos):
            self.avkrysset = not self.avkrysset

    def er_valgt(self):
        return self.avkrysset


# --- Last inn og rens data ---
filnavn = "zfilmvisning.csv"
df = pd.read_csv(filnavn)

df["Sjanger"] = df["Sjanger"].astype(str).str.strip()
df["Toppfilm"] = df["Toppfilm"].astype(str).str.strip()
df["Land"] = df["Land"].astype(str).str.strip()

# Rens tallkolonner
df["Besøkstall"] = pd.to_numeric(df["Besøkstall"], errors="coerce")
df["Årstall"] = pd.to_numeric(df["Årstall"], errors="coerce")

# --- Målingstyper som avkrysningsbokser ---
sjangertyper = (df["Sjanger"].unique())
avkrysningsbokser = []

start_y = 180
for i, sjanger in enumerate(sjangertyper):
    avkrysningsbokser.append(Avkrysningsboks(20, start_y + i * 30, sjanger))

# --- Menyer ---
aar_liste= sorted([str(int(aar)) for aar in df["Årstall"].dropna().unique()])


# Menyer og knapper
alle_menyer = []     
alle_menyer.append(Knapp(450, 50, "Vis graf"))       # index 0
alle_menyer.append(Nedtrekksliste(100, 150, aar_liste))       # index 1
alle_menyer.append(Nedtrekksliste(240, 50, aar_liste)) #2


# --- Pygame setup ---
BAKGRUNNSFARGE = (255, 255, 255)
pg.init()
VINDU = pg.display.set_mode([600, 400])
pg.display.set_caption("Film-statistikk")

# --- Vis graf ---
def vis_graf():
    fra_år = alle_menyer[1].valgt # Henter valgt startår
    til_år = alle_menyer[2].valgt  # Henter valgt sluttår
    valgte_sjangre = [b.tekst for b in avkrysningsbokser if b.er_valgt()]

    if fra_år is None and til_år is None and not valgte_sjangre:  # Sjekker om alle valg er gjort
            print("Du må velge alle tre verdier.")
            return
    elif fra_år is None or til_år is None:
        print("Du må velge begge årene")
        return
    elif not valgte_sjangre:
        print("Du må velge sjanger(e)")
        return
    
    try:
        fra_år = int(fra_år)  # Henter valgt startår
        til_år = int(til_år)  # Henter valgt sluttår

        if fra_år > til_år:  # Sjekker om startår er mindre enn sluttår
            print("Første år må være lavere enn siste")
            return

        overlik_fraår= df[df["Årstall"] >= fra_år]
        mellom_fra_til = overlik_fraår[overlik_fraår["Årstall"] <= til_år] 
        mellom_fra_til = mellom_fra_til.sort_values(by= "Årstall") 

        sjangerbesøk_liste = []
        for sjang in valgte_sjangre:
            filminfo = mellom_fra_til[mellom_fra_til["Sjanger"] == sjang]
            besøkstall = filminfo["Besøkstall"].sum() 
            sjangerbesøk_liste.append(besøkstall)


        plt.figure(figsize=(10, 5))
        plt.bar(valgte_sjangre, sjangerbesøk_liste) 
        plt.title(f"Besøk per sjanger | År: {fra_år} - {til_år}")
        plt.xlabel("Sjanger")
        plt.ylabel("Besøkstall")
        plt.xticks(rotation=45)
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()

    except Exception as e:  # Håndterer feil
        print("Noe gikk galt:", e)

# --- Museklikk ---
def museklikk(pos):
    for b in avkrysningsbokser:
        b.trykk(pos)
    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.visAlternativer(pos)
        elif m.rektangel.collidepoint(pos):
            if isinstance(m, Nedtrekksliste):
                m.visAlternativer(pos)
            elif isinstance(m, Knapp) and m.tekst == "Vis graf":
                vis_graf()

# --- Hovedløkke ---
fortsett = True
scroll_target = None
scroll_delay = 40
last_scroll_time = 0

while fortsett:
    nå = pg.time.get_ticks()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            museklikk(event.pos)
        elif event.type == pg.KEYDOWN:
            for m in alle_menyer:
                if isinstance(m, Nedtrekksliste) and m.aktiv:
                    scroll_target = m

    taster = pg.key.get_pressed()
    if scroll_target:
        if taster[pg.K_DOWN] and nå - last_scroll_time > scroll_delay:
            scroll_target.scroll(1)
            last_scroll_time = nå
        elif taster[pg.K_UP] and nå - last_scroll_time > scroll_delay:
            scroll_target.scroll(-1)
            last_scroll_time = nå

    VINDU.fill(BAKGRUNNSFARGE)
    muspos = pg.mouse.get_pos()
    for m in alle_menyer:
        if m.rektangel.collidepoint(muspos):
            m.tegn(VINDU, HOVERFARGE)
        else:
            m.tegn(VINDU, MENYFARGE)

    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.tegn(VINDU, HOVERFARGE)

    for b in avkrysningsbokser:
        b.tegn(VINDU)

    font = pg.font.SysFont("Tahoma", 24)
    VINDU.blit(font.render("Antall land", True, (0, 0, 0)), (100, 20))
    VINDU.blit(font.render("sjangre", True, (0, 0, 0)), (20, 150))

    pg.display.flip()

pg.quit()

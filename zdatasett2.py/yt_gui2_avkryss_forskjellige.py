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
filnavn = "zytstats.csv"
df = pd.read_csv(filnavn)

df["category"] = df["category"].astype(str).str.strip()
df["Country"] = df["Country"].astype(str).str.strip()
df["Youtuber"] = df["Youtuber"].astype(str).str.strip()

df["subscribers"] = pd.to_numeric(df["subscribers"], errors="coerce")
df["video views"] = pd.to_numeric(df["video views"], errors="coerce")
df["uploads"] = pd.to_numeric(df["uploads"], errors="coerce")

# --- Målingstyper som avkrysningsbokser ---
målingstyper = ["subscribers", "video views", "uploads"]
avkrysningsbokser = []
start_y = 180
for i, måling in enumerate(målingstyper):
    avkrysningsbokser.append(Avkrysningsboks(20, start_y + i * 30, måling))

# --- Menyer ---
antalliste = [str(i) for i in range(1, 21)]
alle_menyer = []
alle_menyer.append(Knapp(450, 50, "Vis graf"))          # index 0
alle_menyer.append(Nedtrekksliste(100, 50, antalliste)) # index 1

# --- Pygame setup ---
BAKGRUNNSFARGE = (255, 255, 255)
pg.init()
VINDU = pg.display.set_mode([600, 400])
pg.display.set_caption("YouTube-statistikk")

# --- Vis graf ---
def vis_graf():
    valgt_antall_str = alle_menyer[1].valgt
    valgte_målinger = [b.tekst for b in avkrysningsbokser if b.er_valgt()]

    if valgt_antall_str is None or not valgte_målinger:
        print("Du må velge antall land og minst én målingstype.")
        return

    valgt_antall = int(valgt_antall_str)

    landliste = []
    målingsdata = {m: [] for m in valgte_målinger}

    flestytland = df["Country"].value_counts().head(valgt_antall)

    for land in flestytland.keys():
        landinfo = df[df["Country"] == land]
        landliste.append(land)
        for m in valgte_målinger:
            gjennomsnitt = landinfo[m].mean()
            målingsdata[m].append(round(gjennomsnitt))

    for m in valgte_målinger:
        plt.figure(figsize=(10, 5))
        plt.bar(landliste, målingsdata[m])
        plt.title(f"Gjennomsnittlig {m} per kanal")
        plt.xlabel("Land")
        plt.ylabel(m.capitalize())
        plt.xticks(rotation=45)
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()

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
    VINDU.blit(font.render("Målinger", True, (0, 0, 0)), (20, 150))

    pg.display.flip()

pg.quit()

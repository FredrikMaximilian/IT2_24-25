import pygame as pg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pg_meny_scroll import Knapp, Nedtrekksliste
from pg_meny_scroll import MENYFARGE, HOVERFARGE

# --- Last inn og rens data ---
filnavn = "zytstats.csv"
df = pd.read_csv(filnavn)

# Rens opp tekst
df["category"] = df["category"].astype(str).str.strip()
df["Country"] = df["Country"].astype(str).str.strip()
df["Youtuber"] = df["Youtuber"].astype(str).str.strip()

# Rens tallkolonner
df["subscribers"] = pd.to_numeric(df["subscribers"], errors="coerce")
df["video views"] = pd.to_numeric(df["video views"], errors="coerce")
df["uploads"] = pd.to_numeric(df["uploads"], errors="coerce")


antalliste = [str(i) for i in range(1, 21)]
målingstyper = ["subscribers", "video views", "uploads"]

# Menyer og knapper
alle_menyer = []     
alle_menyer.append(Knapp(450, 50, "Vis graf"))       # index 0
alle_menyer.append(Nedtrekksliste(100, 150, antalliste))       # index 1
alle_menyer.append(Nedtrekksliste(300, 50, målingstyper))     # index 2 

# --- Pygame setup ---
BAKGRUNNSFARGE = (255, 255, 255)
VINDU_BREDDE = 600
VINDU_HOYDE = 400

pg.init()
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
# --- Funksjon for å vise graf ---


def vis_graf():
    
    landliste = []
    abonnementliste = []
    visningliste = []
    opplastingliste = []

    valgt_måling = alle_menyer[2].valgt
    valgt_antall_str = alle_menyer[1].valgt

    if valgt_måling == None and valgt_antall_str == None:
        print("Du må velge både kategori og antall")
        return

    if valgt_måling == None:
        print("DU må velge en kategori")
        return

    if valgt_antall_str == None:
        print("Du må velge et antall")
        return

    valgt_antall = int(valgt_antall_str)

    flestytland = df["Country"].value_counts().head(valgt_antall)
    for lander in flestytland.keys():
        landinfo = df[(df["Country"] == lander)]
        abonnementer = landinfo["subscribers"].mean()
        visninger = landinfo["video views"].mean()
        opplastninger = landinfo["uploads"].mean()
        landliste.append(str(lander))
        abonnementliste.append(round(abonnementer))
        visningliste.append(round(visninger))
        opplastingliste.append(round(opplastninger))


    if valgt_måling == "subscribers":
        plt.figure(figsize=(10, 5))
        plt.bar(landliste, abonnementliste)
        plt.title("Gjennomsnittlig antall abonnenter per kanal")
        plt.xlabel("Land")
        plt.ylabel("Abonnenter")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
    if valgt_måling == "video views":
    # Diagram 2: Visninger
        plt.figure(figsize=(10, 5))
        plt.bar(landliste, visningliste)
        plt.title("Gjennomsnittlig antall videovisninger per kanal")
        plt.xlabel("Land")
        plt.ylabel("Visninger")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
    if valgt_måling == "uploads":
        # Diagram 3: Opplastninger
        plt.figure(figsize=(10, 5))
        plt.bar(landliste, opplastingliste)
        plt.title("Gjennomsnittlig antall opplastninger per kanal")
        plt.xlabel("Land")
        plt.ylabel("Opplastninger")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()



'''
def vis_graf():
    fig, axs = plt.subplots(1, 3, figsize=(24, 8))  # 1 rad, 3 kolonner

    # Diagram 1: Abonnenter
    axs[0].bar(landliste, abonnementliste)
    axs[0].set_title("Abonnenter")
    axs[0].set_xlabel("Land")
    axs[0].set_ylabel("Gjennomsnitt per kanal")
    axs[0].tick_params(axis='x', rotation=45)
    axs[0].grid(axis='y', linestyle='--', alpha=0.5)

    # Diagram 2: Visninger
    axs[1].bar(landliste, visningliste)
    axs[1].set_title("Visninger")
    axs[1].set_xlabel("Land")
    axs[1].tick_params(axis='x', rotation=45)
    axs[1].grid(axis='y', linestyle='--', alpha=0.5)

    # Diagram 3: Opplastninger
    axs[2].bar(landliste, opplastingliste)
    axs[2].set_title("Opplastninger")
    axs[2].set_xlabel("Land")
    axs[2].tick_params(axis='x', rotation=45)
    axs[2].grid(axis='y', linestyle='--', alpha=0.5)

    fig.suptitle("Gjennomsnitt per kanal i topp 10 land", fontsize=16)
    fig.tight_layout(rect=[0, 0, 1, 0.95])  # Gi plass til tittel
    plt.show()
'''

# --- Museklikk-håndtering ---
def museklikk(pos):
    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.visAlternativer(pos)
        elif m.rektangel.collidepoint(pos):
            print(f"Klikket på: {m.tekst}")
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

    # Tegn GUI
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

    # Tekstlabels
    font = pg.font.SysFont("Tahoma", 24)
    VINDU.blit(font.render("Antall land", True, (0, 0, 0)), (100, 120))
    VINDU.blit(font.render("Kategori", True, (0, 0, 0)), (300, 20))

    pg.display.flip()
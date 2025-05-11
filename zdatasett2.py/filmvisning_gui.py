import pygame as pg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pg_meny_scroll import Knapp, Nedtrekksliste
from pg_meny_scroll import MENYFARGE, HOVERFARGE

# --- Last inn og rens data ---
filnavn = "zfilmvisning.csv"
df = pd.read_csv(filnavn)

# Rens opp tekst

df["Sjanger"] = df["Sjanger"].astype(str).str.strip()
df["Toppfilm"] = df["Toppfilm"].astype(str).str.strip()
df["Land"] = df["Land"].astype(str).str.strip()

# Rens tallkolonner
df["Besøkstall"] = pd.to_numeric(df["Besøkstall"], errors="coerce")
df["Årstall"] = pd.to_numeric(df["Årstall"], errors="coerce")

#aar_liste= sorted([int(aar) for aar in df["Årstall"].dropna().unique()])
aar_liste= sorted([str(int(aar)) for aar in df["Årstall"].dropna().unique()])


# Menyer og knapper
alle_menyer = []     
alle_menyer.append(Knapp(450, 50, "Vis graf"))       # index 0
alle_menyer.append(Nedtrekksliste(100, 150, aar_liste))       # index 1

# --- Pygame setup ---
BAKGRUNNSFARGE = (255, 255, 255)
VINDU_BREDDE = 600
VINDU_HOYDE = 400

pg.init()
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
# --- Funksjon for å vise graf ---


def vis_graf():
    sjangerbesøk_liste = []
    sjangerliste = df["Sjanger"].unique()
    valgt_tekst = alle_menyer[1].valgt

    if valgt_tekst is None:
        print("Du må velge et år")
        return
    
    valgt_aar = int(valgt_tekst)
    
    aar_df = df[df["Årstall"] == valgt_aar]

    sortert_besøk_liste = aar_df.sort_values("Besøkstall", ascending=False)
    mest_land = sortert_besøk_liste["Toppfilm"].iloc[0]

    for sjang in sjangerliste:
        filminfo = aar_df[aar_df["Sjanger"] == sjang]
        besøkstall = filminfo["Besøkstall"].sum() 
        sjangerbesøk_liste.append(besøkstall)


    plt.figure(figsize=(10, 5))
    plt.bar(sjangerliste, sjangerbesøk_liste)
    plt.title(f'Total besøkstall per kategori (toppfilm = {mest_land})')
    plt.xlabel("Kategori")
    plt.ylabel("Besøkstall")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


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

    pg.display.flip()
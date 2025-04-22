
import pygame as pg
import matplotlib.pyplot as plt
import pandas as pd
from pg_meny_scroll import Knapp, Nedtrekksliste
from pg_meny_scroll import MENYFARGE, HOVERFARGE

# --- Last inn og rens data ---
filnavn = "yt_statistikk.csv"
df = pd.read_csv(filnavn)

# Rens opp tekst
df["category"] = df["category"].astype(str).str.strip()
df["Country"] = df["Country"].astype(str).str.strip()
df["Youtuber"] = df["Youtuber"].astype(str).str.strip()

# Rens tallkolonner
df["subscribers"] = pd.to_numeric(df["subscribers"], errors="coerce")
df["video views"] = pd.to_numeric(df["video views"], errors="coerce")
df["uploads"] = pd.to_numeric(df["uploads"], errors="coerce")

# Hent unike verdier
kategoriliste = sorted(df["category"].dropna().unique())
landliste = sorted(df["Country"].dropna().unique())
målingstyper = ["subscribers", "video views", "uploads"]

# --- Pygame setup ---
BAKGRUNNSFARGE = (255, 255, 255)
VINDU_BREDDE = 600
VINDU_HOYDE = 400

pg.init()
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Menyer og knapper
alle_menyer = []
alle_menyer.append(Nedtrekksliste(20, 50, kategoriliste))     # index 0
alle_menyer.append(Nedtrekksliste(100, 150, landliste))       # index 1
alle_menyer.append(Knapp(450, 50, "Vis graf"))                # index 2
alle_menyer.append(Nedtrekksliste(300, 50, målingstyper))     # index 3

# --- Funksjon for å vise graf ---
def vis_graf():
    valgt_kategori = alle_menyer[0].valgt
    valgt_land = alle_menyer[1].valgt
    valgt_måling = alle_menyer[3].valgt

    if None in (valgt_kategori, valgt_land, valgt_måling):
        print("Du må velge kategori, land og måling.")
        return

    print("Valgt kategori:", valgt_kategori)
    print("Valgt land:", valgt_land)
    print("Valgt måling:", valgt_måling)

    # Filtrer
    filtrert = df[
        (df["category"] == valgt_kategori) &
        (df["Country"] == valgt_land)
    ].dropna(subset=["Youtuber", valgt_måling])

    print("Antall rader etter filtrering:", filtrert.shape[0])
    print("Unike Youtubere:", filtrert["Youtuber"].nunique())

    if filtrert.empty or filtrert["Youtuber"].nunique() == 0:
        print("Fant ingen passende data.")
        return

    # Fjern duplikater først, så sorter
    topp10 = (
        filtrert.drop_duplicates(subset="Youtuber")
        .sort_values(by=valgt_måling, ascending=False)
        .head(10)
    )

    # Sjekk igjen
    if topp10.empty:
        print("Ingen nok data til topp 10.")
        return

    # Plot
    plt.figure(figsize=(10, 6))
    plt.barh(topp10["Youtuber"], topp10[valgt_måling])
    plt.gca().invert_yaxis()
    plt.xlabel(valgt_måling.capitalize())
    plt.title(f"Topp 10 '{valgt_kategori}' i {valgt_land}")
    plt.grid(axis="x")
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
    VINDU.blit(font.render("Kategori", True, (0, 0, 0)), (20, 20))
    VINDU.blit(font.render("Land", True, (0, 0, 0)), (100, 120))
    VINDU.blit(font.render("Måling", True, (0, 0, 0)), (300, 20))

    pg.display.flip()
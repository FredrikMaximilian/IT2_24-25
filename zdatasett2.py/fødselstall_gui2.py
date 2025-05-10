import pandas as pd
import pygame as pg
import matplotlib.pyplot as plt
import numpy as np
from pg_meny_scroll import Knapp, Nedtrekksliste
from pg_meny_scroll import MENYFARGE, HOVERFARGE

# --- DATAIMPORT OG RENSING ---
filnavn = "zDatasett_fodselstall.csv"
df = pd.read_csv(filnavn, sep="\t", encoding="latin1")
df.columns = ["År", "Fødselstall", "Innflyttinger", "Utflyttinger"]
kolonner = ["År", "Fødselstall", "Innflyttinger", "Utflyttinger"]
df[kolonner] = df[kolonner].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=kolonner)
df["År"] = df["År"].astype(int)
df["Netto folkevekst"] = df["Fødselstall"] + df["Innflyttinger"] - df["Utflyttinger"]

# --- GUI-OPPSETT ---
årstall = sorted(df["År"].unique())
kategorier = ["Fødselstall", "Innflyttinger", "Utflyttinger", "Netto folkevekst"]

pg.init()
BAKGRUNNSFARGE = (255, 255, 255)
VINDU_BREDDE = 600
VINDU_HOYDE = 400
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Folketallsvisning")

alle_menyer = [
    Nedtrekksliste(20, 50, [str(år) for år in årstall]),      # Startår
    Nedtrekksliste(240, 50, [str(år) for år in årstall]),     # Sluttår
    Nedtrekksliste(460, 50, kategorier),                      # Kategori
    Knapp(450, 300, "Vis graf")                               # Kjør-knapp
]

# --- VIS GRAF ---
def vis_graf():
    try:
        fra_år = int(alle_menyer[0].valgt)
        til_år = int(alle_menyer[1].valgt)
        kategori = alle_menyer[2].valgt

        if fra_år > til_år:
            print("Første år må være lavere enn siste")
            return

        data = df[(df["År"] >= fra_år) & (df["År"] <= til_år)]
        x_år = data["År"].to_numpy()
        ydata = data[kategori].to_numpy()

        gyldige = ~np.isnan(ydata)
        plt.plot(x_år[gyldige], ydata[gyldige])
        plt.title(f"{kategori} fra {fra_år} til {til_år}")
        plt.xlabel("År")
        plt.ylabel(kategori)
        plt.grid()
        plt.show()
    except Exception as e:
        print("Feil:", e)

# --- HÅNDTER MUSEKLIKK ---
def museklikk(posisjon):
    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.visAlternativer(posisjon)
        elif m.rektangel.collidepoint(posisjon):
            if isinstance(m, Nedtrekksliste):
                m.visAlternativer(posisjon)
            elif isinstance(m, Knapp) and m.tekst == "Vis graf":
                vis_graf()

# --- HOVEDLØKKE ---
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

    # Scroll med piltaster
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
        farge = HOVERFARGE if m.rektangel.collidepoint(muspos) else MENYFARGE
        m.tegn(VINDU, farge)

    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:
            m.tegn(VINDU, HOVERFARGE)

    # Tekster
    font = pg.font.SysFont("Tahoma", 24)
    VINDU.blit(font.render("Startår", True, (0, 0, 0)), (20, 20))
    VINDU.blit(font.render("Sluttår", True, (0, 0, 0)), (240, 20))
    VINDU.blit(font.render("Kategori", True, (0, 0, 0)), (460, 20))

    pg.display.flip()

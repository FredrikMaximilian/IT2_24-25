import pygame as pg  # Importerer pygame for GUI
import matplotlib.pyplot as plt  # Importerer matplotlib for plotting
import numpy as np  # Importerer numpy for numeriske operasjoner
from pg_meny_scroll import Knapp, Nedtrekksliste  # Importerer egendefinerte klasser for GUI-elementer
from pg_meny_scroll import MENYFARGE, HOVERFARGE  # Importerer fargekonstanter
import pandas as pd


filnavn = "zgoogleplaystore.csv"  # Navn på CSV-filen som inneholder data
df = pd.read_csv(filnavn)
kategoriliste = sorted((df["Category"].dropna().unique()))
#df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")


# Konstanter for GUI
BAKGRUNNSFARGE = (255, 255, 255)  # Hvit bakgrunnsfarge
VINDU_BREDDE = 600  # Bredde på vinduet
VINDU_HOYDE = 400  # Høyde på vinduet

pg.init()  # Initialiserer pygame
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])  # Oppretter pygame-vindu

# En felles liste med alle menyer
alle_menyer = []  # Liste for å lagre alle GUI-elementer

# Legger til ulike nedtrekkslister og knapper
alle_menyer.append(Nedtrekksliste(20, 50, kategoriliste))  
alle_menyer.append(Knapp(450, 50, "Vis graf")) 



def vis_graf():
    valgt_kategori = alle_menyer[0].valgt
    if valgt_kategori is None:
        print("Du må velge en kategori")
        return
    
    filtrert = df[df["Category"] == valgt_kategori].dropna(subset = ["Rating"])
    topp10 = filtrert.drop_duplicates(subset = "App").sort_values(by = "Rating", ascending = False).head(10)

    if topp10.empty:
        print("Fant ingen apper i denne kategorien")
        return

        # Plotter grafen
    plt.figure(figsize=(10, 6))
    plt.barh(topp10["App"], topp10["Rating"])
    plt.gca().invert_yaxis()  # Høyest øverst
    plt.xlabel("Rating")
    plt.title(f"Topp 10 apper i kategorien '{valgt_kategori}'")
    plt.tight_layout()
    plt.grid(axis="x")
    plt.show()



# Funksjon for å håndtere museklikk
def museklikk(posisjon):
    for m in alle_menyer:  # Itererer gjennom alle GUI-elementer
        if isinstance(m, Nedtrekksliste) and m.aktiv:  # Sjekker om elementet er en aktiv nedtrekksliste
            m.visAlternativer(posisjon)  # Viser alternativer for nedtrekkslisten
        elif m.rektangel.collidepoint(posisjon):  # Sjekker om museklikket er innenfor elementets rektangel
            print(f"Klikket på: {m.tekst}")
            if isinstance(m, Nedtrekksliste):
                m.visAlternativer(posisjon)
            elif isinstance(m, Knapp) and m.tekst == "Vis graf":  # Sjekker om knappen "Vis graf" ble klikket
                vis_graf()  # Kaller funksjonen for å vise graf

# Hovedløkke
fortsett = True  # Variabel for å holde hovedløkken i gang
scroll_target = None  # Holder styr på hvilken nedtrekksliste som skal scrolle
scroll_delay = 40  # Millisekunder mellom scroll
last_scroll_time = 0  # Tidspunkt for siste scroll

while fortsett:
    nå = pg.time.get_ticks()  # Henter nåværende tid i millisekunder

    for event in pg.event.get():  # Itererer gjennom alle pygame-hendelser
        if event.type == pg.QUIT:  # Sjekker om brukeren lukker vinduet
            fortsett = False

        elif event.type == pg.MOUSEBUTTONDOWN:  # Sjekker om brukeren klikker med musen
            museklikk(event.pos)

        elif event.type == pg.KEYDOWN:  # Sjekker om brukeren trykker på en tast
            for m in alle_menyer:
                if isinstance(m, Nedtrekksliste) and m.aktiv:
                    scroll_target = m  # Aktiverer scroll for denne menyen

    # Scroll ved hold-inn av piltast ↑/↓
    taster = pg.key.get_pressed()  # Henter status for alle taster
    if scroll_target:
        if taster[pg.K_DOWN] and nå - last_scroll_time > scroll_delay:  # Sjekker om pil ned er trykket
            scroll_target.scroll(1)  # Scroller ned
            last_scroll_time = nå
        elif taster[pg.K_UP] and nå - last_scroll_time > scroll_delay:  # Sjekker om pil opp er trykket
            scroll_target.scroll(-1)  # Scroller opp
            last_scroll_time = nå

    # Tegner bakgrunn
    VINDU.fill(BAKGRUNNSFARGE)  # Fyller vinduet med bakgrunnsfargen
    muspos = pg.mouse.get_pos()  # Henter museposisjonen

    # Tegner hover + vanlig
    for m in alle_menyer:
        if m.rektangel.collidepoint(muspos):  # Sjekker om musen er over elementet
            m.tegn(VINDU, HOVERFARGE)  # Tegner elementet med hoverfarge
        else:
            m.tegn(VINDU, MENYFARGE)  # Tegner elementet med standardfarge

    # Tegner nedtrekksalternativer hvis aktiv
    for m in alle_menyer:
        if isinstance(m, Nedtrekksliste) and m.aktiv:  # Sjekker om nedtrekkslisten er aktiv
            m.tegn(VINDU, HOVERFARGE)  # Tegner alternativer med hoverfarge


    #Legger til beskrivelse
    font = pg.font.SysFont("Tahoma", 24) #Definerer font

    tekst_start = font.render("Kategori", True, (0, 0, 0)) #Definerer hva som skal stå og farge
    VINDU.blit(tekst_start, (20, 20)) #Definerer posisjon

    # Oppdaterer skjerm
    pg.display.flip()  # Oppdaterer pygame-vinduet


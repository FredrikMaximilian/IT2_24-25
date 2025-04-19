import pygame as pg  # Importerer pygame for GUI
import matplotlib.pyplot as plt  # Importerer matplotlib for plotting
import numpy as np  # Importerer numpy for numeriske operasjoner
from pg_meny_scroll import Knapp, Nedtrekksliste  # Importerer egendefinerte klasser for GUI-elementer
from pg_meny_scroll import MENYFARGE, HOVERFARGE  # Importerer fargekonstanter

filnavn = "leksedatasett.csv"  # Navn på CSV-filen som inneholder data
årliste = []  # Liste for å lagre årstall
levendefødteliste = []  # Liste for å lagre antall levendefødte
innflytterliste = []  # Liste for å lagre antall innflyttere
utflytterliste = []  # Liste for å lagre antall utflyttere
nettoliste = []  # Liste for å lagre nettoverdier
innutliste = [] #Liste for innflyttere vs utflyttere

# Leser data fra CSV-filen
with open(filnavn, encoding="utf-8") as fil:  # Åpner filen med UTF-8-koding
    next(fil)  # Hopper over første linje (header)
    for linje in fil:  # Itererer gjennom hver linje i filen
        info = linje.strip().split(",")  # Fjerner mellomrom og splitter linjen på komma
        år = int(info[0].strip('"'))  # Konverterer første kolonne (år) til heltall
        årliste.append(år)  # Legger til år i årliste

        try:
            levendefødteliste.append(int(info[1]))  # Forsøker å konvertere levendefødte til heltall
        except:
            levendefødteliste.append(np.nan)  # Hvis feil, legger til NaN (ikke et tall)
        try:
            innflytterliste.append(int(info[2]))  # Forsøker å konvertere innflyttere til heltall
        except:
            innflytterliste.append(np.nan)  # Hvis feil, legger til NaN
        try:
            utflytterliste.append(int(info[3]))  # Forsøker å konvertere utflyttere til heltall
        except:
            utflytterliste.append(np.nan)  # Hvis feil, legger til NaN

# Beregner nettoverdier basert på data
for i in range(len(årliste)):
    inn = innflytterliste[i]
    ut = utflytterliste[i]
    lefø = levendefødteliste[i]
    if not np.isnan(inn) and not np.isnan(ut) and not np.isnan(lefø):  # Sjekker om verdiene ikke er NaN
        netto = lefø + inn - ut  # Beregner nettoverdien
    else:
        netto = np.nan  # Setter netto til NaN hvis noen verdier mangler
    nettoliste.append(netto)  # Legger nettoverdien til i listen

for j in range(len(årliste)):
    inna = innflytterliste[j]
    uta = utflytterliste[j]
    if not np.isnan(inna) and not np.isnan(uta):  # Sjekker om verdiene ikke er NaN
        innut = inna - uta  # Beregner inn vs ut
    else:
        innut = np.nan  # Setter netto til NaN hvis noen verdier mangler
    innutliste.append(innut)  # Legger nettoverdien til i listen

# Konstanter for GUI
BAKGRUNNSFARGE = (255, 255, 255)  # Hvit bakgrunnsfarge
VINDU_BREDDE = 600  # Bredde på vinduet
VINDU_HOYDE = 400  # Høyde på vinduet

pg.init()  # Initialiserer pygame
VINDU = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])  # Oppretter pygame-vindu

# En felles liste med alle menyer
alle_menyer = []  # Liste for å lagre alle GUI-elementer
kategorier = ["fødte", "inn", "ut", "netto", "innut"]  # Kategorier for data

# Legger til ulike nedtrekkslister og knapper
alle_menyer.append(Nedtrekksliste(20, 50, [str(år) for år in årliste]))  # Nedtrekksliste for startår
alle_menyer.append(Nedtrekksliste(240, 50, [str(år) for år in årliste]))  # Nedtrekksliste for sluttår
alle_menyer.append(Nedtrekksliste(460, 50, kategorier))  # Nedtrekksliste for kategori
alle_menyer.append(Knapp(450, 300, "Vis graf"))  # Knapp for å vise graf

# Funksjon for å vise graf basert på brukerens valg
def vis_graf():
    try:
        fra_år = int(alle_menyer[0].valgt)  # Henter valgt startår
        til_år = int(alle_menyer[1].valgt)  # Henter valgt sluttår
        kategori = alle_menyer[2].valgt  # Henter valgt kategori

        if fra_år is None or til_år is None or kategori is None:  # Sjekker om alle valg er gjort
            print("Du må velge alle tre verdier.")
            return

        if fra_år > til_år:  # Sjekker om startår er mindre enn sluttår
            print("Første år må være lavere enn siste")
            return

        start_i = årliste.index(fra_år)  # Finner indeksen for startår
        slutt_i = årliste.index(til_år) + 1  # Finner indeksen for sluttår
        x_år = årliste[start_i:slutt_i]  # Henter årstallene i det valgte intervallet

        # Velger riktig datasett basert på kategori
        if kategori == "fødte":
            yinfo = levendefødteliste[start_i:slutt_i]
            ynavn = "Levendefødte"
        elif kategori == "inn":
            yinfo = innflytterliste[start_i:slutt_i]
            ynavn = "Innflyttere"
        elif kategori == "ut":
            yinfo = utflytterliste[start_i:slutt_i]
            ynavn = "Utflyttere"
        elif kategori == "netto":
            yinfo = nettoliste[start_i:slutt_i]
            ynavn = "Nettovekst"
        elif kategori == "innut":
            yinfo = innutliste[start_i:slutt_i]
            ynavn = "Inn vs utflyttere"
        else:
            print("Ugyldig kategori.")
            return

        # Plotter grafen
        plt.plot(x_år, yinfo)
        plt.title(f'{ynavn} fra {fra_år} til {til_år}')
        plt.xlabel("År")
        plt.ylabel(ynavn)
        plt.grid()
        plt.show()

    except Exception as e:  # Håndterer feil
        print("Noe gikk galt:", e)

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

    tekst_start = font.render("Startår", True, (0, 0, 0)) #Definerer hva som skal stå og farge
    VINDU.blit(tekst_start, (20, 20)) #Definerer posisjon
    tekst_slutt = font.render("Sluttår", True, (0, 0, 0)) #Definerer hva som skal stå og farge
    VINDU.blit(tekst_slutt, (240, 20)) #Definerer posisjon
    tekst_kategori = font.render("Kategori", True, (0, 0, 0)) #Definerer hva som skal stå og farge
    VINDU.blit(tekst_kategori, (460, 20)) #Definerer posisjon

    # Oppdaterer skjerm
    pg.display.flip()  # Oppdaterer pygame-vinduet


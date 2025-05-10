import pygame as pg
import pandas as pd
import matplotlib.pyplot as plt

# === GUI-klasser ===
class Knapp:
    def __init__(self, x, y, tekst):
        self.rekt = pg.Rect(x, y, 140, 35)
        self.tekst = tekst

    def tegn(self, vindu, valgt=False):
        farge = (150, 200, 250) if valgt else (200, 200, 200)
        pg.draw.rect(vindu, farge, self.rekt)
        tekst_render = FONT.render(self.tekst, True, (0, 0, 0))
        vindu.blit(tekst_render, (self.rekt.x + 10, self.rekt.y + 7))

    def trykket(self, pos):
        return self.rekt.collidepoint(pos)

class Nedtrekksliste:
    def __init__(self, x, y, valg_liste):
        self.rekt = pg.Rect(x, y, 180, 35)
        self.valg = valg_liste
        self.valgt = valg_liste[0]
        self.åpen = False

    def tegn(self, vindu):
        pg.draw.rect(vindu, (200, 200, 200), self.rekt)
        tekst = FONT.render(self.valgt, True, (0, 0, 0))
        vindu.blit(tekst, (self.rekt.x + 10, self.rekt.y + 7))
        if self.åpen:
            for i, v in enumerate(self.valg):
                r = pg.Rect(self.rekt.x, self.rekt.y + (i+1)*35, 180, 35)
                pg.draw.rect(vindu, (220, 220, 220), r)
                t = FONT.render(v, True, (0, 0, 0))
                vindu.blit(t, (r.x + 10, r.y + 7))

    def trykk(self, pos):
        if self.rekt.collidepoint(pos):
            self.åpen = not self.åpen
        elif self.åpen:
            for i, v in enumerate(self.valg):
                r = pg.Rect(self.rekt.x, self.rekt.y + (i+1)*35, 180, 35)
                if r.collidepoint(pos):
                    self.valgt = v
            self.åpen = False

# === Last inn og klargjør data ===
filnavn = "tid_på_aktiviteter.csv"
df = pd.read_csv(filnavn, sep=";", encoding="utf-8", skiprows=1)
df.columns = ["Aktivitet", "Kjønn", "Tidsbruk"]
df["Aktivitet"] = df["Aktivitet"].str.replace("�", "ø").str.replace(r"^ø\s*", "", regex=True).str.strip()
df["Kjønn"] = df["Kjønn"].str.replace("�", "ø").str.strip()

def timer_og_minutter_til_timer(verdi):
    timer, minutter = divmod(float(verdi), 1)
    minutter = round(minutter * 100)
    return timer + minutter / 60

df["Tidsbruk"] = df["Tidsbruk"].apply(timer_og_minutter_til_timer)

def vis_graf(kjønn, graphtype):
    filtrert = df[df["Kjønn"] == kjønn]
    aktiviteter = filtrert["Aktivitet"]
    timer = filtrert["Tidsbruk"]

    if graphtype == "Stolpe":
        plt.barh(aktiviteter, timer)
        plt.xlabel("Timer per dag")
        plt.title(f"Tidsbruk per aktivitet ({kjønn})")
    elif graphtype == "Kakediagram":
        plt.pie(timer, labels=aktiviteter, startangle=90, wedgeprops={"edgecolor": "white"})
        plt.title(f"Andel av døgnet brukt på aktiviteter ({kjønn})")
    plt.tight_layout()
    plt.show()

# === GUI ===
pg.init()
FONT = pg.font.SysFont("Arial", 20)
vindu = pg.display.set_mode((600, 300))
pg.display.set_caption("Tidsbruk-visualisering")

kjønn_valg = Nedtrekksliste(30, 30, ["Alle", "Menn", "Kvinner"])
graf_valg = Nedtrekksliste(30, 90, ["Stolpe", "Kakediagram"])
vis_knapp = Knapp(30, 160, "Vis graf")

# === Løkke ===
kjør = True
while kjør:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjør = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            kjønn_valg.trykk(pos)
            graf_valg.trykk(pos)
            if vis_knapp.trykket(pos):
                vis_graf(kjønn_valg.valgt, graf_valg.valgt)

    vindu.fill((240, 240, 240))
    kjønn_valg.tegn(vindu)
    graf_valg.tegn(vindu)
    vis_knapp.tegn(vindu)
    pg.display.flip()

pg.quit()

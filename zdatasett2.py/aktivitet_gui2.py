import pygame as pg
import pandas as pd
import matplotlib.pyplot as plt

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
filnavn = "zaktivitet.csv"
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
        # Kombiner og sorter data
        kakedata = pd.DataFrame({"Aktivitet": aktiviteter, "Tidsbruk": timer})
        kakedata = kakedata.sort_values(by="Tidsbruk", ascending=False)

        # Beregn total og prosent
        total = kakedata["Tidsbruk"].sum()
        kakedata["Prosent"] = kakedata["Tidsbruk"] / total * 100

        # Del opp i store og små
        store = kakedata[kakedata["Prosent"] >= 2].copy()
        små = kakedata[kakedata["Prosent"] < 2].copy()

        # Legg til en "Annet"-rad som summerer de små
        if not små.empty:
            annet_sum = små["Tidsbruk"].sum()
            annet_prosent = små["Prosent"].sum()
            store = pd.concat([store, pd.DataFrame([{
                "Aktivitet": "Annet",
                "Tidsbruk": annet_sum,
                "Prosent": annet_prosent
            }])])

        # Funksjon for å vise prosent
        def vis_prosent(pct):
            return f"{pct:.1f}%" if pct >= 2 else ""

        # Plot
        plt.figure(figsize=(9, 7))
        wedges, texts, autotexts = plt.pie(
            store["Tidsbruk"],
            labels=store["Aktivitet"],
            startangle=90,
            autopct=vis_prosent,
            wedgeprops={"edgecolor": "white"},
            labeldistance=1.05,
            pctdistance=0.75
        )

        plt.title(f"Andel av døgnet brukt på aktiviteter ({kjønn})")
        plt.tight_layout()


        # Legg til legend for de små
        if not små.empty:
            etiketter = [f"{r['Aktivitet']} ({r['Prosent']:.1f}%)" for _, r in små.iterrows()]
            plt.legend(etiketter, title="Små kategorier (< 2%)", loc="center left", bbox_to_anchor=(1, 0.5))

        plt.title(f"Andel av døgnet brukt på aktiviteter ({kjønn})")
        plt.tight_layout()

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

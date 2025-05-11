
import pandas as pd
import matplotlib.pyplot as plt


filnavn = "ztid_på_aktiviteter.csv"

df = pd.read_csv(filnavn, sep=";", encoding="utf-8", skiprows=1)

# Gi riktige kolonnenavn
df.columns = ["Aktivitet", "Kjønn", "Tidsbruk"]

# Rens opp i spesialtegn og fjern ledende "ø" kun hvis den står først
df["Aktivitet"] = (
    df["Aktivitet"].str.replace("�", "ø").str.replace(r"^ø\s*", "", regex=True).str.strip())
    #.str.replace(r"^ø\s+", "", regex=True) hvis man kun vil fjerne ø når det ikke er mellomrom

df["Kjønn"] = df["Kjønn"].str.replace("�", "ø").str.strip()

def timer_og_minutter_til_timer(verdi):
    timer, minutter = divmod(float(verdi), 1)
    minutter = round(minutter * 100)
    return timer + minutter / 60

df["Tidsbruk"] = df["Tidsbruk"].apply(timer_og_minutter_til_timer)
#print(df.to_string(index=False)


gyldige_kjønn = df["Kjønn"].unique()

while True:
    kjønntekst = str(input("Skriv inn kjønn (Alle, Menn, Kvinner): ")).capitalize().strip()
    if kjønntekst not in gyldige_kjønn:
        print(f"Ugyldig kjønn. Prøv en av: {', '.join(gyldige_kjønn)}")
    else: 
        filtrert = df[df["Kjønn"] == kjønntekst]
        break


print(f"\nTidsbruk for: {kjønntekst}\n")
#print(filtrert[["Aktivitet", "Tidsbruk"]].to_string(index=False)) #Print liste

aktivitetsliste = filtrert["Aktivitet"].unique()
tidsliste = filtrert["Tidsbruk"].to_list()

"""
##Med bar
plt.figure(figsize=(10, 6))
plt.barh(aktivitetsliste, tidsliste)
plt.xlabel("Timer per dag")
plt.title(f'Tidsbruk per aktivitet ({kjønntekst})')
plt.grid(axis="x", linestyle="--", linewidth=0.7, alpha=0.7)
plt.xticks(ticks=range(0, int(max(tidsliste)) + 2))
plt.tight_layout()
plt.show()
"""


## Pie chart
#Etikett uten prosent
etiketter = [f"{aktivitet} ({tid:.2f} t)" for aktivitet, tid in zip(aktivitetsliste, tidsliste)]

#Med prosent
total = sum(tidsliste)
etikettprosent = [f"{a} ({t:.2f} t / {t / total * 100:.1f}%)" for a, t in zip(aktivitetsliste, tidsliste)]

#Prosent i kaka

plt.figure(figsize=(8, 8))
'''
wedges, texts, autotexts = plt.pie(
    tidsliste,
    #autopct=lambda p: f'{p:.1f}%\n({p * 24 / 100:.2f} t)',
    startangle=90,
    wedgeprops={'edgecolor': 'white'}
)
'''

#Prosent utenfor kaka
plt.pie(tidsliste, startangle=90, wedgeprops={'edgecolor': 'white'})

plt.title(f"Andel av døgnet brukt på aktiviteter ({kjønntekst})")
plt.legend(
    #wedges,
    #aktivitetsliste,
    etiketter,
    title="Aktiviteter",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=9
)
plt.tight_layout()
plt.show()


#Kun de største prosentene
'''
def vis_prosent_hvis_stor(p):
    return f'{p:.1f}%' if p > 5 else ''

plt.pie(
    tidsliste,
    autopct=vis_prosent_hvis_stor,
    startangle=90,
    wedgeprops={'edgecolor': 'white'}
)
plt.title(f"Andel av døgnet brukt på aktiviteter ({kjønntekst})")
plt.legend(
    #wedges,
    #aktivitetsliste,
    etiketter,
    title="Aktiviteter",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=9
)
plt.tight_layout()
plt.show()
'''
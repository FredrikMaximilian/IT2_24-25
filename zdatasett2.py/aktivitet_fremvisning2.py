import pandas as pd

filnavn = "zaktivitet.csv"
df = pd.read_csv(filnavn, sep=";", encoding="utf-8", skiprows = 1)
df.columns = ("Aktivitet", "Kjønn", "Tidsbruk")
df["Aktivitet"] = (
    df["Aktivitet"].str.replace("�", "ø").str.replace(r"^ø\s*", "", regex=True).str.strip())
df["Kjønn"] = df["Kjønn"].str.replace("�", "ø").str.strip()

kjønn = input("Skriv inn kjønn (M, K, A): ").strip().upper()

# Konverter til gyldige verdier
mapping = {"M": "Menn", "K": "Kvinner", "A": "Alle"}
if kjønn in mapping:
    valgt_kjønn = mapping[kjønn]
    dfkjønn = df[df["Kjønn"] == valgt_kjønn]
    print(dfkjønn)
else:
    print("Ugyldig kjønn. Skriv M for Menn, K for Kvinner eller A for Alle.")


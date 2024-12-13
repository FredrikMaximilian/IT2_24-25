from FredrikWatchBiblotek import *
from FredrikWatchBiblotek import skriv_ut_tekst as s

def main():
    # Opprett spiller
    #s("Skriv inn navnet ditt: ")
    #spiller = Spiller(navn=str(input("> ")))
    spiller = Spiller(navn=str(input("Skriv inn navnet ditt: ")))
    
    # Opprett våpen
    pistol = Pistol(navn="Pistol", skade=30)
    gift_kniv = GiftKniv(navn="GiftKniv", skade=20, giftVarighet=3)
    lang_sverd = LangSverd(navn="LangSverd", skade=100, Antallslag=2)
    hagle = Hagle(navn="Hagle", skade=50)
    
    våpen_liste = [pistol, gift_kniv, lang_sverd, hagle]
    
    # Opprett helsegjenstander
    medkit = Medkit(navn="Medkit", helbredelse=100)
    bandasje = Bandasje(navn="Bandasje", helbredelse=15)
    
    spiller.ryggsekk = [medkit, medkit, bandasje, bandasje, bandasje]
    
    # Opprett monstre
    monstre = [
        Troll(navn="Troll", helse=160, skade=20),
        Drage(navn="Drage", helse=200, skade=50),
        Vampyr(navn="Vampyr", helse=130, skade=15, livstapp_skade=10, livstapp_varighet=3)
    ]

    s(f'Velkommen til FredrikWatch')
    for monster in monstre:
        if monster.navn == "Troll":
            s("Du har møtt på et Troll!")
        else:
            s(f"\nEn {monster.navn} dukker opp!")
        
        while spiller.helse > 0 and monster.helse > 0:

            if isinstance(monster, Troll):
                monster.regenerer()

            s("\nHva vil du gjøre?")
            print("1: Velg våpen")
            print("2: Bruk helsegjenstand")
            print("3: Angrip monsteret")
            print("4: Sjekk helse")
            
            valg = input("> ")
            
            if valg == "1":
                s("Velg et våpen:")
                for i, våpen in enumerate(våpen_liste, 1):
                    print(f"{i}: {våpen}")
                våpen_valg = int(input("> ")) - 1
                if 0 <= våpen_valg < len(våpen_liste):
                    spiller.våpen = våpen_liste[våpen_valg]
                    s(f"Du valgte {spiller.våpen.navn}.")
                else:
                    s("Ugyldig valg.")
            
            elif valg == "2":
                s("Velg en helsegjenstand:")
                for i, item in enumerate(spiller.ryggsekk, 1):
                    print(f"{i}: {item.navn}")
                item_valg = int(input("> ")) - 1
                if 0 <= item_valg < len(spiller.ryggsekk):
                    spiller.bruk_item(spiller.ryggsekk[item_valg])
                else:
                    s("Ugyldig valg.")
            
            elif valg == "3":
                if spiller.våpen:
                    if isinstance(spiller.våpen, GiftKniv):
                        spiller.våpen.tilbakestill()
                        if not monster.forgiftet:
                            spiller.våpen.førsteStikk(monster)  # Gjør første stikk
                        for i in range(spiller.våpen.giftVarighet):
                            spiller.våpen.påførGiftSkade(monster)  # Påfør giftskade i etterfølgende runder

                    elif isinstance(spiller.våpen, LangSverd):
                        if spiller.våpen.Antallslag > 0:
                            spiller.våpen.slag(monster)
                        else:
                            s(f'Du kan ikke bruke {spiller.våpen.navn} lenger. Antall slag er brukt opp.')


                    elif isinstance(spiller.våpen, Hagle):
                        spiller.våpen.skyt([monster])  # Endre til en liste med monstre hvis det er flere

                    else:
                        spiller.angrep(monster)

                    # Monsteret angriper hvis det fortsatt er i live
                    if monster.helse > 0:
                        if isinstance(monster, Drage):
                            monster.bruk_ild_pust(spiller)
                        elif isinstance(monster, Vampyr):
                            monster.angrep(spiller)
                        else:
                            monster.angrep(spiller)
                else:
                    s("Du har ikke valgt et våpen!")

            
            elif valg == "4":
                print(spiller)
                print(monster)
            
            else:
                print("Ugyldig valg.")
        
        if monster.helse <= 0:
            print(f"Du har beseiret {monster.navn}!")
    
    if spiller.helse <= 0:
        print("Spillet er over. Du tapte!")
    else:
        print("Gratulerer! Du har beseiret alle monstrene!")

if __name__ == "__main__":
    main()

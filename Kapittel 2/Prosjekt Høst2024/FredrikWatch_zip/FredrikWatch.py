from FredrikWatchBiblotek import * # Importer alt fra FredrikWatchBiblotek
from FredrikWatchBiblotek import skriv_ut_tekst as s # Importer skriv_ut_tekst fra FredrikWatchBiblotek

def main(): # Hovedfunksjonen
    spiller = Spiller(navn=str(input("Skriv inn navnet ditt: "))) # Opprett spiller
    
    # Opprett våpen
    pistol = Pistol(navn="Pistol", skade=30) # Opprett pistol
    gift_kniv = GiftKniv(navn="GiftKniv", skade=20, giftVarighet=3) # Opprett giftkniv
    lang_sverd = LangSverd(navn="LangSverd", skade=100, Antallslag=2) # Opprett lang sverd
    hagle = Hagle(navn="Hagle", skade=50) # Opprett hagle
    
    våpen_liste = [pistol, gift_kniv, lang_sverd, hagle] # Liste med våpen
    
    # Opprett helsegjenstander
    medkit = Medkit(navn="Medkit", helbredelse=100) # Opprett medkit
    bandasje = Bandasje(navn="Bandasje", helbredelse=15) #Opprett bandasje
    
    spiller.ryggsekk = [medkit, medkit, bandasje, bandasje, bandasje] # Ryggsekk med helsegjenstander
    
    # Opprett monstre
    monstre = [
        Troll(navn="Troll", helse=160, skade=20), # Opprett troll
        Drage(navn="Drage", helse=200, skade=50), # Opprett drage
        Vampyr(navn="Vampyr", helse=130, skade=15, livstapp_skade=10, livstapp_varighet=3) # Opprett vampyr
    ]

    s(f'Velkommen til FredrikWatch') # Velkomsttekst
    for monster in monstre: # Gå gjennom monstre
        if monster.navn == "Troll": # Hvis monsteret er et troll
            s("Du har møtt på et Troll!") # Skriv ut at du har møtt på et troll
        else: 
            s(f"\nEn {monster.navn} dukker opp!") # Skriv ut at et monster dukker opp
        
        while spiller.helse > 0 and monster.helse > 0: # Så lenge spilleren og monsteret har helse igjen

            if isinstance(monster, Troll): # Hvis monsteret er et troll
                monster.regenerer() # Regenerer helsen til monsteret

            s("\nHva vil du gjøre?") # Spør hva spilleren vil gjøre
            print("1: Velg våpen") # Alternativ for å velge våpen
            print("2: Bruk helsegjenstand") # Alternativ for å bruke helsegjenstand
            print("3: Angrip monsteret") # Alternativ for å angripe monsteret
            print("4: Sjekk helse") # Alternativ for å sjekke helsen til spilleren og monsteret
            
            valg = input("> ") # Les inn valget til spilleren
            
            if valg == "1": # Hvis valget er 1
                s("Velg et våpen:") # Spør spilleren om å velge et våpen
                for i, våpen in enumerate(våpen_liste, 1): # Gå gjennom våpenlisten
                    print(f"{i}: {våpen}") # Skriv ut våpenet
                våpen_valg = int(input("> ")) - 1 # Les inn valget til spilleren
                if 0 <= våpen_valg < len(våpen_liste): # Hvis valget er gyldig
                    spiller.våpen = våpen_liste[våpen_valg] # Sett våpenet til spilleren til valget
                    s(f"Du valgte {spiller.våpen.navn}.") # Skriv ut at spilleren har valgt våpenet
                else: # Hvis valget er ugyldig
                    s("Ugyldig valg.") # Skriv ut at valget er ugyldig
            
            elif valg == "2": # Hvis valget er 2
                s("Velg en helsegjenstand:") # Spør spilleren om å velge en helsegjenstand
                for i, item in enumerate(spiller.ryggsekk, 1): # Gå gjennom helsegjenstandene i ryggsekken
                    print(f"{i}: {item.navn}") # Skriv ut helsegjenstanden
                item_valg = int(input("> ")) - 1 # Les inn valget til spilleren
                if 0 <= item_valg < len(spiller.ryggsekk): # Hvis valget er gyldig
                    spiller.bruk_item(spiller.ryggsekk[item_valg]) # Bruk helsegjenstanden
                else:   # Hvis valget er ugyldig
                    s("Ugyldig valg.") # Skriv ut at valget er ugyldig
            
            elif valg == "3": # Hvis valget er 3
                if spiller.våpen: # Hvis spilleren har valgt et våpen
                    if isinstance(spiller.våpen, GiftKniv): # Hvis spilleren har valgt giftkniv
                        spiller.våpen.tilbakestill() # Tilbakestill giftkniven sånn at giftskaden fortsetter
                        if not monster.forgiftet: # Hvis monsteret ikke er forgiftet
                            spiller.våpen.førsteStikk(monster)  # Gjør første stikk
                        for i in range(spiller.våpen.giftVarighet): # Gå gjennom giftvarigheten
                            spiller.våpen.påførGiftSkade(monster)  # Påfør giftskade i etterfølgende runder

                    elif isinstance(spiller.våpen, LangSverd): # Hvis spilleren har valgt lang sverd
                        if spiller.våpen.Antallslag > 0: # Hvis spilleren har flere slag igjen
                            spiller.våpen.slag(monster) # Slå monsteret
                        else: # Hvis spilleren ikke har flere slag igjen
                            s(f'Du kan ikke bruke {spiller.våpen.navn} lenger. Antall slag er brukt opp.') # Skriv ut at spilleren ikke kan bruke lang sverd lenger


                    elif isinstance(spiller.våpen, Hagle): # Hvis spilleren har valgt hagle
                        spiller.våpen.skyt([monster])  # Endre til en liste med monstre hvis det er flere

                    else: # Hvis spilleren har valgt et annet våpen
                        spiller.angrep(monster) # Angrip monsteret

                    # Monsteret angriper hvis det fortsatt er i live
                    if monster.helse > 0: # Hvis monsteret fortsatt har helse igjen
                        if isinstance(monster, Drage): # Hvis monsteret er en drage
                            monster.bruk_ild_pust(spiller) # Bruk ildpusten til dragen
                        elif isinstance(monster, Vampyr): # Hvis monsteret er en vampyr
                            monster.angrep(spiller) # Angrip spilleren med tikkskade
                        else: # Hvis monsteret er et annet monster
                            monster.angrep(spiller) # Angrip spilleren
                else: # Hvis spilleren ikke har valgt et våpen
                    s("Du har ikke valgt et våpen!") # Skriv ut at spilleren ikke har valgt et våpen

            
            elif valg == "4": # Hvis valget er 4
                print(spiller) # Skriv ut spilleren
                print(monster) # Skriv ut monsteret
            
            else: # Hvis valget er ugyldig
                print("Ugyldig valg.") # Skriv ut at valget er ugyldig
        
        if monster.helse <= 0: # Hvis monsteret har mistet all helse
            print(f"Du har beseiret {monster.navn}!") # Skriv ut at spilleren har beseiret monsteret
    
    if spiller.helse <= 0: # Hvis spilleren har mistet all helse
        print("Spillet er over. Du tapte!") # Skriv ut at spilleren har tapt
    else: # Hvis spilleren har beseiret alle monstrene
        print("Gratulerer! Du har beseiret alle monstrene!") # Skriv ut at spilleren har beseiret alle monstrene

if __name__ == "__main__": # Hvis filen kjøres som et script
    main() # Kjør main-funksjonen

# Spill_bibliotek.py
import time

# Grunnklasse for monstre
class Monster:
    """
    Grunnklasse for monstre. Inneholder navn, helse, og skade. 
    Samt funksjoner som returnerer informasjon om monsteret,
    angriper spiller, sjekker om monster lever, eller viser hvor mye helse monsteret har.
    """
    def __init__(self, navn:str, helse:int, skade:int=30):
        """
        Konstruktør
        """
        self.navn = navn
        self._helse = helse  # Bruker et privat attributt for helse
        self.skade = skade
        self.forgiftet = False #Brukes for giftkniv-våpen
        self.giftSkade = 0
        self.giftVarighet = 0
    
    def håndterGift(self):
        """
        Metode for håndtering av giftskade
        """
        if self.forgiftet and self.giftVarighet > 0: #Sjekker om monsteret er forgiftet og om giftvarigheten er over 0
            self.helse -= self.giftSkade #Reduserer helsen
            self.giftVarighet -= 1 #Reduserer varigheten
            print(f"Giften skader {self.navn} med {self.gift_skade}. Helse nå: {self.helse}.") 
        if self.giftVarighet <= 0: #Sjekker om giftvarigheten er over 0
            self.forgiftet = False #Fjerner forgiftet-statusen
            print(f'Giften på {self.navn} har sluttet å virke.') #Skriver ut at giften har sluttet å virke


    @property #Bruker property for å kunne bruke getter og setter for helse
    def helse(self): #Getter for helse
        """Getter for helse-attributt. 
        Returnerer den nåværende helsen til objektet
        """
        return self._helse #Returnerer helsen til objektet


    @helse.setter #Setter for helse
    def helse(self, ny_helse:int): #Setter for helse
        """Setter for helse-attributt. Sørger for at helsen ikke blir negativ.
        Kaller til død-metode om helsen blir 0 
        """
        self._helse = max(0, ny_helse)  # Sørger for at helse aldri er negativ
        if self._helse == 0: #Sjekker om helsen er 0
            self.død() #Kaller død


    def død(self): 
        """
        Metode dersom et monster-objekt dør, skriver ut passende melding
        """
        print(f'{self.navn} er død.')


    def __str__(self):
        """
        Metode for å skrive ut standardinfo om monster-objekt. Funker som visInfo
        """
        return f"{self.navn} med helse {self._helse} og skade {self.skade}"


    def angrep(self, spiller:str):
        """
        Metode for angrep. Som standard reduserer den helsen til spiller og skriver ut passende melding
        """
        spiller.helse -= self.skade
        print(f"{self.navn} angriper spilleren og reduserer helsen til {spiller.helse}")
  

    def sjekkHelse(self):
        """
        Metode for å sjekke helsen til monster-objekt.
        Return: Melding basert på objekt sin levestatus
        """
        if self.helse <= 0:
            print(f'{self.navn} er død.')
        else:
            print(f'{self.navn} har {self.helse} helse.')

# Avansert monster: Troll
class Troll(Monster):
    """
    Første monster, troll. Kan regenerere helse, 5 av gangen. 
    """
    def __init__(self, navn:str, helse:int, skade:int):
        """
        Konstruktør
        """
        super().__init__(navn, helse, skade)
        self.helseRegenerering = 5  #Troll kan regenerere helse

    def regenerer(self):
        """
        Metode for regenerering av liv. Regenererer 5 hver runde objektet er i livet.
        """
        if self.helse > 0:
            self.helse += self.helseRegenerering
            print(f"{self.navn} regenererer {self.helseRegenerering} helse. Ny helse: {self.helse}")

# Avansert monster: Drage
class Drage(Monster):
    """
    Andre monster, drage. Kan puste ild, noe som forårsaker 1.5x skade på spilleren.
    """
    def __init__(self, navn:str, helse:int, skade:int):
        """
        Konstruktør
        """
        super().__init__(navn, helse, skade)
        self.ild_pust = skade * 1.5 #Drage kan puste ild og det tar 1.5x skade

    def bruk_ild_pust(self, spiller:str):
        """
        Metode for ildpust. Return: Reduserer spillers helse og skriver ut passende melding
        """
        spiller.helse -= self.ild_pust
        print(f"{self.navn} bruker ildpust på spilleren og reduserer helsen til {spiller.helse}")

class Vampyr(Monster):
    """
    Tredje monster, vampyr. Gjør tikkskade på spilleren, for en viss skade og durasjon.
    """
    def __init__(self, navn:str, helse:int, skade:int, livstapp_skade:int=5, livstapp_varighet:int=3):
        """
        Konstruktør
        """
        super().__init__(navn, helse, skade)
        self.livstapp_skade = livstapp_skade
        self.livstapp_varighet = livstapp_varighet

    def angrep(self, spiller:str):
        """
        Metode for angrep som forårsaker livstapping av spiller. Return: Passende melding og aktiverer livstapping
        """
        super().angrep(spiller)
        print(f"{self.navn} aktiverer livstapping på {spiller.navn}!")
        self.livstapp(spiller)

    def livstapp(self, spiller:str):
        """
        Metode for livstapping. Return: Reduserer spillers helse for antall tikk bestemt. Skriver ut passende melding
        """
        for tikk in range(1, self.livstapp_varighet + 1):
            spiller.helse -= self.livstapp_skade
            print(f"Livstapping {tikk}/{self.livstapp_varighet}: {spiller.navn} mister {self.livstapp_skade} helse. Helse nå: {spiller.helse}.")

# Spilleren
class Spiller:
    """
    Spiller klassen. Inneholder navn, helse, våpen, og en ryggsekk.
    Har en funksjon som viser navn og helse, en som angriper monster, en som lar deg bruke items, og en for å sjekke helse
    """
    def __init__(self, navn:str, helse:int=100):
        """
        Konstruktør
        """
        self.navn = navn
        self.helse = helse
        self.våpen = None
        self.ryggsekk = []

    @property #Bruker property for å kunne bruke getter og setter for helse
    def helse(self): #Getter for helse
        """Getter for helse-attributt. 
        Returnerer den nåværende helsen til objektet
        """
        return self._helse #Returnerer helsen til objektet
    
    @helse.setter #Setter for helse
    def helse(self, nyHelse:int): #Setter for helse
        """Setter for helse-attributt. Sørger for at helsen ikke blir negativ.
        Kaller til død-metode om helsen blir 0 
        """
        self._helse = nyHelse # Sørger for at helse aldri er negativ
        if self._helse <= 0: #Sjekker om helsen er 0 eller mindre
            self._helse = 0 #Setter helsen til 0
            self.død()  #Kaller død

    def død(self):
        """
        Metode dersom et monster-objekt dør, skriver ut passende melding
        """
        print(f'{self.navn} er død. Game over!')
        exit()

    def __str__(self):
        """
        Metode for å skrive ut standardinformasjon om spiller
        """
        return f"Spiller {self.navn} med helse {self.helse}."

    def angrep(self, monster:str):
        """
        Metode for angrep av monster-objekt. Baserer seg på hvilket våpen som er valgt. Return: reduserer liv til monster og passende melding
        """
        skade = self.våpen.skade if self.våpen else 10
        monster.helse -= skade
        print(f"{self.navn} angriper {monster.navn} og påfører {skade} skade. {monster.navn} har nå {monster.helse} helse.")

    def bruk_item(self, item:str):
        """
        Metode for bruk av items. Baserer seg på om du har ønsket metode i ryggsekk. Return: Bruk, fjern eller print passende melding
        """
        if item in self.ryggsekk:
            item.bruk(self)
            self.ryggsekk.remove(item)
        else:
            print(f"Du har ikke {item.navn} i ryggsekken.")

    def sjekkHelse(self):
        """Metode for å sjekke helse til spiller. Return: Passende melding
        """
        if self.helse <= 0:
            print(f'{self.navn} er død, spillet er over.')
        return self.helse <= 0

# Våpen
class Våpen:
    """
    Standardklasse for våpen. Beskriver navn og hvor mye skade den gjør
    """
    def __init__(self, navn:str, skade:int):
        """
        Konstruktør
        """
        self.navn = navn
        self.skade = skade
        self.skadegrense = 20

    def __str__(self):
        """
        Viser standardinfo om våpen
        """
        if self.navn =="GiftKniv":
            return f'Våpen: {self.navn} med skade {self.skade} og videre tikkskade på {self.giftSkade} i {self.giftVarighet} tikk' 
        elif self.navn == "LangSverd":
            return f'Våpen: {self.navn} med skade {self.skade} og {self.Antallslag} slag igjen'
        else:
            return f"Våpen: {self.navn} med skade {self.skade} og evig skudd"

class Pistol(Våpen):
    def __init__(self, navn:str, skade:int=30):
        """
        Konstruktør
        """
        super().__init__(navn, skade)

    def skyt(self, monster:str):
        """Metode for angrep mot monster. Return: Reduserer monster sin helse og skriver passende melding
        """
        monster.helse -= self.skade
        print(f'{monster.navn} sin helse har blitt redusert til {monster.helse}')

    
class GiftKniv(Våpen):
    def __init__(self, navn:str, skade:int=20, giftSkade:int=10, giftVarighet:int=3):
        """
        Konstruktør
        """
        super().__init__(navn, skade)
        self.giftSkade = giftSkade
        self.giftVarighet = giftVarighet
        self.opprinneligGiftVarighet = giftVarighet

    def førsteStikk(self, monster:str):
        """¨
        Metode for første stikk. Gjør skade, skriver ut passende melding, og starter giftskade-funksjon.
        """
        monster.helse -= self.skade
        print(f'{self.navn} gjør {self.skade} skade på {monster.navn}. Helse nå: {monster.helse}.')
        return self.giftVarighet
    
    def påførGiftSkade(self, monster:str):
        """Metode for påføring av giftskade"""
        if self.giftVarighet > 0: #Sjekker om giftvarigheten er over 0
            monster.helse -= self.giftSkade #Reduserer helsen til monster
            self.giftVarighet -= 1 #Reduserer varigheten
            print(f'Giften påfører {self.giftSkade} skade på {monster.navn}. Helse nå: {monster.helse}.') #Skriver ut at giften påfører skade
            monster.forgiftet = True 
            monster.giftSkade = self.giftSkade #Setter giftskaden til monsteret
            monster.giftVarighet = self.giftVarighet #Setter giftvarigheten til monsteret

    def tilbakestill(self):
        self.giftVarighet = self.opprinneligGiftVarighet

giftkniv = GiftKniv('Giftkniv', 20, 10, 5)


class LangSverd(Våpen):
    def __init__(self, navn:str, skade:int, Antallslag:int=2):
        """
        Konstruktør
        """
        super().__init__(navn, skade)
        self.Antallslag = Antallslag

    def slag(self, monster:str):
        """
        Metode for angrep mot monster. Return: Reduserer liv til monster-objekt. Printer ut passende melding
        """

        if self.Antallslag > 0:
            monster.helse -= self.skade
            self.Antallslag -= 1
            print (f'{self.navn} gjør {self.skade} skade på {monster.navn}. {monster.navn} har nå {monster.helse} helse.')
            print(f'{self.navn} har {self.Antallslag} igjen.')
        else:
            print (f'{self.navn} kan ikke brukes mer. Du har ingen slag igjen')

class Hagle(Våpen):
    def __init__(self, navn:str, skade:int=50):
        """
        Konstruktør
        """
        super().__init__(navn, skade)

    def skyt(self, monstre:str):
        """
        Metode for angrep av monster. Return: Skader alle monster-objekt og skriver passende melding
        """
        for monster in monstre:
            monster.helse -= self.skade
            print(f'{self.navn} gjør {self.skade} skade på {monster.navn}. {monster.navn} har nå {monster.helse} helse.')
        

# Helsegjenstander
class HelseGjenstand:
    """
    Standardklasse for helsegjenstander. 
    """
    def __init__(self, navn:str, helbredelse:int):
        """
        Konstruktør
        """
        self.navn = navn
        self.helbredelse = helbredelse

    def bruk(self, spiller:str):
        """
        Metode for bruk av helsegjenstander. Return: Øker helse til spiller og skriver ut passende melding
        """
        spiller.helse += self.helbredelse
        print(f"{spiller.navn} bruker {self.navn} og gjenoppretter {self.helbredelse} helse. Ny helse: {spiller.helse}")

class Medkit(HelseGjenstand):
    def __init__(self, navn:str, helbredelse:int):
        """
        Konstruktør
        """
        super().__init__(navn, helbredelse=None) #Setter til 100 uansett, så helbredelse er unødvendig

    def bruk(self, spiller:str):
        """
        Metode for bruk av medkit. Return: Øker spillers helse til 100, med mindre helse allerede er 100
        """
        if spiller.helse >= 100:
            print(f'Helsen er allerede {spiller.helse}, {self.navn} ble ikke brukt.')
        else:
            spiller.helse = 100
            print(f'{spiller.navn} bruker {self.navn}. Helsen er nå {spiller.helse}.')
    
class Bandasje(HelseGjenstand):
    def __init__(self, navn:str, helbredelse:int=15):
        """
        Konstruktør
        """
        super().__init__(navn, helbredelse)
    
    def bruk(self, spiller:str):
        """Metode for bruk av bandasje. Return: Øker helse med 15, med mindre helse allerede er 75. Setter til 75 dersom helse etter bandasje overgår dette"""
        if spiller.helse >= 75:
            print(f'Helsen er allerede {spiller.helse}, {self.navn} ble ikke brukt.')
        else: 
            spiller.helse += self.helbredelse
            if spiller.helse > 75:
                spiller.helse = 75
            print(f'{spiller.navn} bruker {self.navn}. Helsen er nå {spiller.helse}')

def skriv_ut_tekst(tekst:str, forsinkelse=0.025): #Funksjon for å skrive ut tekst med forsinkelse
        for bokstav in tekst: #Går gjennom bokstavene i teksten
            print(bokstav, end="", flush=True) #Skriver ut bokstaven
            time.sleep(forsinkelse) #Venter litt før neste bokstav
        print() 

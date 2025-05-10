import pygame as pg #Pygame
import random as r #Random
import math as m #matte

#farger

HVIT = (255, 255, 255)
SVART = (0, 0, 0)
ROD = (255, 0, 0)
GUL = (255, 255, 0)
GRONN = (0, 255, 0)
BLA = (0, 0, 255)
GRAA = (150, 150, 150)

VINDU_BREDDE, VINDU_HOYDE = 200, 400 

class Plass:
    '''
    Konstruktø
    x : int  ; x posisjon
    y : int ; yposijon
    bordplass : bool
    gulvplass  : bool
    laerer_paa_plass : bool ; ulike tilstander
    kunnskap : int ; start_verdi
    kunnskaps_farger : list ; ulike farge tilstander
    '''
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.bordplass = False
        self.gulvplass = True
        self.laerer_paa_plass = False
        self.drivkraft = r.randint(1,33) * 3
        self.kunnskap = 0.1
        self.kunnskaps_farger = ["white", "yellow", "orange", "green", "blue", "purple", "brown"]

    def tegn(self, vindu, lengde):
        """
        Metode for å tegne plassene
        """
        if self.gulvplass:
            pg.draw.rect(vindu,"lightyellow", (self.x, self.y, lengde, lengde))
            pg.draw.rect(vindu, "black", (self.x, self.y, lengde, lengde), 1)
        if self.bordplass:
            pg.draw.rect(vindu, f'gray{self.drivkraft}', (self.x, self.y, lengde, lengde))
            pg.draw.rect(vindu, "black", (self.x, self.y, lengde, lengde), 1)
            pg.draw.circle(vindu, self.kunnskaps_farger[m.floor(self.kunnskap)], ((self.x+lengde/2), (self.y +lengde/2)), lengde/3)
        if self.laerer_paa_plass:
            pg.draw.rect(vindu, "lightyellow", (self.x, self.y, lengde, lengde))
            pg.draw.circle(vindu, "brown", ((self.x+lengde/2), (self.y + lengde/2)), lengde/3)
            pg.draw.rect(vindu, "black", (self.x, self.y, lengde, lengde), 1)

class Klasserom:
    """
    Konstruktør
    vindu: surface ; vinduet som det skal tegnes i
    kolonner : int ; antallet kolonner
    rader : int ; antallet rader
    lengde : int ; lengden til til hver side til hver rute
    rom : list ; lager rutebrettet for rommet
    """
    def __init__(self, vindu: pg.surface):
        self.vindu = vindu
        self.kolonner = 8
        self.rader = 16
        self.lengde = VINDU_BREDDE//self.kolonner
        self.rom = [[Plass(i * self.lengde, j* self.lengde) for j in range(self.rader)] for i in range(self.kolonner)]

    def start(self):
        """
        Metode for å lage start brettet
        """
        for i in range(self.rader):
            for j in range(self.kolonner):
                if i == 0 and j == 0:
                    self.rom[j][i].laerer_paa_plass = True
                if i in [1, 2, 5,6, 9, 10 , 13, 14] and j in [1,2 ,5, 6]:
                    self.rom[j][i].bordplass = True

    def tegn_klasserom(self):
        """Metode for å tegne klasserommet
        """
        lengde = self.lengde
        for i in range(self.rader):
            for j in range(self.kolonner):
                self.rom[j][i].tegn(self.vindu, lengde)


    def laerer_naer(self):
        """
        Metode for å sjekke om læreren er nær
        """
        for i in range(self.rader):
            for j in range(self.kolonner):
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x != 0 and y != 0: 
                            continue
                        if (i+x >= 0 and i+x < self.rader) and (j+y >= 0 and j+y < self.kolonner):
                            if self.rom[j+y][i+x].laerer_paa_plass and self.rom[j][i].bordplass== True:
                                self.rom[j][i].kunnskap += 0.3


    def flytt_laerer(self):
        """
        Metode for å flytte læreren
        """
        for i in range(self.rader):
                    for j in range(self.kolonner):
                        if self.rom[j][i].laerer_paa_plass:
                            self.rom[j][i].laerer_paa_plass = False
        x = [0,3,4,7]
        y= [0,3,4,7,8,11,12,15]
        x_en =r.choice(x)
        y_en = r.choice(y)
        self.rom[x_en][y_en].laerer_paa_plass = True

    def oppdater_kunnskap(self):
        """
        Metode for å oppdatere kunnskapsnivået til elevene
        """
        for i in range(self.rader):
            for j in range(self.kolonner):
                plass = self.rom[j][i]
                if plass.bordplass: 
                    if r.randint(1, 100) <= plass.drivkraft: 
                        firerbord = []
                        for x in [-1, 0, 1]:
                            for y in [-1, 0, 1]:
                                if abs(x) + abs(y) == 1:  
                                    nabo_x, nabo_y = j + x, i + y
                                    if 0 <= nabo_x < self.kolonner and 0 <= nabo_y < self.rader:
                                        nabo_plass = self.rom[nabo_x][nabo_y]
                                        if nabo_plass.bordplass:
                                            firerbord.append(nabo_plass.kunnskap)
                        
                        if firerbord:
                            gjennomsnitt_kunnskap = sum(firerbord) / len(firerbord)
                        else:
                            gjennomsnitt_kunnskap = 0
                        
                        kunnskapsokning = 0.05 * gjennomsnitt_kunnskap + 0.2
                        plass.kunnskap = min(plass.kunnskap + kunnskapsokning, 6.99)  
    def avsluttspill(self):
        """
        Metode for å avslutte spillet
        """
        for i in range(self.rader):
            for j in range(self.kolonner):
                plass = self.rom[j][i]
                if plass.laerer_paa_plass:
                    plass.laerer_paa_plass = False  
                    pg.draw.circle(self.vindu, "white", ((plass.x + self.lengde / 2), (plass.y + self.lengde / 2)), self.lengde / 3)

        total_kunnskap = 0
        antall_elever = 0
        for i in range(self.rader):
            for j in range(self.kolonner):
                plass = self.rom[j][i]
                if plass.bordplass:
                    total_kunnskap += plass.kunnskap
                    antall_elever += 1

        gjennomsnitt_kunnskap = total_kunnskap / antall_elever if antall_elever > 0 else 0

        font = pg.font.SysFont("Arial", 14)
        tekst = font.render(f"Gj.snitt kunnskap: {gjennomsnitt_kunnskap:.2f}", True, SVART)
        tekst_rect = tekst.get_rect(center=(VINDU_BREDDE // 2, VINDU_HOYDE - 10))
        self.vindu.blit(tekst, tekst_rect)
        


vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))

klasserommet = Klasserom(vindu) # Lager objektet
klasserommet.start() # Lager brettet

fortsett = True

tallet = 0

pg.init()
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    if tallet <= 70*90:
        klasserommet.tegn_klasserom() # Tegner klasserommet

    if tallet % 70 == 0 and tallet != 0 and tallet < 70*90: # Gjør sånn at simuleringen skjer med en delay
        klasserommet.flytt_laerer()
        klasserommet.laerer_naer()
        klasserommet.oppdater_kunnskap()

    if tallet == 70*95: # Kjører 90 simuleringer
        fortsett = False
    
    if tallet >= 70*90 and tallet < 70*95: # Kjører avsluttssimuleringen
        klasserommet.avsluttspill()
        
    tallet += 1

    pg.display.flip()

pg.quit()

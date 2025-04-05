"""
Eksempeloppgave:
Eksamen høsten 2024, oppgave 6 (oppgaven er noe endret)


Det skal lages en applikasjon for et energistystem med en klasse som beskriver et batteri. 
Batteri-objektene vil trenge en ID for identifikasjon. 
Store og små batterier vil ha forskjellig energikapasitet, altså en angivelse av hvor mye energi de kan lades med. 
Denne klassen skal gjøre det mulig å håndtere lading av et batteri (øke energinivået) og bruk av energi fra batteriet (senke energinivået), samt å vise hvor mye energi som er igjen i batteriet. 
Egenskapene skal ha tilgangsnivå privat (-), mens metodene skal ha tilgangsnivå public (+)


	a) Lag et UML-diagram basert på problemstillingen over.
	b) Implementer klassen i en python-fil
	c) Lag et eget testprogram for klassefilen, hvor du oppretter objekter og tester at metodene virker uten syntaxfeil
	d) Identifiser to mulige feil og ett unntak (exception) som programmene må ta høyde for
		a. Lag en testspesifikasjon for disse tre
		b. Identifiser problematiske kombinasjoner av input, og hva som er ønsket output
		c. Oppdater testprogrammet for å demonstrere disse logiske feil og/eller kjøretidsfeil
Implementer nødvendig håndtering av feilene og unntaket du identifiserte i punkt d)
"""



class Batteri:
    def __init__(self, ID: str, kapasitet: str, nivå: int):
        self._ID = ID
        self._kapasitet = kapasitet #Høy, middels, lav
        self._nivå = nivå #Energinivå målt i prosent
    
        if self._nivå < 0:
            print("Prosenten kan ikke være under null")
        else:
            continue


    def lading(self):
        if self._nivå < 100:
            deltanivå = 100 - self._nivå
            if self._kapasitet == "høy":
                strøm = 3*deltanivå
            elif self._kapasitet == "middel":
                strøm = 2*deltanivå
            elif self._kapasitet == "lav":
                strøm = deltanivå
            else:
                print("Ugyldig kapasitet. Vennligst bruk 'høy', 'middel' eller 'lav'.")
                return
            self._nivå = 100
            print(f'Strømmen brukt er {strøm} og nå er batterinivået på {self._nivå}%')
        else:
            print("Batteriet er allerede fulladet")

    def bruk_energi(self, mengde):
        if self._nivå >= mengde:
            self._nivå -= mengde
            print(f'Det ble brukt {mengde} energi og batteriet er nå på {self._nivå}%')
        else:
            print("Ikke nok strøm i batteriet")

    def visinfo(self):
        print(self._ID, self._kapasitet, self._nivå)



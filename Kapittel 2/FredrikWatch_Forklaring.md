##**Hvilke bibloteker som må importeres**
####**Biblotek**
For å bruke Spill-Bibloteket trenger man å importere _time_-bibloteket som _import time_
####**Spill**
For å bruke spillet må du først importere spill-bibloteket _FredrikWatchBiblotek_ som _from FredrikWatchBiblotek import *_. Du må i tillegg importere funksjonen __Skriv_ut_tekst__ som __from FredrikWatchBiblotek import skriv_ut_tekst as s__. 

##**Forklare spillets funksjoner**
I spillet spiller hovedkarakteren mot monstre, en av gangen. Det er tre forskjellige monstre, med forskjellige egenskaper. I tillegg har karakteren flere muligheter også. 

###Monstrene
Det er tre forskjellige monstre:
####Troll
Troll kan regenerere helse, 5 av gangen
####Drage
Dragen har høy skade, og har i tillegg _ildpust_ som multipliserer skaden med 1.5
####Vampyr
Vampyren biter og tar deretter tikkskade på spilleren

###Spilleren
Spilleren har 4 muligheter:
####Velg våpen
Lar spilleren velge mellom 4 forskjellige våpen, våpnene er forklart i spillet
####Bruk helsegjenstand
Lar spilleren velge mellom helsegjenstandene i ryggsekken sin. Medkit fyller opp til 100 liv og bandasje øker helse med 15, til og med 75. 
####Angrip monsteret
Angriper monsteret med våpenet som er valgt. Deretter angriper monsteret tilbake
####Sjekk helse
Sjekker helsen til spiller og monster, samt hvor mye skade monsteret tar

##**Spillet i praksis**
Spillet er ganske rett fram. Skriv først inn navnet ditt. Velg våpenet du mener er mest hensiktsmessig å bruke mot monsteret, du kan bytte våpen når som helst. Angrip deretter monstrene og hver gang du vinner mot et monster, så vil du møte ett nytt ett. Dersom helsen din eller helsen til monstrene går under 0, så dør du/de. Du kan bruke helsegjenstander for å holde helsen din over 0. Dersom du er usikker på helsen din eller helsen til monsteret, så kan du bruke _sjekk helse_

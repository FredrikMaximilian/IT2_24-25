import pandas as pd
"""
###Sjekke versjon
print(pd.__version__)
"""

###Lage en simpel Pandas Series fra en liste #Serie er som en rad, Dataframe er hele periodesystemet
#Med mindre annet spesifisert, er de labeled etter indexnummer
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0]) #Kan retunere biter i koden

myvar = pd.Series(a, index = ["x", "y", "z"]) #Kan lage egne labels
print(myvar)
print(myvar["y"]) #Retunerer items med nylaget label  


###Ordbok, nøkkel/verdier for å lage Series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar) #Nøkler i ordbok blir labels

spesifisert = pd.Series(calories, index = ["day1", "day2"]) #Kan bruke index til å spesifisere ønskede items
print(spesifisert) #Printer kun spesifisert


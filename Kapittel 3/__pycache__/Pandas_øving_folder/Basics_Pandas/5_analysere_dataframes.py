import pandas as pd
df = pd.read_csv('å_csv.csv')

#Bruk head() for å printe overskrift og første x rader
print(df.head(10)) #Uspesifisert returnerer 5

#Bruk tail() for å returnere x nedereste og headers
print(df.tail(10))

#Print informasjon om datasettet
print(df.info())
#Printer antall rows(169) og antall søyler(4)
#Deretter navnet på hver + antall non-null + datatypen


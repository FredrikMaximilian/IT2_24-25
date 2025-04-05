#Cleaning data = Fikse dårlig data som: Tomme celler, data i feil format, feil data, duplikater
import pandas as pd
df = pd.read_csv('å_data.csv')

#Bruke dropna() for å fjerne rader med tomme celler
"""
ny_df = df.dropna() #Lager en ny dataframe
print(ny_df)
"""

#Bruke dropna(inplace = True) for å endre originalen i minnet. Endrer ikke den faktiske filen
"""
df.dropna(inplace = True)
print(df.to_string())
"""

#Bruk fillna for å fylle tomme celler, skjer da på alle
"""
df.fillna(130, inplace = True)
"""

#Definer hvilken søyle som skal fylles inn
"""
df["Calories"].fillna(130, inplace = True)
"""
"""
#Bruk mean() for å legge inn gjennomsnitt
gjennomsnitt = df["Calories"].mean()
df["Calories"].fillna(gjennomsnitt, inplace = True)
"""

#Bruk median() for å legge inn median
"""
media = df["Calories"].median()
df["Calories"].fillna(media, inplace = True)
"""

#bruk mode() for å legge inn typetall
"""
typetall = df["Calories"].mode()[0] #Første tall som er typetall, i tilfelle flere
df["Calories"].fillna(typetall, inplace = True)
print(df)
"""


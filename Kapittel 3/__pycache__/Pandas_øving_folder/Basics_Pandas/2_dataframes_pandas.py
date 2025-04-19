#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
import pandas as pd

#Printe dataframe og returnere med LOC

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df) #Skriver ut hele datasettet

print(df.loc[0]) #Returnerer med en spesifikk row
print(df.loc[[0, 1]]) #Kan returnere flere


#Endre index på dataframe + returnering

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["dag1", "dag2", "dag3"]) #Endrer på indeksnavnet 
print(df)
print(df.loc["dag2"]) #Bruk loc for å returnere 


#Henter csv fil og fikser den

df = pd.read_csv('eksempel.csv') 
print(df)
print(df.loc[0])


#Returner header, og rows for 3 første
df = pd.read_csv('eksempel.csv')
print(df)
print()
print(df.head(3)) #Standard uten innskriving er 5 rows
import pandas as pd

#Bruk to_string() for å returnere hele settet. Uten = 5 oppe og 5 nede

df = pd.read_csv('å_csv.csv')
print(df.to_string())


#Sjekk maksimalverdier, endre verdier innad i systemet
"""
print(pd.options.display.max_rows) #Default 60

pd.options.display.max_rows = 9999 #Endrer
df = pd.read_csv('å_csv.csv')
print(df)
"""
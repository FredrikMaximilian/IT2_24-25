import pandas as pd
df = pd.read_csv('å_data.csv')

#True for hver linje som er duplikat
print(df.duplicated())

#Fjern duplikat 
df.drop_duplicates(inplace = True)
print(df)

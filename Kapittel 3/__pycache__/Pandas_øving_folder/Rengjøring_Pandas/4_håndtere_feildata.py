import pandas as pd
df = pd.read_csv('å_data.csv')

#replace verdi en etter en
"""
df.loc[7, 'Duration'] = 45
"""

#Løkke som bytter ut feildata
"""
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120
print(df)
"""

#Løkke som fjerner rows med feildata

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace = True)
print(df)
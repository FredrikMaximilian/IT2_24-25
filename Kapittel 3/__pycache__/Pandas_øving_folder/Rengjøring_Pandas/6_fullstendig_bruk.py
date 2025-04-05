import pandas as pd

dt = pd.read_csv('å_data.csv')

gjennomsnitt = dt['Calories'].mean()
dt['Calories'].fillna(gjennomsnitt, inplace = True)


dt['Date'] = pd.to_datetime(dt['Date'], format = 'mixed')
dt.dropna(subset = ['Date'], inplace=True)

typetall = dt['Duration'].mode()[0]

for x in dt.index:
    if dt.loc[x, 'Duration'] > 120:
        dt.loc[x, 'Duration'] = typetall

dt.drop_duplicates(inplace = True)
print(dt.to_string())
import pandas as pd
dt = pd.read_csv('å_data.csv')

#Konvertere til datolesing
dt['Date'] = pd.to_datetime(dt['Date'], format = 'mixed')

#Fjerne NaT verdier 
dt.dropna(subset = ['Date'], inplace=True)
print(dt.to_string())


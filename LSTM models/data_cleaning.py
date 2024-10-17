import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\AI-in-forex-trading\Datasets\30min\Aug and Sep 30min dataset.csv', sep=',', header=None)
df.columns = ['date', 'open', 'high', 'low', 'close']
df['date']= pd.to_datetime(df['date'])
df['date_only']= df['date'].dt.date
df['time_only']= df['date'].dt.time
df.drop('date', axis=1, inplace=True)
df.rename(columns={'date_only': 'date', 'time_only': 'time'}, inplace=True)
print(df.head())
print(df.tail())
print(df.info())

df['date'] = df['date'].apply(lambda x: x.toordinal())
df['time'] = df['time'].apply(lambda x: x.hour + x.minute/60)
print(df)
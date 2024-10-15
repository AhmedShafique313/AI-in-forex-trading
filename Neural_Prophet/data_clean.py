import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\AI-in-forex-trading\Datasets\daily\oct2023 to sep2024 daily.csv', sep=',', header=None)
df.columns = ['date', 'open', 'high', 'low', 'close']
df['date']= pd.to_datetime(df['date'])
print(df.info())
print(df)
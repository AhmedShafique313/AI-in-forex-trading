import pandas as pd
df = pd.read_csv(r'C:\Users\haiqa\OneDrive\Documents\Projects with Ahmed\Forex trading Project\AI-Forext-Trading-Project\Datasets\30min\September 2024 30min dataset.csv', sep=',', header=None)
df.columns = ['date', 'open', 'high', 'low', 'close']
print(df)

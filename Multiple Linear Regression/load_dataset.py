import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\Personal\Documents\AI Forex trading project and training\Multiple Linear Regression\EURUSDM1.csv'
dataset = pd.read_csv(file_path)

plt.figure(figsize=(12,6))
plt.plot(dataset.index, dataset['open'], label='open', color='blue', marker='o')
plt.plot(dataset.index, dataset['high'], marker='o', label='high', color='green')
plt.plot(dataset.index, dataset['low'], label='low', color='red', marker='o')
plt.plot(dataset.index, dataset['close'], label='clsoe', color='black', marker='o')
plt.grid(True)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Forex Trading Data')
plt.show()
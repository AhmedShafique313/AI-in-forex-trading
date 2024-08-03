import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\Personal\Documents\AI Forex trading project and training\Multiple Linear Regression\EURUSDM1.csv'
dataset = pd.read_csv(file_path)

print(dataset.head())
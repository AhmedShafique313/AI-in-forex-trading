from data_clean import *
import matplotlib.pyplot as plt

df = df[['date', 'close']]
df.columns = ['ds', 'y']
plt.plot(df['ds'], df['y'], label= 'actual', color = 'g')
plt.show()
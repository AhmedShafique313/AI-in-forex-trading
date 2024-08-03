from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from load_dataset import dataset
import matplotlib.pyplot as plt

x1 = dataset[['open', 'high']]
y = dataset['close']

x1_train, x1_temp, y_train, y_temp = train_test_split(x1,y, random_state=42, test_size=0.3)
x1_test, x1_val, y_test, y_val = train_test_split(x1_temp, y_temp, random_state=42, test_size=0.3)

print(f'Training set size: {x1_train.shape[0]} samples')
print(f'Testing set size: {x1_test.shape[0]} samples')
print(f'Validation set size: {x1_val.shape[0]} samples')

model1 = LinearRegression()
model1.fit(x1_train, y_train)

test_pred1 = model1.predict(x1_test)


plt.scatter(dataset.index, dataset['open'], label='open', color='blue')
plt.scatter(dataset.index, dataset['high'], label='high', color='green')
plt.plot(y_test, test_pred1, color='brown', label='Line2')
plt.grid(True)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Forex trading data')
plt.show()

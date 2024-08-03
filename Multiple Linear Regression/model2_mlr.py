from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from load_dataset import dataset
import matplotlib.pyplot as plt
from model_mlr import y_train, test_pred1, y

x2 = dataset[['open', 'high', 'low']]
x2_train, x2_temp, y_train, y_temp = train_test_split(x2,y, random_state=42, test_size=0.3)
x2_test, x2_val, y_test, y_val = train_test_split(x2_temp, y_temp, random_state=42, test_size=0.3)

model2 = LinearRegression()
model2.fit(x2_train, y_train)
test_pred2 = model2.predict(x2_test)

plt.scatter(dataset.index, dataset['open'], label='open', color='blue')
plt.scatter(dataset.index, dataset['high'], label='high', color='green')
plt.plot(y_test, test_pred1, color='brown', label='Line1')
plt.plot(y_test, test_pred2, color='pink', label='Line2')
plt.grid(True)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Forex trading data')
plt.show()
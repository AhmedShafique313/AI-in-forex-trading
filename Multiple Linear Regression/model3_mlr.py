from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from load_dataset import dataset
import matplotlib.pyplot as plt
from model_mlr import y_train, test_pred1, y
from model2_mlr import test_pred2

x3 = dataset[['open', 'high', 'low', 'volume']]
x3_train, x3_temp, y_train, y_temp = train_test_split(x3,y, random_state=42, test_size=0.3)
x3_test, x3_val, y_test, y_val = train_test_split(x3_temp, y_temp, random_state=42, test_size=0.3)

model2 = LinearRegression()
model2.fit(x3_train, y_train)
test_pred3 = model2.predict(x3_test)

plt.scatter(dataset.index, dataset['open'], label='open', color='blue')
plt.scatter(dataset.index, dataset['high'], label='high', color='green')
plt.plot(y_test, test_pred1, color='brown', label='Line1')
plt.plot(y_test, test_pred2, color='pink', label='Line2')
plt.plot(y_test, test_pred3, color='pink', label='Line2')
plt.grid(True)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Forex trading data')
plt.show()
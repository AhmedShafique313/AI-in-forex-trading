import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

file_path = r'C:\Users\Personal\Documents\AI Forex trading project and training\Multiple Linear Regression\EURUSDM1.csv'
dataset = pd.read_csv(file_path)
x = dataset[['open', 'high', 'low', 'volume']]
y = dataset[['close']]
x_train, x_temp, y_train, y_temp =train_test_split(x, y, test_size=0.3, random_state=42)
x_test, x_val, y_test, y_val = train_test_split(x_temp, y_temp, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)
test_predictions = model.predict(x_test)
print('Coefficient: ', model.coef_)
print('Intercept: ', model.intercept_)
test_score = model.score(x_test, y_test)
print('Test set score: ', test_score)

val_predictions = model.predict(x_val)
val_score = model.score(x_val, y_val)
print('Validation Set Score:', val_score)

plt.figure(figsize=(12, 6))
plt.scatter(y_test, test_predictions, label='Test set', alpha=0.5, color='blue')
plt.scatter(y_val, val_predictions, label='Validation set', alpha=0.5, color='red')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('Actual Close Prices')
plt.ylabel('Predicted Close Prices')
plt.legend()
plt.title('Actual vs Predicted Close Prices')
plt.show()
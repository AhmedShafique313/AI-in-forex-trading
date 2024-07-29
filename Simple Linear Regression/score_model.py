from model_LR import model, x_test, y_test, x_val, y_val
import matplotlib.pyplot as plt

print('Coefficient: ', model.coef_)
print('Intercept: ', model.intercept_)

test_score = model.score(x_test, y_test)
print('Test set score: ', test_score)

val_predictions = model.predict(x_val)
plt.scatter(y_val, val_predictions)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices (Validation Set)')
plt.show()

val_score = model.score(x_val, y_val)
print('Validation Set Score:', val_score)

plt.plot(y_val.values, label='Actual Prices')
plt.plot(val_predictions, label='Predicted Prices', linestyle='--')
plt.xlabel('Index')
plt.ylabel('Prices')
plt.title('Actual vs Predicted Prices (Validation Set)')
plt.legend()
plt.show()
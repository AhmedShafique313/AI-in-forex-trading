from model_LR import model, x_test, y_test, x_val, y_val
import matplotlib.pyplot as plt
import joblib

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

plt.figure(figsize=(12, 6))
plt.plot(y_val.values, label='Actual Prices', color='green')
plt.plot(val_predictions, label='Predicted Prices', linestyle='--', color='orange')
plt.xlabel('Index')
plt.ylabel('Prices')
plt.title('Actual vs Predicted Prices (Validation Set)')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.style.use('dark_background')
plt.show()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot actual prices
ax1.plot(y_val.values, label='Actual Prices', color='green')
ax1.set_title('Actual Prices')
ax1.legend()
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Plot Linear Regression predictions
ax2.plot(val_predictions, label='Predicted Prices', linestyle='--', color='blue')
ax2.set_title('Linear Regression Predictions')
ax2.legend()
ax2.grid(True, which='both', linestyle='-', linewidth=0.5)

# Set the same style as the provided image
plt.style.use('dark_background')

# Set labels for x and y axis
ax1.set_ylabel('Price')
ax2.set_xlabel('Index')
ax2.set_ylabel('Price')

# Show plot
plt.show()

joblib.dump(model, 'forex_LR_model.pkl')
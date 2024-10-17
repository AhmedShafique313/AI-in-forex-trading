from LSTM_model import *
from sklearn.metrics import mean_absolute_error, accuracy_score

y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'MSE: {mse}')
print(f'MAE: {mae}')
print(f'RMSE: {rmse}')

y_train_binary = (y_train[1:] > y_train[:-1]).astype(int)
y_test_binary = (y_test[1:] > y_test[:-1]).astype(int)

y_pred_binary = (y_pred[1:] > y_pred[:-1]).astype(int)
accuracy = accuracy_score(y_test_binary, y_pred_binary)
print(f'Accuracy: {accuracy * 100:.2f}%')
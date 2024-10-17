from scaling import *
from keras.models import Sequential
from keras.layers import LSTM, Dense

# building model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 6)))
model.add(LSTM(units=50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(x_train, y_train, epochs=180, batch_size=20, validation_data=(x_test, y_test))
mse = model.evaluate(x_test, y_test)
print(f'MSE: {mse}')
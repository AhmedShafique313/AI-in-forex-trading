from initial_plot import *
from neuralprophet import NeuralProphet

model = NeuralProphet(
        # # seasonality='daily',
        # # season_duration=1,
        # yearly_seasonality=False,
        # weekly_seasonality=True,
        # daily_seasonality=True,
        # changepoints=None,
        # n_changepoints=50,
        # changepoints_range=0.8,
        # # trend='linear',
        # growth='off',
        # # uncertainty='off'
)

# model = NeuralProphet()
# model.add_seasonality(name='daily', period=1, condition_name=None)
# model.add_seasonality(name='weekly', period=7, condition_name=None)
model.fit(df, epochs=100, batch_size=32)
# metrics = model.fit(df, freq="D")
future = model.make_future_dataframe(df, periods=30)
forecast = model.predict(future)
actual = model.predict(df)

plt.plot(actual['ds'], actual['yhat1'], label = "Actual Values", c = 'r')
plt.plot(forecast['ds'], forecast['yhat1'], label = 'future Values', c = 'b')
plt.plot(df['ds'], df['y'], label = 'actual', c = 'g')
plt.legend()
plt.title('EUR/USD')
plt.show()
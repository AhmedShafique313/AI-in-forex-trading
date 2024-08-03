from model_mlr import model1, x1_test, x1_val, x1_train
from model2_mlr import model2, x2_test, x2_train
from model3_mlr import model3, y_test, x3_test, y_val, y_train, x3_train
import matplotlib.pyplot as plt

print('Coefficient of model #01: ', model1.coef_)
print('Intercept of model #01: ', model1.intercept_)
print('Coefficient of model #02: ', model2.coef_)
print('Intercept of model #02: ', model2.intercept_)
print('Coefficient of model #03: ', model3.coef_)
print('Intercept of model #03: ', model3.intercept_)

test_score1 = model1.score(x1_test, y_test)
print('Test set score of model #01: ', test_score1)

test_score2 = model2.score(x2_test, y_test)
print('Test set score of model #01: ', test_score2)

test_score3 = model3.score(x3_test, y_test)
print('Test set score of model #01: ', test_score3)

val_predictions1 = model1.predict(x1_val)
val_score1 = model1.score(x1_val, y_val)
print('Validation Set Score:', val_score1)


plt.figure(figsize=(12, 6))
plt.scatter(y_train, model1.predict(x1_train), label='Model 1 - Train', alpha=0.5)
plt.scatter(y_train, model2.predict(x2_train), label='Model 2 - Train', alpha=0.5)
plt.scatter(y_train, model3.predict(x3_train), label='Model 3 - Train', alpha=0.5)
plt.scatter(y_test, model1.predict(x1_test), label='Model 1 - Test', alpha=0.5)
plt.scatter(y_test, model2.predict(x2_test), label='Model 2 - Test', alpha=0.5)
plt.scatter(y_test, model3.predict(x3_test), label='Model 3 - Test', alpha=0.5)
plt.xlabel('Actual Close Prices')
plt.ylabel('Predicted Close Prices')
plt.legend()
plt.title('Actual vs Predicted Close Prices')
plt.show()
plt.figure(figsize=(12, 6))
from flask import Flask, request, render_template_string
import joblib
import numpy as np

# Load the model
model = joblib.load('forex_LR_model.pkl')

# Initialize the Flask application
app = Flask(__name__)

# HTML template for the home page with a form
home_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>Forex Prediction</title>
</head>
<body>
    <h1>Forex Prediction API</h1>
    <form action="/" method="post">
        <label for="open">Open Price:</label><br>
        <input type="number" step="0.0001" id="open" name="open" required><br><br>
        <label for="high">High Price:</label><br>
        <input type="number" step="0.0001" id="high" name="high" required><br><br>
        <label for="low">Low Price:</label><br>
        <input type="number" step="0.0001" id="low" name="low" required><br><br>
        <label for="volume">Volume:</label><br>
        <input type="number" id="volume" name="volume" required><br><br>
        <input type="submit" value="Predict">
    </form>

    {% if prediction %}
    <h2>Predicted Close Price: {{ prediction }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        open_price = float(request.form['open'])
        high_price = float(request.form['high'])
        low_price = float(request.form['low'])
        volume = int(request.form['volume'])

        input_data = np.array([[open_price, high_price, low_price, volume]])
        
        prediction = model.predict(input_data)[0][0]
    
    return render_template_string(home_page, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

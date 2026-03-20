from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model (make sure model.pkl exists)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        features = [
            float(request.form['Nitrogen']),
            float(request.form['Phosphorus']),
            float(request.form['Potassium']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['pH']),
            float(request.form['rainfall'])
        ]

        # Convert to numpy array
        final_features = np.array([features])

        # Predict
        prediction = model.predict(final_features)

        return render_template("index.html",
                               prediction_text=f"Recommended Crop is: {prediction[0]}")

    except Exception as e:
        return render_template("index.html",
                               prediction_text="Error in prediction")

if __name__ == "__main__":
    app.run(debug=True)
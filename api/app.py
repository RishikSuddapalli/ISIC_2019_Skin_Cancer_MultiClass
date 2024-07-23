from flask import Flask, request, render_template
from flask_cors import CORS
from model import Model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load the model
model_path = '/Users/KIIT/Desktop/ISICscm/ENB1_8Class30.h5'
model = Model(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # Read the image
    img = Image.open(file.stream)from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from model import Model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load the model
model_path = '/Users/KIIT/Desktop/ISICscm/ENB1_8Class30.h5'  # Update this path if necessary
model = Model(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Read the image
    img = Image.open(file.stream)
    img_array = np.array(img)

    # Make prediction
    prediction = model.predict(img_array)

    # Return prediction as JSON
    return jsonify({"prediction": prediction})

# Vercel requires this entry point
if __name__ == '__main__':
    app.run(debug=True)

    img_array = np.array(img)

    # Make prediction
    prediction = model.predict(img_array)
    return prediction

if __name__ == '__main__':
    app.run(debug=True)


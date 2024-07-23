from flask import Flask, request, render_template
from flask_cors import CORS
from model import Model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load the model
model_path = '/Users/KIIT/Desktop/ISICscm/ENB1_8Class30.h5' # Update with your model path
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
    img = Image.open(file.stream)
    img_array = np.array(img)

    # Make prediction
    prediction = model.predict(img_array)
    return prediction

if __name__ == '__main__':
    app.run(debug=True)

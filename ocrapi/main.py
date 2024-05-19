from flask import Flask, request, jsonify
from PIL import Image
import pytesseract

# Establecer la ruta del ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_process():
    if request.method == 'POST':
        image_file = request.files['image']
        image_data = Image.open(image_file)

        #Perform OCR using Pytesseract
        text = pytesseract.image_to_string(image_data)

        response = {
            'status': 'success',
            'text': text
        }

        return jsonify(response)

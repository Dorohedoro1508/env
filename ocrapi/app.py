from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract

# Establecer la ruta del ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
CORS(app)  # Habilitar CORS

@app.route('/ocr', methods=['POST'])
def ocr_process():
    try:
        if 'image' not in request.files:
            return jsonify({'status': 'error', 'message': 'No image file found'}), 400

        image_file = request.files['image']
        image_data = Image.open(image_file)

        # Perform OCR using Pytesseract
        text = pytesseract.image_to_string(image_data)

        response = {
            'status': 'success',
            'text': text
        }
        return jsonify(response)
    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e)
        }
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)

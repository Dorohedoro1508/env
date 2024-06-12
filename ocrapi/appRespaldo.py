from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract
import csv
import os

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

# Nueva ruta para manejar la subida de imágenes desde el disco
@app.route('/upload', methods=['POST'])
def upload_image():
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

@app.route('/create_csv', methods=['POST'])
def create_csv():
    try:
        data = request.json
        if 'text' not in data:
            return jsonify({'status': 'error', 'message': 'No text provided'}), 400

        text = data['text']
        csv_filename = 'ocr_result.csv'
        
        # Dividir el texto en líneas y palabras
        lines = text.split('\n')
        csv_data = [line.split() for line in lines]

        # Guardar el texto como un archivo CSV
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)

        response = {
            'status': 'success',
            'message': f'CSV file created successfully: {csv_filename}',
            'csv_filename': csv_filename
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

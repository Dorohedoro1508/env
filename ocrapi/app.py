from flask import Flask, request, jsonify, send_file
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
        data = request.get_json()
        text = data.get('text', '')
        
        # Crear archivo CSV
        csv_file = 'ocr_result.csv'
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Text'])
            writer.writerow([text])
        
        return jsonify({'status': 'success', 'message': 'CSV created successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/download_csv', methods=['GET'])
def download_csv():
    try:
        csv_filename = 'ocr_result.csv'
        csv_path = os.path.join('C:\\Users\\tatan\\OneDrive\\Documents\\Ing Conocimiento\\env', csv_filename)
        if os.path.exists(csv_path):
            return send_file(csv_path, as_attachment=True)
        else:
            return jsonify({'status': 'error', 'message': 'CSV file not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

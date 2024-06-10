"""
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


from PIL import Image
import pytesseract

# Establecer la ruta del ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

from PIL import Image
import pytesseract

# Establecer la ruta del ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)
    
"""
from PIL import Image
import pytesseract

# Establecer la ruta del ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_image(image_path):
    try:
        print(f"Processing image at {image_path}")
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print(f"Extracted text: {text}")
        return text
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return str(e)
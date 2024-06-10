"""
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
/////////////////////////////////////////////////////////////////////////////////////
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from main import process_image  # Asumiendo que process_image es la función para el OCR

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        text = process_image(filepath)
        return jsonify({'status': 'success', 'text': text})

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        text = process_image(filepath)
        return jsonify({'status': 'success', 'text': text})

if __name__ == '__main__':
    app.run(debug=True)
///////////////////////////////////////
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from main import process_image  # Importar la función de procesamiento de imagen desde main.py

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        text = process_image(filepath)
        return jsonify({'status': 'success', 'text': text})

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        print("No image part")
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        print("No selected file")
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print(f"File saved at {filepath}")
        text = process_image(filepath)
        print(f"Extracted text: {text}")
        return jsonify({'status': 'success', 'text': text})

if __name__ == '__main__':
    app.run(debug=True)
"""
"""
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from main import process_image  # Importar la función de procesamiento de imagen desde main.py

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        text = process_image(filepath)
        return jsonify({'status': 'success', 'text': text})

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        print("No image part")
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        print("No selected file")
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print(f"File saved at {filepath}")
        text = process_image(filepath)
        print(f"Extracted text: {text}")
        return jsonify({'status': 'success', 'text': text})

if __name__ == '__main__':
    app.run(debug=True)
"""
"""
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from main import process_image  # Importar la función de procesamiento de imagen desde main.py

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        text = process_image(filepath)
        return jsonify({'status': 'success', 'text': text})

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        print("No image part")
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        print("No selected file")
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print(f"File saved at {filepath}")
        text = process_image(filepath)
        print(f"Extracted text: {text}")
        return jsonify({'status': 'success', 'text': text})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from main import process_image  # Importar la función de procesamiento de imagen desde main.py

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        text = process_image(filepath)
        print(f"Processed OCR text: {text}")  # Mensaje de depuración adicional
        return jsonify({'status': 'success', 'text': text})

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        print("No image part")
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        print("No selected file")
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print(f"File saved at {filepath}")
        text = process_image(filepath)
        print(f"Processed OCR text: {text}")  # Mensaje de depuración adicional
        return jsonify({'status': 'success', 'text': text})

if __name__ == '__main__':
    app.run(debug=True)
"""

from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from main import process_image  # Importar la función de procesamiento de imagen desde main.py

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        text = process_image(filepath)
        print(f"Processed OCR text: {text}")  # Mensaje de depuración adicional
        return jsonify({'status': 'success', 'text': text})

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        print("No image part")
        return jsonify({'status': 'error', 'message': 'No image part'})
    file = request.files['image']
    if file.filename == '':
        print("No selected file")
        return jsonify({'status': 'error', 'message': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print(f"File saved at {filepath}")
        text = process_image(filepath)
        print(f"Processed OCR text: {text}")  # Mensaje de depuración adicional
        return jsonify({'status': 'success', 'text': text})

if __name__ == '__main__':
    app.run(debug=True)

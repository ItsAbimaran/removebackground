import requests
from flask import Flask, request, render_template, send_file, redirect
from rembg import remove
import tempfile

@app.route('/')
app = Flask(__name__)

def index():
    return render_template('index.html')

@app.route('/remove_bg', methods=['POST'])
def remove_background():
    file = request.files['image']
    image_data = file.read()

    try:
        result_image = remove(image_data)
        temp_image = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_image.write(result_image)
        temp_image.close()
        return send_file(temp_image.name, as_attachment=True)
    except requests.exceptions.RequestException as e:
        return "Error: pls try again"

if __name__ == "__main__":
    app.run(debug=True)
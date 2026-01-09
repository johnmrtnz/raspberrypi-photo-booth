# photobooth.py
from flask import Flask, render_template, Response, send_file
from picamera2 import Picamera2
import io
import os
from datetime import datetime

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

# Create photos directory if it doesn't exist
PHOTOS_DIR = 'photos'
os.makedirs(PHOTOS_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('booth.html')

@app.route('/capture')
def capture():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'Bittersweet_{timestamp}.jpg'
    filepath = os.path.join(PHOTOS_DIR, filename)

    picam2.start()
    picam2.capture_file(filepath)
    picam2.stop()

    return send_file(filepath, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
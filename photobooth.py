# photobooth.py
from flask import Flask, render_template, Response, send_file
from picamera2 import Picamera2
import io
from datetime import datetime

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

@app.route('/')
def index():
    return render_template('booth.html')

@app.route('/capture')
def capture():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filepath = f'/tmp/photo_{timestamp}.jpg'
    picam2.start()
    picam2.capture_file(filepath)
    picam2.stop()
    return send_file(filepath, as_attachment=True, download_name=f'photobooth_{timestamp}.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
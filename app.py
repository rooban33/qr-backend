from flask import Flask, jsonify, request
from flask_cors import CORS
import cv2
import webbrowser

app = Flask(__name__)
CORS(app)
app = Flask(__name__)

@app.route('/scan_qr_code', methods=['GET', 'POST'])
def scan_qr_code():
    print("I am Called")
    _, img = cv2.VideoCapture(0).read()
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    if data:
        if data.startswith('http://') or data.startswith('https://'):
            webbrowser.open(str(data))
            return jsonify({'message': 'Link opened successfully'})
        else:
            return jsonify({'data': str(data)})
    else:
        return jsonify({'message': 'No QR code detected'})

@app.route('/', methods=['GET', 'POST'])
def handle_root():
    if request.method == 'POST':
        print('Hello Shajith!!')
        return jsonify({'message': 'POST request processed successfully'})
    else:
        return jsonify({'message': 'Hello, this is a GET request!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

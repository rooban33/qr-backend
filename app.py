from flask import Flask, jsonify, request
import cv2
import webbrowser

app = Flask(__name__)

@app.route('/scan_qr_code', methods=['POST'])
def scan_qr_code():
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

if __name__ == '__main__':
    app.run(debug=True)

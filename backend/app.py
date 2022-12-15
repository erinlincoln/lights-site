from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import socket

app = Flask(__name__)
CORS(app)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

@app.route('/lights/', methods=['GET', 'POST'])
def welcome():
    data = request.json
    # zone = data.zone
    zone = 0
    color = data['colors'][0][1:]

    HOST = "10.0.0.252"  # The server's hostname or IP address
    PORT = 1234  # The port used by the server

    colorString = '0'+ str(zone)

    for x in range(100):
        colorString += color

    arr = bytearray.fromhex(colorString)

    s.connect((HOST, PORT))
    s.sendall(arr)
    s.close()

    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
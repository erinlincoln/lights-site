from flask import Flask, request, render_template
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)

PORT = 1234  # The port used by the server

STRIP_LEN = 100

currArr = [] #init for test view

@app.route('/lights/', methods=['GET', 'POST'])
def setLights():
    data = request.json
    # zone = data.zone
    zone = 0
    colors = [ c[1:] for c in data['colors'] ]

    HOST = "10.0.0.252"  # The server's hostname or IP address

    colorArr = ['0'+ str(zone)]

    while len(colorArr) < (STRIP_LEN + 2):
        for color in colors:
            colorArr.append(color)

    colorString = "".join(colorArr)

    # for test route
    global currArr
    currArr= [ "#" + c for c in colorArr ]


    arr = bytearray.fromhex(colorString)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(arr)
    s.close()

    return 'success'

@app.route('/test/', methods=['GET'])
def test():
    return render_template('test.html', colors=currArr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
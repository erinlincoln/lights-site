from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/lights/', methods=['GET', 'POST'])
def welcome():
    data = request.json
    print(data['colors'])
    # zone = data.zone
    zone = 0
    color = data.colors[0][1:]

    print(color)

    HOST = "10.0.0.252"  # The server's hostname or IP address
    PORT = 1234  # The port used by the server

    arr = [zone]

    for x in range(100):
        arr.append(color)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
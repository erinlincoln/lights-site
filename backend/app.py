from flask import Flask, request, render_template
from flask_cors import CORS
from setup import rooms
import threading
import time
import modes

app = Flask(__name__)
CORS(app)

queue = []
DELAY = 0.02 # delay between sending data

@app.route('/lights/', methods=['GET', 'POST'])
def setLights():
    data = request.json
    room = [ r for r in rooms if r.name == data[ 'area' ][ 'room' ] ][ 0 ]

    global queue
    queue.append( { **data, 'area': { **data[ 'area' ], 'room': room } } )

    if len(queue) > 10:
        for i in range(4):
            queue.pop( i * 2 + 1 )

    return 'success'


def getMode( type):
    modes_dict = {
        'single-color': modes.LEDMode_Solid,
        'multi-color': modes.LEDMode_Alternating
    }

    return modes_dict[ type ]


def sendData():
    global queue

    # give strips update
    ms_since_epoch = round(time.time()*1000)
    for room in rooms:
        room.updateStrips(ms_since_epoch)

    if len(queue) > 0:
        data = queue.pop(0)
        print(data)
        room = data[ 'area' ][ 'room' ]
        mode = getMode(data[ 'mode' ][ 'type' ])

        # update data to have mode object
        data = { **data, "mode": mode }

        if not room.open():
            # ms_since_epoch = round(time.time()*1000)
            # room.updateStrips(ms_since_epoch)
            ret = room.sendAll(data)
            if ret and len(queue) == 0: 
                queue.insert( 0, data )
                print('retry: ', queue)
        

    threading.Timer( DELAY, sendData ).start()

sendData()

# @app.route('/test/', methods=['GET'])
# def test():
#     print('here')
#     print(currArr)
#     return render_template('test.html', colors=currArr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
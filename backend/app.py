from flask import Flask, request, render_template
from flask_cors import CORS
from setup import rooms
import threading
import time
import modes
import json

app = Flask(__name__)
CORS(app)

queue = []
updateInProgress = False
DELAY = 0.02 # delay between sending data

@app.route('/lights/', methods=['GET', 'POST'])
def setLights():
    global queue

    # get data and get room object based on room name
    data = request.json
    room = [ r for r in rooms if r.name == data[ 'area' ][ 'room' ] ][ 0 ]

    # if queue is over 10 entries, take out odd numbered entries
    if len(queue) > 10:
        for i in range(4):
            queue.pop( i * 2 + 1 )

    # add data to the queue with room object
    queue.append( { **data, 'area': { **data[ 'area' ], 'room': room } } )

    return 'added to queue'


# def getMode( type):
#     modes_dict = {
#         'single-color': modes.LEDMode_Solid,
#         'multi-color': modes.LEDMode_Alternating
#     }

#     return modes_dict[ type ]

# schedule data to be added to queue later
def scheduleData(data):
    d = 1


def sendData():
    global queue
    global updateInProgress

    while True:

        # if another thread isn't in progress
        if not updateInProgress:

            # indicate process is running
            updateInProgress = True

            # update room
            for room in rooms:
                room.updateStrips()

            # if there is data in the queue
            if len(queue) > 0:
                data = queue[0]

                # if data is scheduled
                if 'scheduled' in data:
                    scheduleData(data)
                
                # if not scheduled, change mode
                else:
                    room = data[ 'area' ][ 'room' ]
                    zone = data['area'].get('zone')
                    strip = data['area'].get('strip')
                    mode = data['payload']

                    room.changeMode(mode, zone, strip)

                # var to keep track of whether current data can be deleted from queue
                canDelete = True

                # update strips in all rooms
                for room in rooms:
                    try:
                        # try to update room
                        result = room.updateStrips()

                        # if returns false, cannot delete
                        if not result: canDelete = False
                    except:
                        # if error is thrown, cannot delete
                        canDelete = False

                # if still can delete, pop data from queue
                if canDelete:
                    queue.pop()
            
            # indicate process is done
            updateInProgress = False

        time.sleep(DELAY)

    # start timer over
    # threading.Timer( DELAY, sendData ).start()
    
    # # give strips update
    # ms_since_epoch = round(time.time()*1000)
    # for room in rooms:
    #     room.updateStrips(ms_since_epoch)

    # if len(queue) > 0:
    #     data = queue.pop(0)
    #     print(data)
    #     room = data[ 'area' ][ 'room' ]
    #     mode = getMode(data[ 'mode' ][ 'type' ])

    #     # update data to have mode object
    #     data = { **data, "mode": mode }

    #     if not room.open():
    #         # ms_since_epoch = round(time.time()*1000)
    #         # room.updateStrips(ms_since_epoch)
    #         ret = room.sendAll(data)
    #         if ret and len(queue) == 0: 
    #             queue.insert( 0, data )
    #             print('retry: ', queue)
        

    



# @app.route('/test/', methods=['GET'])
# def test():
#     print('here')
#     print(currArr)
#     return render_template('test.html', colors=currArr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
    sendData()
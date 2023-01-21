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
DELAY = 0.2 # delay between sending data

# Global semaphore used to control access to the mode queue
queue_sem = threading.Semaphore(1)

@app.route('/lights/', methods=['GET', 'POST'])
def setLights():
    global queue, queue_sem

    queue_sem.acquire()
    # BEGIN CRITICAL SECTION

    # get data and get room object based on room name
    data = request.json
    room = [ r for r in rooms if r.name == data[ 'area' ][ 'room' ] ][ 0 ]

    # if queue is over 10 entries, take out odd numbered entries
    if len(queue) > 10:
        for i in range(4):
            queue.pop( i * 2 + 1 )

    # add data to the queue with room object
    queue.append( { **data, 'area': { **data[ 'area' ], 'room': room } } )

    # END CRITICAL SECTION
    queue_sem.release()

    return 'added to queue'


@app.errorhandler(Exception)
def handle_exception(e):
    print(e)
    return str(e)

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
    global queue, queue_sem

    # Infinite loop over queue
    while True:

        # update room
        for room in rooms:
            room.updateStrips()

        if queue_sem.acquire(timeout=0.1):
            # BEGIN CRITICAL SECTION

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
                    queue.pop(0)

            # END CRITICAL SECTION
            queue_sem.release()

        else:
            # Failed to grab semaphore, print debug line
            print("Failed to grab semaphore: data thread")

        # Wait until next loop
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

def run_backend():
    app.run(host='0.0.0.0', port=3001)

if __name__ == '__main__':
    t_bend = threading.Thread(target = run_backend)
    t_data = threading.Thread(target = sendData)
    
    t_bend.start()
    t_data.start()
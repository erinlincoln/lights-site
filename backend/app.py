from flask import Flask, request, render_template
from flask_cors import CORS
from setup import strips
import threading
import time
from modes.create_mode import create_mode
from test_timing import TimingTester

app = Flask(__name__)
CORS(app)

queue = []
updateInProgress = False
DELAY = 0.02 # delay between sending data

# Global semaphore used to control access to the mode queue
queue_sem = threading.Semaphore(1)

# Global timers
tt_setLights = TimingTester("SetLights()")

@app.route('/lights/', methods=['GET', 'POST'])
def setLights():
    global queue, queue_sem

    tt_setLights.start()

    queue_sem.acquire()
    # BEGIN CRITICAL SECTION

    # get data and get room object based on room name
    data = request.json

    # if queue is over 10 entries, take out odd numbered entries
    if len(queue) > 10:
        for i in range(4):
            queue.pop( i * 2 + 1 )

    # add data straight to the queue
    queue.append( data )

    # END CRITICAL SECTION
    queue_sem.release()

    tt_setLights.stop()
    tt_setLights.print()

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
    global queue, queue_sem, strips

    # Debugging timing
    tt_sendData = TimingTester("SendData()")
    tt_queueSem = TimingTester("Queue Sem.")
    tt_stripUpd = TimingTester("Strip Upd.")

    # Infinite loop over queue
    while True:

        tt_sendData.start()
        tt_queueSem.start()

        # Pull in new modes from queue
        if queue_sem.acquire(timeout=0.01):
            # BEGIN CRITICAL SECTION

            # if there is data in the queue
            if len(queue) > 0:
                data = queue[0]

                # if data is scheduled
                # TODO this
                #if 'scheduled' in data:
                #    scheduleData(data)
                
                # var to keep track of whether current data can be deleted from queue
                canDelete = True

                # Update all strips in data
                if "strips" in data:
                    for strip_json in data["strips"]:
                        # error checking
                        if "id" not in strip_json:
                            print("Invalid JSON received: No strip ID. Skipping strip.")
                            continue
                        if "mode" not in strip_json:
                            print("Invalid JSON received: No mode. Skipping strip.")
                            continue
                        if strip_json["id"] not in strips:
                            print("Invalid strip ID. Skipping strip.")
                            continue
                        if "name" not in strip_json["mode"]:
                            print("Invalid JSON received: No name in mode. Skipping strip.")
                            continue
                        if "data" not in strip_json["mode"]:
                            print("Invalid JSON received: No data in mode. Skipping strip.")

                        # parse strip
                        strip = strips[strip_json["id"]]
                        mode = create_mode(strip.length, strip_json["mode"])

                        if mode is None:
                            print("Failed to parse mode JSON. Skipping strip.")
                            continue

                        # Finally change the mode of the strip
                        #print("Changing mode of ", strip_json["id"])
                        strip.changeMode(mode)

                # if still can delete, pop data from queue
                if canDelete:
                    queue.pop(0)

            # END CRITICAL SECTION
            queue_sem.release()

        else:
            # Failed to grab semaphore, print debug line
            print("Failed to grab semaphore: data thread")

        tt_queueSem.stop()
        tt_queueSem.print()

        # Update all strips
        tt_stripUpd.start()

        t = time.time() * 1000
        for strip in strips.values():
            strip.update(t)

        tt_stripUpd.stop()
        tt_stripUpd.print()
        

        # Wait until next loop
        time.sleep(DELAY)

        tt_sendData.stop()
        tt_sendData.print()





def run_backend():
    app.run(host='0.0.0.0', port=3001)

if __name__ == '__main__':
    t_bend = threading.Thread(target = run_backend)
    t_data = threading.Thread(target = sendData)
    
    t_bend.start()
    t_data.start()
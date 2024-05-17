from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from setup import strips
import threading
import time
from mode_data import create_mode_message, create_ota_message
from database import init_db, EventHistory, Devices
from test_timing import TimingTester

queue = []
# Global semaphore used to control access to the mode queue
queue_sem = threading.Semaphore(1)

# Global timers
tt_setLights = TimingTester("SetLights()")

def create_app():
    
    app = Flask(__name__)
    CORS(app)

    init_db(app)

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

    @app.route('/eventhistory/', methods=['GET'])
    def getEventHistory():
        # TODO support filtering history by dates
        events = EventHistory.get_events_by_time()
        return jsonify([event.to_dict() for event in events])

    @app.route('/devices/', methods=['GET'])
    def getDevices():
        devices = Devices.get_devices()
        return jsonify([device.to_dict() for device in devices])

    @app.route('/devices/', methods=['POST'])
    def addDevice():
        data = request.json
        if 'device' not in data:
            return "devices endpoint requires devices entry", 404
        if 'ip' not in data['device'] or 'id' not in data['device']:
            return "device entry requires ip and id", 404
        device = Devices.add_device(data['device']['id'], data['device']['ip'])
        return jsonify(device.to_dict())
    
    @app.route('/eventhistoryclear/', methods=['POST'])
    def clearEventHistory():
        return str(EventHistory.clear())


    @app.errorhandler(Exception)
    def handle_exception(e):
        print(e)
        return str(e)
    
    return app


# TODO Change json handling to queue strip requests individually
def sendData():
    global queue, queue_sem, strips

    # Debugging timing
    tt_sendData = TimingTester("SendData()")
    tt_queueSem = TimingTester("Queue Sem.")

    app = create_app()

    with app.app_context():

        # Infinite loop over queue
        while True:

            tt_sendData.start()
            tt_queueSem.start()

            # Always send timestamp on startup
            last_time_sent = time.time() - 500

            # Pull in new modes from queue
            if queue_sem.acquire(timeout=0.01):
                # BEGIN CRITICAL SECTION

                # if there is data in the queue
                if len(queue) > 0:
                    data = queue[0]
                    
                    # var to keep track of whether current data can be deleted from queue
                    canDelete = True

                    # Create a system message if necessary
                    if "system" in data:
                        if "ota" in data["system"] and data["system"]["ota"] in strips.keys():
                            message = create_ota_message()
                            strip = strips[data["system"]["ota"]]
                            print("Sending OTA task to " + data["system"]["ota"])
                            strip.setData(message)
                            canDelete = canDelete and strip.send()

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
                                continue

                            # parse strip
                            strip = strips[strip_json["id"]]
                            message = create_mode_message(strip.index, strip_json["mode"])

                            if message is None:
                                print("Failed to parse mode JSON. Skipping strip.")
                                continue

                            # Finally change the mode of the strip
                            print("Changing mode of ", strip_json["id"])
                            strip.setData(message)
                            canDelete = canDelete and strip.send()

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

            # Wait until next loop
            time.sleep(0.02)

            tt_sendData.stop()
            tt_sendData.print()


if __name__ == '__main__':
    app = create_app()
    t_data = threading.Thread(target = sendData)
    t_data.start()
    app.run(host='0.0.0.0', port=3001)
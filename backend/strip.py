import socket
from modes.basic_modes import get_default_mode
from threading import Semaphore
import json
import ast

PORT = 1234  # The port used by the server
STRIP_LEN = 100 # LEDS on a strip

class Strip:
    def __init__(self, host, index, length):
        self.open = False
        self.index = index
        self.length = length
        self.most_recent_timestamp = -1
        self.mode = get_default_mode(self.length)
        self.host = host
        self.semaphore = Semaphore() # Semaphore used to protect self.mode
        # Right now this semaphore essentially does nothing
        
    @property
    def data(self):
        return self.mode.data

    # tell mode to update
    def update(self):
        
        self.semaphore.acquire()
        # CRITICAL SECTION

        # tell mode to update and get var back whether to send new data
        send = self.mode.progress()

        result = True

        # if strip data is updated, send new data
        if send:
            result = self.send()

        # END CRITICAL SECTION
        self.semaphore.release()

        return result

    # sets new mode of strip
    def changeMode(self, mode):
        
        self.semaphore.acquire()
        # CRITICAL SECTION

        # set new previous mode
        self.prevMode = self.mode

        # set new mode
        self.mode = mode

        # END CRITICAL SECTIOn
        self.semaphore.release()

    # Sends the data to the pico
    # CALL THIS FROM A CRITICAL SECTION ONLY!
    def send( self ):

        # Append index to front of data
        data_final = ['0'+ str(self.index) ]
        for color in self.data:
            data_final.append(color[1:])
        data_final = bytearray.fromhex("".join(data_final))

        print('about to send')
        print(self.host)

        self.open = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print('about to connect')
        self.socket.connect(( self.host, PORT ))

        result = False

        try:
            print('trying to send')
            # attempt to read to see if socket is closed
            self.socket.settimeout(2)
            # self.socket.recv(1)
            self.socket.sendall( data_final )

            result = str(self.socket.recv(7))[2:-1]
        except Exception as e:
            print('error on reading', e)
            print('length of data being sent:'. len(data_final))
            ConnectionAbortedError('upload failed - try again')


        print('closing socket')

        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

        self.open = False

        return result == 'Success'

    def bitArr( self ):
        # indicate strip to write to
        colorArr = ['0'+ str(self.index) ]

        # add list of colors
        while len(colorArr) < (STRIP_LEN + 2):
            for color in self.data:
                colorArr.append(color[ 1 : ])

        # make into a string
        colorString = "".join(colorArr)

        # return bytearray of colors
        return bytearray.fromhex(colorString)
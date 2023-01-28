import socket
from modes.basic_modes import get_default_mode
from threading import Semaphore
from test_timing import TimingTester
import time

PORT = 1234  # The port used by the server
STRIP_LEN = 100 # LEDS on a strip

# Global dict used to manage socket connections
sockets = dict()

tt_testing  = TimingTester("Testing")

class Strip:
    def __init__(self, host, index, length):
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
    def update(self, t):
        
        self.semaphore.acquire()
        # CRITICAL SECTION

        # tell mode to update and get var back whether to send new data
        
        send = self.mode.progress(t)

        result = True

        # if strip data is updated, send new data
        if send:
            tt_testing.start()
            result = self.send()
            tt_testing.stop()
            tt_testing.print()

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
        global sockets

        # Append index to front of data
        data_final = ['0'+ str(self.index) ]
        for color in self.data:
            data_final.append(color[1:])
        data_final = bytearray.fromhex("".join(data_final))

        print('about to send')
        print(self.host)

        if self.host not in sockets.keys():
            sockets[self.host] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockets[self.host].connect(( self.host, PORT ))
        self.socket = sockets[self.host]

        result = False

        try:
            #print('trying to send')
            self.socket.settimeout(2)
            self.socket.sendall( data_final )
        except (ConnectionResetError, ConnectionAbortedError, ConnectionError) as e:
            # Attempt reconnection
            print('socket error, attempting reconnection:', e)
            self.socket.connect(( self.host, PORT ))
            return False

        try:
            # Check for 'Success'
            result = str(self.socket.recv(7))[2:-1]
        except Exception as e:
            print('error on reading', e)
            print('length of data being sent:', len(data_final))
            return False


        if result == 'Success':
            print('message success')
            return True

        return False

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
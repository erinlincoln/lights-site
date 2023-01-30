import socket
from mode_data import create_mode_message
from threading import Semaphore
from test_timing import TimingTester
from constants import *
import time
import struct

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
        self.mode = TASK_UNUSED
        self.data = None
        self.lastresponse = None
        self.host = host
        self.semaphore = Semaphore() # Semaphore used to protect self.mode
        # Right now this semaphore essentially does nothing

    # tell mode to update
    def setData(self, data):
        self.data = data
        self.data_msg_id = struct.unpack('>I', data[0:4])

    # Sends the data to the pico
    # CALL THIS FROM A CRITICAL SECTION ONLY!
    def send( self ):
        global sockets

        print('about to send')
        print(self.host)

        if self.host not in sockets.keys():
            sockets[self.host] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockets[self.host].connect(( self.host, PORT ))
        self.socket = sockets[self.host]

        try:
            #print('trying to send')
            self.socket.settimeout(2)
            self.socket.sendall( self.data )
        except (ConnectionResetError, ConnectionAbortedError, ConnectionError) as e:
            # Attempt reconnection
            print('socket error, attempting reconnection:', e)
            self.socket.connect(( self.host, PORT ))
            return False

        res_last_message_id = 0
        res_old_task_id = 0
        res_length = 0
        res_success = False
        try:
            # Receive and parsemessage response
            res_header = str(self.socket.recv(8))[2:-1]
            res_last_message_id = struct.unpack('>I', res_header[0:4])
            res_old_task_id = struct.unpack('>B', res_header[4])
            res_length = struct.unpack('>H', res_header[5:7])
            res_success = struct.unpack('>?', res_header[7])
            res_body = str(self.socket.recv(res_length - 8))

        except Exception as e:
            print('error on reading', e)
            print('length of data being sent:', len(self.data))
            print('length of data being received:', res_length)
            return False
        
        if res_success and self.data_msg_id == res_last_message_id:
            print('message success')
            return True

        # TODO other parsing, error checking, and correction here

        return False
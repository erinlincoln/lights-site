import socket
import modes

PORT = 1234  # The port used by the server
STRIP_LEN = 100 # LEDS on a strip


class Room:
    def __init__( self, name, zones ):
        self.zones = zones
        self.name = name

    def sendAll(self):
        for zone in self.zones:
            zone.sendAll()

    # Updates all LED strips' data with new time
    def updateStrips(self, t):
        for zone in self.zones:
            zone.updateData(t)

    def __eq__( self, obj ):
        return obj.name == self.name

    def open( self ):
        return len([ zone for zone in self.zones if zone.open ]) > 0

class Strip:
    def __init__(self, index, length):
        self.index = index
        self.length = length
        self.most_recent_timestamp = -1
        self.mode = modes.get_default_mode(self.length)
        self.data = []
        for i in range(length):
            self.data.append('#000000')
        

    # Updates the data of a strip depending on the current mode
    def updateData(self, t):
        self.data = self.mode.getData(t)
        self.most_recent_timestamp = t

    # Sets the mode of this strip (does not update data)
    def setMode(self, mode):
        self.mode = mode

    # Sends the data to the pico
    def send( self, host ):

        # Append index to front of data
        data_final = ['0'+ str(self.index) ]
        for color in self.data:
            data_final.append(self.data[1:])
        data_final = bytearray.fromhex("".join(data_final))

        self.open = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(( host, PORT ))
        self.socket.sendall( data_final )
        self.open = False

        result = str(self.socket.recv(7))

        self.socket.close()

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

class Zone:
    def __init__( self, host, strip_count, strip_lengths):
        self.host = host
        self.strip_count = strip_count
        self.strip_lengths = strip_lengths
        self.strips = []
        for i in range(strip_count):
            s = Strip(i, strip_lengths[i])
            self.strips.append(s)
        self.currColors = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.open = False

    # Updates the data in a zone with a new time. Does not send anything.
    def updateData(self, t):
        for strip in self.strips:
            strip.updateData(t)
    
    # Sends all strip data
    def sendAll(self):
        for strip in self.strips:
            strip.send(self.host)
    
    # Sets the mode of a strip
    def setStripMode(self, index, mode):
        self.strips[index].setMode(mode)

    # Sets the mode of all strips
    def setAllModes(self, mode):
        for strip in self.strips:
            strip.setMode(mode)
import socket
import modes

PORT = 1234  # The port used by the server
STRIP_LEN = 100 # LEDS on a strip


class Room:
    def __init__( self, name, zones ):
        self.zones = zones
        self.name = name

    def sendAll(self, data):
        # if zone isn't specified, send to all zones
        if not data or not data.get('zone'):
            for zone in self.zones:
                zone.sendAll( data )
        
        # if zone is specified, only send to that zone
        else:
            index = data[ 'area' ][ 'zone' ]
            self.zones[ index ].sendAll( data )

    # tell mode of strips to update
    def updateStrips(self, zones = None, strips = None):
        if zones == None:
            zones = self.zones; 

        for zone in zones:
            zone.updateStrips(strips)

    # change mode of strip(s)
    def changeMode( self, mode, zones, strips ):
        if zones == None:
            zones = self.zones
        else:
            zones = [ self.zones[i] for i in zones ]

        for zone in zones:
            zone.changeMode(mode, strips)

    # # change mode of all strips in room
    # def changeAllModes(self, mode):
    #     for zone in self.zones:
    #         zone.changeAllModes(mode)

    # # change mode of a single strip in the room
    # def changeStripMode(self, zoneIndex, stripIndex, mode):
    #     self.zones[zoneIndex].changeStripMode(stripIndex, mode)

    def __eq__( self, obj ):
        return obj.name == self.name

    def open( self ):
        return len([ zone for zone in self.zones if zone.open() ]) > 0

    def __hash__(self) -> int:
        return hash(self.name)

class Strip:
    def __init__(self, index, length, host):
        self.open = False
        self.index = index
        self.length = length
        self.most_recent_timestamp = -1
        self.mode = modes.get_default_mode(self.length)
        self.host = host
        
    @property
    def data(self):
        return self.mode.data

    # tell mode to update
    def update(self):
        # tell mode to update and get var back whether to send new data
        send = self.mode.progress()

        # if strip data is updated, send new data
        if send:
            self.send()

    # sets new mode of strip
    def changeMode(self, mode):
        # set new previous mode
        self.prevMode = self.mode

        # set new mode
        self.mode = self.getMode(mode)

    #TODO: replace with real modes - off as placeholder
    # transform mode data to a mode object
    def getMode(self, mode):
        return modes.LEDMode_Solid(self.length, [ '#A020F0' ])

    # Sends the data to the pico
    def send( self ):

        # Append index to front of data
        data_final = ['0'+ str(self.index) ]
        print(data_final)
        for color in self.data:
            data_final.append(color[1:])
        data_final = bytearray.fromhex("".join(data_final))

        print('about to send')

        self.open = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(( self.host, PORT ))

        try:
            print('trying to send')
            # attempt to read to see if socket is closed
            self.socket.settimeout(2)
            # self.socket.recv(1)
            self.socket.sendall( data_final )
        except:
            print('error on reading')
            ConnectionAbortedError('upload failed - try again')

        result = str(self.socket.recv(7))

        print('closing socket')

        self.socket.shutdown('SHUT_RDWR')
        self.socket.close()

        self.open = False

        return result == 'Success'
        # return True

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

    # def transformData(self, data ):
    #     self.setMode( data[ 'mode' ]( self.length, **data['data']))
    #     return data['data'][ 'colors' ]

class Zone:
    def __init__( self, host, strip_count, strip_lengths):
        self.host = host
        self.strip_count = strip_count
        self.strip_lengths = strip_lengths
        self.strips = []
        for i in range(strip_count):
            s = Strip(i, strip_lengths[i], self.host)
            self.strips.append(s)
        self.currColors = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # tell mode of strips to update
    def updateStrips(self, strips):
        if strips == None:
            strips = self.strips
        else:
            strips = [ self.strips[i] for i in strips ]

        for strip in strips:
            strip.update()
    
    # Sends all strip data
    def sendAll(self, data):
        # if strip isn't specified, send to all strips
        if not data or not data[ 'area' ].get( 'strip' ):
            for strip in self.strips:
                strip.send(self.host, data)
        # if strip is specified, only send to that strip
        else:
            index = data[ 'area' ][ 'strip' ]
            self.strips[ index ].send(self.host, data)

    # change mode of strip(s)
    def changeMode(self, mode, strips):
        if strips == None:
            strips = self.strips
        else:
            strips = [ self.strips[i] for i in strips ]

        for strip in strips:
            strip.changeMode(mode)
    
    # # Sets the mode of a strip
    # def changeStripMode(self, index, mode):
    #     self.strips[index].changeMode(mode)

    # # Sets the mode of all strips
    # def changeAllModes(self, mode):
    #     for strip in self.strips:
    #         strip.changeMode(mode)

    def open(self):
        return len([ strip for strip in self.strips if strip.open ]) > 0
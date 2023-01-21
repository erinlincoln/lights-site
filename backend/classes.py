import socket
import modes
from threading import Semaphore
import json
import ast

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

        result = True

        for zone in zones:
            res = zone.updateStrips(strips)
            if not res: result = False

        return result

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
        self.mode = self.getMode(mode)

        # END CRITICAL SECTIOn
        self.semaphore.release()

    #TODO: replace with real modes - off as placeholder
    # transform mode data to a mode object
    def getMode(self, mode):
        colors = ast.literal_eval(mode['colors'])

        match mode['name']:
            case 'solid':
                return modes.LEDMode_Solid(self.length, colors)
            case 'multi':
                return modes.LEDMode_Alternating(self.length, colors, mode.get('width'))
            case 'gradient':
                return modes.LEDMode_Gradient(self.length, colors, mode.get('center'))
            case _:
                print('INVALID MODE: ' + mode['name'])
        # return modes.LEDMode_Solid(self.length, [ '#000000' ])

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

        result = True

        for strip in strips:
            res = strip.update()
            if not res: result = False

        return result
    
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
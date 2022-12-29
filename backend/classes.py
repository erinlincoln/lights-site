import socket

PORT = 1234  # The port used by the server
STRIP_LEN = 100 # LEDS on a strip


class Room:
    def __init__( self, name, zones ):
        self.zones = zones
        self.name = name

    def set( self, colors ):
        result = True
        for zone in self.zones:
            ret = zone.set(colors)
            if ( not ret ): result = False
        
        return result

    def __eq__( self, obj ):
        return obj.name == self.name

    def open( self ):
        return len([ zone for zone in self.zones if zone.open ]) > 0


class Zone:
    def __init__( self, host, length ):
        self.host = host
        self.length = length
        self.currColors = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.open = False

    def set( self, colors ):
        print(colors)
        if colors == ['last']: colors = self.currColors
        elif colors != ['#000000']: self.currColors = colors

        result = True
        for l in range( self.length ):
            arr = self.bitArr( l, colors )   
            ret = self.send( arr )
            if not ret: result = False
        print(colors)
        return result

    def bitArr( self, pos, colors ):
        # indicate strip to write to
        colorArr = ['0'+ str(pos) ]

        # add list of colors
        while len(colorArr) < (STRIP_LEN + 2):
            for color in colors:
                colorArr.append(color[ 1 : ])

        # make into a string
        colorString = "".join(colorArr)

        # return bytearray of colors
        return bytearray.fromhex(colorString)

    def send( self, data ):
        self.open = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(( self.host, PORT ))
        self.socket.sendall( data )
        self.open = False

        result = str(self.socket.recv(7))

        self.socket.close()

        return result == 'Success'
import time
import math


# An abstract class representing the "mode" a strip is in
class LEDMode:
    def __init__(self, length):
        self.length = length
        self.data = []
        for i in range(self.length):
            self.data.append("#000000")
        self.init = True

    # tell leds to progress
    def progress(self):
        init = False

        # checks if needs to send to initialize self
        if self.init:
            init = True
            self.init = False

        return init or self.progressMode()

    def progressMode(self):
        print('ERROR - NEED TO IMPLEMENT PROGRESS MODE')

    # Utility function for converting R, G, and B values to color strings ('#000000')
    def rgbToColor(self, r, g, b):
        # return ('#{:X}{:X}{:X}').format(r, g, b)
        return '#%02x%02x%02x' % (r,g,b)

    # Utility function for converting color strings ('#000000') to R, G, and B values
    def colorToRGB(self, color):
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        return (r, g, b)

# Updating mode: an abstract class for a mode that will need to update
class DynamicLEDMode(LEDMode):
    def __init__( self, length, colors, delay ):
        super().__init__(length)
        self.delay = delay
        self.colors = colors
        self.index = 0
        self.lastUpdate = time.time()
        self.data = []

    def progressMode(self, t):
        # if time to update, update index
        if self.lastUpdate - t > self.delay:
            self.update()
            
            self.data = []
            for i in range( self.length / len( self.colors[ self.index ])):
                for color in self.colors[ self.index ]:
                    self.data.append( color )
        
        return self.data

    # update the index of colors to display
    def update(self):
        self.index += 1
        
        if self.index >= len(self.colors):
            self.index = 0

# static mode: abstract class for a mode that doesn't need to update
class StaticLEDMode(LEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, colors):
        super().__init__(length)
        self.colors = colors
        self.data = []
        for i in range( math.ceil(length / len(self.colors))):
            for color in self.colors:
                self.data.append(color)

    def progressMode(self):
        return False
            

# Solid mode: maintains a constant color on the strip
class LEDMode_Solid(StaticLEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, colors):
        super().__init__(length, colors)


# Alternating mode: alternates between two colors
class LEDMode_Alternating(StaticLEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, colors, width = 1):
        super().__init__(length, colors)
        if width == None: width = 1
        
        self.data = []
        for i in range(math.ceil(self.length / len(self.colors) / width )):
            for color in self.colors:
                [ self.data.append(color) for i in range(width) ]

class LEDMode_Gradient(StaticLEDMode):
    def __init__(self, length, colors, center = 0.5):
        super().__init__(length, colors)
        if center == None: center = 0.5

        self.data = []
        # RGB of inputted colors
        first = self.colorToRGB(colors[0])
        last = self.colorToRGB(colors[-1])

        # calculate rounded rgb of middle LED
        middle = [ round(( first[i] + last[i] ) / 2) for i in range(3) ]

        # where the center LED should be
        centerLED = round(center * length)

        # get list of r,g,b to change the increments by
        firstRange = [math.floor( ( middle[i] - first[i] ) / centerLED) for i in range(3)]
        lastRange = [math.floor( ( last[i] - middle[i] ) / (length - centerLED)) for i in range(3)]

        # add each progressive color to the data
        for j in range(centerLED):
            l = [ first[i] + ( firstRange[i] * j ) if first[i] + ( firstRange[i] * j ) > 0  else 0 for i in range(3) ]
            self.data.append(self.rgbToColor(*l))

        for j in range(length-centerLED):
            l = [ middle[i] + ( lastRange[i] * j ) if middle[i] + ( lastRange[i] * j ) > 0  else 0 for i in range(3) ] 
            self.data.append(self.rgbToColor(*l))

class Updating_LEDMode_Alternating(LEDMode):
    def __init__(self, length):
        super().__init__(length)


# Default mode is off
def get_default_mode(length):
    return LEDMode_Solid(length, [ '#000000' ])

# Creates a mode from the json received from an API request
def create_mode(length, mode_json):
    # Previously, the presence of the 'name' and 'data' properties have been verified
    # The only error checking we need to do is the contents of 'data' and the validity of 'name'

    match mode_json["name"]:
        case "off":
            return LEDMode_Solid(length, ["#000000"])
        case "solid":
            if "colors" not in mode_json["data"] or len(mode_json["data"]["colors"]) != 1:
                return None
            return LEDMode_Solid(length, [mode_json["data"]["colors"][0]])
        # TODO implement others
        
    return None

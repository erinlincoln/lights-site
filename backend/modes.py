import time


# An abstract class representing the "mode" a strip is in
class LEDMode:
    def __init__(self, length):
        self.length = length
        self.data = []
        for i in range(self.length):
            self.data.append("#000000")

    # Gets the data the LEDs should display at time t, depending on parameter param
    # OVERRIDE THIS!
    def getData(self, t):
        return self.data

    # Utility function for converting R, G, and B values to color strings ('#000000')
    def rgbToColor(r, g, b):
        return ('#{:X}{:X}{:X}').format(r, g, b)

    # Utility function for converting color strings ('#000000') to R, G, and B values
    def colorToRGB(color):
        r = color[1:3]
        g = color[3:5]
        b = color[5:7]
        return (r, g, b)

# Updating mode: an abstract class for a mode that will need to update
class Updating_LEDMode(LEDMode):
    def __init__( self, length, colors, delay ):
        super().__init__(length)
        self.delay = delay
        self.colors = colors
        self.index = 0
        self.lastUpdate = time.time()
        self.data = []

    def getData(self, t):
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
            

# Solid mode: maintains a constant color on the strip
class LEDMode_Solid(LEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, colors):
        super().__init__(length)
        self.color = colors[ 0 ]
        self.data = []
        for i in range(self.length):
            self.data.append(self.color[1:])

    def getData(self, t):
        return self.data # solid color is independent of time

# Alternating mode: alternates between two colors
class LEDMode_Alternating(LEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, colors):
        super().__init__(length)
        self.colors = colors
        self.data = []
        for i in range(self.length / len(self.colors)):
            for color in self.colors:
                self.data.append(color)

    def getData(self, t):
        return self.data

class Updating_LEDMode_Alternating(LEDMode):
    def __init__(self, length):
        super().__init__(length)


# Default mode is off
def get_default_mode(length):
    return LEDMode_Solid(length, [ '#000000' ])
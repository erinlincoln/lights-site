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
        self.last_t = time.time()

    # Tell leds to progress. This does nothing for static modes.
    def progress(self, t):
        self.last_t = t

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
            

# Solid mode: maintains a constant color on the strip
class LEDMode_Solid(StaticLEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, colors):
        super().__init__(length, colors)


# Multicolor mode: alternates between any number of colors
class LEDMode_MultiColor(StaticLEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, colors):
        super().__init__(length, colors)
        
        self.data = []
        for i in range(math.ceil(self.length / len(self.colors))):
            for color in self.colors:
                self.data.append(color)

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

class LEDMode_RunningMultiColor(LEDMode):

    # The max speed of this mode.
    # A speed of 1 will rotate pixels 100 times (one standard loop) every SPEED_MULTIPLIER_MS ms.
    SPEED_MULTIPLIER_MS = 1000 # units ms

    def __init__(self, length, colors, speed):
        super().__init__(length)
        self.colors = colors
        self.num_colors = len(colors)
        self.speed = speed
        self.offset = 0 # The offset of the colors array on the LED strip

        # Initial data is beginning of colors, repeated as necessary
        self.data = []
        for i in range(length):
            self.data.append(colors[i % self.num_colors])

    def progress(self, t):
        # Calculate change in time
        delta_t = t - self.last_t

        # Calculate number of offsets
        num_pixels_offset = int(delta_t) * self.speed * 100 / self.SPEED_MULTIPLIER_MS
        self.offset = (self.offset + num_pixels_offset) % len(self.colors)

        # Update pixels
        for i in range(self.length):
            self.data[i] = self.colors[(self.offset + i) % len(self.colors)]

        # Update last time
        self.last_t = t

# Default mode is off
def get_default_mode(length):
    return LEDMode_Solid(length, [ '#000000' ])



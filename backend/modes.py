
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

# Solid mode: maintains a constant color on the strip
class LEDMode_Solid(LEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, color):
        super().__init__(length)
        self.color = color
        self.data = []
        for i in range(self.length):
            self.data.append(color)

    def getData(self, t):
        return self.data # solid color is independent of time

# Alternating mode: alternates between two colors
class LEDMode_Alternating(LEDMode):
    # color as string '#RRGGBB'
    def __init__(self, length, color1, color2):
        super().__init__(length)
        self.color1 = color1
        self.color2 = color2
        self.data = []
        for i in range(self.length / 2):
            self.data.append(color1)
            self.data.append(color2)

    def getData(self, t):
        return self.data


# Default mode is off
def get_default_mode(length):
    return LEDMode_Solid(length, '#000000')

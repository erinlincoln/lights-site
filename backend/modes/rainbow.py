from modes.basic_modes import LEDMode

# THIS FILE IS DEPRECATED AS DEVICES RUN MOST DYNAMIC MODES LOCALLY

# generates rgb color from hsv data
# h is hue between 0-360 degrees
# s is saturation betwen 0-1
# v is value betwen 0-1
def hsv_to_rgb(h, s, v):
    c = v*s
    x = c*(1 - abs((h/60) % 2 - 1))
    m = v - c
    Rp, Gp, Bp = (0, 0, 0)
    if h < 60:
        (Rp, Gp, Bp) = (c, x, 0)
    elif h < 120:
        (Rp, Gp, Bp) = (x, c, 0)
    elif h < 180:
        (Rp, Gp, Bp) = (0, c, x)
    elif h < 240:
        (Rp, Gp, Bp) = (0, x, c)
    elif h < 300:
        (Rp, Gp, Bp) = (x, 0, c)
    else:
        (Rp, Gp, Bp) = (c, 0, x)
    R = int((Rp + m) * 255) % 255
    G = int((Gp + m) * 255) % 255
    B = int((Bp + m) * 255) % 255
    return (R, G, B)

class LEDMode_Rainbow(LEDMode):

    # Parameter affecting kax speed of rainbow
    # A speed of 1 will rotate rainbow every SPEED_MULTIPLIER_MS ms.
    SPEED_MULTIPLIER_MS = 500 # units ms

    def get_rainbow(self, index):
        hue = (((self.offset + index) % self.length) / self.length) * 360
        (R, G, B) = hsv_to_rgb(hue, 1, 1)
        return self.rgbToColor(R, G, B)  

    def __init__(self, length, speed):
        super().__init__(length)
        self.speed = speed
        self.offset = 0

        # initial values
        for i in range(self.length):
            self.data[i] = self.get_rainbow(i)

    def progress(self, t):
        # Calculate change in time
        delta_t = t - self.last_t

        # Calculate offset
        num_pixels_offset = int(delta_t * self.speed * self.length / self.SPEED_MULTIPLIER_MS)
        self.offset = (self.offset + num_pixels_offset) % self.length

        # Update pixels
        for i in range(self.length):
            self.data[i] = self.get_rainbow(i)

        # Update last time
        self.last_t = t

        # Require strip update
        return True


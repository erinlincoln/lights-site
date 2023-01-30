from modes.basic_modes import LEDMode
from random import randint, normalvariate

# THIS FILE IS DEPRECATED AS DEVICES RUN MOST DYNAMIC MODES LOCALLY

class Twinkle:
    def __init__(self, lifespan, power):
        self.lifespan = lifespan    # time (in ms) that the twinkle will last
        self.power = power          # 0-1 brightness of twinkle
        self.stage = 0              # 0-1, current life stage

        if self.power < 0: self.power = 0
        if self.power > 1: self.power = 1

    # Twinkle function:
    #       4(2x)^3     x < 0.7
    #       -(2x-2)^3   x > 0.7
    # Max at 1, min at 0
    def twinkle(self):
        x = self.stage
        if x < 0.7:
            return max(0, min(1, 4*(2*x)**3))
        return max(0, min(1, -(2*x-2)**3))

    # Updates the twinkle, returns the new strength 0-1
    def update_strength(self, delta_t):
        self.stage = delta_t / self.lifespan + self.stage

        if self.stage < 0 or self.stage >= 1:
            return 0

        return self.twinkle()
        

class LEDMode_Twinkle(LEDMode):

    # Parameter affecting frequency of twinkle generation
    # A speed of 1 will cause an average of FREQUENCY_MULTIPLIER twinkles to generate every ms
    FREQUENCY_MULTIPLIER = 0.1

    # The standard distribution of twinkle generation count in twinkles / ms
    TWINKLE_GEN_STDEV = 0.5 # TODO Check this

    # The max and min ranges of twinkle generation. Setting these the same will remove randomness of generation.
    TWINKLE_GEN_MAX = 20
    TWINKLE_GEN_MIN = 0

    # Parameters affecting lifespan of twinkle
    # average lifespan in ms = SPEED_MULTIPLIER * speed + SPEED_MIN
    SPEED_MIN = 100
    SPEED_MAX = 1000
    SPEED_MULTIPLIER = SPEED_MAX - SPEED_MIN

    # The standard deviation of the lifespan of twinkles in ms
    SPEED_STDEV = 200

    # The power of twinkles
    POWER_STDEV = 0.3

    def __init__(self, length, colors, speed, frequency):
        super().__init__(length)

        if speed == None: speed = 0.5
        if frequency == None: frequency = 0.5

        (self.r, self.g, self.b) = self.colorToRGB(colors[0])
        self.speed = speed
        self.frequency = frequency

        self.twinkles = [None] * self.length

    def update_twinkles(self, delta_t):
        # Iterate over each twinkle, updating and removing finished twinkles
        for i in range(self.length):
            if self.twinkles[i] != None:
                # update twinkles
                strength = self.twinkles[i].update_strength(delta_t)
                # update data
                result_color = self.rgbToColor(int(self.r * strength), int(self.g * strength), int(self.b * strength))
                self.data[i] = result_color
                # cleanup
                if strength <= 0:
                    self.twinkles[i] = None

    def generate_new_twinkles(self, delta_t):
        # number of new twinkles to generate depends on delta_t and frequency
        avg_num_twinkles = self.frequency * self.FREQUENCY_MULTIPLIER * delta_t
        
        # use a normal distribution to generate a different number each time
        num_twinkles = normalvariate(avg_num_twinkles, self.TWINKLE_GEN_STDEV)
        num_twinkles = min(self.TWINKLE_GEN_MAX, num_twinkles)
        num_twinkles = int(max(self.TWINKLE_GEN_MIN, num_twinkles))

        avg_lifespan = self.SPEED_MULTIPLIER * self.speed + self.SPEED_MIN

        # randomly generate twinkles. Existing twinkles will not be overridden.
        for i in range(num_twinkles):
            # generate location
            loc = randint(0, self.length-1)
            # generate lifespan
            lifespan = normalvariate(avg_lifespan, self.SPEED_STDEV)
            # generate power
            power = normalvariate(0.5, self.POWER_STDEV)
            if self.twinkles[loc] == None:
                self.twinkles[loc] = Twinkle(lifespan, power)

    def progress(self, t):
        # Calculate change in time
        delta_t = t - self.last_t

        # Update existing twinkles
        self.update_twinkles(delta_t)

        # Generate new twinkles
        self.generate_new_twinkles(delta_t)

        # Update last time
        self.last_t = t

        return True
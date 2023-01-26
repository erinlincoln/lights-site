from modes.basic_modes import LEDMode

# Instructions for making another mode on the backend
#
#   1) Implement your class in a new file (use this one as a template) within the
#      modes subdirectory (where this file is), extending modes.basic_modes.LEDMode
#
#   2) Implement __init__ within the class, passing the strip length to 
#      super().__init__(length) and saving all other relevant data
#
#   3) If the mode is dynamic (changes over time), override progress(self, t) where
#      t is a timestamp in ms since epoch. Ensure this function returns True so the
#      backend continuously updates the mode
#
#   4) Add the mode to create_mode.py so that it can be created. This involves
#      importing the class at the top and adding an entry to the switch statement.
#      Make sure to error-check all values of mode_json["data"].
#

# Here is the basic class template for a new LED mode
class LEDMode_Custom(LEDMode):

    # TODO Define any constants here
    # SPEED_MULTIPLIER_MS = 1000 # units ms

    def __init__(self, length, other_parameters_here):
        super().__init__(length)

        # TODO Add other initialization here
        self.other_parameters_here = other_parameters_here
    
    # You only need this function if the mode is dynamic, otherwise remove it
    def progress(self, t):
        # Calculate change in time
        delta_t = t - self.last_t

        # TODO Do dynamic calculations here

        # Update last time
        self.last_t = t

        # Require strip update
        return True

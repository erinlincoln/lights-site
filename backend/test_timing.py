from modes.basic_modes import *
from modes.twinkle import LEDMode_Twinkle

import time

# Quickly enable/disable timing analysis
PRINT_ENABLED = False
PRINT_ENABLED_NAMES = [
    #"SetLights()",
    #"SendData()",
    #"Queue Sem.",
    #"Strip Upd."
]

# A class to test timing in the backend. Probably don't want this in the final code
class TimingTester:
    def __init__(self, name="TT"):
        self.num_measurements = 0
        self.sum = 0
        self.running = False
        self.start_time = 0
        self.name = name

    def start(self):
        self.running = True
        self.start_time = time.time() * 1000
        return self.start_time
    
    def stop(self):
        self.sum += time.time() * 1000 - self.start_time
        self.num_measurements += 1

        if not self.running:
            print("Timing Tester Error: Stop before Start")
            return -1

        self.running = False

        return self.sum / self.num_measurements

    def get_result(self):
        return self.sum / self.num_measurements

    def get_num_measurements(self):
        return self.num_measurements
    
    def print(self):
        if PRINT_ENABLED and self.name in PRINT_ENABLED_NAMES:
            print("TT ", self.name, " : ", self.get_result(), "\t CNT: ", self.get_num_measurements())
        

# Use this area to test and document function timing results
#   FUNCTION                    EXEC TIME           DATE        NOTES
#   LEDMode_Twinkle.progress    0.01 ms             1/25/23     

if __name__ == "__main__":
    COUNT = 1000

    mode = LEDMode_Twinkle(100, ["#ffffff"], 0.5, 0.5)

    tt = TimingTester()
    for i in range(COUNT):
        start = tt.start()

        mode.progress(start)

        end = time.time() * 1000
        tt.stop()

    print("Average runtime: ", tt.get_result(), " ms")
    
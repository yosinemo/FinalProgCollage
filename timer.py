import time
import threading
import os
from GameSetup import *
class Timer(threading.Thread):
    def __init__(self):
        self.GameSetup = GameSetup()
        self.SETUP_VARS = self.GameSetup.get_SetupValues()
        self.StratTimeSec = 5
        threading.Thread.__init__(self)

    def run(self):
        while self.StratTimeSec >= -1:
            self.StratTimeSec -= 1
            if self.StratTimeSec == -1:
                self.StratTimeSec = 5

            time.sleep(1)

    def Reset(self):
        self.StratTimeSec = 5



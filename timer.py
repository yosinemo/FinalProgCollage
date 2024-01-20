import time
import threading
import os
from GameSetup import *
class Timer(threading.Thread):
    def __init__(self):
        self.GameSetup = GameSetup()
        self.SETUP_VARS = self.GameSetup.get_SetupValues()
        self.StratTimeSec:int = 5
        self.OneSecFlag:bool = False
        threading.Thread.__init__(self)

    def run(self):
        while self.StratTimeSec >= -1:
            self.OneSecFlag = True
            time.sleep(1e-10)
            self.StratTimeSec -= 1
            if self.StratTimeSec == -1:
                self.StratTimeSec = 5

            self.OneSecFlag = False

            time.sleep(1)

    def Reset(self):
        self.StratTimeSec = 5



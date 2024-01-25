import threading
import time
from Interrupts import *
class Interrupts(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0
        self.stop_flag = False
        self.file_path_Timer = "C:\\Users\\ymamo\\PycharmProjects\\final_proj\\files\\timer.txt"
        self.file_path_OneSecTimer = "C:\\Users\\ymamo\\PycharmProjects\\final_proj\\files\\onesectimer.txt"

    def Timer(self):
        while not self.stop_flag:
            time.sleep(1)
            if self.i == 6:
                self.i = 0
            with open(self.file_path_Timer, "w") as file:
                file.write(f"{self.i}")
                self.i+=1

    def stop(self):
        self.stop_flag = True

    def ResetTimer(self):
        with open(self.file_path_Timer, "w") as file:
            file.write("0")
            self.i = 0



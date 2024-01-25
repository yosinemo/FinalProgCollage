import time

import numpy as np
import cv2
import re
from util import *
from shapes import *
from Interrupts import *

class games:
    def __init__(self):
        self.util = utils()
        self.shape = shapes()
        self.loc = ["up", "down", "left", "right"]
        self.col = ["Green", "Yellow"]
        self.simloc = ["RU","LU","LD","RD"]
        self.simplay = []
        self.simplay.append(self.simloc[random.randint(0, 3)])
        self.i = 0
        self.score = 0
        self.c = self.col[random.randint(0, 1)]
        self.interrupts_thread = Interrupts()
        thread1 = threading.Thread(target=self.interrupts_thread.Timer)
        self.interrupts_thread.ResetTimer()
        thread1.start()
        self.file_path_Timer = "C:\\Users\\ymamo\\PycharmProjects\\final_proj\\files\\timer.txt"
        self.time_up = False
        self.inside = False
        self.counter = 0
        self.no_object_on_screen = False
        self.nextlevel = True

    def Oded_Amar(self,imageFrame,axis_x = 180,axis_y = 120):
        with open(self.file_path_Timer, "r") as file:
            time = file.read()
        color = self.util.ColorDataBase(self.c)["paint"]
        if self.i < 4:
            self.util.locatin_text(f"please go {self.loc[self.i]}", axis_x, axis_y, imageFrame, color)
        if time == "5":
            self.interrupts_thread.ResetTimer()
            self.c = self.col[random.randint(0, 1)]
            self.i = random.randint(0, 3)
            self.score -= 1

        self.util.locatin_text(f"Time = {time}, Score = {self.score}", axis_x, 200, imageFrame, color)

        contours= self.util.get_ContursandHirarchy(np.array(self.util.ColorDataBase(self.c)["up"]),
                                                          np.array(self.util.ColorDataBase(self.c)["low"]), imageFrame)
        for contour in contours:
            area = cv2.contourArea(contour)
            if (area > 1000):
                center = self.util.get_ObjectCenter(contour)
                cv2.circle(imageFrame,center , 1, color, 2)
                location = self.util.get_location(center[0],center[1])
                if self.score == 10:
                    return True
                if self.i > 3:
                    self.i = self.col[random.randint(0, 3)]
                if self.loc[self.i] == location:
                    self.interrupts_thread.ResetTimer()
                    self.c = self.col[random.randint(0, 1)]
                    self.i = random.randint(0, 3)
                    self.score += 1

    def GoTo(self,imageFrame,axis_x = 180,axis_y = 120):
        with open(self.file_path_Timer, "r") as file:
            time = file.read()
        color = self.util.ColorDataBase(self.c)["paint"]
        self.util.get_ColorTraker(np.array(self.util.ColorDataBase(self.c)["up"]),
                                  np.array(self.util.ColorDataBase(self.c)["low"]), imageFrame,
                                  color=color)
        self.util.locatin_text(f"color = {self.c}", axis_x, axis_y, imageFrame, color)
        self.util.locatin_text(f"Time = {time}, Score = {self.score}", axis_x, 200, imageFrame, color)
        contours= self.util.get_ContursandHirarchy(np.array(self.util.ColorDataBase(self.c)["up"]),
                                                               np.array(self.util.ColorDataBase(self.c)["low"]),
                                                               imageFrame)
        arr = self.util.set_MakeShapeScreen(imageFrame, flag=0)
        if time == "5":
            self.interrupts_thread.ResetTimer()
            self.c = self.col[random.randint(0, 1)]
            self.util.set_MakeShapeScreen(imageFrame, flag=1)
            self.score -= 1
        for contour in contours:
            area = cv2.contourArea(contour)
            if (area > 1000):
                center = self.util.get_ObjectCenter(contour)
                xmid = center[0]
                ymid = center[1]

                if self.score == 10:
                    return True
                l = len(arr)
                if l == 3:
                    pos = self.shape.get_PointCircle(xmid, ymid, arr[0], arr[1], arr[2])
                elif l == 6:
                    pos = self.shape.get_PointTriangle(xmid, ymid, arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
                elif l == 4:
                    pos = self.shape.get_PointRectangle(xmid, ymid, arr[0], arr[1], arr[2], arr[3])
                # print(pos)
                if pos == "Inside":
                    self.interrupts_thread.ResetTimer()
                    self.c = self.col[random.randint(0, 1)]
                    self.util.set_MakeShapeScreen(imageFrame, flag=1)
                    self.score +=1

    def Simon(self,imageFrame,axis_x = 180,axis_y = 120):
        with open(self.file_path_Timer, "r") as file:
            time = file.read()
        self.util.DrawMTRectinles(imageFrame)
        color = self.util.ColorDataBase("Green")["paint"]
        self.util.get_ColorTraker(np.array(self.util.ColorDataBase("Green")["up"]),
                                  np.array(self.util.ColorDataBase("Green")["low"]), imageFrame,
                                  color=color)

        contours= self.util.get_ContursandHirarchy(np.array(self.util.ColorDataBase("Green")["up"]),
                                                               np.array(self.util.ColorDataBase("Green")["low"]),
                                                               imageFrame)

        if self.nextlevel:
            try:
                if time > "1" and time < "5":
                    cv2.rectangle(imageFrame, self.shape.get_MTRectingle(f"{self.simplay[self.i]}")["start"],
                                  self.shape.get_MTRectingle(f"{self.simplay[self.i]}")["end"],
                                  self.util.ColorDataBase("Green")["paint"], -1)
                if time == "5":
                    self.interrupts_thread.ResetTimer()
                    self.i += 1

            except:
                self.i = 0
                self.nextlevel = False

        else:
            for pic, contour in enumerate(contours):
                if pic != 0:
                    self.counter =0
                else:
                    self.counter +=1
                if self.counter == 4:
                    self.no_object_on_screen = True
                else:
                    self.no_object_on_screen = False
                area = cv2.contourArea(contour)
                if (area > 1000):
                    *_, radius = cv2.minEnclosingCircle(contour)
                    x, y, w, h = cv2.boundingRect(contour)
                    center = [int(x + radius - 3), int(y + radius - 3)]
                    xmid = center[0]
                    ymid = center[1]

                    placeMTRectingle = f"MT_{self.simplay[self.i]}"
                    palceFullRectingle = f"{self.simplay[self.i]}"
                    # print(palceFullRectingle)
                    p00 = self.shape.get_MTRectingle(placeMTRectingle)["start"][0]
                    p01 = self.shape.get_MTRectingle(placeMTRectingle)["start"][1]
                    p10 = self.shape.get_MTRectingle(placeMTRectingle)["end"][0]
                    p11 = self.shape.get_MTRectingle(placeMTRectingle)["end"][1]
                    if palceFullRectingle == "RU" or palceFullRectingle == "LD":
                        pos = self.shape.get_PointRectangle(xmid, ymid,p10,p11 , p00, p01)
                    else:
                        pos = self.shape.get_PointRectangle(xmid, ymid, p10, p01,p00, p11)
                    if pos == "Inside":
                        cv2.rectangle(imageFrame, self.shape.get_MTRectingle(palceFullRectingle)["start"],
                                      self.shape.get_MTRectingle(palceFullRectingle)["end"],
                                      self.util.ColorDataBase("Red")["paint"], -1)
                        try:
                            # print("TRYYYY")
                            self.i+=1
                            self.simplay[self.i]
                        except:
                            # print("CATCHHHHH")
                            self.i = 0
                            self.simplay.append(self.simloc[random.randint(0, 3)])
                            self.nextlevel = True





    def Reset(self,i = random.randint(0, 3),c = random.randint(0, 1),score = 0,time_up=False):
        self.i = i
        self.c = self.col[c]
        self.score = score
        self.time_up = time_up
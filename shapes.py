import math
import random
import time
from GameSetup import *

class shapes:
    def __init__(self):
        self.GameSetup = GameSetup()
        # self.GameSetup.PrintAllSETUP_VARS()
        self.SETUP_VARS = self.GameSetup.get_SetupValues()
        self.random_number = 3
        self.x = self.SETUP_VARS["XMID"]
        self.y = self.SETUP_VARS["YMID"]

    def get_PointCircle(self, x, y, center_x, center_y, radius):
        distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        if distance < radius:
            return "Inside"
        else:
            return "Outside"

    def get_PointRectangle(self,x, y, x1, y1, x2, y2):
        if x2 <= x <= x1 and y1 <= y <= y2:
            return "Inside"
        else:
            return "Outside"

    def get_PointTriangle(self,x, y, x1, y1, x2, y2, x3, y3):
        a = self.distance(x1,x2,y1,y2)
        b = self.distance(x1,x3,y1,y3)
        c = self.distance(x3,x2,y3,y2)
        a1 = self.distance(x1,x,y1,y)
        b1 = self.distance(x,x2,y,y2)
        c1 = self.distance(x3,x,y3,y)
        area1 = abs(0.5 * (a + self.get_high(a1,self.get_Teta(b1,a,a1)))) #(b**2 + c**2 -a**2)/(2*b*c)
        area2 = abs(0.5 * (b + self.get_high(a1,self.get_Teta(c1,b,a1))))
        area3 = abs(0.5 * (c + self.get_high(a1,self.get_Teta(b1,c,c1))))
        area_total = 0.5 * (-y2 * x3 + y1 * (-x2 + x3) + x1 * (y2 - y3) + x2 * y3)
        if 0 < (area_total - (area1 + area2 + area3)) < 100 :
            return "Inside"
        else:
            return "Outside"

    def distance(self,x,x1,y,y1):
        return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

    def get_Teta(self,a,b,c):
        # print(a,b,c)
        value = (b**2 + c**2 -a**2)/(2*b*c)
        if int(value) == -1:
            pass
        else:
            teta = math.degrees(math.acos(value))
            return teta

    def get_high(self,a,teta):
        # print(math.degrees(math.sin(teta)) * a)
        return math.degrees(math.sin(teta)) * a

    def get_RandomShape(self,flag = 0):
        if flag == 1:
            self.random_number = random.randint(1, 100)
        if self.random_number % 4 == 0:
            return 4
        elif self.random_number % 3 == 0:
            return 3
        else:
            return 1

    def get_CenterPoint(self,flag = 0):
        if flag == 1:
            self.x = random.randint(10, self.SETUP_VARS["XRES"])
            self.y = random.randint(10, self.SETUP_VARS["YRES"])
        return self.x,self.y

    def set_RandomShape(self,flag = 0):
        x,y = self.get_CenterPoint(flag)
        if self.get_RandomShape(flag) == 1:
            r = 40
            return [x, y, r]

        elif self.get_RandomShape(flag) == 3:
            tringle = [0,0,0,0,0,0]
            scalar = 30
            tringle[0] = x
            tringle[1] = y + scalar
            tringle[2] = x - scalar
            tringle[3] = y - scalar
            tringle[4] = x + scalar
            tringle[5] = y - scalar
            return tringle

        elif self.get_RandomShape(flag) == 4:
            rectringle = [0, 0, 0, 0]
            scalar = 30
            rectringle[0] = x + scalar
            rectringle[1] = y - scalar
            rectringle[2] = x - scalar
            rectringle[3] = y + scalar
            return  rectringle


    def get_MTRectingle(self, rectingle,thick=5):
        RECTINGLE = {   "MT_LU": {'start': (0,0), 'end': (160,115), "color": (0, 0, 0),},
                        "MT_RU": {'start': (480,115), 'end': (640,0), "color": (0, 0, 0)},
                        "MT_LD": {'start': (0, 480), 'end': (160, 345), "color": (0, 0, 0)},
                        "MT_RD": {'start': (480, 345), 'end': (640,480 ), "color": (0, 0, 0)},
                        "LU": {'start': (0+thick, 0+thick), 'end': (160-thick, 115-thick), "color": (0, 0, 0)},
                        "RU": {'start': (480+thick, 115+thick), 'end': (640-thick, 0-thick), "color": (0, 0, 0)},
                        "LD": {'start': (0+thick, 480+thick), 'end': (160-thick, 345-thick), "color": (0, 0, 0)},
                        "RD": {'start': (480+thick, 345+thick), 'end': (640-thick, 480-thick), "color": (0, 0, 0)}}

        return RECTINGLE[rectingle]
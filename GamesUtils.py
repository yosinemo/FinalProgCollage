# import time
# import numpy as np
# import cv2
# import re
# from util import *
# from shapes import *
# from Interrupts import *
# from MainDynGui import *
# from timer import *
#
#
# class GameEngine:
#     def __init__(self):
#         self.util = utils()
#         self.shape = shapes()
#         # self.Timer = Timer()  ## only if the i define the timer here its works, in th
#         # self.Timer.start()  ## GameSetup class i enter in envry iteration when i call in the GameStart function (go to the constaractor)
#         self.FileLocation = f"C:\\Users\\ymamo\\PycharmProjects\\final_proj\\files\\timer.txt"
#         self.ArrayColors = ["Green", "Yellow"]
#         self.ArrayLocations = ["up", "down", "left", "right"]
#         self.CurrentColor = "Green"
#         self.CurrentLocation = "up"
#         self.CurrntUpperRange = np.array(self.util.ColorDataBase(self.CurrentColor)["up"])
#         self.CurrentLowerRange = np.array(self.util.ColorDataBase(self.CurrentColor)["low"])
#         self.CurrentPaintColor = self.util.ColorDataBase(self.CurrentColor)["paint"]
#         self.CurrentScore = 0
#
#     def GameStart(self,GameSetup):
#         pass
#
#     # def TimerReset(self):
#     #     self.Timer.Reset()
#
#     def ResetGame(self):
#         self.CurrentScore = 0
#         self.set_RandomColor()
#         self.set_RandomLocation()
#
#     def GameEnd(self):
#         if self.CurrentScore == 10:
#             return True
#         else:
#             return False
#
#     # def CurrentTime(self):
#     #     with open(self.FileLocation, "r") as file:
#     #         print(file.read())
#     #         return file.read()
#
#
#
#     # def LocationTextOnImage(self, text:str,axis_x = 180,axis_y = 120):
#     #     self.axis_x = axis_x
#     #     self.axis_y = axis_y
#     #     _,_,color = self.get_CurrentUpperLowwerColorRange()
#     #     self.util.locatin_text(text, self.axis_x, self.axis_y, self.get_CurrentIamge(), color)
#
#     def set_RandomColor(self):
#         self.CurrentColor = self.ArrayColors[random.randint(0, 1)]
#
#
#     def set_RandomLocation(self):
#         self.CurrentLocation = self.ArrayLocations[random.randint(0, 3)]
#
#
#     def set_UpperLowwerColorRange(self,flag = False):
#         if flag:
#             self.set_RandomColor()
#
#         self.CurrntUpperRange = np.array(self.util.ColorDataBase(self.get_CurrentColor())["up"])
#         self.CurrentLowerRange = np.array(self.util.ColorDataBase(self.get_CurrentColor())["low"])
#         self.CurrentPaintColor = self.util.ColorDataBase(self.get_CurrentColor())["paint"]
#
#
#
#
#     def set_UpPoint(self):
#         self.CurrentScore +=1
#
#     def set_DownPoint(self):
#         self.CurrentScore -=1
#
#     def get_CurrentScore(self):
#         return self.CurrentScore
#
#     def get_CurrentIamge(self):
#         return self.imageFrame
#
#     def get_CurrentUpperLowwerColorRange(self):
#         return self.CurrntUpperRange, self.CurrentLowerRange, self.CurrentPaintColor
#
#     def get_CurrentColor(self):
#         return self.CurrentColor
#
#     def get_CurrentLocation(self):
#         return self.CurrentLocation
#
#
#
#
#
# class OdedAmar(GameEngine):
#
#     def __init__(self):
#         super().__init__()
#         self.Timer = Timer()
#         self.Timer.start()
#         self.FileLocation = f"C:\\Users\\ymamo\\PycharmProjects\\final_proj\\files\\timer.txt"
#
#     def GameStart(self,GameSetup):
#         with open(self.FileLocation, "r") as file:
#             print(file.read())
#             return file.read()
#         location = self.get_CurrentLocation()
#         image = GameSetup.get_CurrentIamge()
#         up, low, color = self.get_CurrentUpperLowwerColorRange()
#         score = self.get_CurrentScore()
#         time  = self.CurrentTime()
#
#         if time == "0":
#                 self.set_RandomColor()
#                 self.set_DownPoint()
#                 # self.TimerReset()
#
#
#
#         if self.GameEnd():
#             return True
#
#         # if GameUtils.GameManeger.SelectGame() == 1:
#         #     GameUtils.ResetGame(self)
#
#
#         GameSetup.LocationTextOnImage(text = f"please go {location}",axis_x = 180,axis_y = 50)
#
#         GameSetup.LocationTextOnImage(f"Time = {time}, Score = {score}")
#
#         contours = self.util.get_ContursandHirarchy(up,low, image)
#         for contour in contours:
#             area = cv2.contourArea(contour)
#             if (area > 1000):
#                 center = self.util.get_ObjectCenter(contour)
#                 # center = GameUtils.get_CurrentObjectCenter()
#                 cv2.circle(image, center, 1, color, 2)
#                 WereAMI = self.util.get_location(center[0],center[1])
#                 if location == WereAMI:
#                     self.set_UpPoint()
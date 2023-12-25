import numpy

from timer import Timer
import random
from util import *
import numpy as np
import cv2 as cv
from GameSetup import *
from shapes import shapes
from MainDynGui import MainDynGUI

##using type hints can help catch errors early in development, improve code readability, and provide better documentation, but it doesn't affect the runtime performance of the Python code

class GameEngine(Timer):## the gamengine is where all the game are mades,the class is inheritet from Timer
                        ## to solve the time reading to be from variable and not from file
    def __init__(self): ## init mehode
        super().__init__() ## read first all the var anf func members from Timer
        super().start() ## start thr timer
        super().Reset() ## reset thr timer
        self.GameSetup = GameSetup() ## call GameSetup class
        self.ShapeUtils = shapes() ##v call shape class
        # self.GameSetup.PrintAllSETUP_VARS()
        self.SETUP_VARS = self.GameSetup.get_SetupValues() ## get all setup values
        self.GameSetup.SearchLastGameDataFile() ## search the last file data ( in the gamesetup class is search one time only)
        self.GameDataFile = self.SETUP_VARS["GameDataFile"] ## get the game dta location in computer
        ## get the mid-screen point
        self.Xdot:int = self.SETUP_VARS["XMID"]
        self.Ydot:int = self.SETUP_VARS["YMID"]
        self.AllCenterDotArray = []
        self.CenterDot:tuple[int,int] = (self.Xdot,self.Ydot)
        self.ColorUtils = utils() ## call color utilts class
        self.GameAttempt:int = 0 ## num of attemptes of player
        self.GameName:str = "No Game"
        self.ArrayColors:list[str] = ["Green", "Blue"] ## color array
        self.ArrayLocations:list[str] = ["up", "down", "left", "right"] ## location array
        self.set_UpperLowwerColorRange(True) ## setting UpperLowwerColorRange
        self.ResetScore() ## reset score
        self.ResetStoper() ## reaset stopper
        self.flag:bool = False
        self.flag1:bool = False


    def GAME_ACTIONS(self,Mode:int,GameName:str) -> 'makes decisions about the continuation of the game':
        self.ResetTime()
        if Mode == 0: ## 0 will reset the score
            self.ResetScore()
        elif Mode == 1:
            self.CurrentScore +=1 ## POINT UP
            self.CREATE_RESULTE_FILE("SUCCESS",GameName) ##write to file
        elif Mode == 2:
            self.CurrentScore -=1 ## POINT DOWN
            self.CREATE_RESULTE_FILE("FAILED",GameName) ## write to file

        self.ResetStoper() ## reset stopper every time the user failed or successed

        if GameName == "ODED AMAR": ## if the game ODED AMAR need to choose new color and location when user finish task
            self.set_UpperLowwerColorRange(True)
        elif GameName == "GO-TO": ## ## if the GoTo need to choose new color,location and make new shape on screen after user finosh task
            self.set_UpperLowwerColorRange(True)
            self.ColorUtils.set_MakeShapeScreen(self.image,self.CurrentPaintColor, flag=1)
        elif GameName == "SIMON":## if the game is SIMON ....
            self.set_NewCenterPoint()

    def START_GAME(self,GameName:str)-> 'opperate when game start':
        if self.GameName != GameName: ## if the game name is diff from the new one make new action according to the game name
            self.GameName = GameName ## save the game name for the next time
            self.GAME_ACTIONS(0,GameName)
        else:
            self.StartStoper()## if it the same game start the timer (inc by 1)


    def END_GAME(self)-> 'end game when user get scire 10 return bool':
        if self.CurrentScore == 10:
            return True
        return False

    def END_TIME(self,GameName:str)-> 'check if time end':
        Time = self.get_CurrentTime() ## get the current time
        if Time == -1: ## if the var is equ to -1 it endd of time
            self.flag = True ## turn flag on
            super().Reset() ## reset timer
        if self.flag and Time == 5: ## only is flag and time are true make game action
                                    ## if i didnt have the flag it can lead that it can enter to game action when ever the function wants
            self.GAME_ACTIONS(2, GameName)
            self.flag = False


    def WIN_GAME(self,x:int,y:int,GameName:str)-> 'check if the user win':
        if GameName == "ODED AMAR":
            WereAMI = self.ColorUtils.get_location(x, y) ## get the location of the user
            if self.get_Currentlocation() == WereAMI: ## comper the location to the location he need to be
                self.GAME_ACTIONS(1,"ODED AMAR")      ## if he succeed make game action
        if GameName == "GO-TO":
            if self.get_INSIDEorOUTSIDE(x,y) == "Inside": ## comper if the user inside or outside the eara
                self.GAME_ACTIONS(1,"GO-TO")              ## if succeed make game action
        if GameName == "SIMON":
            pass




    def CREATE_GAME_DATA_FILE(self)-> 'create a file every stating new game give time and date':
        date= self.SETUP_VARS["DATE"]
        time = self.SETUP_VARS["TIME"]
        try: ## try to make new file
            with open(self.GameDataFile, 'w') as file: ## open new file
                file.write(f"Game Data File {time} {date} \n") ## write the current time and date
        except Exception as e: ## in case the is an exeption
            print(f"Error: {e}") ## write the exetion

    def GameStart(self,CurentCaptureImage: numpy.ndarray,GameName: str)-> 'this func change in every class game':
        pass



    def CREATE_RESULTE_FILE(self,SuccessOrFiled:str,GameName:str)-> 'write to the file data the user attempet info':
        with open(self.GameDataFile, "a") as file:
            if GameName == "ODED AMAR":
                file.write(f"Action = {self.get_CurrentColor()},{self.get_Currentlocation()}.\n")
            if GameName == "GO-TO":
                file.write(f"Action = {self.get_CurrentColor()},{self.get_Shape()}.\n")
            file.write(f"{GameName} {self.GameAttempt} {SuccessOrFiled} {self.get_CurrentStoper()}.\n")
        self.GameAttempt +=1

    # def AddActiontoDataFile(self,GameName):
    #     Time = self.get_CurrentTime()
    #     if Time == 5:
    #         self.flag1 = True
    #     if self.flag1 and Time == 4:
    #         with open(self.GameDataFile, "a") as file:
    #             if GameName == "ODED AMAR":
    #                 file.write(f"Action = {self.get_CurrentColor()},{self.get_Currentlocation()}.\n")
    #             if GameName == "GO-TO":
    #                 file.write(f"Action = {self.get_CurrentColor()},{self.get_Shape()}.\n")
    #         self.flag1 = False

    def TextOnScreen(self,text:str)-> 'write text':
        Time = self.get_CurrentTime()
        Score = self.get_CurrentScore()
        Stoper = self.get_CurrentStoper()

        x = self.SETUP_VARS["XTEXT"]
        y = self.SETUP_VARS["YTEXT"]
        self.ColorUtils.locatin_text(f"Time = {Time}, Score = {Score} , Stoper = {Stoper}", x, y,self.image, (0,0,0))
        X = self.SETUP_VARS["XTEXTCOLOR"]
        Y = self.SETUP_VARS["YTEXTCOLOR"]
        _,_,color = self.get_UpperLowwerColorRange()
        if self.get_CurrentTime() != "0":
            self.ColorUtils.locatin_text(text, X, Y, self.image, color)
        if self.END_GAME():
            Xmid = self.SETUP_VARS["XMID"]
            Ymid = self.SETUP_VARS["YMID"]
            self.ColorUtils.locatin_text(f"Game End Good For YOU!!!!!!", Xmid, Ymid, self.image, (0,0,0))

    def StartStoper(self):
        self.CurrentStoper +=1



######### ALL RESETS ########
    def ResetTime(self):
        super().Reset()

    def ResetScore(self):
        self.CurrentScore = 0

    def ResetStoper(self):
        self.CurrentStoper = 0

######## ALL SETES #######################3

    def set_RandomColor(self,flag:bool = False)-> 'change var member to current color':
        if flag:
            self.CurrentColor = self.ArrayColors[random.randint(0, 1)]

    def set_NewCenterPoint(self)-> '':
        self.Xdot, self.Ydot = self.ShapeUtils.get_CenterPoint(flag=1)
        Xsmall = abs(self.Xdot - self.CenterDot[0]) < 300
        Xhigh = abs(self.Xdot - self.CenterDot[0]) > 300
        Ysmall = abs(self.Ydot - self.CenterDot[1]) < 300
        Yhigh = abs(self.Ydot - self.CenterDot[1]) > 300
        if (Xhigh and Yhigh) or (Xhigh and Ysmall) or (Xsmall and Yhigh) or (Xsmall and Ysmall):
            self.CenterDot = [self.Xdot, self.Ydot]
            self.AllCenterDotArray.append(np.array(self.CenterDot, dtype=np.int32))

    def set_UpperLowwerColorRange(self,flag = False):
        if flag:
            self.set_RandomColor(flag) ## choose rand color
            self.set_RandomLocation(flag) ## choose rand location
        self.CurentLowwerColorRange = np.array(self.ColorUtils.ColorDataBase(self.CurrentColor)["low"]) ## make low range color
        self.CurrentUpperColorRange = np.array(self.ColorUtils.ColorDataBase(self.CurrentColor)["up"]) ## make up range  color
        self.CurrentPaintColor      = self.ColorUtils.ColorDataBase(self.CurrentColor)["paint"] ## make paint color

    def set_RandomLocation(self,flag = False):
        if flag:
            self.CurrentLocation = self.ArrayLocations[random.randint(0,3)]

    def set_CaptureImage(self,image):
        self.image = image


################## ALL GETERS ####################
    def get_CurrentTime(self):
        # with open(self.Timer.get_FileLocation(), "r") as file:
        #     return file.read()
        return self.StratTimeSec

    # def get_RandomDotArray(self):
    #     Xdot, Ydot = self.ShapeUtils.get_CenterPoint(flag=1)
    #     center  = (Xdot,Ydot)
    #     CenterArray = []
    #     CenterArray[0] = center
    #     for i in range(1,10):
    #         Xdot, Ydot = self.ShapeUtils.get_CenterPoint(flag=1)
    #         if abs(Xdot - center[0]) > 300 and abs(Ydot - center[1]) > 300:
    #             center = (Xdot, Ydot)
    #             CenterArray[i] = center
    #     return CenterArray


    def get_CurrentStoper(self):
        return self.CurrentStoper

    def get_CurrentScore(self):
        return self.CurrentScore

    def get_ShapePoints(self):
         return self.ColorUtils.set_MakeShapeScreen(self.image,self.CurrentPaintColor ,flag=0)

    def get_Shape(self):
        l = len(self.get_ShapePoints())
        if l == 3:
            return "CIRCLE"
        elif l == 6:
            return "TRIANGLE"
        elif l == 4:
            return "RECTANGLE"

    def get_INSIDEorOUTSIDE(self,x,y):
        arr = self.get_ShapePoints()
        # pos = "outside"
        l = len(arr)
        if l == 3:
            pos = self.ShapeUtils.get_PointCircle(x, y, arr[0], arr[1], arr[2])
        elif l == 6:
            pos = self.ShapeUtils.get_PointTriangle(x, y, arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
        elif l == 4:
            pos = self.ShapeUtils.get_PointRectangle(x, y, arr[0], arr[1], arr[2], arr[3])

        return pos

    def get_CurrentColor(self):
        return self.CurrentColor

    def get_Currentlocation(self):
        return self.CurrentLocation

    def get_UpperLowwerColorRange(self):
        return self.CurentLowwerColorRange,self.CurrentUpperColorRange,self.CurrentPaintColor






class OdedAmar(GameEngine):
    def GameStart(self,CurentCaptureImage,GameName):
        ## GAME VALUES ####
        self.set_CaptureImage(CurentCaptureImage)
        Lowwer, Upper, Color = self.get_UpperLowwerColorRange()

        ### CREATE COTOURS AND PRINTS ###
        contours = self.ColorUtils.get_ContursandHirarchy(Upper, Lowwer, CurentCaptureImage)
        self.TextOnScreen(f"{self.get_CurrentColor()},{self.get_Currentlocation()}")

        self.START_GAME(GameName)
        self.END_TIME(GameName)

        for contour in contours:
            area = cv.contourArea(contour)
            if (area > 1000):
                center = self.ColorUtils.get_ObjectCenter(contour)
                cv.circle(CurentCaptureImage, center, 1, Color, 2)
                self.WIN_GAME(center[0],center[1],GameName)



class GoTo(GameEngine):
    def GameStart(self,CurentCaptureImage,GameName):
        ## GAME VALUES ####
        self.set_CaptureImage(CurentCaptureImage)
        Lowwer, Upper, Color = self.get_UpperLowwerColorRange()

        ### CREATE COTOURS AND PRINTS ###
        contours = self.ColorUtils.get_ContursandHirarchy(Upper, Lowwer, CurentCaptureImage)
        self.TextOnScreen(f"{self.get_CurrentColor()},{self.get_Shape()}")

        self.START_GAME(GameName)
        self.END_TIME(GameName)


        for contour in contours:
            area = cv.contourArea(contour)
            if (area > 1000):
                center = self.ColorUtils.get_ObjectCenter(contour)
                cv.circle(CurentCaptureImage, center, 1, Color, 2)
                self.WIN_GAME(center[0],center[1],GameName)

class SIMON(GameEngine):

    def GameStart(self,CurentCaptureImage,GameName):
        ## GAME VALUES ####
        self.set_CaptureImage(CurentCaptureImage)
        Lowwer, Upper, Color = self.get_UpperLowwerColorRange()

        ### CREATE COTOURS AND PRINTS ###
        contours = self.ColorUtils.get_ContursandHirarchy(Upper, Lowwer, CurentCaptureImage)
        self.TextOnScreen(f" ")

        self.START_GAME(GameName)
        self.END_TIME(GameName)

        for shape in self.AllCenterDotArray:
            print(shape)
            # cv2.circle(CurentCaptureImage, [shape], 30, Color, 5)


        for contour in contours:
            area = cv.contourArea(contour)
            if (area > 1000):
                center = self.ColorUtils.get_ObjectCenter(contour)
                cv.circle(CurentCaptureImage, center, 1, Color, 2)
                self.WIN_GAME(center[0],center[1],GameName)








import numpy as np


## Global Vars

Red = "Red"
Green = "Green"
Blue = "Blue"
Pink = "Pink"
Paint = "Paint"
Color_Range = "Color Range"

class ColorDataBase:
    def __init__(self,option:str,color:str):
        self.__option  = option
        self.__color   = color

    def get_ChosenColor(self):
        return self.__color

    def get_ChosenOption(self):
        return self.__option

    def Get_Data(self):
        if self.get_ChosenOption() == Paint:
            return self.PaintDataBase(self.get_ChosenColor())
        elif self.get_ChosenOption() == Color_Range:
            return self.UpperColorRangeData(self.get_ChosenColor()),self.LowwerColorRangeData(self.get_ChosenColor())

    def PaintDataBase(self,color):
        Paint_Color_Dict = {
                "Green" : (0,255,0),
                "Red"   : (0,0,255),
                "Blue"  : (255,0,0),
                "Pink"  : (193, 182, 255),
                "Black" : (0, 0, 0),
                "Purpel": (128, 0, 128),
                "Yellow": (0, 255, 255)
        }
        return Paint_Color_Dict[color]
    def UpperColorRangeData(self,color):
        Upper_Color_Dict = {
                "Green" : np.array([85, 255, 255]),
                "Red"   : np.array([7, 219, 255]),
                "Blue"  : np.array([113, 255, 255]),
                "Pink"  : np.array([179, 175, 255]),
                "Black" : np.array([0, 0, 0]),
                "Purpel": np.array([145, 165, 187]),
                "Yellow": np.array([22, 250, 241])
        }

        return Upper_Color_Dict[color]


    def LowwerColorRangeData(self,color):
        Lowwer_Color_Dict = {
                "Green" : np.array([35, 50, 50]),
                "Red"   : np.array([0,170,196]),
                "Blue"  : np.array([104,127,147]),
                "Pink"  : np.array([164,97,95]),
                "Black" : np.array([0, 0, 0]),
                "Purpel": np.array([121, 75, 61]),
                "Yellow": np.array([0,163,97])
        }
        return Lowwer_Color_Dict[color]
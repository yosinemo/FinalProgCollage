import select
from screeninfo import get_monitors
import platform
import datetime
import subprocess
import os


class GameSetup:

    def __init__(self):
        self.SV = {}
        monitors = get_monitors()
        self.system_platform = platform.system()
        self.m = monitors[0]
        self.get_SetupValues()



    def get_SetupValues(self):

        self.SV["XRES"]             = self.m.width
        self.SV["YRES"]             = self.m.height
        self.SV["XMAINRES"]         = int(self.PresentFormula(88,self.SV["XRES"]))
        self.SV["YMAINRES"]         = int(self.PresentFormula(83,self.SV["YRES"]))
        self.SV["UP"]               = int(self.PresentFormula(20,self.SV["YRES"]))
        self.SV["LEFT"]             = int(self.PresentFormula(20,self.SV["XRES"]))
        self.SV["RIGHT"]            = int(self.SV["XRES"] - self.SV["LEFT"])
        self.SV["DOWN"]             = int(self.SV["YRES"] - self.SV["UP"])
        self.SV["MT_LU_Rectingle"]  = {"start":(0,0),"end":(300,300)}
        self.SV["MT_LD_Rectingle"]  = {"start":(0,self.SV["YMAINRES"] - 300),"end":(300,self.SV["YMAINRES"])}
        self.SV["MT_RU_Rectingle"]  = {"start":(self.SV["XMAINRES"] - 360,0),"end":(self.SV["XMAINRES"]-40,300)}
        self.SV["MT_RD_Rectingle"]  = {"start":(self.SV["XMAINRES"] - 360,self.SV["YMAINRES"] - 300),"end":(self.SV["XMAINRES"]-40,self.SV["YMAINRES"])}
        self.SV["XTEXT"]            = int(self.PresentFormula(10,self.SV["XRES"]))
        self.SV["YTEXT"]            = int(self.PresentFormula(20,self.SV["YRES"]))
        self.SV["XTEXTCOLOR"]       = self.SV["XTEXT"] - 20
        self.SV["YTEXTCOLOR"]       = self.SV["YTEXT"] - 70
        self.SV["XMID"]             = int(self.SV["XRES"]/2)
        self.SV["YMID"]             = int(self.SV["YRES"]/2)
        self.SV["PLATFORN"]         = self.CurrentPlatform()
        self.SV["TIME"]             = self.CurrentTime()
        self.SV["DATE"]             = self.CurrentDate()
        self.SV["FileName"]         = self.get_FileName()
        self.SV["HOMEDIR"]          = self.get_HomeDir()
        self.SV["GAMEDIR"]          = self.CreateGameHomeDir()
        self.SV["GameDataDir"]      = self.CreateGamesDataDir()
        self.SV["GameDataFileNum"]  = self.SearchLastGameDataFile()
        self.SV["GameDataFile"]     = self.get_GameDataFile()
        # self.SV["WHICHGAME"]        = self.GUI.get_SelectedGame()


        return self.SV


    def PresentFormula(self,some,all):
        return (all*some)/100

    def CurrentPlatform(self):
        if self.system_platform == "Windows":
            return "Windows"
        elif self.system_platform == "Linux":
            return "Linux"

    def CurrentTime(self):
        current_time = datetime.datetime.now().time()
        return current_time.strftime("%H:%M:%S")

    def CurrentDate(self):
         return datetime.date.today()

    def get_FileName(self):
        return f"{self.CurrentDate()}-{self.CurrentTime()}"

    def get_HomeDir(self):
        if self.SV["PLATFORN"] == "Windows":
            return os.environ['USERPROFILE']
        elif self.SV["PLATFORN"] == "Linux":
            return os.path.expanduser("~")

    def CreateGameHomeDir(self):
        if self.SV["PLATFORN"] == "Windows":
            new_directory = f"{self.get_HomeDir()}\GameFiles"
        elif self.SV["PLATFORN"] == "Linux":
            new_directory = f"{self.get_HomeDir()}/GameFiles"

        if not os.path.exists(new_directory):
            os.mkdir(new_directory)

        return new_directory

    def PrintAllSETUP_VARS(self):
        for key, value in self.SV.items():
            print(f"{key}: {value}")


    def CreateGamesDataDir(self):
        if self.SV["PLATFORN"] == "Windows":
            GamesDataDirPath =  f"{self.get_HomeDir()}\GameFiles\Gamedata"
        elif self.SV["PLATFORN"] == "Linux":
            GamesDataDirPath = f"{self.get_HomeDir()}/GameFiles/Gamedata"

        if not os.path.exists(GamesDataDirPath):
            os.mkdir(GamesDataDirPath)

        return GamesDataDirPath

    def get_GameDataFile(self):
        GameDataFileNum  = self.SV["GameDataFileNum"]
        GamesDataFilePath = None
        if self.SV["PLATFORN"] == "Windows":
            GamesDataFilePath =  f"{self.get_HomeDir()}\GameFiles\Gamedata\{GameDataFileNum}.txt"
        elif self.SV["PLATFORN"] == "Linux":
            GamesDataFilePath = f"{self.get_HomeDir()}/GameFiles/Gamedata/{GameDataFileNum}.txt"

        return GamesDataFilePath

    def SearchLastGameDataFile(self):
        import re
        numbers = []
        file_names = os.listdir(self.SV["GameDataDir"])
        if not file_names:
            return 0
        else:
            for file in file_names:
                number = re.findall(r'\d+', file)
                numbers.append(int(number[0]))
            sorted_numbers = sorted(numbers)
            return sorted_numbers[-1] + 1

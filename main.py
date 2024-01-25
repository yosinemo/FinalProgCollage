# # #
# # #
# # # from gamesTest import OdedAmar
# # # import cv2
# # # webcam = cv2.VideoCapture(0)
# # #
# # # t = OdedAmar()
# # # while 1:
# # #     ret, camera = webcam.read()
# # #     imageFrame = cv2.flip(camera, 1)
# # #
# # #     t.GameStart(imageFrame)
# # #
# # #     cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)     # show the final resulte
# # #     # if cv2.waitKey(10) & 0xFF == ord('q'):                              # if the user hit the 'q' button quit the game
# # #     #     # interrupts_thread.stop()                                        # stop the interrupts from count
# # #     #     cap.release()                                                   # realse the cpture video
# # #     #     cv2.destroyAllWindows()                                         # destroy all windwos
# # #     #     break
# # #
# # #
# # #
# # #
# #
# #
# #
# #
# #
# #
# # # from GameSetup import GameSetup
# # #
# # # GameSetup = GameSetup()
# # # S = GameSetup.get_SetupValues()
# # # for value in my_dict.values():
# # #     print(value)
# #
# #
# #
# #
# #
# #
# #
# #
# # ### what problams i have so far
# # ## the timer have been started over kand over again to infinite
# # ## i put the constractor inside the while loop so it would read the init func for ever
# #
# # ## sandly have problam with reading the timer file
# # ## the GameEngine is inharited the Timer class so it can have accsess yo the memeber var and function
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # import cv2
# # # from gamesTest import *
# # from GameSetup import *
# # #
# # # from timer import *
# # #
# # # GameSetup = GameSetup()
# # #
# # # # self.GameSetup.PrintAllSETUP_VARS()
# from GameSetup import GameSetup
# g = GameSetup()
#
# g.PrintAllSETUP_VARS()
# # #
# # # class time(Timer):
# # #     def __init__(self):
# # #         super().__init__()
# # #         super().start()
# # #         self.flag = False
# # #
# # #     def PrintTime(self):
# # #         print(self.StratTimeSec)
# # #
# # #     def END_TIME(self):
# # #         Time = self.get_Time()
# # #         # print("falggg",self.flag)
# # #         if Time == 0:
# # #             self.flag = True
# # #             # print("falggg0000000000000000000", self.flag)
# # #             super().Reset()
# # #         if self.flag and Time == 5:
# # #             print("helooooooooo")
# # #             self.flag = False
# # #
# # #     def get_Time(self):
# # #         return self.StratTimeSec
# # #
# # #
# # # t = time()
# # # while 1:
# # #     t.END_TIME()
# #     # print(t.get_Time())
# #
# # # timer = Timer()
# # # timer.start()
# # # # FileLocation = f"C:\\Users\\ymamo\\PycharmProjects\\final_proj\\files\\timer.txt"
# # # while 1:
# # #
# # #     with open(SETUP_VARS["TIMERFILEPATH"], "r") as file:
# # #         temp = file.read()
# # #         print(temp)
# # #         if temp == "0":
# # #             print(temp)
# # #             timer.Reset()
# # #         else:
# # #             print('false')
# #
# #
# #
# #
# # # from GameSetup import *
# # #
# # # webcam = cv2.VideoCapture(0)
# # #
# # # while 1:
# # #     ret, camera = webcam.read()
# # #     imageFrame = cv2.flip(camera, 1)
# # #     y = GameSetup(imageFrame)
# # #     t = OdedAmar()
# # #     t.GameStart(y)
# # # t = test2()
# # # t.gamestart()
# #
# # #
# # # from GamesUtils import *
# # import cv2
# # from gamesTest import *
# # webcam = cv2.VideoCapture(0)
# #
# # #
# # # OdedAmar = OdedAmar()
# #
# # oded_amar = OdedAmar()
# # GoTo = GoTo()
# # SIMON = SIMON()
# # while (1):
# #     ret, camera = webcam.read()                     # read the video from weabcam, set to default
# #
# #     if ret == False:                                # if not capure any video break the while and enf the game
# #         break
# #     imageFrame = cv2.flip(camera, 1)                # flip the capture video if not we will see mirror riflaction
# #     imageFrame = cv2.resize(imageFrame, (1920, 1080))
# #     if SIMON.GameStart(imageFrame,"SIMON"):
# #         print("end game")
# #         break
# #
# #     # cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
# #     cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)     # show the final resulte
# #     if cv2.waitKey(10) & 0xFF == ord('q'):                              # if the user hit the 'q' button quit the game
# #         # interrupts_thread.stop()                                        # stop the interrupts from count
# #         cap.release()                                                   # realse the cpture video
# #         cv2.destroyAllWindows()                                         # destroy all windwos
# #         break                                                           # break the while
# #
# # from shapes import shapes
# # import numpy
# # import cv2
# # Xdot = 700
# # Ydot = 800
# # shapes = shapes()
# # CenterDot = [Xdot,Ydot]
# # AllCenterDotArray = []
# # AllCenterDotArray.append(numpy.array(CenterDot, dtype=numpy.int32))
# # for i in range(0,10):
# #     Xdot, Ydot = shapes.get_CenterPoint(flag=1)
# #     while 1 :
# #         Xsmall = abs(Xdot - CenterDot[0]) < 500
# #         Xhigh = abs(Xdot - CenterDot[0]) > 500
# #         Ysmall = abs(Ydot - CenterDot[1]) < 500
# #         Yhigh = abs(Ydot - CenterDot[1]) > 500
# #
# #         if (Xhigh and Yhigh) or (Xhigh and Ysmall) or (Xsmall and Yhigh) or (Xsmall and Ysmall):
# #             CenterDot = [Xdot, Ydot]
# #             AllCenterDotArray.append(numpy.array(CenterDot, dtype=numpy.int32))
# # webcam = cv2.VideoCapture(0)
# # while (1):
# #     ret, camera = webcam.read()                     # read the video from weabcam, set to default
# #
# #     if ret == False:                                # if not capure any video break the while and enf the game
# #         break
# #     imageFrame = cv2.flip(camera, 1)                # flip the capture video if not we will see mirror riflaction
# #     imageFrame = cv2.resize(imageFrame, (1920, 1080))
# #     for i in AllCenterDotArray:
# #         cv2.circle(imageFrame,i, 100, (0,0,0), 5)
# #
# #     # cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
# #     cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)     # show the final resulte
# #     if cv2.waitKey(10) & 0xFF == ord('q'):                              # if the user hit the 'q' button quit the game
# #         # interrupts_thread.stop()                                        # stop the interrupts from count
# #         cap.release()                                                   # realse the cpture video
# #         cv2.destroyAllWindows()                                         # destroy all windwos
# #         break

#
# import pygame
# import time
#
# def play_note(frequency, duration):
#     pygame.mixer.init()
#     sound_wave = generate_sine_wave(frequency, duration)
#     sound = pygame.sndarray.make_sound((sound_wave * 32767).astype(np.int16))
#     sound.play()
#     pygame.time.delay(int(duration * 1000))
#
# def generate_sine_wave(frequency, duration, sample_rate=44100):
#     t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
#     wave = 0.5 * np.sin(2 * np.pi * frequency * t)
#     return wave
#
# # Replace these values with your desired frequencies and durations
# notes = [
#     (261.63, 1.0),  # C (do)
#     (293.66, 1.0),  # D (re)
#     (329.63, 1.0),  # E (mi)
#     (349.23, 1.0),  # F (fa)
#     (392.00, 1.0),  # G (sol)
# ]
#
# for note in notes:
#     play_note(*note)

# from timer import Timer
# class time(Timer):
#     def __init__(self):
#         super().__init__()
#         super().Reset()
#         super().start()
#         self.flag = False
#
#     def Ptime(self):
#         print(self.StratTimeSec)
#
#     def Ponesecflag(self):
#         print(self.OneSecFlag)
#
#     def time(self):
#         flag = False
#         c = 0
#         while 1:
#             if self.OneSecFlag:
#                 c+=1
#                 print(c)
#             else:
#                 c = 0
#                 print(c)
#
#             # self.Ponesecflag()
#             # self.Ptime()
#
# t = time()
# t.time()

#
# counter = 4
# c = 0
# SimonPattren0 = ["lu","ld","rd","ru"]
# while counter != c :
#         print(SimonPattren0[c],c,end=" ")
#         c+=1
# # [print(f"{SimonPattren0[pattern]}  ") for pattern in  range(1,counter)]
#

# class SharedVariableContainer:
#     def __init__(self):
#         self.shared_variable = None
#
#     def function1(self,container, new_value):
#         container.shared_variable = new_value
#         # Perform actions using container.shared_variable
#         print(f"Function 1: {container.shared_variable}")
#
#     def function2(self,c):
#         # Use container.shared_variable in function2
#         print(f"Function 2: {c.shared_variable}")
#
#     def function3(self,container):
#         # Use container.shared_variable in function3
#         print(f"Function 3: {container.shared_variable}")
#
# # Example usage:
# container_instance = SharedVariableContainer()
#
# container_instance.function1(container_instance, 42)
# container_instance.function2(container_instance)
# container_instance.function3(container_instance)
from abc import ABC, abstractmethod

# Step 1: Product Interface/Abstract Class
# class Product(ABC):
#     @abstractmethod
#     def operation(self):
#         pass
#
# # Step 2: Concrete Products
# class ConcreteProductA(Product):
#     def operation(self):
#         return "ConcreteProductA operation"
#
# class ConcreteProductB(Product):
#     def operation(self):
#         return "ConcreteProductB operation"
#
# # Step 3: Creator Interface/Abstract Class
# class Creator(ABC):
#     @abstractmethod
#     def factory_method(self):
#         pass
#
#     def some_operation(self):
#         product = self.factory_method()
#         result = f"Creator: {product.operation()}"
#         return result
#
# # Step 4: Concrete Creators
# class ConcreteCreatorA(Creator):
#     def factory_method(self):
#         return ConcreteProductA()
#
# class ConcreteCreatorB(Creator):
#     def factory_method(self):
#         return ConcreteProductB()
#
# # Step 5: Usage of the Factory Pattern
# def client_code(creator):
#     print(f"Client: {creator.some_operation()}")
#
# # Usage with ConcreteCreatorA
# creator_a = ConcreteCreatorA()
# client_code(creator_a)
#
# # Usage with ConcreteCreatorB
# creator_b = ConcreteCreatorB()
# client_code(creator_b)

import numpy as np

class ColorDataBase:
    def __init__(self,option:str,color:str):
        self.__option  = option
        self.__color   = color

    def get_ChosenColor(self):
        return self.__color

    def get_ChosenOption(self):
        return self.__option

    def Get_Data(self):
        if self.get_ChosenOption() == "Paint":
            return self.PaintDataBase(self.get_ChosenColor())
        elif self.get_ChosenOption() == "Color Range":
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




# database = ColorDataBase()

print(ColorDataBase("Paint","Green").Get_Data())



class DynamicAttributes:
    def __init__(self):
        self.attributes = {'key1': 'value1', 'key2': 'value2'}

    def __getattr__(self, name):
        # This method is called when accessing an attribute that doesn't exist
        if name in self.attributes:
            return self.attributes[name]
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

# Example usage:
obj = DynamicAttributes()

# Accessing existing attribute
print(getattr(obj, 'key1')) # Outputs: value1

# Accessing non-existing attribute (calls __getattr__)
print(getattr(obj, 'key3'))  # Raises: AttributeError: 'DynamicAttributes' object has no attribute 'key3'

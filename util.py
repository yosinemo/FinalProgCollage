
import numpy as np
import cv2
import time
from shapes import *
from GameSetup import GameSetup

class utils:
    def __init__(self):
        self.shape = shapes()
        self.GameSetup = GameSetup()
        self.SETUP_VARS = self.GameSetup.get_SetupValues()
    def get_ContursandHirarchy(self,up_color,low_color,image): #get the color range and the ca[ture video , return detected boundry location
        mask = self.set_Mask(up_color,low_color,image)
        contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # find the contours and hirarcy


        return contours

    def set_Mask(self,up_color,low_color,image):
        hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # covert the image from rgb to hsv color space format
        lower = np.array(low_color, np.uint8)
        upper = np.array(up_color, np.uint8)
        mask = cv2.inRange(hsvFrame, lower,
                           upper)                           # Checks if array elements lie between the elements of two other arrays
                                                            # the mask will appear when tha camera see the color we want
        kernel = np.ones((15, 15), "uint8")                 # make a kernal for the size of the object
                                                            # to samll dedect smaller objects
                                                            # big dedect biggers
        mask = cv2.dilate(mask, kernel)                     # make an convulation mask and kernael to to perform an filter
                                                            # dilate will thicken the dtected object (make it blur on the edges)

        return mask

    def get_location(self,xmid,ymid):



        if ymid > 0 and ymid < self.SETUP_VARS["UP"]:
            return "up"

        if ymid > self.SETUP_VARS["DOWN"]:
            return "down"

        if xmid > 0 and xmid < self.SETUP_VARS["LEFT"]:
            return "left"

        if xmid > self.SETUP_VARS["RIGHT"]:
            return "right"

        else:
            return "middle"


    def locatin_text(self,text,axis_x,axis_y,imageFrame,color):
        font = cv2.FONT_HERSHEY_SIMPLEX

        font_scale = 1
        font_color = color
        thickness = 2

        # Position to place the text
        text_position = (axis_x, axis_y)  # (x, y) coordinates

        # Add text to the image
        if text != "middle":
            cv2.putText(imageFrame, text, text_position, font, font_scale, font_color, thickness)

    def get_ColorTraker(self,up_color,low_color,imageFrame,color = (0,255,0)): # get the color dondaries and draw rec and thr middle dot
        contours = self.get_ContursandHirarchy(up_color,low_color, imageFrame)
        for contour in contours: # get the spesific location from all thr position of the contour
            area = cv2.contourArea(contour) # det an treashold bondary area
            if (area > 1000):               # only if object is bigger  1000 darw
                *_, radius = cv2.minEnclosingCircle(contour) # surround in a circle
                x, y, w, h = cv2.boundingRect(contour)         # quadruple
                moments = cv2.moments(contour)

                # Calculate the centroid coordinates
                if moments["m00"] != 0:
                    cx = int(moments["m10"] / moments["m00"])
                    cy = int(moments["m01"] / moments["m00"])
                else:
                    cx, cy = 0, 0  # Avoid division by zero

                center = (cx,cy)
                # center = (int(x + radius - 3), int(y + radius - 3)) # serch the center
                cv2.circle(imageFrame, center, 1, color, 2) # darw center dot
                # cv2.rectangle(imageFrame, (x+w,y), (x,y+w), color, 1)   # darw rec

    def get_ObjectCenter(self,contour):
        moments = cv2.moments(contour)

        # Calculate the centroid coordinates
        if moments["m00"] != 0:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])
        else:
            cx, cy = 0, 0  # Avoid division by zero

        return (cx, cy)

    def get_PointColor(self,image,x,y):
        hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        pixel = hsvFrame[x,y]
        hsv = pixel[0]
        if hsv < 5:
            return f"RED"
        elif hsv < 22:
            return "ORANGE"
        elif hsv < 33:
            return "YELLOW"
        elif hsv < 75:
            return "GREEN"
        elif hsv < 131:
            return "BLUE"
        elif hsv < 167:
            return "VAIOLET"
        else:
            return "RED"


    def set_MakeShapeScreen(self,image,color,thikness = 5,flag = 0):
        arr = self.shape.set_RandomShape(flag)
        if arr == None:
            return

        if len(arr) == 3:
            point1 = (arr[0], arr[1])
            cv2.circle(image, point1, arr[2], color, thikness)
            return arr

        elif len(arr) == 6:
            point1 = (arr[0],arr[1])
            point2 = (arr[2],arr[3])
            point3 = (arr[4],arr[5])
            cv2.line(image, point1, point2, color, thikness)
            cv2.line(image, point2, point3, color, thikness)
            cv2.line(image, point3, point1, color, thikness)
            return arr


        elif len(arr) == 4:
            point1 = (arr[0], arr[1])
            point2 = (arr[2], arr[3])
            cv2.rectangle(image, point1, point2, color, thikness)
            return arr

    # def ColorDataBase(self,color):
    #     COLORS = {"Green": {'up': [85, 255, 255], 'low': [35, 50, 50],"paint":(0,255,0)},
    #               "Red": {'up': [7,219,255], 'low': [0,170,196],"paint":(0,0,255)},
    #               "Blue": {'up': [113,255,255], 'low': [104,127,147],"paint":(255,0,0)},
    #               "Pink": {'up': [179,175,255], 'low': [164,97,95],"paint":(193, 182, 255)},
    #               "Black": {'up': [0,0,0], 'low': [0,0,0],"paint":(0, 0, 0)},
    #               "Purpel": {'up': [145, 165, 187], 'low': [121, 75, 61], "paint": (128, 0, 128)},
    #               "Yellow": {'up': [22,250,241], 'low': [0,163,97], "paint": (0, 255, 255)}}
    #
    #     return COLORS[color]


    def DrawRectinles(self,image,selectREC:str = None,color:tuple = (0,0,0), thickness:int = 5):
        if selectREC == "LU":
            cv2.rectangle(image, self.SETUP_VARS["MT_LU_Rectingle"]["start"], self.SETUP_VARS["MT_LU_Rectingle"]["end"],
                            color, -1)
        else:
            cv2.rectangle(image, self.SETUP_VARS["MT_LU_Rectingle"]["start"], self.SETUP_VARS["MT_LU_Rectingle"]["end"],
                            color, thickness)
        if selectREC == "RU":
            cv2.rectangle(image, self.SETUP_VARS["MT_RU_Rectingle"]["start"], self.SETUP_VARS["MT_RU_Rectingle"]["end"],
                            color, -1)
        else:
            cv2.rectangle(image, self.SETUP_VARS["MT_RU_Rectingle"]["start"], self.SETUP_VARS["MT_RU_Rectingle"]["end"],
                            color, thickness)
        if selectREC == "LD":
            cv2.rectangle(image, self.SETUP_VARS["MT_LD_Rectingle"]["start"], self.SETUP_VARS["MT_LD_Rectingle"]["end"],
                            color, -1)
        else:
            cv2.rectangle(image, self.SETUP_VARS["MT_LD_Rectingle"]["start"], self.SETUP_VARS["MT_LD_Rectingle"]["end"],
                            color, thickness)
        if selectREC == "RD":
            cv2.rectangle(image, self.SETUP_VARS["MT_RD_Rectingle"]["start"], self.SETUP_VARS["MT_RD_Rectingle"]["end"],
                            color, -1)
        else:
            cv2.rectangle(image,self.SETUP_VARS["MT_RD_Rectingle"]["start"], self.SETUP_VARS["MT_RD_Rectingle"]["end"],
                            color, thickness)

    def DrawFullReactinles(self,image,thickness = -1,color = "Blue",thic=5):
        cv2.rectangle(image, self.shape.get_MTRectingle("LU")["start"], self.shape.get_MTRectingle("LU")["end"],
                      self.ColorDataBase(color)["paint"], thickness)

        cv2.rectangle(image, self.shape.get_MTRectingle("RU")["start"], self.shape.get_MTRectingle("RU")["end"],
                      self.ColorDataBase(color)["paint"], thickness)

        cv2.rectangle(image, self.shape.get_MTRectingle("LD")["start"], self.shape.get_MTRectingle("LD")["end"],
                      self.ColorDataBase(color)["paint"], thickness)

        cv2.rectangle(image, self.shape.get_MTRectingle("RD")["start"], self.shape.get_MTRectingle("RD")["end"],
                      self.ColorDataBase(color)["paint"], thickness)


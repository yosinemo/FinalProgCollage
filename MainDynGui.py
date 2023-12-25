import sys
import cv2
from QTutils import *
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QSlider,QTextEdit,QPushButton,QTabWidget
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from util import *
from GameSetup import GameSetup
# from games import *
from MainGUI import  *
from gamesTest import *

class MainDynGUI(MainGUI): ## create new class inheritate from MainGUI
    def __init__(self):    ## create new init function
        super().__init__() ## read first the MainGUI init to see all the var and func members
        self.AllColorRanges = [0] * 6
        self.AllColorRanges[3] = 179
        self.AllColorRanges[4] = 255
        self.AllColorRanges[5] = 255
        self.CurrentGame = 0
        self.OdedAmar = OdedAmar() ## call OdedAmar class
        self.GoTo = GoTo()         ## call GoTo class
        # self.game = games()
        self.capture = cv2.VideoCapture(0)  # Open the default camera (usually the built-in webcam)
        # Create a timer to update the webcam feed
        self.timer = QTimer(self)   ## create an QTimer object
        self.timer.timeout.connect(self.showCaptureImage)   ## when time out (30 milliseconds) goto showCaptureImage func (show the GUI)
        self.timer.start(30)  ## Update every 30 milliseconds (you can adjust this value)
                              ## the update make sure the video would not stuck or overload the local memory
        self.util = utils()   ## call utils class for all color and trucking functions

    def pushButtonGame(self) -> 'search selected button' :
        button_text = None ## init the button_text var
        sender_button = self.sender()  # Get the button that triggered the event
        if sender_button in self.AllButtonsGamesData: ## is the triggered button address in the AllButtonsGamesData array?
            button_text = sender_button.text() ## get the name of the triggred button
        ## search the name of the triggerd button
        if button_text == "ODED AMAR":
            self.CurrentGame =  1
        elif button_text == "GO-TO":
            self.CurrentGame =  2
        elif button_text == "SIMON":
            self.CurrentGame =  3
        elif button_text == "END GAMES":
            self.CurrentGame =  0

    def changeSliderColorRange(self)-> 'search selected slider':
        sender_slider = self.sender()  # Get the button that triggered the event
        if sender_slider in self.AllSlidersColorRangeData: ## is the trrigered adress in the AllSlidersColorRangeData array?
            index = self.AllSlidersColorRangeData.index(sender_slider) ## get the index of selected address in AllSlidersColorRangeData
            value = sender_slider.value()                              ## get the scalar value of currant slider on
            self.AllTextSliderColorRangeData[index].setPlainText(str(value)) ## put the scalar value inside the text edit widjet
                                                                             ## the value turn to STR so the text edit widjet can read him propely
            self.AllColorRanges[index] = value                          ## save the last value for the of the current slider

    def showCaptureImage(self)-> 'show image from camera after filtered':
        try: ## try to read camrea frames
            ret, frame = self.capture.read()  # Read a frame from the webcam , frame is the image , ret in bool 1 read 0 fail to read
            if not ret: ## if fail to read
                print("Failed to read a frame from the webcam.")
                return  # Exit the function if reading the frame failed
            imageFrame = cv2.flip(frame, 1) ## flip the frame : 0 vertically(upside dowm) 1 horizontally(left to right -1  -1: Flip both vertically and horizontally.
            imageFrame = cv2.resize(imageFrame, (800, 1000)) ## reasize the frame
            ColorTrackerImage = cv2.resize(imageFrame, (self.SETUP_VARS["XMAINRES"], self.SETUP_VARS["YMAINRES"])) ## resize the main fame
            LowwerColor = [self.AllColorRanges[0], self.AllColorRanges[1], self.AllColorRanges[2]] ## define the lowwer color the user want to detecte
            UpperColor = [self.AllColorRanges[3], self.AllColorRanges[4], self.AllColorRanges[5]]  ## define the upper color the user want to detecte
            ## warp both colors in np.array unsigned 8-bit integer hold integer values in the range from 0 to 255
            LowwerColor = np.array(LowwerColor, np.uint8)
            UpperColor = np.array(UpperColor, np.uint8)
            mask = self.util.set_Mask(UpperColor,LowwerColor, imageFrame) ## create mask for the color ( in clibration tab)
            hsv = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) ## turn the bgr color soace fram to hsv
            result1 = cv2.inRange(hsv, LowwerColor, UpperColor) ##
            result = cv2.bitwise_and(imageFrame, imageFrame, mask=result1)
            ## show the filtered image of the seleccted button
            if self.SelectGame() == 1:
                if self.OdedAmar.GameStart(ColorTrackerImage,"ODED AMAR"):
                    print("Done")
            elif self.SelectGame() == 2:
                if self.GoTo.GameStart(ColorTrackerImage,"GO-TO"):
                    print("Done")
            elif self.SelectGame() == 3:
                if self.game.Simon(ColorTrackerImage):
                    print("Done")
            else:
                ColorTrackerImage = cv2.resize(imageFrame, (1700, 900)) ## in case of none button has been bushed
            GoToGameImageCapturePixmap = QPixmap.fromImage(self.qtutil.setOutputImage(ColorTrackerImage))  ## create a qt image from the frame
            pixmap = QPixmap.fromImage(self.qtutil.setOutputImage(result)) # create a function to deal with pic output
            maskpixmap = QPixmap.fromImage(self.qtutil.setOutputImage(mask))

            # Set the QPixmap as the pixmap for the QLabel
            self.GoToGame_image_label.setPixmap(GoToGameImageCapturePixmap) ## palce the QT immage on the creatred label
            self.resulte_image_label.setPixmap(pixmap)
            self.mask_image_label.setPixmap(maskpixmap)



        except Exception as e:
            print("Error in updateFrame:", str(e)) ## in case of unexpected error e will write the Exception

    def SelectGame(self):
        return self.CurrentGame

    def action1Function(self):
        print('Action 1 was triggered.')

    def action2Function(self):
        print('Action 2 was triggered.')


def main():
    print("running GUI")

if __name__ == '__main__': ## when import new class the python iterperter read the file and execute the file while reading it
                           ## using __name__ make sure the program run only the what in side the if statemaent
    main()                 ## run the main function
    try:
        app = QApplication(sys.argv)    ## pass all scripts args in our case it will be only the name of the script
        run = MainDynGUI()              ## run the MainDynGUI class which run all the program
        run.show()                      ## show the GUI using show function build-in methode
        sys.exit(app.exec_())           ## when user user exit main window exit methode make sure the app executed properly
    except Exception as e:
        print('Houston, we have a problem:', str(e))

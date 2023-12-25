import sys
import cv2
from QTutils import *
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QSlider,QTextEdit,QPushButton,QTabWidget,QAction
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from GameSetup import *

class MainGUI(QMainWindow): ## create an class which inharetate from QMainWindow class function and var members
    def __init__(self): ## create an initial methode
        super().__init__() ## the super func allow the init methode to read first the init func of the QMainWindow class
        self.GameSetup = GameSetup() ## call GameSetup class
        self.qtutil = QTutils()     ## call QTutils class
        self.SETUP_VARS = self.GameSetup.get_SetupValues() ## resive all the setup vars of the game
        # self.app = QApplication(sys.argv) ##  the sys.argv pass application args to QApplication class to customize the behavior of Qt from the command-line in case the user enter --command
                                            ##  the sys.argv[0] is the name of the script and others commands will be in the other cells
                                            ##  the user can pass styles or change the look of the progtram
        self.setGeometry(0, 0, self.SETUP_VARS["XRES"], self.SETUP_VARS["YRES"]) ## set the gometry of the all window
        self.AllButtomsGamesName = ["ODED AMAR","GO-TO","SIMON","GO FECH","END GAMES"]
        self.AllSildersColorRangeName = ["Lowwer H = ","Lowwer S = ","Lowwer V = ","Upper H = ","Upper S = ","Upper V = "]
        ## create an arrays to enter the address of the push buttons, sliders wheen user click, to pass them to MaunDynGUI script
        self.AllButtonsGamesData = [None]*5
        self.AllSlidersColorRangeData = [None]*6
        self.AllTextSliderColorRangeData = [None]*6
        self.initUI() ## enter to initUI func to create all objects on screen window

    def initUI(self) -> 'object creator' :
        self.setWindowTitle('Webcam Display') # title of the window
        toolbar = self.addToolBar('My Toolbar') # craete toolbar
        ## styling the toolbar buttons
        toolbar.setStyleSheet('QToolButton { background-color: #3498db; color: #ffffff; }')
        ## create first  action button to toolbar
        action1 = QAction('Action 1', self)
        action1.setStatusTip('Perform Action 1')
        action1.triggered.connect(self.action1Function) ## connected function for toolbar button when push (trigered)

        ## create secound action button to toolbar
        action2 = QAction('Action 2', self)
        action2.setStatusTip('Perform Action 2')
        action2.triggered.connect(self.action2Function)

        toolbar.addAction(action1)  ## add button to the toolbar
        toolbar.addAction(action2)

        # create two tags
        central_widget = QWidget(self) # create the basic GUI of the application
        self.setCentralWidget(central_widget) ## set the main GUI exicuted the setCentralWidget is a built-in function from QMainWindow
        layout = QVBoxLayout() ## class QVBoxLayout is an arrange widgets vertically in a top-down fashion
        central_widget.setLayout(layout) ## impliment the vertically layout on the GUI
        tab_widget = QTabWidget() ## call QTabWidget class to create an tabs in the window
        layout.addWidget(tab_widget) ## add tab_widget to the GUI


        games = QWidget() ## create new QWidget
        tab_widget.addTab(games, 'Games GUI') ## define the new QWidget as tab
        ## create an 5 buttons ( all games ) using the QTUtils
        factor = 20 ## set an scalar to arrange the buttons in some order
        for i in range(0,5): ## craete all 5 buttons in one loop
            button = self.qtutil.setButton(10,factor,games,200,100,self.AllButtomsGamesName[i]) ## create the button
            self.AllButtonsGamesData[i] = button ## put the button in array
            self.AllButtonsGamesData[i].clicked.connect(self.pushButtonGame) ## each button is stored in array
            ## the main idae of the arrays --> when we dealing with large data of of widjets
            ## it priferd to use the sender function wich can get the address of the widjet
            ## and then we search if the address it got is in the the button widjets array
            ## in this case we can create one function to commaunicates with all buttons
            factor+=150

        self.GoToGame_image_label = self.qtutil.setLabel(250, 0, games, " ", 1650, 900, True) ## label for the image output



        calibration = QWidget()
        # self.calibration = calibration
        tab_widget.addTab(calibration,'Calbration GUI')
        factor = 30
        for i in range(0,3): ## craete all the sliders
            if i == 0 or i+3 == 3: ##
                low_slider = self.qtutil.setSlider(x = 1650, y = factor, name = self.AllSildersColorRangeName[i], x_name = 1660, y_name = factor - 20,tag = calibration, min_value = 0, max_value = 179, default_value = 0)
                up_slidder = self.qtutil.setSlider(x= 1650, y = factor + 300, name = self.AllSildersColorRangeName[i+3], x_name = 1670, y_name = factor + 300 - 20, tag = calibration, min_value = 0, max_value = 179, default_value = 179)
            else:
                low_slider = self.qtutil.setSlider(x = 1650, y = factor, name = self.AllSildersColorRangeName[i], x_name = 1660, y_name =factor - 20 ,tag = calibration, min_value = 0, max_value = 255, default_value = 0)
                up_slidder = self.qtutil.setSlider(x= 1650, y = factor + 300, name = self.AllSildersColorRangeName[i+3], x_name = 1670, y_name = factor + 300 - 20, tag = calibration, min_value = 0, max_value = 255, default_value = 255)
            low_slider_text = self.qtutil.setTextEdit(1780, factor - 20, calibration, 35, 30)
            up_slidder_text = self.qtutil.setTextEdit(1780,factor + 300 - 20,calibration,35,30)
            self.AllSlidersColorRangeData[i] = low_slider
            self.AllTextSliderColorRangeData[i] = low_slider_text
            self.AllSlidersColorRangeData[i+3] = up_slidder
            self.AllTextSliderColorRangeData[i+3] = up_slidder_text
            self.AllSlidersColorRangeData[i].valueChanged.connect(self.changeSliderColorRange)
            self.AllTextSliderColorRangeData[i].textChanged.connect(self.changeSliderColorRange)
            self.AllSlidersColorRangeData[i+3].valueChanged.connect(self.changeSliderColorRange)
            self.AllTextSliderColorRangeData[i+3].textChanged.connect(self.changeSliderColorRange)
            factor += 100

        self.resulte_image_label = self.qtutil.setLabel(0,0,calibration," ",800, 800,True)
        self.mask_image_label = self.qtutil.setLabel(800, 0, calibration, " ", 800, 800, True)
        # self.ResulteImageLableData = resulte_image_label
        # self.ResulteImageLableData. (self.showCaptureImage)



        # central_widget.setLayout(layout) ##
        self.makeDarkMode(tab_widget,games,calibration) ## create an dark mode to the gui


    ## all the connect function need to be create in order the program can see there is an function
    ## in the MainDynGUI script all 5 function will be overwritten
    def pushButtonGame(self)-> 'search selected button':
        print("pushButtonGame method should be in MainDynGUI class")
    def changeSliderColorRange(self)-> 'search selected slider':
        print("changeSliderColorRange method should be in MainDynGUI class")

    def showCaptureImage(self) -> 'show image from camera after filtered':
        print("showCaptureImage method should be in MainDynGUI class")

    def action1Function(self)-> 'exec action button 1 from tool bar':
        print("action1Function method should be in MainDynGUI class")

    def action2Function(self)-> 'exec action button 2 from tool bar':
        print("action2Function method should be in MainDynGUI class")

    def makeDarkMode(self,tab_widget,games,calibration)-> 'create dark mode GUI':
        self.setStyleSheet('''
                           QMainWindow {
                               background-color: #333333; /* Background color */
                               color: #FFFFFF; /* Text color */
                           }
                           QPushButton {
                               background-color: #555555; /* Button background color */
                               color: #FFFFFF; /* Button text color */
                           }
                           QPushButton:hover {
                               background-color: #777777; /* Hover background color */
                           }
                       ''')
        tab_widget.setStyleSheet('''
                            QTabWidget::pane {
                                background-color: #333333; /* Background color of tab content area */
                            }
                            QTabBar::tab {
                                background-color: #555555; /* Tab background color */
                                color: #FFFFFF; /* Tab text color */
                            }
                            QTabBar::tab:selected, QTabBar::tab:hover {
                                background-color: #777777; /* Selected and hover tab background color */
                            }
                        ''')
        games.setStyleSheet('''
                    background-color: #333333; /* Dark background color */
                    color: #FFFFFF; /* Light text color */
                ''')
        calibration.setStyleSheet('''
                            background-color: #333333; /* Dark background color */
                            color: #FFFFFF; /* Light text color */
                        ''')

# if __name__ == '__main__': ## if the code has been exectuted from here (MainGUI)
#     window = MainGUI()

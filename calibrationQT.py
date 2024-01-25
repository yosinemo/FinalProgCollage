
import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QSlider,QTextEdit,QPushButton
from PyQt5.QtGui import QImage, QPixmap,QFont
from PyQt5.QtCore import Qt, QTimer

class WebcamDisplay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 600)
        self.AllSliderName = ["Lowwer H = ","Lowwer S = ","Lowwer V = ","Upper H = ","Upper S = ","Upper V = "]
        self.AllSliderArray = [None] * 6
        self.AllTextArray = [None] * 6
        self.AllColorRanges = [0] * 6
        self.AllColorRanges[3] = 179
        self.AllColorRanges[4] = 255
        self.AllColorRanges[5] = 255

        self.initUI()
        self.capture = cv2.VideoCapture(0)  # Open the default camera (usually the built-in webcam)

        # Create a timer to update the webcam feed
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(30)  # Update every 30 milliseconds (you can adjust this value)

    def initUI(self):
        self.setWindowTitle('Webcam Display')

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.make_label(150,10,"Final Resulte")
        self.make_label(650, 10, "Mask Resulte")
        self.make_button(700,360,self,250,200,"Done",self.pushB)
        self.label = QLabel(self)
        self.masklabel = QLabel(self)
        self.makeAllSliders()

        layout.addWidget(self.label)

        central_widget.setLayout(layout)

        self.show()

    def makeAllSliders(self):
        # lowwer U
        factor = 50
        i = 0
        # a = self.set_Slider(50,350,self.AllSliderName[i],90,320,Qt.Horizontal,0,100,0,200,30)
        a = self.set_Slider(x = 50, y = 350 + factor, name = self.AllSliderName[i], x_name = 90, y_name = 320 + factor, min_value = 0, max_value = 179, default_value = 0)
        b = self.make_text(220, 320 + factor, 40, 30)
        self.AllSliderArray[i] = a
        self.AllTextArray[i] = b

        # lowwer S
        factor +=70
        i +=1
        a = self.set_Slider(x = 50, y = 350 + factor, name = self.AllSliderName[i], x_name = 90, y_name = 320 + factor, min_value = 0, max_value = 255, default_value = 0)
        b = self.make_text(220, 320 + factor, 40, 30)
        self.AllSliderArray[i] = a
        self.AllTextArray[i] = b

        # lowwer V
        factor += 70
        i += 1
        a = self.set_Slider(x = 50, y = 350 + factor, name = self.AllSliderName[i], x_name = 90, y_name = 320 + factor, min_value = 0, max_value = 255, default_value = 0)
        b = self.make_text(220, 320 + factor, 40, 30)
        self.AllSliderArray[i] = a
        self.AllTextArray[i] = b

        # upper U
        factor =50
        i += 1
        a = self.set_Slider(x= 400, y = 350 + factor, name = self.AllSliderName[i], x_name = int((700 + 200) / 2), y_name = 320 + factor, min_value = 0, max_value = 179, default_value = 179)
        b = self.make_text(560, 320 + factor, 40, 30)
        self.AllSliderArray[i] = a
        self.AllTextArray[i] = b

        # upper S
        factor += 70
        i += 1
        a = self.set_Slider(x= 400, y = 350 + factor, name = self.AllSliderName[i], x_name = int((700 + 200) / 2), y_name = 320 + factor, min_value = 0, max_value = 255, default_value = 255)
        b = self.make_text(560, 320 + factor, 40, 30)
        self.AllSliderArray[i] = a
        self.AllTextArray[i] = b

        # upper V
        factor += 70
        i += 1
        a = self.set_Slider(x= 400, y = 350 + factor, name = self.AllSliderName[i], x_name = int((700 + 200) / 2), y_name = 320 + factor, min_value = 0, max_value = 255, default_value = 255)
        b = self.make_text(560, 320 + factor, 40, 30)
        self.AllSliderArray[i] = a
        self.AllTextArray[i] = b

    def make_Output(self,image):
        frame_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convert the OpenCV image to a QImage
        height, width, channel = frame_rgb.shape
        bytes_per_line = 3 * width

        q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

        return q_image

    def set_Slider(self, x, y,name,x_name,y_name,  orientation=Qt.Horizontal,min_value=0, max_value=100, default_value=0, width=200,height=30):
        slider = QSlider(orientation,self)
        slider.setGeometry(x, y, width, height)  # Set the slider's position and size
        slider.setMinimum(min_value)
        slider.setMaximum(max_value)
        slider.setValue(default_value)

        self.make_label(x_name,y_name,name)
        self.make_label(x-10,y,min_value)
        self.make_label(x + width, y, max_value)
        def slider_value_changed(value):
            sender_slider = self.sender()  # Get the button that triggered the event
            if sender_slider in self.AllSliderArray:
                index = self.AllSliderArray.index(sender_slider)
                self.AllColorRanges[index] = value
                self.AllTextArray[index].setPlainText(str(value))

        slider.valueChanged.connect(slider_value_changed)
        return slider

    def updateFrame(self):
        try:
            ret, frame = self.capture.read()  # Read a frame from the webcam
            if ret:
                imageFrame = cv2.flip(frame, 1)
                imageFrame = cv2.resize(imageFrame, (400, 300))
                LowwerColor =[self.AllColorRanges[0], self.AllColorRanges[1], self.AllColorRanges[2]]
                UpperColor = [self.AllColorRanges[3], self.AllColorRanges[4], self.AllColorRanges[5]]
                LowwerColor = np.array(LowwerColor, np.uint8)
                UpperColor = np.array(UpperColor, np.uint8)
                mask = self.mask(LowwerColor, UpperColor, imageFrame)
                hsv = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
                result1 = cv2.inRange(hsv, LowwerColor, UpperColor)
                result = cv2.bitwise_and(imageFrame, imageFrame, mask=result1)
                # cv2.imshow("1", result)
                pixmap = QPixmap.fromImage(self.make_Output(result)) # create a function to deal with pic output
                maskpixmap = QPixmap.fromImage(self.make_Output(mask))

                self.masklabel.setFixedSize(400,300) # the screen was to samll Ensure the QLabel has the same size as the image
                self.masklabel.move(500,50)
                self.masklabel.setPixmap(maskpixmap)

                # Set the QPixmap as the pixmap for the QLabel
                self.label.setFixedSize(400, 300)
                self.label.move(10,50)
                self.label.setPixmap(pixmap)

        except Exception as e:
            print("Error in updateFrame:", str(e))


    def mask(self,low_color,up_color,image):
        # print(low_color,up_color)
        hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array(low_color, np.uint8)
        upper = np.array(up_color, np.uint8)
        mask = cv2.inRange(hsvFrame, lower,upper)
        kernel = np.ones((15, 15), "uint8")
        mask = cv2.dilate(mask, kernel)
        # cv2.imshow("1", mask)

        return mask


    def make_text(self, x, y, xloc, yloc, RW=True):
        self.console_output = QTextEdit(self)
        console_output = self.console_output
        console_output.setFixedWidth(xloc)  # Set the width
        console_output.setFixedHeight(yloc)  # Set the height
        console_output.move(x, y)
        console_output.adjustSize()
        console_output.setReadOnly(RW)  # Make it read-only
        return console_output

    def make_label(self, x, y, text, text_size=14):
        label = QLabel(f"{text}",self)
        font = QFont("Arial", text_size)
        label.setFont(font)
        label.move(x, y)
        label.adjustSize()

    def make_button(self, x, y, tag,xloc,yloc, text, func, text_size=14):
        get_data_button = QPushButton(f'{text}', tag)
        get_data_button.setFixedWidth(xloc)  # Set the width
        get_data_button.setFixedHeight(yloc)  # Set the height
        get_data_button.clicked.connect(func)
        font = QFont("Arial", text_size)
        get_data_button.setFont(font)
        get_data_button.move(x, y)
        get_data_button.adjustSize()

    def pushB(self):
        LowwerColor = [self.AllColorRanges[0], self.AllColorRanges[1], self.AllColorRanges[2]]
        UpperColor = [self.AllColorRanges[3], self.AllColorRanges[4], self.AllColorRanges[5]]
        print("Lowwer Range",LowwerColor)
        print("Upper Range",UpperColor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebcamDisplay()
    sys.exit(app.exec_())


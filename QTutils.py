import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QSlider,QTextEdit,QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer

class QTutils(QMainWindow):
    def __init__(self):
        super().__init__()


    def setLabel(self, x, y,tag, text,xfixsize = 0,yfixsize = 0,retuenLabel = False, text_size=14):
        label = QLabel(f"{text}",tag)
        font = QFont("Arial", text_size)
        label.setFont(font)
        label.move(x, y)
        label.adjustSize()
        if retuenLabel:
            label.setFixedSize(xfixsize, yfixsize)
            return label

    def setSlider(self, x, y,name,x_name,y_name,tag, orientation=Qt.Horizontal,min_value=0, max_value=100, default_value=0, width=200,height=30):
        slider = QSlider(orientation,tag)
        slider.setGeometry(x, y, width, height)  # Set the slider's position and size
        slider.setMinimum(min_value)
        slider.setMaximum(max_value)
        slider.setValue(default_value)
        self.setLabel(x_name, y_name,tag, name)
        self.setLabel(x - 10, y,tag, min_value)
        self.setLabel(x + width, y,tag, max_value)
        return slider

    def setButton(self, x, y, tag, xloc, yloc, text, text_size=14):
        font = QFont("Arial", text_size)
        button = QPushButton(f'{text}', tag)
        button.setFixedWidth(xloc)  # Set the width
        button.setFixedHeight(yloc)  # Set the height
        button.setFont(font)
        button.move(x, y)
        button.adjustSize()

        return button

    def setTextEdit(self, x, y,tag, xloc, yloc, RW=True):
        console_output = QTextEdit(tag)
        console_output.setFixedWidth(xloc)  # Set the width
        console_output.setFixedHeight(yloc)  # Set the height
        console_output.move(x, y)
        console_output.adjustSize()
        console_output.setReadOnly(RW)  # Make it read-only
        return console_output

    def setOutputImage(self,image):
        frame_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Convert the OpenCV image to a QImage
        height, width, channel = frame_rgb.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return q_image


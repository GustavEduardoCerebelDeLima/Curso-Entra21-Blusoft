from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 300

        self.width = 700
        self.height = 500

        self.title = 'First Window'

        self.lable1 = QLabel(self)
        self.lable1.setText('hello world')
        self.lable1.setStyleSheet('QLabel {font:bold; font-size: 20px; color: blue;}')
        self.lable1.move(200, 100)
        self.lable1.resize(300, 100)

        button1 = QPushButton('Button_1', self)
        button1.move(150, 200)
        button1.resize(100, 100)
        button1.setStyleSheet('QPushButton {background-color: cyan; font:bold; font-size: 20px}')
        button1.clicked.connect(self.button1_click)

        button2 = QPushButton('Button_2', self)
        button2.move(300, 200)
        button2.resize(100, 100)
        button2.setStyleSheet('QPushButton {background-color: purple; font:bold; font-size: 20px}')
        button2.clicked.connect(self.button2_click)

        self.load_window()

    def load_window(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def button1_click(self):
        self.lable1.setText('The Button_1 was clicked')
        self.lable1.setStyleSheet('QLabel {font:bold; font-size: 20px; color: cyan;}')

    def button2_click(self):
        self.lable1.setText('The Button_2 was clicked')
        self.lable1.setStyleSheet('QLabel {font:bold; font-size: 20px; color: purple;}')


aplication = QApplication([])
window = Window()
aplication.exec()

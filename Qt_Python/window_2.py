from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def click():
    window.lable.setText('The Button 1 was clicked')


app = QApplication([])
window = uic.loadUi('Janela.ui')
window.pushButton.clicked.connect(click)
window.pushButton_2.clicked.connect(click)

window.show()
app.exec()
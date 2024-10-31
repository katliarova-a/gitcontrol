from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDate
import sys

from design import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

width = 8

def changeWidth():
    global width
    width = ui.horizontalSlider.value()
    ui.label_3.setText(str(width))

ui.horizontalSlider.valueChanged.connect(changeWidth)
sys.exit(app.exec())
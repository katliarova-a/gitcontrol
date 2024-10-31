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

sys.exit(app.exec())
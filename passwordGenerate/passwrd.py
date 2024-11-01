import random

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
numbers = "0123456789"
lettersSmall = "abcdefghijklmnopqrstuvwxyz"
lettersBig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+"
width = 8

def changeWidth():
    global width
    width = ui.horizontalSlider.value()
    ui.label_3.setText(str(width))

def generatePass():
    global width
    allSymbols = ""
    passwordUser = ""
    if ui.checkBox.isChecked() or ui.checkBox_2.isChecked() or ui.checkBox_3.isChecked() or ui.checkBox_4.isChecked():
        if ui.checkBox.isChecked():
            allSymbols = allSymbols + numbers
        if ui.checkBox_2.isChecked():
            allSymbols = allSymbols + lettersSmall
        if ui.checkBox_3.isChecked():
            allSymbols = allSymbols + lettersBig
        if ui.checkBox_4.isChecked():
            allSymbols = allSymbols + symbols
        for i in range(width):
            passwordUser = passwordUser + allSymbols[random.randint(0, len(allSymbols))]
        ui.plainTextEdit.clear()
        ui.plainTextEdit.insertPlainText(passwordUser)

    else:
        msg = QMessageBox().warning(MainWindow, "Warning", "Select data to generate a password",
                                    QMessageBox.StandardButton.Ok)

ui.checkBox.setChecked(True)
ui.horizontalSlider.valueChanged.connect(changeWidth)
ui.pushButton.clicked.connect(generatePass)

sys.exit(app.exec())
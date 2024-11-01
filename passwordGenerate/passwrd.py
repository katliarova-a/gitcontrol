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

def selectTheme():
    if ui.comboBox.currentText() == "dark":
        MainWindow.setStyleSheet("background: #2F4F4F;")
        ui.groupBox.setStyleSheet("background-color: rgb(105, 105, 105);")
        ui.label.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2F4F4F, stop:1 rgba(129, 169, 222, 255));")
        ui.label_2.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(129, 169, 222, 255), stop:1 #2F4F4F)")
    if ui.comboBox.currentText() == "light":
        MainWindow.setStyleSheet("background: #f0f0f0;")
        ui.groupBox.setStyleSheet("background-color: rgb(219, 216, 222);")
        ui.label.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(129, 169, 222, 255));")
        ui.label_2.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(129, 169, 222, 255), stop:1 rgba(255, 255, 255, 255))")

ui.checkBox.setChecked(True)
ui.horizontalSlider.valueChanged.connect(changeWidth)
ui.pushButton.clicked.connect(generatePass)
ui.comboBox.currentTextChanged.connect(selectTheme)
sys.exit(app.exec())
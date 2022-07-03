#!usr/bin/env python3
import this
import time
from math import *
from PyQt5 import QtCore, QtGui, QtWidgets


def is_value_in_string(value: str, the_string: str):
    return value in the_string.lower()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputScreen = QtWidgets.QLabel(self.centralwidget)
        self.outputScreen.setGeometry(QtCore.QRect(20, 20, 321, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.outputScreen.setFont(font)
        self.outputScreen.setFrameShape(QtWidgets.QFrame.Box)
        self.outputScreen.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputScreen.setLineWidth(3)
        self.outputScreen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputScreen.setObjectName("outputScreen")

        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("%"))
        self.percentButton.setGeometry(QtCore.QRect(20, 125, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")

        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("C"))
        self.clearButton.setGeometry(QtCore.QRect(90, 125, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")

        self.muchGreaterButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("<<"))
        self.muchGreaterButton.setGeometry(QtCore.QRect(160, 125, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.muchGreaterButton.setFont(font)
        self.muchGreaterButton.setObjectName("muchGreaterButton")

        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("/"))
        self.divideButton.setGeometry(QtCore.QRect(260, 125, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")

        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("7"))
        self.sevenButton.setGeometry(QtCore.QRect(20, 195, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")

        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("8"))
        self.eightButton.setGeometry(QtCore.QRect(90, 195, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")

        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("9"))
        self.nineButton.setGeometry(QtCore.QRect(160, 195, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")

        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(260, 195, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")

        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("4"))
        self.fourButton.setGeometry(QtCore.QRect(20, 265, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")

        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("6"))
        self.sixButton.setGeometry(QtCore.QRect(160, 265, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")

        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("5"))
        self.fiveButton.setGeometry(QtCore.QRect(90, 265, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")

        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("-"))
        self.minusButton.setGeometry(QtCore.QRect(260, 265, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")

        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("3"))
        self.threeButton.setGeometry(QtCore.QRect(160, 335, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")

        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("2"))
        self.twoButton.setGeometry(QtCore.QRect(90, 335, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")

        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("+"))
        self.plusButton.setGeometry(QtCore.QRect(260, 335, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")

        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("1"))
        self.oneButton.setGeometry(QtCore.QRect(20, 335, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")

        self.plusMinusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("+/-"))
        self.plusMinusButton.setGeometry(QtCore.QRect(20, 405, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.plusMinusButton.setFont(font)
        self.plusMinusButton.setObjectName("plusMinusButton")

        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("0"))
        self.zeroButton.setGeometry(QtCore.QRect(90, 405, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")

        self.dotButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("."))
        self.dotButton.setGeometry(QtCore.QRect(160, 405, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.dotButton.setFont(font)
        self.dotButton.setObjectName("dotButton")

        self.equalsButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressButton("="))
        self.equalsButton.setGeometry(QtCore.QRect(260, 405, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.equalsButton.setFont(font)
        self.equalsButton.setObjectName("equalsButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputScreen.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.muchGreaterButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.plusMinusButton.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.equalsButton.setText(_translate("MainWindow", "="))

    def pressButton(self,pressed):
        if pressed == "C":
            self.outputScreen.setText("0")
        elif pressed == "=":
            answer = int(eval(self.outputScreen.text()))
            print(answer)
            self.outputScreen.setText(str(answer))
        elif pressed == ".":
            text = self.outputScreen.text()

            if is_value_in_string(".", text) == False:
                self.outputScreen.setText(f"{self.outputScreen.text()}{pressed}")
        # These 2 are not finished
        elif pressed == "+/-":
            pass

        elif pressed == "<<":
            pass
        #

        elif pressed == "/":
            self.outputScreen.setText(f"{self.outputScreen.text()}{pressed}")
            print(float(eval(self.outputScreen.text())))


        else:
            # Check if theres 0 first
            if self.outputScreen.text() == "0":
                if pressed != ".":
                    self.outputScreen.setText("")

            self.outputScreen.setText(f"{self.outputScreen.text()}{pressed}")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

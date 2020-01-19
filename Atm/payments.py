# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\python_final\payments.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Modules.__init__ import *
from Atm.waterPayment import WaterPayment

user = None
mainWindow = None
previousWindow = None

def onbtnWaterClicked(self):
    openWindowWithData(self.mainWindow, WaterPayment, [self.user, self.previousWindow, WaterPayment])

class Payments(object):
    def __init__(self, obj):
        self.mainWindow = obj[0]
        self.user = obj[1][0]
        print(self.user)
        self.previousWindow = obj[1][1]

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1080, 720)
        mainWindow.setStyleSheet("background-color: #0B3A97")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnTopup = QtWidgets.QPushButton(self.centralwidget)
        self.btnTopup.setGeometry(QtCore.QRect(560, 410, 231, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btnTopup.setFont(font)
        self.btnTopup.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnTopup.setObjectName("btnTopup")
        self.btnWater = QtWidgets.QPushButton(self.centralwidget)
        self.btnWater.setGeometry(QtCore.QRect(260, 220, 231, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btnWater.setFont(font)
        self.btnWater.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnWater.setObjectName("btnWater")
        self.btnWater.clicked.connect(lambda : onbtnWaterClicked(self))
        self.btnInternet = QtWidgets.QPushButton(self.centralwidget)
        self.btnInternet.setGeometry(QtCore.QRect(260, 410, 231, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btnInternet.setFont(font)
        self.btnInternet.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnInternet.setObjectName("btnInternet")
        self.btnElectricity = QtWidgets.QPushButton(self.centralwidget)
        self.btnElectricity.setGeometry(QtCore.QRect(560, 220, 231, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btnElectricity.setFont(font)
        self.btnElectricity.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnElectricity.setObjectName("btnElectricity")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(180, 80, 711, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("color: white")
        self.lblTitle.setObjectName("lblTitle")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.btnTopup.setText(_translate("mainWindow", "Phone Topup"))
        self.btnWater.setText(_translate("mainWindow", "Water"))
        self.btnInternet.setText(_translate("mainWindow", "Internet"))
        self.btnElectricity.setText(_translate("mainWindow", "Electricity"))
        self.lblTitle.setText(_translate("mainWindow", "Please select payment below:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Payments()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

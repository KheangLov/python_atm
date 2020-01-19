# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\python_final\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Modules.__init__ import *

user = None
mainWindow = None
previousWindow = None
title = None
content = None
withdraw = None

def onBtnOkClicked(self):
    openWindowWithData(self.mainWindow, self.previousWindow, self.user)
    # openWindowWithData(self.mainWindow, self.withdraw, self.user)
    # openWindowWithData(self.mainWindow, self.currentWindow, [self.user, self.previousWindow, self.currentWindow])

    # openWindowWithData(
    #     self.mainWindow,
    #     dialog,
    #     [
    #         self.user,
    #         self.previousWindow,
    #         {"title": "Fail", "content": "You don't have enough balance"},
    #         self.currentWindow
    #     ]
    # )



class DialogWithdraw(object):
    def __init__(self, obj):
        self.mainWindow = obj[0]
        self.user = obj[1][0]
        print(self.user)
        self.previousWindow = obj[1][1]
        self.withdraw = obj[1][2]
        self.title = obj[1][2]["title"]
        self.content = obj[1][2]["content"]


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 200)
        MainWindow.setStyleSheet("background-color: #0B3A97")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(40, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("color: white")
        self.lblTitle.setObjectName("lblTitle")
        self.lblContent = QtWidgets.QLabel(self.centralwidget)
        self.lblContent.setGeometry(QtCore.QRect(40, 70, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblContent.setFont(font)
        self.lblContent.setStyleSheet("color: white")
        self.lblContent.setObjectName("lblContent")
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(420, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnOk.setFont(font)
        self.btnOk.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(lambda : onBtnOkClicked(self))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", self.title))
        self.lblContent.setText(_translate("MainWindow", self.content))
        self.btnOk.setText(_translate("MainWindow", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DialogWithdraw()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

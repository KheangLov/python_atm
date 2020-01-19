# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\python_final\withdraw.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Utils.func import openWindowWithData
from Atm.dialogWithdraw import DialogWithdraw as dialog
# from Atm.atm import Atm
# from Modules.__init__ import *


user = None
mainWindow = None
previousWindow = None
withdraw = None


def onBtnOkClicked(self):
    self.window = QtWidgets.QMainWindow()
    amount = None
    if (len(self.txtAmount.text()) == 0):
        amount = 0
    else:
        amount = float(self.txtAmount.text())
    if (float(self.user["balanceUSD"]) >= amount):
        if (amount % 10 > 0):
            openWindowWithData(
                self.mainWindow,
                dialog,
                [
                    self.user,
                    self.previousWindow,
                    {"title": "Sorry, ", "content": "Please input amount as a multiple of $10"},
                    self.withdraw
                ]
            )
        else:
            self.user["balanceUSD"] = str(float(self.user["balanceUSD"]) - amount)
            openWindowWithData(self.mainWindow, self.previousWindow, self.user)
    else:
        print('You dont have enought balance')
        openWindowWithData(
            self.mainWindow,
            dialog,
            [
                self.user,
                self.previousWindow,
                {"title": "Sorry,", "content": "You don't have enough balance"},
                self.withdraw
            ]
        )
        self.window = QtWidgets.QMainWindow()
        # openWindowWithData(self, self.window, Dialog, {"title": "Fail,", "msgContent": "You don't have enough balance."})
    print(self.user)

def onBtnCancelClicked(self):
    openWindowWithData(self.mainWindow, self.previousWindow, self.user)


class Withdraw(object):
    def __init__(self, obj):
        self.mainWindow = obj[0]
        self.user = obj[1][0]
        print(self.user)
        self.previousWindow = obj[1][1]
        self.withdraw = obj[1][2]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: #0B3A97")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAmount.setGeometry(QtCore.QRect(90, 210, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txtAmount.setFont(font)
        self.txtAmount.setStyleSheet("color: white")
        self.txtAmount.setMaxLength(4)
        self.txtAmount.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtAmount.setObjectName("txtAmount")
        self.lblWithdrawLimit = QtWidgets.QLabel(self.centralwidget)
        self.lblWithdrawLimit.setGeometry(QtCore.QRect(150, 150, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblWithdrawLimit.setFont(font)
        self.lblWithdrawLimit.setStyleSheet("color: white")
        self.lblWithdrawLimit.setObjectName("lblWithdrawLimit")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(60, 110, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("color: white")
        self.lblTitle.setObjectName("lblTitle")
        self.lblCurrencySymbol = QtWidgets.QLabel(self.centralwidget)
        self.lblCurrencySymbol.setGeometry(QtCore.QRect(60, 210, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrencySymbol.setFont(font)
        self.lblCurrencySymbol.setStyleSheet("color: white")
        self.lblCurrencySymbol.setObjectName("lblCurrencySymbol")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(520, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnCancel.setFont(font)
        self.btnCancel.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.clicked.connect(lambda : onBtnCancelClicked(self))
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(420, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnOk.setFont(font)
        self.btnOk.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(lambda: onBtnOkClicked(self))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        self.lblWithdrawLimit.setText(_translate("MainWindow", "Withdraw limit per transaction $ 1,000"))
        self.lblTitle.setText(_translate("MainWindow", "Please enter amount to withdraw"))
        self.lblCurrencySymbol.setText(_translate("MainWindow", "$"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.btnOk.setText(_translate("MainWindow", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Withdraw()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

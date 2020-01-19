# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\python_final\waterPayment.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Modules.__init__ import *
from Atm.dialogWaterPayment import DialogWaterPayment as dialog

pendingPayment = [
    {"usageNo": "1000000000", "amountUSD": 11},
    {"usageNo": "1000000001", "amountUSD": 200},
    {"usageNo": "1000000002", "amountUSD": 7.5},
    {"usageNo": "1000000003", "amountUSD": 4.5}
]


mainWindow = None
previousWindow = None
user = None

usageNo = None
usageObj = {"usageNo": None, "amountUSD": None}
costOfWater = None
totalAmount = None

def onBtnSearchClicked(self):
    for i in pendingPayment:
        if i["usageNo"] == self.txtUsageNo.text():
            self.usageObj = i
            self.costOfWater = i["amountUSD"]
            self.totalAmount = self.costOfWater + 0.50
            print(self.usageObj)
            self.lblCostOfWater.setText(str(self.costOfWater))
            self.lblTotal.setText(str(self.totalAmount))
            break

def onBtnCancelClicked(self):
    openWindowWithData(self.mainWindow, self.previousWindow, self.user)
def onBtnOkClicked(self):
    if self.totalAmount <= self.user["balanceUSD"]:
        self.user["balanceUSD"] = self.user["balanceUSD"] - self.totalAmount
        pendingPayment.remove(self.usageObj)
        print(pendingPayment)
        openWindowWithData(
            self.mainWindow,
            dialog,
            [
                self.user,
                self.previousWindow,
                {"title": "Successfully, ", "content": "Water paid, don't forget to take your receipt."}
            ]
        )
    else:
        openWindowWithData(
            self.mainWindow,
            dialog,
            [
                self.user,
                self.previousWindow,
                {"title": "Sorry,", "content": "You don't have enough balance."}
            ]
        )


class WaterPayment(object):
    def __init__(self, obj):
        self.mainWindow = obj[0]
        self.user = obj[1][0]
        print(self.user)
        self.previousWindow = obj[1][1]

        # self.pendingPayment = [
        #     {"usageNo": "1000000000", "amountUSD": 11},
        #     {"usageNo": "1000000001", "amountUSD": 5},
        #     {"usageNo": "1000000002", "amountUSD": 7.5},
        #     {"usageNo": "1000000003", "amountUSD": 4.5}
        # ]
        self.costOfWater = None
        self.totalAmount = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: #0B3A97")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(140, 20, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("color: white")
        self.lblTitle.setObjectName("lblTitle")
        self.lblAccountNo = QtWidgets.QLabel(self.centralwidget)
        self.lblAccountNo.setGeometry(QtCore.QRect(250, 100, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblAccountNo.setFont(font)
        self.lblAccountNo.setStyleSheet("color: white")
        self.lblAccountNo.setObjectName("lblAccountNo")
        self.txtUsageNo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsageNo.setGeometry(QtCore.QRect(90, 200, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txtUsageNo.setFont(font)
        self.txtUsageNo.setStyleSheet("color: white")
        self.txtUsageNo.setMaxLength(10)
        self.txtUsageNo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtUsageNo.setObjectName("txtUsageNo")
        self.txtUsageNo.setText("1000000000")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setObjectName("label_4")
        self.lblCostOfService = QtWidgets.QLabel(self.centralwidget)
        self.lblCostOfService.setGeometry(QtCore.QRect(300, 270, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCostOfService.setFont(font)
        self.lblCostOfService.setStyleSheet("color: white")
        self.lblCostOfService.setObjectName("lblCostOfService")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 310, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white")
        self.label_6.setObjectName("label_6")
        self.lblCostOfWater = QtWidgets.QLabel(self.centralwidget)
        self.lblCostOfWater.setGeometry(QtCore.QRect(300, 310, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCostOfWater.setFont(font)
        self.lblCostOfWater.setStyleSheet("color: white")
        self.lblCostOfWater.setObjectName("lblCostOfWater")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white")
        self.label_8.setObjectName("label_8")
        self.lblTotal = QtWidgets.QLabel(self.centralwidget)
        self.lblTotal.setGeometry(QtCore.QRect(300, 350, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTotal.setFont(font)
        self.lblTotal.setStyleSheet("color: white")
        self.lblTotal.setObjectName("lblTotal")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(530, 400, 91, 31))
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
        self.btnOk.setGeometry(QtCore.QRect(430, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnOk.setFont(font)
        self.btnOk.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(lambda : onBtnOkClicked(self))
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(460, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnSearch.setFont(font)
        self.btnSearch.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnSearch.setObjectName("btnSearch")
        self. btnSearch.clicked.connect(lambda : onBtnSearchClicked(self))
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
        self.label.setText(_translate("MainWindow", "Pay from account:"))
        self.lblTitle.setText(_translate("MainWindow", "Water Supply Authority"))
        self.lblAccountNo.setText(_translate("MainWindow", self.user["accountNo"]))
        self.label_3.setText(_translate("MainWindow", "Please enter the usage number:"))
        self.label_4.setText(_translate("MainWindow", "Cost of service:"))
        self.lblCostOfService.setText(_translate("MainWindow", "0.50"))
        self.label_6.setText(_translate("MainWindow", "Cost of water usage:"))
        self.lblCostOfWater.setText(_translate("MainWindow", str(self.costOfWater)))
        self.label_8.setText(_translate("MainWindow", "Total:"))
        self.lblTotal.setText(_translate("MainWindow", str(self.totalAmount)))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.btnOk.setText(_translate("MainWindow", "Ok"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WaterPayment()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

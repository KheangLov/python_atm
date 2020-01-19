
from PyQt5 import QtCore, QtGui, QtWidgets
# from Utils.func import openWindow, applicationExit, openWindowWithData
from Atm.payments import Payments
from Atm.withdraw import Withdraw
from Atm.deposit import Deposit
# from Atm.login import Login
from Modules.__init__ import *
user = {}

name = None
accountBalance = 0
mainWindow = None
login = None

def logout(self):
    print("Logout")

def onBtnGetCashClicked(self):
    openWindowWithData(self.mainWindow, Withdraw, [self.user, Atm, Withdraw])

def onBtnPaymentClicked(self):
    openWindowWithData(self.mainWindow, Payments, [self.user, Atm, Payments])

def onBtnDepositClicked(self):
    openWindowWithData(self.mainWindow, Deposit, [self.user, Atm])

def onBtnAccountSettingCliced(self):
    self.window = QtWidgets.QMainWindow()

# def onLblCardReturnClicked(self):
#     openWindowWithData(self.mainWindow, Login, self.user)

class Atm(object):
    def __init__(self, obj):
        self.mainWindow = obj[0]
        self.user = obj[1]
        print('Login by userID: ', self.user)
        # self.name = userObj["name"]
        self.name = self.user["name"]
        # self.accountBalance = userObj["balanceUSD"]
        self.accountBalance = self.user["balanceUSD"]
        # for i in account:
        #     if (self.user["id"] == i["userID"]):
        #         if (i["accountTypeID"] == 1):
        #             self.savingAccountBalance = i["balance"]
        #             print('savingAccountBalance: ', self.savingAccountBalance)
        #         if (i["accountTypeID"] == 2):
        #             self.currentAccountBalance = i["balance"]
        #             print('currentAccountBalance: ', self.currentAccountBalance)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #0B3A97")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #00CAFB")
        self.label_2.setObjectName("label_2")
        self.lblUsername = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername.setGeometry(QtCore.QRect(50, 240, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsername.setFont(font)
        self.lblUsername.setStyleSheet("color: white")
        self.lblUsername.setObjectName("lblUsername")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 340, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #00CAFB")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 400, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #00CAFB")
        self.label_7.setObjectName("label_7")
        self.btnGetCash = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetCash.setGeometry(QtCore.QRect(290, 180, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnGetCash.setFont(font)
        self.btnGetCash.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnGetCash.setObjectName("btnGetCash")
        self.btnDeposit = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeposit.setGeometry(QtCore.QRect(510, 180, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnDeposit.setFont(font)
        self.btnDeposit.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnDeposit.setObjectName("btnDeposit")
        self.btnDeposit.clicked.connect(lambda : onBtnDepositClicked(self))
        self.btnPayments = QtWidgets.QPushButton(self.centralwidget)
        self.btnPayments.setGeometry(QtCore.QRect(290, 270, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnPayments.setFont(font)
        self.btnPayments.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnPayments.setObjectName("btnPayments")
        self.btnPayments.clicked.connect(lambda : onBtnPaymentClicked(self))
        self.btnCreditCard = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreditCard.setGeometry(QtCore.QRect(510, 270, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnCreditCard.setFont(font)
        self.btnCreditCard.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnCreditCard.setObjectName("btnCreditCard")
        self.btnAccountSetting = QtWidgets.QPushButton(self.centralwidget)
        self.btnAccountSetting.setGeometry(QtCore.QRect(290, 360, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnAccountSetting.setFont(font)
        self.btnAccountSetting.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnAccountSetting.setObjectName("btnAccountSetting")
        self.btnOther = QtWidgets.QPushButton(self.centralwidget)
        self.btnOther.setGeometry(QtCore.QRect(510, 360, 201, 71))
        self.btnAccountSetting.clicked.connect(lambda : onBtnAccountSettingCliced(self))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnOther.setFont(font)
        self.btnOther.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnOther.setObjectName("btnOther")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 490, 421, 41))
        self.label_8.setStyleSheet("background-color: #F6006B")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 500, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"background-color: rgb(246, 0, 107); color: white;")
        self.label_9.setObjectName("label_9")
        self.lblAccount = QtWidgets.QLabel(self.centralwidget)
        self.lblAccount.setGeometry(QtCore.QRect(80, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblAccount.setFont(font)
        self.lblAccount.setStyleSheet("color: white")
        self.lblAccount.setObjectName("lblAccount")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 430, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white")
        self.label_6.setObjectName("label_6")
        self.lblSaving = QtWidgets.QLabel(self.centralwidget)
        self.lblSaving.setGeometry(QtCore.QRect(80, 430, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblSaving.setFont(font)
        self.lblSaving.setStyleSheet("color: white")
        self.lblSaving.setObjectName("lblSaving")
        self.lblAmount = QtWidgets.QLabel(self.centralwidget)
        self.lblAmount.setGeometry(QtCore.QRect(360, 500, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblAmount.setFont(font)
        self.lblAmount.setStyleSheet("\n"
"background-color: rgb(246, 0, 107); color: white;")
        self.lblAmount.setObjectName("lblAmount")
        self.lblUsername_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername_2.setGeometry(QtCore.QRect(610, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsername_2.setFont(font)
        self.lblUsername_2.setStyleSheet("color: white")
        self.lblUsername_2.setObjectName("lblUsername_2")
        # self.lblUsername_2.mousePressEvent(lambda : logout(self))
        self.lblUsername_2.linkActivated.connect(lambda : self.onLblCardReturnClicked(self))
        # self.lblUsername_2.mouseDoubleClickEvent(logout(self))
        self.lblQickCash = QtWidgets.QLabel(self.centralwidget)
        self.lblQickCash.setGeometry(QtCore.QRect(580, 500, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblQickCash.setFont(font)
        self.lblQickCash.setStyleSheet("\n"
"background-color: rgb(246, 0, 107); color: white;")
        self.lblQickCash.setObjectName("lblQickCash")
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lblUsername.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.btnGetCash.raise_()
        self.btnGetCash.clicked.connect(lambda : onBtnGetCashClicked(self))
        self.btnDeposit.raise_()
        self.btnPayments.raise_()
        self.btnCreditCard.raise_()
        self.btnAccountSetting.raise_()
        self.btnOther.raise_()
        self.label_9.raise_()
        self.lblAccount.raise_()
        self.label_6.raise_()
        self.lblSaving.raise_()
        self.lblAmount.raise_()
        self.lblUsername_2.raise_()
        self.lblQickCash.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 21))
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
        self.label.setText(_translate("MainWindow", "ATM"))
        self.label_2.setText(_translate("MainWindow", "Welcome"))
        self.lblUsername.setText(_translate("MainWindow", self.name))
        self.label_4.setText(_translate("MainWindow", "$"))
        self.label_5.setText(_translate("MainWindow", "Account #1"))
        # self.label_7.setText(_translate("MainWindow", "Saving #2"))
        self.btnGetCash.setText(_translate("MainWindow", "Get Cash"))
        self.btnDeposit.setText(_translate("MainWindow", "Deposit"))
        self.btnPayments.setText(_translate("MainWindow", "Payments"))
        self.btnCreditCard.setText(_translate("MainWindow", "Credit Card"))
        self.btnAccountSetting.setText(_translate("MainWindow", "Account Setting"))
        self.btnOther.setText(_translate("MainWindow", "Other"))
        self.label_9.setText(_translate("MainWindow", "$"))
        self.lblAccount.setText(_translate("MainWindow", str(self.accountBalance)))
        # self.label_6.setText(_translate("MainWindow", "$"))
        # self.lblSaving.setText(_translate("MainWindow", str(self.savingAccountBalance)))
        # self.lblAmount.setText(_translate("MainWindow", "70"))
        self.lblUsername_2.setText(_translate("MainWindow", "Card Return"))
        self.lblQickCash.setText(_translate("MainWindow", "Qick Cash"))

    def onBtnGetCashClicked(self):
        print('Button Get Cash Clicked')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Atm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

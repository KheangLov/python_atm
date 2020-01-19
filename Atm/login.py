from PyQt5 import QtCore, QtGui, QtWidgets
from Atm.atm import Atm
# from Atm.dashboard import Dashboard
from Utils.func import openWindowWithData
from Modules.__init__ import *

# userList = [{"id": 1, "username": "sokleang", "pwd": "123"}, {"id": 2, "username": "kheang", "pwd": "123"}]
language = ["KHR", "ENG"]

userList = [
    {"id": "1011801", "name": "Mr. Sok", "accountNo": "0000011110001", "password": "123456", "balanceUSD": 100, "active": "Yes"},
    {"id": "1011805", "name": "Mr. Pyna", "accountNo": "0000011110002", "password": "123456", "balanceUSD": 100, "active": "Yes"},
    {"id": "1011804", "name": "Mr. Born", "accountNo": "0000011110003", "password": "123456", "balanceUSD": 100, "active": "Yes"},
    {"id": "1011903", "name": "Ms. Rita", "accountNo": "0000011110004", "password": "123456", "balanceUSD": 0, "active": "No"},
]

def onBtnLoginClicked(self):
    for i in userList:
        if (self.txtUsername.text() == i['accountNo'] and self.txtPassword.text() == i['password']):
            print('Username and password correct.')
            if (i["active"] == "Yes"):
                # openWindows(self, i)
                self.window = QtWidgets.QMainWindow()
                openWindowWithData(MainWindow, Atm, i)
                # MainWindow.hide()
                break
            else:
                print("Your account is deactivated!")
        else:
            print("incorrent account number or password")

def openWindows(self, userObj):
    self.window = QtWidgets.QMainWindow()
    self.userObj = userObj
    self.ui = Atm(self.userObj)
    self.ui.setupUi(self.window)
    self.window.show()
    Ui_MainWindow.hide()


class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 386)
        MainWindow.setStyleSheet("background-color: #0B3A97")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblUsername = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername.setGeometry(QtCore.QRect(110, 40, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsername.setFont(font)
        self.lblUsername.setStyleSheet("color: white")
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername_2.setGeometry(QtCore.QRect(210, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblUsername_2.setFont(font)
        self.lblUsername_2.setStyleSheet("color: white")
        self.lblUsername_2.setObjectName("lblUsername_2")
        self.lblUsername_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername_3.setGeometry(QtCore.QRect(80, 150, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblUsername_3.setFont(font)
        self.lblUsername_3.setStyleSheet("color: white")
        self.lblUsername_3.setObjectName("lblUsername_3")
        self.txtUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsername.setGeometry(QtCore.QRect(190, 150, 351, 31))
        self.txtUsername.setText('0000011110001')
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txtUsername.setFont(font)
        self.txtUsername.setStyleSheet("color: white")
        self.txtUsername.setMaxLength(20)
        self.txtUsername.setObjectName("txtUsername")
        self.lblUsername_4 = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername_4.setGeometry(QtCore.QRect(80, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblUsername_4.setFont(font)
        self.lblUsername_4.setStyleSheet("color: white")
        self.lblUsername_4.setObjectName("lblUsername_4")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(190, 210, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.txtPassword.setFont(font)
        self.txtPassword.setStyleSheet("color: white")
        self.txtPassword.setInputMask("")
        self.txtPassword.setText("123456")
        self.txtPassword.setMaxLength(20)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setReadOnly(False)
        self.txtPassword.setObjectName("txtPassword")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(430, 270, 111, 31))
        self.btnLogin.clicked.connect(lambda : onBtnLoginClicked(self))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btnLogin.setObjectName("btnLogin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 21))
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
        self.lblUsername.setText(_translate("MainWindow", "ATM Machine Transaction"))
        self.lblUsername_2.setText(_translate("MainWindow", "Please login to continues..."))
        self.lblUsername_3.setText(_translate("MainWindow", "AccountNo:"))
        self.lblUsername_4.setText(_translate("MainWindow", "Password:"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle('ATM Machine Transaction')
    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

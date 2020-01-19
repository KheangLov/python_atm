from PyQt5 import QtCore
from PyQt5.uic.properties import QtWidgets

# from Atm.deposit import Deposit
# from Atm.cashWithdraw import CashWithdraw
# from Atm.atm import Atm


def openWindowWithData(qMainWindow, className, obj):

    # self.window = qMainWindow
    ui = className([qMainWindow, obj])
    ui.setupUi(qMainWindow)
    # qMainWindow.show()
    # qMainWindow.hide()



def openWindow(self, qMainWindow, className):
    self.window = qMainWindow
    self.ui = className()
    self.ui.setupUi(self.window)
    self.window.show()

def applicationExit():
    QtCore.QCoreApplication.instance().quit()

def hideWindow(self):
    self.window = QtWidgets.QMainWindow()

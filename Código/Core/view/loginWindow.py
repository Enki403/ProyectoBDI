import sys
from PyQt5 import uic, QtWidgets

Ui_MainWindow, QtBaseClass = uic.loadUiType("LoginWindow.ui")

class Login(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setGeometry(550,140,413,578)


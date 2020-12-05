# from tkinterApp.draw import *
# from view.login import *
# from view.portada_rc import *
from Core.view.login import Ui_Login
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# from Core.view import *
from Core.tkinterApp.draw import DrawingApplication
from Core.tkinterApp import *
# from Core.view.login import Ui_Login
# from PyQt5 import QtCore, QtGui, QtWidgets

import turtle
import tkinter.colorchooser
import tkinter.filedialog

class Controller:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        Login = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(Login)
        self.ui.buttonLogin.clicked.connect(self.appTkinter)
        Login.show()
        sys.exit(self.app.exec_())
        
    def appTkinter(self):
        root = tkinter.Tk()
        drawingApp = DrawingApplication(root)
        drawingApp.mainloop()
        print("Program Execution Completed.")

# controller = Controller()


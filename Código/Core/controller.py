from Core.draw import *
from Core.login import *
import sys


class Controller:
    def __init__(self):
        pass

    def authentication(self,username,password,Login):
            Login.hide()
            root = tkinter.Tk()
            drawingApp = DrawingApplication(root)
            drawingApp.mainloop()
            print("Program Execution Completed.")



        
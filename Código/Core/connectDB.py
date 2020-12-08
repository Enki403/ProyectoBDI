from Core.draw import *
import sys

class ConnectDB:
    def __init__(self):
        pass

    def validateLogin(self,username,password,Login):
        if(True):
            Login.hide()    
            root = tkinter.Tk()
            admin = self.isAdmin(username,password)
            drawingApp = DrawingApplication(root,admin)
            drawingApp.mainloop()
            print("Program Execution Completed.")
            sys.exit(0)

    def isUser(self,username,password):
        stade = True
        return stade

    def isAdmin(self,username,password):
        return True




from Core.draw import *
from Core.connection import *
import configparser
import sys

class StartApplication:
    def __init__(self,credentials):
        self.credentials = credentials

    def validateLogin(self,username,password,Login):

        conect = ConnectionDB(self.credentials)
        user = username.text()
        passw = password.text()

        if(conect.validateUser(user,passw)):

            Login.hide()    
            root = tkinter.Tk()
            admin = self.isAdmin(username,password)
            drawingApp = DrawingApplication(self.credentials,root,admin)
            drawingApp.mainloop()
            print("Program Execution Completed.")
            sys.exit(0)
        else:
            username.setText('INVALID USER')

    def isAdmin(self,username,password):
        return True




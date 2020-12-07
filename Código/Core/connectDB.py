from Core.draw import *
from Core.dbConfig import *
import sys

class ConnectDB:
    def __init__(self):
       db = DBConfig()

    def validateLogin(self,username,password,Login):
        if(self.isUser(username,password)):
            Login.hide()    
            root = tkinter.Tk()
            admin = self.isAdmin(username,password)
            drawingApp = DrawingApplication(root,admin)
            drawingApp.mainloop()
            print("Program Execution Completed.")
            sys.exit(0)

    def isUser(self,username,password):
        stade = True
        # self.mycursor.execute('SELECT * FROM User')
            # for x in self.mycursor
        #     if (username ==x[1] and password ==[2] ):
        #         stade = True
        #     else: stade = False
        return stade

    def isAdmin(self,username,password):
        return True




from Core.draw import *
# import mysql.connector

class ConnectDB:
    def __init__(self):
        # self.cnx = mysql.connector.connect(user='admin',password='admin',host='192.168.0.13',database='testUser')
        # print(self.cnx)
        pass

    def validateLogin(self,username,password,Login):
        if(self.isUser(username,password)):
            Login.hide()    
            root = tkinter.Tk()
            admin = self.isAdmin(username,password)
            drawingApp = DrawingApplication(root,admin)
            drawingApp.mainloop()
            print("Program Execution Completed.")

    def isUser(self,username,password):
        return True

    def isAdmin(self,username,password):
        return True




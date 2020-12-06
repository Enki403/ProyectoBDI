from Core.draw import *

def openTkinterApp(username,password,Login,ui):
    Login.hide()
    root = tkinter.Tk()
    drawingApp = DrawingApplication(ui,root)
    drawingApp.mainloop()
    print("Program Execution Completed.")

# def closeAppFunction():
    # root = tkinter.Tk()
    # drawingApp = DrawingApplication(root)
    # drawingApp.
    # print("Program Execution Completed.")
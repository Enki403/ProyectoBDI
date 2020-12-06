from Core.draw import *

def openTkinterApp(username,password,Login):
    Login.hide()
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)
    drawingApp.mainloop()
    print("Program Execution Completed.")

# def closeAppFunction():
    # root = tkinter.Tk()
    # drawingApp = DrawingApplication(root)
    # drawingApp.
    # print("Program Execution Completed.")
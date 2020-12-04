import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import json
from tkinter_app.drawCommands import *
from tkinter_app.drawActions import *
from tkinter_app.drawTools import *


class DrawingApplication(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.tkinter = tkinter
        self.initializeDrawVariables()
    def getT(self):
        return self.tkinter
    def initializeDrawVariables(self):
        self.master.title("Draw")
        self.bar = self.tkinter.Menu(self.master)
        self.fileMenu = self.tkinter.Menu(self.bar, tearoff = 0)

        self.pack()

        canvas = self.tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=self.tkinter.LEFT)

        self.theTurtle = turtle.RawTurtle(canvas)
        self.theTurtle.shape("circle")
        
        self.screen = self.theTurtle.getscreen()
        self.graphicsCommands = PyList()
        self.buildWindow()
        
        self.action = (DrawAction(self.fileMenu, self.theTurtle, self.screen, self.graphicsCommands))
        self.createDrawActions()
    
    def createDrawActions(self):
        self.fileMenu.add_command(label="New", command=self.action.newWindow)
        self.fileMenu.add_command(label="Load",command=self.action.loadFile)
        self.fileMenu.add_command(label="Save As",command=self.action.saveFile)
        self.fileMenu.add_command(label="Download",command=self.action.downloadFile)
        self.fileMenu.add_command(label="Configuration",command=self.action.openConfigDialog)
        self.fileMenu.add_command(label="Exit",command=self.master.quit)

    def buildWindow(self):
        print('self.tkinter: ', self.tkinter)
        self.screen.tracer(0)
        self.bar.add_cascade(label="File", menu=self.fileMenu)
        self.master.config(menu=self.bar)
        self.sideBar = self.tkinter.Frame(self,padx=5,pady=5)
        self.sideBar.pack(side=self.tkinter.RIGHT, fill=self.tkinter.BOTH)
        self.tools = (DrawTools(self.graphicsCommands, self.theTurtle, self.screen, self.sideBar, self.master, self))

        pointLabel = self.tkinter.Label(self.sideBar, text="Width")
        pointLabel.pack()

        """ widthSize = self.tkinter.StringVar()
        widthEntry = self.tkinter.Entry(self.sideBar,textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))

        radiusLabel = self.tkinter.Label(self.sideBar, text="Radius")
        radiusLabel.pack()
        radiusSize = self.tkinter.StringVar()
        radiusEntry = self.tkinter.Entry(self.sideBar,textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack() """

        def circleHandler():
            cmd = CircleCommand(float (radiusSize.get()), float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

            screen.update()
            screen.listen()

        circleButton = self.tkinter.Button(self.sideBar, text = "Draw_Circle", command=self.tools.circleHandler)
        circleButton.pack(fill=self.tkinter.BOTH)

        self.screen.colormode(255)
        penLabel = self.tkinter.Label(self.sideBar, text="Pen_Color")
        penLabel.pack()
        penColor = self.tkinter.StringVar()
        penEntry = self.tkinter.Entry(self.sideBar, textvariable=penColor)
        penEntry.pack()

        penColor.set("#000000")

        def getPenColor():
            color = self.tkinter.colorchooser.askcolor()
            if color != None:
                penColor.set(str(color)[-9:-2])

        penColorButton = self.tkinter.Button(self.sideBar, text="Pick_Pen_Color", command=getPenColor)
        penColorButton.pack(fill=self.tkinter.BOTH)

        fillLabel = self.tkinter.Label(self.sideBar, text="Fill_Color")
        fillLabel.pack()
        fillColor = self.tkinter.StringVar()
        fillEntry = self.tkinter.Entry(self.sideBar, textvariable=fillColor)
        fillEntry.pack()
        fillColor.set("#000000")

        def getFillColor():
            color = self.tkinter.colorchooser.askcolor()
            if color != None:
                fillColor.set(str(color)[-9: -2])

        fillColorButton = \
            self.tkinter.Button(self.sideBar, text="Pick_Fill_Color", command=getFillColor)
        fillColorButton.pack(fill=self.tkinter.BOTH)

        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)

        beginFillButton = self.tkinter.Button(self.sideBar, text = "Begin_Fill", command=beginFillHandler)
        beginFillButton.pack(fill=self.tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)

        endFillButton = self.tkinter.Button(self.sideBar, text="End_fill", command=endFillHandler)
        endFillButton.pack(fill=self.tkinter.BOTH)

        penLabel= self.tkinter.Label(self.sideBar, text="Pen_Is_Down")
        penLabel.pack()

        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(self.theTurtle)
            penLabel.configure(text="Pen_Is_Up")
            self.graphicsCommands.append(cmd)

        penUpButton = self.tkinter.Button(self.sideBar, text="Pen_Up", command=penUpHandler)
        penUpButton.pack(fill=self.tkinter.BOTH)

        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(self.theTurtle)
            penLabel.configure(text="Pen_Is_Down")
            self.graphicsCommands.append(cmd)

        penDownButton = self.tkinter.Button(self.sideBar, text="Pen_Down", command=penDownHandler)
        penDownButton.pack(fill=self.tkinter.BOTH)

        def clickHandler(x, y):
            cmd = GoToCommand(x, y, float(widthSize.get()), penColor.get())
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)
            self.screen.update()
            self.screen.listen()

        def dragHandler(x, y):
            """ widthSize = self.tkinter.StringVar()
            widthEntry = self.tkinter.Entry(self.sideBar,textvariable=widthSize)
            widthEntry.pack()
            widthSize.set(str(1)) """
            print('width', widthSize.get())

            cmd = GoToCommand(x, y, float(widthSize.get()), penColor.get())
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)
            self.screen.update()
            self.screen.listen()

        self.theTurtle.ondrag(dragHandler)

        def undoHandler():
            print('undoHandler')
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.removeLast()
                self.theTurtle.clear()
                self.theTurtle.penup()
                self.theTurtle.goto(0, 0)
                self.theTurtle.pendown()

                for cmd in self.graphicsCommands:
                    cmd.draw(self.theTurtle)
                self.screen.update()
                self.screen.listen()

        self.screen.onkeypress(undoHandler, "u")
        self.screen.listen()

    

""" def main():
    root = self.tkinter.Tk()
    drawingApp = DrawingApplication(root)

    drawingApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main() """
import turtle
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import json
from tkinter_app.drawCommands import *
from tkinter_app.drawActions import *


class DrawTools():
    def __init__(self, graphicsCommands, theTurtle, screen, sideBar, master, ob):
        self.graphicsCommands = graphicsCommands
        self.theTurtle = theTurtle
        self.screen = screen
        self.sideBar = sideBar
        self.master = master
        self.app = ob
        self.tkinter = self.app.tkinter
        self.radiusSize = self.tkinter.StringVar()
        self.radiusEntry = self.tkinter.Entry(self.sideBar,textvariable=self.radiusSize)
        self.radiusSize.set(str(10))

        self.widthSize = self.tkinter.StringVar()
        self.widthEntry = self.tkinter.Entry(self.sideBar,textvariable=self.widthSize)
        self.widthEntry.pack()
        self.widthSize.set(str(1))
        self.penLabel = self.tkinter.Label(self.sideBar, text="Pen_Color")
        self.penLabel.pack()
        self.penColor = self.tkinter.StringVar()
        self.penEntry = self.tkinter.Entry(self.sideBar, textvariable=self.penColor)
        self.penEntry.pack()
        self.penColor.set("#000000")
    
    def circleHandler(self):
        self.screen.update()
        self.screen.listen()
        print('Creando circulo: ', self.app.getT())
        self.tkinter = self.app.getT()
        
        print('radius', self.tkinter.StringVar().get())
        print('width', self.widthSize.get())
        print('color', self.penColor.get())

        cmd = CircleCommand(float (self.radiusSize.get()), float(self.widthSize.get()), self.penColor.get())
        cmd.draw(self.theTurtle)
        self.graphicsCommands.append(cmd)
        print('self graphics: ', self.graphicsCommands)

        self.screen.update()
        self.screen.listen()
    
        
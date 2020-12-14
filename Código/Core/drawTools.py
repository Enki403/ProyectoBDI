# -*- coding: utf-8 -*-
"""
    @author hjvasquez@unah.hn
    @author nelson.sambula@unah.hn
    @author lggutierrez@unah.hn
    @author renata.dubon@unah.hn
    @date 12/12/2020
    @version 0.1
"""

import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
from Core.drawCommands import *
from Core.drawActions import *
import json
import turtle

class DrawTools():
    """
        ! Clase DrawTools
    """
    def __init__(self, app):
        self.app = app

    def circleHandler(self):
        app = self.app.getApp() 
        app.screen.update()
        app.screen.listen()
        cmd = CircleCommand(float (app.radiusSize.get()), float(app.widthSize.get()), app.penColor.get())
        cmd.draw(app.theTurtle)
        app.graphicsCommands.append(cmd)

        app.screen.update()
        app.screen.listen()
    
    def getPenColor(self):
        app = self.app.getApp()
        color = app.tkinter.colorchooser.askcolor()
        if color != None:
            app.penColor.set(str(color)[-9:-2])
    
    def getFillColor(self):
        app = self.app.getApp()
        color = app.tkinter.colorchooser.askcolor()
        if color != None:
            app.fillColor.set(str(color)[-9: -2])
    
    def beginFillHandler(self):
        app = self.app.getApp()
        cmd = BeginFillCommand(app.fillColor.get())
        cmd.draw(app.theTurtle)
        app.graphicsCommands.append(cmd)
    
    def endFillHandler(self):
        app = self.app.getApp()
        cmd = EndFillCommand()
        cmd.draw(app.theTurtle)
        app.graphicsCommands.append(cmd)

    def penUpHandler(self):
        app = self.app.getApp()
        cmd = PenUpCommand()
        cmd.draw(app.theTurtle)
        app.penLabel.configure(text="Pen_Is_Up")
        app.graphicsCommands.append(cmd)

    def penDownHandler(self):
        app = self.app.getApp()
        cmd = PenDownCommand()
        cmd.draw(app.theTurtle)
        app.penLabel.configure(text="Pen_Is_Down")
        app.graphicsCommands.append(cmd)

    def dragHandler(self, x, y):
        dt = self.app.getApp() 
        cmd = GoToCommand(x, y, float(dt.widthSize.get()), dt.penColor.get())
        cmd.draw(dt.theTurtle)
        dt.graphicsCommands.append(cmd)
        dt.screen.update()
        dt.screen.listen()
    
    def undoHandler(self):
        print('undoHandler')
        dt = self.app.getApp()
        if len(self.graphicsCommands) > 0:
            dt.graphicsCommands.removeLast()
            dt.theTurtle.clear()
            dt.theTurtle.penup()
            dt.theTurtle.goto(0, 0)
            dt.theTurtle.pendown()

            for cmd in dt.graphicsCommands:
                cmd.draw(self.theTurtle)
            dt.screen.update()
            dt.screen.listen()
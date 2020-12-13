# -*- coding: utf-8 -*-
"""
    @author hjvasquez@unah.hn
    @author nelson.sambula@unah.hn
    @author lggutierrez@unah.hn
    @author renata.dubon@unah.hn
    @date 12/12/2020
    @version 0.1
"""
import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import json
from Core.drawCommands import *
from Core.drawActions import *
from Core.configure import *

class DrawAction():
    """
        ! Clase DrawAction
        * La clase contiene todas las acciones respecto al dibujo en referencia a la Base de Datos
        * @constructor fileMenu
        * @constructor theTurtle
        * @constructor screen
    """
    def __init__(self, fileMenu=None, theTurtle = None, screen = None, graphicsCommands = None, app = None):
        self.fileMenu_ = fileMenu
        self.theTurtle = theTurtle
        self.screen = screen
        self.graphicsCommands = graphicsCommands
        self.app = app

    def newWindow(self):
        """
            * Limpia la ventana de dibujo actual.
        """
        print('Limpiando la ventana...')
        self.theTurtle.clear()
        self.theTurtle.penup()
        self.theTurtle.goto(0,0)
        self.theTurtle.pendown()
        self.screen.update()
        self.screen.listen()
        self.graphicsCommands = PyList()
    
    def saveFile(self):
        """
            * Realiza el guardado de los registros del dibujo realizado, escribiendolos en formato JSON en un .json
        """
        print('Guardando dibujo...')
        filename = tkinter.filedialog.asksaveasfilename(title="Save Picture AS...")
        self.write(filename + '.json')
    
    def parse(self, data):
        """
            * Realizar un parseo de los registros de un archivo, para convertirtir el dibujo que representa.
        """
        dt = self.app.getApp()
        dict_ = data['data']
        for key in dict_:
            print('key: ', key)
            current = dict_[str(key)]
            command = current['command']
            if command == "GoTo":
                x = float(current["x"])
                y = float(current["y"])
                width = float(current["width"])
                color = current["color"].strip()
                cmd = GoToCommand(x,y,width,color)
            elif command == "Circle":
                radius = float(current["radius"])
                width = float(current["width"])
                color = current["color"].strip()
                cmd = CircleCommand(radius,width,color)

            elif command == "BeginFill":
                color = current["color"].strip()
                cmd = BeginFillCommand(color)

            elif command == "EndFill":
                cmd = EndFillCommand()

            elif command == "PenUp":
                cmd = PenUpCommand()

            elif command == "PenDown":
                cmd = PenDownCommand()

            else:
                raise RuntimeError("Unknown Command:" + command)
            dt.graphicsCommands.append(cmd)

    def write(self, filename):
        file = open(filename, "w")
        file.write('{\n')
        json = {}
        c = 0
        for cmd in self.graphicsCommands:
            c = c + 1
            key = '"%s": %s' % (c, cmd)
            if c is len(self.graphicsCommands):
                file.write('    '+str(key)+"\n")
            else:
                file.write('    '+str(key)+",\n")
        file.write('}')
        file.close()

    

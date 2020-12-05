import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import json
from tkinterApp.drawCommands import *
from tkinterApp.drawActions import *

"""
* La clase contiene todas las acciones respecto al dibujo en referencia a la Base de Datos
* @constructor fileMenu
* @constructor theTurtle
* @constructor screen
"""
class DrawAction():
    def __init__(self, fileMenu=None, theTurtle = None, screen = None, graphicsCommands = None, app = None):
        self.fileMenu_ = fileMenu
        self.theTurtle = theTurtle
        self.screen = screen
        self.graphicsCommands = graphicsCommands
        self.app = app

    """
    * Limpia la ventana de dibujo actual.
    """
    def newWindow(self):
            print('Limpiando la ventana...')
            self.theTurtle.clear()
            self.theTurtle.penup()
            self.theTurtle.goto(0,0)
            self.theTurtle.pendown()
            self.screen.update()
            self.screen.listen()
            self.graphicsCommands = PyList()
    """
    * Abre una ventana de dialogo con la lista de los dibujos guardados por el usuario que ejecute la accion.
    * Permitiendo la seleccion de dibujo para posteriormente cargar dicho dibujo en la ventana y mostrarlo.
    """
    def loadFile(self):
        dt = self.app.getApp()
        print('Abriendo ventana de dialogo para cargar dibujo...')
        filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")
        self.newWindow()
        self.graphicsCommands = PyList()
        self.parse(filename)
        for cmd in dt.graphicsCommands:
            cmd.draw(dt.theTurtle)

    """
    * Realiza el guardado de los registros del dibujo realizado, escribiendolos en formato JSON en un .json
    """
    def saveFile(self):
        print('Guardando dibujo...')
        filename = tkinter.filedialog.asksaveasfilename(title="Save Picture AS...")
        self.write(filename + '.json')
    
    """
    * Permite descargar los registros del dibujo actual en la ventana de dibujo, este se guarda en formato JSON.
    """
    def downloadFile(self):
        print('Descargando dibujo')
    
    """
    * Abre la ventana de configuracion de la cual solo el usuario administrador puede acceder.
    """
    def openConfigDialog(self):
        print('Abriendo ventana de configuracion')
    
    """
    * Realizar un parseo de los registros de un archivo, para convertirtir el dibujo que representa.
    """
    def parse(self, filename):
            dt = self.app.getApp()
            print('fileNamae: ', filename)
            file = open(filename,'r')
            data = file.read()
            dict_ = json.loads(data)
            file.close()
            for key in dict_:
                current = dict_[key]
                print('current: ', current)
                command = current['command']
                if command == "GoTo":
                    x = float(current["x"])
                    y = float(current["y"])
                    width = float(current["width"])
                    color = current["color"].strip()
                    cmd = GoToCommand(x,y,width,color)

                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = CircleCommand(radius,width,color)

                elif command == "BeginFill":
                    color = attr["color"].value.strip()
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
            """ for commandElement in graphicsCommands:
                print(type(commandElement))
                command = commandElement.firstChild.data.strip()
                attr = commandElement.attributes
                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = GoToCommand(x,y,width,color)
                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = CircleCommand(radius,width,color)
                elif command == "BeginFill":
                    color = attr["color"].value.strip()
                    cmd = BeginFillCommand(color)
                elif command == "EndFill":
                    cmd = EndFillCommand()
                elif command == "PenUp":
                    cmd = PenUpCommand()
                elif command == "PenDown":
                    cmd = PenDownCommand()
                else:
                    raise RuntimeError("Unknown Command:" + command)
                
                self.graphicsCommands.append(cmd) """

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
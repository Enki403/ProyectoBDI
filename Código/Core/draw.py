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
from Core.drawTools import *
from Core.load import *
from Core.save import *
from Core.connection import *


class DrawingApplication(tkinter.Frame):
    """
    ! Clase principal de la aplicacion de dibujo.
    * Inicializacion de las variables globales, cuales son bases y representacion del dibujo actual en ventana.
    * Se crea el menu de acciones respecto al dibujo.
    * Se hacen llamados a diferentes funciones que se encargan de construir el componente de dibujado.
    * Se construyen los componentes / herramientas para dibujar, permitidas por tkinter.
    * Se inicializan la clase de acciones sobre el dibujo, las cuales les permite al usuario decidir que hacer respecto a su dibujo.
    """
    def __init__(self,credentials, idUserLogin, master=None,admin=False):
        self.admin = admin
        self.credentials = credentials
        super().__init__(master)
        self.tkinter = tkinter
        self.turtle = turtle
        self.initializeDrawVariables()
        self.idUserLogin = idUserLogin


    def initializeDrawVariables(self):
        self.master.title("Draw")
        self.bar = self.tkinter.Menu(self.master)
        self.fileMenu = self.tkinter.Menu(self.bar, tearoff = 0)

        self.pack()

        canvas = self.tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=self.tkinter.LEFT)

        self.theTurtle = self.turtle.RawTurtle(canvas)
        self.theTurtle.shape("circle")
        
        self.screen = self.theTurtle.getscreen()
        self.graphicsCommands = PyList()
        self.buildWindow()
        
        self.action = (DrawAction(self.fileMenu, self.theTurtle, self.screen, self.graphicsCommands, self))
        self.createDrawActions()
    """
    * Se crea las acciones sobre el dibujo y se define la funcion a ejecutar al interactuar con una determinada accion.
    """
    def createDrawActions(self):
        self.fileMenu.add_command(label="New", command=self.newWindow)
        self.fileMenu.add_command(label="Load",command=self.loadMenu)
        self.fileMenu.add_command(label="Save As",command=self.saveMenu)
        # self.fileMenu.add_command(label="Download",command=self.action.downloadFile)
        if(self.admin):
            self.fileMenu.add_command(label="Configuration",command=self.configMenu)
        self.fileMenu.add_command(label="Exit",command=self.master.quit)
    
    def buildWindow(self):
        """
            * Construye los componentes de las herramientas de dibujo en la ventana.
            * A su vez se define la accion a ejecutar cuando se interactua con una herramienta de dibujo.
            * Se crea una pestana principal, la cual este desglosa las diferentes acciones que el usuario puede realizar.
        """
        self.screen.tracer(0)
        self.bar.add_cascade(label="File", menu=self.fileMenu)
        self.master.config(menu=self.bar)
        self.sideBar = self.tkinter.Frame(self,padx=5,pady=5)
        self.sideBar.pack(side=self.tkinter.RIGHT, fill=self.tkinter.BOTH)
        self.tools = (DrawTools(self))

        # Campo de ancho.
        self.widthSize = self.tkinter.StringVar()
        self.widthSize.set(str(1))
        pointLabel = self.tkinter.Label(self.sideBar, text="Width")
        pointLabel.pack()
        widthEntry = self.tkinter.Entry(self.sideBar,textvariable=self.widthSize)
        widthEntry.pack()

        # Campo de radio
        self.radiusSize = self.tkinter.StringVar()
        self.radiusSize.set(str(10))
        radiusLabel = tkinter.Label(self.sideBar, text="Radius")
        radiusLabel.pack()
        radiusEntry = self.tkinter.Entry(self.sideBar,textvariable=self.radiusSize)
        radiusEntry.pack()

        # Dibujar circulo
        circleButton = self.tkinter.Button(self.sideBar, text = "Draw_Circle", command=self.tools.circleHandler)
        circleButton.pack(fill=self.tkinter.BOTH)

        # Seleccion de color de pintado, color negro por defecto
        self.screen.colormode(255)
        self.penColor = self.tkinter.StringVar()
        self.penColor.set((ConnectionDB(self.credentials)).executeQueryRead("CALL sp_getConfig")[0][0])
        penLabel = self.tkinter.Label(self.sideBar, text="Pen_Color")
        penLabel.pack()
        penEntry = self.tkinter.Entry(self.sideBar, textvariable=self.penColor)
        penEntry.pack()

        penColorButton = self.tkinter.Button(self.sideBar, text="Pick_Pen_Color", command=self.tools.getPenColor)
        penColorButton.pack(fill=self.tkinter.BOTH)

        # Seleccion de relleno.
        self.fillColor = self.tkinter.StringVar()
        self.fillColor.set((ConnectionDB(self.credentials)).executeQueryRead("CALL sp_getConfig")[0][1])
        fillLabel = self.tkinter.Label(self.sideBar, text="Fill_Color")
        fillLabel.pack()
        fillEntry = self.tkinter.Entry(self.sideBar, textvariable=self.fillColor)
        fillEntry.pack()

        # Estableciendo el color y funcion respecto al relleno.
        fillColorButton = self.tkinter.Button(self.sideBar, text="Pick_Fill_Color", command=self.tools.getFillColor)
        fillColorButton.pack(fill=self.tkinter.BOTH)

        beginFillButton = self.tkinter.Button(self.sideBar, text = "Begin_Fill", command=self.tools.beginFillHandler)
        beginFillButton.pack(fill=self.tkinter.BOTH)

        endFillButton = self.tkinter.Button(self.sideBar, text="End_fill", command=self.tools.endFillHandler)
        endFillButton.pack(fill=self.tkinter.BOTH)

        self.penLabel= self.tkinter.Label(self.sideBar, text="Pen_Is_Down")
        self.penLabel.pack()

        penUpButton = self.tkinter.Button(self.sideBar, text="Pen_Up", command=self.tools.penUpHandler)
        penUpButton.pack(fill=self.tkinter.BOTH)

        penDownButton = self.tkinter.Button(self.sideBar, text="Pen_Down", command=self.tools.penDownHandler)
        penDownButton.pack(fill=self.tkinter.BOTH)

        self.theTurtle.ondrag(self.tools.dragHandler)

        self.screen.onkeypress(self.tools.undoHandler, "u")
        self.screen.listen()
    
   
    def getApp(self):
        """
            * Permite obtener la referencia a la clase principal del dibujo.
        """
        return self


    def configMenu(self):
        """
            * Permite mostrar el menu de configuracion al usuario administrador
        """
        tl = Toplevel()
        conf = Config(tl,self.credentials)

    def loadMenu(self):
        """
            * Permite abrir un menu para elegir un dibujo de la base de datos
        """
        tl = Toplevel()
        load = Load(tl,self.credentials, self.action, self, self.idUserLogin)

    def saveWindow(self):
        self.editWind = Toplevel()
        self.editWind.title = 'Save as ...'

        Label(self.editWind, text = 'Name:').grid(row = 4, column = 1)
        newName = Entry(self.editWind)
        newName.grid(row = 4, column = 2)
       
        Button(self.editWind, text = 'Save', command = lambda: self.saveMenu(newName.get())).grid(row = 5, column = 2, sticky = W)
        
        self.editWind.mainloop()
        #self.nameValue = "nombre de orueba"
        #print(self.nameValue)

    def saveMenu(self, name):
 
        print('Guardar dibujo')
        """
        * Permite abrir un menu para guardar dibujo
        """
        c = 0
        obj = '{'
        for cmd in self.graphicsCommands:
            c += 1
            obj += '"%s": %s,' % (c, cmd)
        obj = obj[:-1]
        obj += '}'
        print('obj: ', obj)


        binaryObj = self.dict_to_binary(json.loads('{"data": %s}' % (obj)))
        # binaryObj = self.binary_to_dict(binaryObj)

        # print('binaryData: ', binaryObj)
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.callproc('sp_createDrawing', [self.idUserLogin, name, binaryObj])
        cnx.commit()
        cnx.close()
        print('Dibujo agregado')
    """
        * Convierte el contenido json a binario
    """
    def dict_to_binary(self, the_dict):
        str = json.dumps(the_dict)
        binary = ' '.join(format(ord(letter), 'b') for letter in str)
        return binary

    """
        * Convierte el contenido binario a json
    """
    def binary_to_dict(self, the_binary):
        jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
        d = json.loads(jsn)  
        return d
    
    def loadDrawing(self, content):
        self.parse(content)
        for cmd in self.graphicsCommands:
            cmd.draw(self.theTurtle)
    
    def parse(self, data):
        """
            * Realizar un parseo de los registros de un archivo, para convertirtir el dibujo que representa.
        """
        dict_ = data['data']
        for key in dict_:
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
            self.graphicsCommands.append(cmd)
            print('comando agregado')
        self.screen.update()
        self.screen.listen()
    
    def newWindow(self):
            print('Limpiando la ventana...')
            self.theTurtle.clear()
            self.theTurtle.penup()
            self.theTurtle.goto(0,0)
            self.theTurtle.pendown()
            self.screen.update()
            self.screen.listen()
            self.graphicsCommands = PyList()
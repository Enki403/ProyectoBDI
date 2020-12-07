import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import json
from Core.drawCommands import *
from Core.drawActions import *
from Core.drawTools import *

"""
* Clase principal de la aplicacion de dibujo.
"""
class DrawingApplication(tkinter.Frame):
    def __init__(self,master=None,admin=False):
        self.admin = admin
        super().__init__(master)
        self.tkinter = tkinter
        self.turtle = turtle
        self.initializeDrawVariables()

    """
    * Inicializacion de las variables globales, cuales son bases y representacion del dibujo actual en ventana.
    * Se crea el menu de acciones respecto al dibujo.
    * Se hacen llamados a diferentes funciones que se encargan de construir el componente de dibujado.
    * Se construyen los componentes / herramientas para dibujar, permitidas por tkinter.
    * Se inicializan la clase de acciones sobre el dibujo, las cuales les permite al usuario decidir que hacer respecto a su dibujo.
    """
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
        self.fileMenu.add_command(label="New", command=self.action.newWindow)
        self.fileMenu.add_command(label="Load",command=self.action.loadFile)
        self.fileMenu.add_command(label="Save As",command=self.action.saveFile)
        self.fileMenu.add_command(label="Download",command=self.action.downloadFile)
        if(self.admin):
            self.fileMenu.add_command(label="Configuration",command=self.action.openConfigDialog)
        self.fileMenu.add_command(label="Exit",command=self.master.quit)
    
    """
    * Construye los componentes de las herramientas de dibujo en la ventana.
    * A su vez se define la accion a ejecutar cuando se interactua con una herramienta de dibujo.
    * Se crea una pestana principal, la cual este desglosa las diferentes acciones que el usuario puede realizar.
    """
    def buildWindow(self):
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
        self.penColor.set("#000000")
        penLabel = self.tkinter.Label(self.sideBar, text="Pen_Color")
        penLabel.pack()
        penEntry = self.tkinter.Entry(self.sideBar, textvariable=self.penColor)
        penEntry.pack()

        penColorButton = self.tkinter.Button(self.sideBar, text="Pick_Pen_Color", command=self.tools.getPenColor)
        penColorButton.pack(fill=self.tkinter.BOTH)

        # Seleccion de relleno.
        self.fillColor = self.tkinter.StringVar()
        self.fillColor.set("#4C53C6")
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
    
    """
    * Permite obtener la referencia a la clase principal del dibujo.
    """
    def getApp(self):
        return self

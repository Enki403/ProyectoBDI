from tkinter import ttk
from tkinter import *
from Core.connection import *
from Core.drawTools import *

class Load:
    def __init__(self,window,credentials):
        self.credentials = credentials
        self.cnx = ConnectionDB(self.credentials)
        self.wind = window
        self.wind.title('')

        # Creando el frame que almacenara todo el contenido 
        frame = LabelFrame(self.wind, text = 'LOAD')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)


        # Creando la tabla en donde se visualizaran los dibujos
        self.tree = ttk.Treeview(frame, height=10, columns=[f"#{n}" for n in range(1, 3)])
        self.tree.config(show='headings')
        self.tree.grid(row = 3, column = 0, columnspan = 2)
        self.tree.heading('#1', text='Name', anchor=CENTER)
        self.tree.heading('#2', text='Date', anchor=CENTER)

        #Button Boton para cargar
        ttk.Button(frame,text = 'LOAD').grid(row = 9, column = 0, sticky = W + E)
        
        # self.getUsers()

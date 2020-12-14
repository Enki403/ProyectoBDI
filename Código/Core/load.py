"""
    @author hjvasquez@unah.hn
    @author nelson.sambula@unah.hn
    @author lggutierrez@unah.hn
    @author renata.dubon@unah.hn
    @date 12/12/2020
    @version 0.1
"""

from tkinter import ttk
from tkinter import *
from Core.connection import *
from Core.drawTools import *

class Load:
    def __init__(self,window,credentials, actionRef, app, userId):
        self.credentials = credentials
        self.cnx = ConnectionDB(self.credentials)
        self.wind = window
        self.wind.title('')
        self.id = None
        self.action = actionRef
        self.app = app
        self.userId = userId

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
        ttk.Button(frame,text = 'LOAD', command = self.loadDrawing).grid(row = 9, column = 0, sticky = W + E)
        
        self.getDrawings()

    def getDrawings(self):
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.callproc('sp_getDrawingsByUser', [self.userId])
        # print('dibujos obtenidos: ', self.credentials)
        rows = []
        for result in cursor.stored_results():
            for row in result:
                data = {"user": row[0]}
                self.tree.insert('', 0, text=row[0], values=[row[3], row[2]])
                rows.append(row)
        cnx.close()
    
    def loadDrawing(self):
        data = self.tree.item(self.tree.selection())
        self.id = data['text']
        print('id a cargar: ', data['text'])
        cnx = mysql.connector.connect(**self.credentials)
        cursor = cnx.cursor()
        cursor.callproc('sp_getSketch', [self.userId, self.id])
        print("======")
        print(self.userId)
        print("======")
        binaryDrawing = None
        for result in cursor.stored_results():
            for data in result:
                binaryDrawing = data[2]
                #print('rowLOAD: ', data)

        drawing = self.binary_to_dict(binaryDrawing)
        self.app.setCurrentDrawing(self.id)
        self.app.getApp().loadDrawing(drawing)
        cnx.close()

    def binary_to_dict(self, the_binary):
        jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
        d = json.loads(jsn)  
        return d
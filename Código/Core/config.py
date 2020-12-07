from tkinter import ttk
from tkinter import *

class Config:
    def __init__(self,window):
        # Incicializando la ventana
        self.wind = window
        self.wind.title('')

        # Creando el frame que almacenara todo el contenido 
        frame = LabelFrame(self.wind, text = 'CREATE NEW USER')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Name Input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1,columnspan= 2,sticky= W + E)

        # UserName Input
        Label(frame, text = 'Username: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1, sticky= W + E)

        # PassWord Input
        Label(frame, text = 'Password: ').grid(row = 3, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 3, column = 1, sticky= W + E)

        # Button Create 
        ttk.Button(frame, text = 'CREATE').grid(row = 4, columnspan =3,column=1,sticky=W+E)

        # Output Messagess
        self.message = Label(frame,text = '', fg = 'green')
        self.message.grid(row = 5, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(frame, height=10, columns=[f"#{n}" for n in range(1, 7)])
        self.tree.config(show='headings')
        self.tree.grid(row = 7, column = 0, columnspan = 2)
        self.tree.heading('#1', text='id', anchor=CENTER)
        self.tree.heading('#2', text='Name', anchor=CENTER)
        self.tree.heading('#3', text='User Name', anchor=CENTER)
        self.tree.heading('#4', text='Password', anchor=CENTER)
        self.tree.heading('#5', text='Creation Date', anchor=CENTER)
        self.tree.heading('#6', text='Modification Date', anchor=CENTER)

        # Button Edit
        ttk.Button(frame,text = 'EDIT').grid(row = 8, column = 0, sticky = W + E)

        #Button Delete
        ttk.Button(frame,text = 'DELETE').grid(row = 8, column = 1, sticky = W + E)

        #Button PenColor
        ttk.Button(frame,text = 'PEN COLOR').grid(row = 9, column = 0, sticky = W + E)
        Label(frame, text = '#000000').grid(row = 9, column = 1)

        #Button FillColor
        ttk.Button(frame,text = 'FILL COLOR').grid(row = 10, column = 0, sticky = W + E)
        Label(frame, text = '#000000').grid(row = 10, column = 1)


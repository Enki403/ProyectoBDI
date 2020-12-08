from tkinter import ttk
from tkinter import *
import mysql.connector

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
        self.user = Entry(frame)
        self.user.grid(row = 2, column = 1, sticky= W + E)

        # PassWord Input
        Label(frame, text = 'Password: ').grid(row = 3, column = 0)
        self.password = Entry(frame)
        self.password.grid(row = 3, column = 1, sticky= W + E)

        # Button Create 
        ttk.Button(frame, text = 'CREATE',command = self.createUser).grid(row = 4, columnspan =3,column=1,sticky=W+E)

        # Mensaje en pantalla que cambia conforme al evento
        self.message = Label(frame,text = '', fg = 'green')
        self.message.grid(row = 5, column = 1, columnspan = 3, sticky = W+E)

        # Creando la tabla en donde se visualizaran los usuarios
        self.tree = ttk.Treeview(frame, height=10, columns=[f"#{n}" for n in range(1, 7)])
        self.tree.config(show='headings')
        self.tree.grid(row = 7, column = 0, columnspan = 2)
        self.tree.heading('#1', text='id', anchor=CENTER)
        self.tree.heading('#2', text='Name', anchor=CENTER)
        self.tree.heading('#3', text='User Name', anchor=CENTER)
        self.tree.heading('#4', text='Password', anchor=CENTER)
        self.tree.heading('#5', text='Creation Date', anchor=CENTER)
        self.tree.heading('#6', text='Modification Date', anchor=CENTER)

        #Button Delete
        ttk.Button(frame,text = 'DELETE' ,command = self.deleteUser).grid(row = 9, column = 0, sticky = W + E)

        # Button Edit
        ttk.Button(frame,text = 'EDIT NAME' , command = self.editUser).grid(row = 8, column = 0, sticky = W + E)
        ttk.Button(frame,text = 'EDIT PASSWORD', command = self.editPassword).grid(row = 8, column = 1, sticky = W + E)

        #Button PenColor
        ttk.Button(frame,text = 'PEN COLOR').grid(row = 10, column = 0, sticky = W + E)
        Label(frame, text = '#000000').grid(row = 10, column = 1)

        #Button FillColor
        ttk.Button(frame,text = 'FILL COLOR').grid(row = 11, column = 0, sticky = W + E)
        Label(frame, text = '#000000').grid(row = 11, column = 1)

        self.getUsers()

    #Metodo para guardar todos los datos de la DB en un array de tuplas
    def executeQueryRead(self, query, parameters = ()):
        valuesReturn = []
        config = {
        'user': 'admin',
        'password': 'admin',
        'host': '192.168.0.13',
        'database': 'testUser'
        }
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(query,parameters)
        for x in cursor:
            valuesReturn.append(x)
        cnx.close()
        return valuesReturn

    # Este metodo se encarga de crear y eliminar usuarios
    def executeQueryWrite(self,query,parameters = ()):
        config = {
            'user': 'admin',
            'password': 'admin',
            'host': '192.168.0.13',
            'database': 'testUser'
            }
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(query,parameters)
        cnx.commit()
        cnx.close()

    #Este metodo muestra los valores de la DB en la tabla de configuracion
    def getUsers(self):
        #Limpiando los datos que existen en la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM User ORDER BY id DESC'
        rows = self.executeQueryRead(query)
        #Rellenando la fila
        for row in rows:
            self.tree.insert('',0,text= row[1],values=row)
        
    #Verificar si se estan recibiendo datos
    def validateValue(self):
        return (len(self.name.get()) != 0 and (self.user.get()) != 0 and (self.password.get()) != 0)

    # Creando usuarios
    def createUser(self):
        if self.validateValue():
            query = 'INSERT INTO User (name,username,password) VALUES (%s,%s,%s)'
            parameters =(self.name.get(),self.user.get(),self.password.get())
            self.executeQueryWrite(query,parameters)
            self.message['fg'] = 'green'
            self.message['text'] = 'User Created Successfully!!!'
            self.name.delete(0,END)
            self.user.delete(0,END)
            self.password.delete(0,END)
        else:
            self.message['fg'] = 'red'
            self.message['text'] = 'Please fill all fields'
        self.getUsers()

    #Metodo para eliminar usuarios
    def deleteUser(self):
        self.message['text'] = ''
        self.message['fg'] = 'red'
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Please Select Registry'
            return
        self.message['text'] = ''
        query = 'DELETE FROM User WHERE name = %s'
        name = (self.tree.item(self.tree.selection())['text'],)
        
        self.executeQueryWrite(query,name)

        self.message['text'] = 'Deleted User!!'
        self.getUsers()

    #Metodo para editar en name del usuario
    def editUser(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['fg'] = 'red'
            self.message['text'] = 'Please, select Registry'
            return

        self.editWind = Toplevel()
        self.editWind.title = 'Update User'

        oldName = self.tree.item(self.tree.selection())['values'][1]
        id = self.tree.item(self.tree.selection())['values'][0]
        Label(self.editWind, text = 'Old Name:').grid(row = 3, column = 1)
        Entry(self.editWind, textvariable = StringVar(self.editWind, value = oldName), state = 'readonly').grid(row = 3, column = 2)

        Label(self.editWind, text = 'New Name:').grid(row = 4, column = 1)
        newName = Entry(self.editWind)
        newName.grid(row = 4, column = 2)

        Button(self.editWind, text = 'Update', command= lambda:self.editRegistry(newName.get(),id,'name')).grid(row = 5, column = 2, sticky = W)
        self.editWind.mainloop()

    #Metodo para editar el password del usuario
    def editPassword(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['fg'] = 'green'
            self.message['text'] = 'Please, select Registry'
            return

        self.editWind = Toplevel()
        self.editWind.title = 'Update User'

        oldPassword = self.tree.item(self.tree.selection())['values'][3]
        id = self.tree.item(self.tree.selection())['values'][0]
        Label(self.editWind, text = 'Old Password:').grid(row = 3, column = 1)
        Entry(self.editWind, textvariable = StringVar(self.editWind, value = oldPassword), state = 'readonly').grid(row = 3, column = 2)

        Label(self.editWind, text = 'New Password:').grid(row = 4, column = 1)
        newPassword = Entry(self.editWind)
        newPassword.grid(row = 4, column = 2)

        Button(self.editWind, text = 'Update', command= lambda:self.editRegistry(newPassword.get(),id,'password')).grid(row = 5, column = 2, sticky = W)
        self.editWind.mainloop()

    # Metodo para actualizar la data en la DB
    def editRegistry(self,new,id,value):
        self.message['fg'] = 'green'
        if(value == 'password'):
            query = 'UPDATE User SET password = %s WHERE id = %s '
            parameters = (new,id)
            self.executeQueryWrite(query, parameters)
        else:
            query = 'UPDATE User SET name = %s WHERE id = %s '
            parameters = (new,id)
            self.executeQueryWrite(query, parameters)

        self.editWind.destroy()
        self.message['text'] = 'Registry Updated successfylly'
        self.getUsers()
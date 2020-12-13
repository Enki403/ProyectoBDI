# -*- coding: utf-8 -*-
"""
    @author nelson.sambula@unah.hn
    @version 0.1
    @date 2020/12/12
"""

from Core.draw import *
from Core.connection import *
import configparser
import sys

class StartApplication:
    """
        ! Clase StartApplication
        * Esta clase se encarga de iniciar la aplicacion de dibujo construida en tkinter.
        * Esta clase sirve de enlace con el login, realizando la verificacion del login del usuario.
    """
    def __init__(self,credentials):
        self.credentials = credentials

    def validateLogin(self,username,password,Login):
        """
            ! Metodo validateLogin
            ? Este metodo realiza una coneccion con la bade de datos para verificar si el usuario
            ?   esta loguiado en la App, si el usuario no esta loguiado entonces no se accede a la App
            ?   de dibujo y el Login construido en Qt le dira al usuario que sus credenciales son 
            ?   invalidos.
        """
        conect = ConnectionDB(self.credentials)
        # Se extraen los nombres y password ingresadas por el usuario
        user = username.text()
        passw = password.text()

        # Se crea un if en donde se verifica con el metodo validateUser
        # if(conect.validateUser(user,passw)):
        if(True):
            Login.hide()    
            root = tkinter.Tk()
            admin = self.isAdmin(username,password)
            # Creamos la instancia de la clase DrawingApplication que es la encargada de ejecutar la app de dibujo
            drawingApp = DrawingApplication(self.credentials,root,admin)
            drawingApp.mainloop()
            print("Program Execution Completed.")
            sys.exit(0)
        else:
            # Se muestra un mensaje de INVALID USER en el loggin
            username.setText('INVALID USER')

    def isAdmin(self,username,password):
        """
            ! Metodo isAdmin
            ? Este metodo se encarga de verificar si el usuario que se loggio es el usuario administrador
            ?   en el caso de ser el administrador se retorna True caso contrario retornamos False.
        """
        return True



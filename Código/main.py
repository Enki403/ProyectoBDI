# -*- coding: utf-8 -*-
"""
    @author nelson.sambula@unah.hn
    @version 0.1
    @date 2020/12/12
"""

from Core.portada_rc import *
import configparser
from Core.startApplication import *
from Core.connection import *
from Core.login import *
import sys
import os

# os.system("ls")

"""
    ? Se Obtienen las credenciales de configuracion de la base de datos del usuario de
    ? Se crea un diccionario en donde se almacena las credenciales 
"""
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
values = config['DATABASE']

# Creacion de archivo 
dbCredentials = {
    'user': values['user'] ,
    'password':values['pass'] ,
    'host': values['host'],
    'database': config['DEFAULT']['db']
}

"""
    ! Login en PyQT5
    * El login de la aplicacion esta construido en PyQT5
    ? Se crea una instancia de la clase Ui_Login() que es la encargada de ejecutar el Login creado en Qt
    ? Se crea una instancia de la clase StartApplication() la cual es la encargada de ejecutar
    ?   la aplicacion de dibujo creada en tkinter.
    ? Esta instancia recibe las credenciales de configuracion para crear una conexion con la base de Datos.
"""
startApp= StartApplication(dbCredentials)
app = QtWidgets.QApplication(sys.argv)
Login = QtWidgets.QMainWindow()
ui = Ui_Login()
ui.setupUi(Login)
user = ui.textLineUser
password = ui.textLinePassword

"""
    ? El metodo buttonLogin es el encargado de activar el evento validateLogin()
    ? El metodo validate se encarga de verificar si el usuario esta loguiado en la App
"""
ui.buttonLogin.clicked.connect(
    lambda: startApp.validateLogin(user,password,Login)
)
Login.show()
sys.exit(app.exec_())

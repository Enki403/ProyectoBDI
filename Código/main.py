from Core.startApplication import *
from Core.portada_rc import *
from Core.connection import *
from Core.login import *
import configparser
import os
import sys


config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
values = config['DATABASE']

dbCredentials = {
    'user': values['user'] ,
    'password':values['pass'] ,
    'host': values['host'],
    'database': config['DEFAULT']['db']
}

host = values['host']
user = values['user']
password = values['pass']

os.system('cd Scripts; mysql -u%s -h %s -p%s < testU.sql' %(user,host,password))

# connectionDB = ConnectionDB(dbCredentials)
startApp= StartApplication(dbCredentials)

app = QtWidgets.QApplication(sys.argv)
Login = QtWidgets.QMainWindow()
ui = Ui_Login()
ui.setupUi(Login)
user = ui.textLineUser
password = ui.textLinePassword
ui.buttonLogin.clicked.connect(
    lambda: startApp.validateLogin(user,password,Login)
)
Login.show()
sys.exit(app.exec_())

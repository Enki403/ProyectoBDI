from Core.portada_rc import *
from Core.login import *
from Core.startApplication import *
import sys


app = QtWidgets.QApplication(sys.argv)
Login = QtWidgets.QMainWindow()
ui = Ui_Login()
ui.setupUi(Login)
user = ui.textLineUser.text()
password = ui.textLinePassword.text()
ui.buttonLogin.clicked.connect(
    lambda: StartApplication().validateLogin(user,password,Login)
)
Login.show()
sys.exit(app.exec_())
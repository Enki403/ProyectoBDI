from Core.draw import *
from Core.login import *
from Core.portada_rc import *
from Core.controller import *


if __name__ == "__main__":
    controller = Controller()
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.setGeometry(555,180,413,518)
    username = ui.textLineUser.text()
    password = ui.textLinePassword.text()
    ui.buttonLogin.clicked.connect(lambda:controller.authentication(username,password,Login))
    Login.show()
    sys.exit(app.exec_())

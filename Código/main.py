from Core.tkinterAppFunction import *
from Core.login import *
from Core.portada_rc import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.setGeometry(555,180,413,518)
    username = ui.textLineUser.text()
    password = ui.textLinePassword.text()
    ui.buttonLogin.clicked.connect(lambda:openTkinterApp(username,password,Login,ui))
    Login.show()
    # ui.Configure.show()
    sys.exit(app.exec_())

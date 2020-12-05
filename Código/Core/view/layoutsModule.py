import sys
from PyQt5 import uic, QtWidgets
import loginWindow

app = QtWidgets.Application(sys.argv)
login = loginWindow.Login()
login.show()
sys.exit(app.exec_())


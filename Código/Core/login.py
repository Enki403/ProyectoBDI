# -*- coding: utf-8 -*-
"""
    @author hjvasquez@unah.hn
    @author nelson.sambula@unah.hn
    @author lggutierrez@unah.hn
    @author renata.dubon@unah.hn
    @date 12/12/2020
    @version 0.1
"""

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Login(object):
    """
        ! Clase Ui_Login
        * Esta clase se autogenero conforme al Login diseñado en QTDesigner
    """
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setEnabled(True)
        Login.resize(413, 578)
        Login.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/paints.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        Login.setStyleSheet("background-color: rgb(51, 102, 153);")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 281, 151))
        self.label_2.setStyleSheet("border-image: url(:/cct/paints.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 150, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.buttonLogin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLogin.setGeometry(QtCore.QRect(110, 420, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonLogin.setFont(font)
        self.buttonLogin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(19, 98, 173);")
        self.buttonLogin.setObjectName("buttonLogin")
        self.textLinePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.textLinePassword.setEnabled(True)
        self.textLinePassword.setGeometry(QtCore.QRect(80, 330, 251, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textLinePassword.setFont(font)
        self.textLinePassword.setStyleSheet("background-color: rgb(206, 201, 206);")
        self.textLinePassword.setInputMask("")
        self.textLinePassword.setText("")
        self.textLinePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textLinePassword.setAlignment(QtCore.Qt.AlignCenter)
        self.textLinePassword.setObjectName("textLinePassword")
        self.textLineUser = QtWidgets.QLineEdit(self.centralwidget)
        self.textLineUser.setEnabled(True)
        self.textLineUser.setGeometry(QtCore.QRect(80, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textLineUser.setFont(font)
        self.textLineUser.setStyleSheet("background-color: rgb(206, 201, 206);")
        self.textLineUser.setInputMask("")
        self.textLineUser.setText("")
        self.textLineUser.setAlignment(QtCore.Qt.AlignCenter)
        self.textLineUser.setObjectName("textLineUser")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.buttonLogin.raise_()
        self.textLinePassword.raise_()
        self.textLineUser.raise_()
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "DrawingApp"))
        self.label.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-style:italic; color:#ececec;\">DRAWING </span></p></body></html>"))
        self.label_3.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-style:italic; color:#ececec;\">APP</span></p></body></html>"))
        self.buttonLogin.setText(_translate("Login", "LOGIN"))
        self.textLinePassword.setPlaceholderText(_translate("Login", "PASSWORD"))
        self.textLineUser.setPlaceholderText(_translate("Login", "USERNAME"))





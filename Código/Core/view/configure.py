# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Configure.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Configure(object):
    def setupUi(self, Configure):
        Configure.setObjectName("Configure")
        Configure.setEnabled(True)
        Configure.resize(401, 461)
        Configure.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/paints.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Configure.setWindowIcon(icon)
        Configure.setLayoutDirection(QtCore.Qt.LeftToRight)
        Configure.setStyleSheet("background-color: rgb(51, 102, 153);")
        self.centralwidget = QtWidgets.QWidget(Configure)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 80, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.buttonManageUsers = QtWidgets.QPushButton(self.centralwidget)
        self.buttonManageUsers.setGeometry(QtCore.QRect(70, 200, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonManageUsers.setFont(font)
        self.buttonManageUsers.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(19, 98, 173);")
        self.buttonManageUsers.setObjectName("buttonManageUsers")
        self.buttonPenColor = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPenColor.setGeometry(QtCore.QRect(40, 290, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonPenColor.setFont(font)
        self.buttonPenColor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(19, 98, 173);")
        self.buttonPenColor.setObjectName("buttonPenColor")
        self.labelPenColor = QtWidgets.QLabel(self.centralwidget)
        self.labelPenColor.setGeometry(QtCore.QRect(250, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelPenColor.setFont(font)
        self.labelPenColor.setStyleSheet("color: rgb(235, 235, 235);")
        self.labelPenColor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelPenColor.setObjectName("labelPenColor")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 161, 101))
        self.label_4.setStyleSheet("border-image: url(:/cct/paints.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.buttonFillColor = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFillColor.setGeometry(QtCore.QRect(40, 370, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonFillColor.setFont(font)
        self.buttonFillColor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(19, 98, 173);")
        self.buttonFillColor.setObjectName("buttonFillColor")
        self.labelFilColor = QtWidgets.QLabel(self.centralwidget)
        self.labelFilColor.setGeometry(QtCore.QRect(250, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelFilColor.setFont(font)
        self.labelFilColor.setStyleSheet("color: rgb(235, 235, 235);")
        self.labelFilColor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelFilColor.setObjectName("labelFilColor")
        self.buttonReturn = QtWidgets.QPushButton(self.centralwidget)
        self.buttonReturn.setGeometry(QtCore.QRect(280, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonReturn.setFont(font)
        self.buttonReturn.setStyleSheet("background-color: rgb(20, 111, 223);\n"
"color:rgb(239, 239, 239);")
        self.buttonReturn.setObjectName("buttonReturn")
        self.buttonManageUsers.raise_()
        self.buttonPenColor.raise_()
        self.labelPenColor.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.buttonFillColor.raise_()
        self.labelFilColor.raise_()
        self.buttonReturn.raise_()
        Configure.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Configure)
        self.statusbar.setObjectName("statusbar")
        Configure.setStatusBar(self.statusbar)

        self.retranslateUi(Configure)
        QtCore.QMetaObject.connectSlotsByName(Configure)

    def retranslateUi(self, Configure):
        _translate = QtCore.QCoreApplication.translate
        Configure.setWindowTitle(_translate("Configure", "DrawingApp"))
        self.label_3.setText(_translate("Configure", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ececec;\">CONFIGURE</span></p></body></html>"))
        self.buttonManageUsers.setText(_translate("Configure", "Manage Users"))
        self.buttonPenColor.setText(_translate("Configure", "Pen Color"))
        self.labelPenColor.setText(_translate("Configure", "#0000000"))
        self.buttonFillColor.setText(_translate("Configure", "Fil Color"))
        self.labelFilColor.setText(_translate("Configure", "#0000000"))
        self.buttonReturn.setText(_translate("Configure", "RETURN"))

import portada_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Configure = QtWidgets.QMainWindow()
    ui = Ui_Configure()
    ui.setupUi(Configure)
    Configure.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadDrawing.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadDrawing(object):
    def setupUi(self, LoadDrawing):
        LoadDrawing.setObjectName("LoadDrawing")
        LoadDrawing.setEnabled(True)
        LoadDrawing.resize(640, 568)
        LoadDrawing.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/paints.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoadDrawing.setWindowIcon(icon)
        LoadDrawing.setLayoutDirection(QtCore.Qt.LeftToRight)
        LoadDrawing.setStyleSheet("background-color: rgb(51, 102, 153);")
        self.centralwidget = QtWidgets.QWidget(LoadDrawing)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 181, 91))
        self.label_2.setStyleSheet("border-image: url(:/cct/paints.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 70, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableUsers = QtWidgets.QTableWidget(self.centralwidget)
        self.tableUsers.setGeometry(QtCore.QRect(50, 140, 531, 281))
        self.tableUsers.setObjectName("tableUsers")
        self.tableUsers.setColumnCount(0)
        self.tableUsers.setRowCount(0)
        self.buttonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLoad.setGeometry(QtCore.QRect(140, 450, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoad.setFont(font)
        self.buttonLoad.setStyleSheet("background-color: rgb(30, 235, 30);\n"
"color: rgb(255, 255, 255);")
        self.buttonLoad.setObjectName("buttonLoad")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.tableUsers.raise_()
        self.buttonLoad.raise_()
        LoadDrawing.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoadDrawing)
        self.statusbar.setObjectName("statusbar")
        LoadDrawing.setStatusBar(self.statusbar)

        self.retranslateUi(LoadDrawing)
        QtCore.QMetaObject.connectSlotsByName(LoadDrawing)

    def retranslateUi(self, LoadDrawing):
        _translate = QtCore.QCoreApplication.translate
        LoadDrawing.setWindowTitle(_translate("LoadDrawing", "DrawingApp"))
        self.label.setText(_translate("LoadDrawing", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-style:italic; color:#ececec;\">LIST</span></p></body></html>"))
        self.label_3.setText(_translate("LoadDrawing", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-style:italic; color:#ececec;\">DRAWING</span></p></body></html>"))
        self.buttonLoad.setText(_translate("LoadDrawing", "LOAD"))

import portada_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadDrawing = QtWidgets.QMainWindow()
    ui = Ui_LoadDrawing()
    ui.setupUi(LoadDrawing)
    LoadDrawing.show()
    sys.exit(app.exec_())


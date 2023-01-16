
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Gyan_Mela_GUI(object):
    def setupUi(self, Gyan_Mela_GUI):
        Gyan_Mela_GUI.setObjectName("Gyan_Mela_GUI")
        Gyan_Mela_GUI.resize(683, 443)
        self.centralwidget = QtWidgets.QWidget(Gyan_Mela_GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Media/gif.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 380, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 380, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 280, 361, 161))
        self.label_2.setStyleSheet("background : black\n"
"")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        Gyan_Mela_GUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(Gyan_Mela_GUI)
        QtCore.QMetaObject.connectSlotsByName(Gyan_Mela_GUI)

    def retranslateUi(self, Gyan_Mela_GUI):
        _translate = QtCore.QCoreApplication.translate
        Gyan_Mela_GUI.setWindowTitle(_translate("Gyan_Mela_GUI", "MainWindow"))
        self.pushButton.setText(_translate("Gyan_Mela_GUI", "Start"))
        self.pushButton_2.setText(_translate("Gyan_Mela_GUI", "Exterminate"))
        self.label_2.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gyan_Mela_GUI = QtWidgets.QMainWindow()
    ui = Ui_Gyan_Mela_GUI()
    ui.setupUi(Gyan_Mela_GUI)
    Gyan_Mela_GUI.show()
    sys.exit(app.exec_())


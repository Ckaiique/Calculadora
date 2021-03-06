# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculadora_Vencer.ui.'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from  vencer_leitura import funcoes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 831)
        MainWindow.setMinimumSize(QtCore.QSize(0, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/vencer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"background-repeat:no-repeat;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(330, 290, 271, 121))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton.setMinimumSize(QtCore.QSize(191, 81))
        self.pushButton.setMaximumSize(QtCore.QSize(191, 81))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border:3px solid rgb(181, 185, 255);\n"
"    border-radius:10px;font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color :rgb(181, 185, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border:3px solid rgb(255, 243, 252);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 243, 252);\n"
"    border:3px solid rgb(181, 185, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 611, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setStyleSheet("background-image: url(:/imagem/vencer leitura.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 253, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(161, 21))
        self.label_3.setMaximumSize(QtCore.QSize(235, 21))
        self.label_3.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"color :rgb(181, 185, 255)")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(113, 41))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(113, 41))
        self.lineEdit_3.setStyleSheet("    background-color: rgb(170, 255, 255);\n"
"    border:3px solid rgb(181, 185, 255);\n"
"    border-radius:10px;font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color :rgb(181, 185, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(251, 21))
        self.label_2.setMaximumSize(QtCore.QSize(251, 21))
        self.label_2.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"color :rgb(181, 185, 255)")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(113, 41))
        self.lineEdit.setMaximumSize(QtCore.QSize(113, 41))
        self.lineEdit.setStyleSheet("    background-color: rgb(170, 255, 255);\n"
"    border:3px solid rgb(181, 185, 255);\n"
"    border-radius:10px;font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color :rgb(181, 185, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(161, 21))
        self.label.setMaximumSize(QtCore.QSize(235, 21))
        self.label.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"color :rgb(181, 185, 255)")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(113, 41))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(113, 41))
        self.lineEdit_2.setStyleSheet("    background-color: rgb(170, 255, 255);\n"
"    border:3px solid rgb(181, 185, 255);\n"
"    border-radius:10px;font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color :rgb(181, 185, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 530, 611, 241))
        self.textEdit.setStyleSheet("    background-color: rgb(170, 255, 255);\n"
"    border:3px solid rgb(181, 185, 255);\n"
"    border-radius:10px;font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color :rgb(181, 185, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 500, 235, 21))
        self.label_4.setMinimumSize(QtCore.QSize(161, 21))
        self.label_4.setMaximumSize(QtCore.QSize(235, 21))
        self.label_4.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"color :rgb(181, 185, 255)")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora_Vencer Leitura"))
        self.pushButton.setText(_translate("MainWindow", "Calcular"))
        self.pushButton.clicked.connect(self.calcular)

        self.label_3.setText(_translate("MainWindow", "Acertos :"))
        self.label_2.setText(_translate("MainWindow", "Tempo :"))
        self.label.setText(_translate("MainWindow", "Quantide de Palavras do Texto  :"))
        self.label_4.setText(_translate("MainWindow", "Resultado do Aluno :"))


    #Pegando o imput  dos  Acertos,tempo e  quantidade de palavras
    def calcular(self):



         self.acerto =  int(self.lineEdit_3.text())
         self.tempo  =  float (self.lineEdit.text())
         self.quantpl=  int(self.lineEdit_2.text())

         self.ppm = self.quantpl/self.tempo

         self.segundos = self.tempo * 60

         self.compreensao = (self.acerto / 100 ) * self.ppm

         self.total = self.compreensao

         self.textEdit.setText(f"Palavras por Minutos : {str(self.ppm) } "
                                    f"\n\nSegundos : {str(self.segundos)}s   "
                                        f"\n\nPalavras Compreendidas : {str(self.total)}  ")








import files_rc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

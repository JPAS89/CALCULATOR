from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QPushButton
from uiCalculator import Ui_MainWindow

class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    num1 = None
    userIsTypingSecondNumb = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        #connect BTNS
        self.pushButton_1.clicked.connect(self.agregar)
        self.pushButton_2.clicked.connect(self.agregar)
        self.pushButton_3.clicked.connect(self.agregar)
        self.pushButton_4.clicked.connect(self.agregar)
        self.pushButton_5.clicked.connect(self.agregar)
        self.pushButton_6.clicked.connect(self.agregar)
        self.pushButton7.clicked.connect(self.agregar)
        self.pushButton_8.clicked.connect(self.agregar)
        self.pushButton_9.clicked.connect(self.agregar)
        self.pushButton_0.clicked.connect(self.agregar)

        self.pushButton_mr.clicked.connect(self.sumaDecimal)

        self.pushButton_Div.clicked.connect(self.operadores)
        self.pushButton_Mult.clicked.connect(self.operadores)
        self.pushButton_Resta.clicked.connect(self.operadores)
        self.pushButton_Suma.clicked.connect(self.operadores)

        self.pushButton_igual.clicked.connect(self.resultado)
        self.pushButton_Suma.setCheckable(True)
        self.pushButton_Div.setCheckable(True)
        self.pushButton_Resta.setCheckable(True)
        self.pushButton_Mult.setCheckable(True)

    def agregar(self):
        btn = self.sender()
        if ((self.pushButton_Suma.isChecked() or self.pushButton_Resta.isChecked() or
                self.pushButton_Mult.isChecked() or self.pushButton_Div.isChecked()) and
                (not self.userIsTypingSecondNumb)):
            newResDec = format(float(btn.text()),'.15g')
            self.userIsTypingSecondNumb = True  
        else:
            newResDec = format(float(self.ResultDec.text() + btn.text()),'.15g')

        self.ResultDec.setText(newResDec)

    def sumaDecimal(self):
        btn = self.sender()
        ResultDec = float(self.ResultDec.text())
        if btn.text() == "+ -":
            ResultDec = ResultDec *-1

        newResBin = format(ResultDec,'.15g')
        self.ResultDec.setText(newResBin)

    def operadores(self):
        btn = self.sender()

        self.num1 = float(self.ResultDec.text())
        btn.setChecked(True)

    def resultado(self):
        num2 = float(self.ResultDec.text())

        if self.pushButton_Suma.isChecked():
            labelNumb= self.num1 + num2
            newLabel = format(labelNumb,'.15g')
            self.ResultDec.setText(newLabel)
            self.pushButton_Suma.setChecked(False)
        elif self.pushButton_Div.isChecked():
            labelNumb= self.num1 / num2
            newLabel = format(labelNumb,'.15g')
            self.ResultDec.setText(newLabel)
            self.pushButton_Div.setChecked(False)
        elif self.pushButton_Resta.isChecked():
            labelNumb= self.num1 - num2
            newLabel = format(labelNumb,'.15g')
            self.ResultDec.setText(newLabel)
            self.pushButton_Resta.setChecked(False)
        elif self.pushButton_Mult.isChecked():
            labelNumb= self.num1 * num2
            newLabel = format(labelNumb,'.15g')
            self.ResultDec.setText(newLabel)
            self.pushButton_Mult.setChecked(False)


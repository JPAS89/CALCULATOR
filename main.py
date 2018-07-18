import sys
from PyQt5.QtWidgets import QApplication
from Calc import CalculatorWindow

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())
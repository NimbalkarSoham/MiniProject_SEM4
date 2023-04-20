from PySide6 import QtWidgets, QtGui, QtCore
from googletrans import Translator
from main import MainWindow

import sys

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

#! python3
# -*- coding:utf-8 -*-
import sys
from PySide2 import QtCore, QtGui, uic
from PySide2

qtCreatorFile = r"D:\Script\QT_Designer\tax_calc.ui"  # Enter .UI file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

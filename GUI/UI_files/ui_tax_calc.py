# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/QIDONGKAI/AppData/Local/Temp/tax_calcZOZExz.ui',
# licensing of 'C:/Users/QIDONGKAI/AppData/Local/Temp/tax_calcZOZExz.ui' applies.
#
# Created: Sat Jan 19 22:53:05 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.price_box = QtWidgets.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(300, 100, 104, 87))
        self.price_box.setObjectName("price_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 140, 71, 31))
        self.label.setMinimumSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tax_rate = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(330, 250, 46, 22))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 250, 121, 31))
        self.label_2.setMinimumSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.calc_tax = QtWidgets.QPushButton(self.centralwidget)
        self.calc_tax.setGeometry(QtCore.QRect(120, 400, 93, 28))
        self.calc_tax.setObjectName("calc_tax")
        self.result_window = QtWidgets.QTextEdit(self.centralwidget)
        self.result_window.setGeometry(QtCore.QRect(300, 360, 104, 87))
        self.result_window.setObjectName("result_window")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # 后面新增的
        self.calc_tax.clicked.connect(self.CalculateTax)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def CalculateTax(self):
        # 计算部分新增的
        price = int(self.price_box.toPlainText())
        tax = (self.tax_rate.value())
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.result_window.setText(total_price_string)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Price", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "tax_rate", None, -1))
        self.calc_tax.setText(QtWidgets.QApplication.translate("MainWindow", "calc_tax", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Sales Tax Calculator", None, -1))


if __name__ == '__main__':
    # 生成以后主函数要自己加
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



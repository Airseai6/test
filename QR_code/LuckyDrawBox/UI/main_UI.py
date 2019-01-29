# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\tmp\homework\LuckyDrawBox\UI\main.ui',
# licensing of 'D:\tmp\homework\LuckyDrawBox\UI\main.ui' applies.
#
# Created: Tue Jan 29 10:36:58 2019
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 535)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(252, 253, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputLineEdit = QtWidgets.QLineEdit(self.page)
        font = QtGui.QFont()
        font.setFamily("萍方-简")
        font.setPointSize(26)
        self.inputLineEdit.setFont(font)
        self.inputLineEdit.setObjectName("inputLineEdit")
        self.verticalLayout.addWidget(self.inputLineEdit)
        self.startLuckyButton = QtWidgets.QPushButton(self.page)
        self.startLuckyButton.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        self.startLuckyButton.setFont(font)
        self.startLuckyButton.setObjectName("startLuckyButton")
        self.verticalLayout.addWidget(self.startLuckyButton)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LuckLabel = QtWidgets.QLabel(self.page_2)
        self.LuckLabel.setText("")
        self.LuckLabel.setPixmap(QtGui.QPixmap(":/images/loading.gif"))
        self.LuckLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LuckLabel.setObjectName("LuckLabel")
        self.gridLayout_2.addWidget(self.LuckLabel, 0, 0, 1, 1)
        self.restartButton = QtWidgets.QPushButton(self.page_2)
        self.restartButton.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        self.restartButton.setFont(font)
        self.restartButton.setObjectName("restartButton")
        self.gridLayout_2.addWidget(self.restartButton, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.startLuckyButton.setText(QtWidgets.QApplication.translate("MainWindow", "我抽", None, -1))
        self.restartButton.setText(QtWidgets.QApplication.translate("MainWindow", "再来", None, -1))

import main_rc

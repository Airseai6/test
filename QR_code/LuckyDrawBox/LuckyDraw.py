#! python3
# -*- coding:utf-8 -*-

from qrcode_test import gen_qrcode
from random import randint
from PIL import Image

from PySide2 import QtCore, QtGui, QtWidgets
import sys

from UI import main_UI
import main_rc
import base64


class LuckyWidget(QtWidgets.QMainWindow, main_UI.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        # connect signal and slots
        self.startLuckyButton.clicked.connect(self.OnStartLuckyButtonClicked)
        self.restartButton.clicked.connect(self.OnRestartButtonClicked)

        # init LuckyDrawBox data
        with open('LuckyDrawBox.txt', 'r', encoding='utf8') as f:
            self.data = f.readlines()

    @QtCore.Slot()
    def OnRestartButtonClicked(self):
        self.stackedWidget.setCurrentIndex(0)

    @QtCore.Slot()
    def OnStartLuckyButtonClicked(self):
        # 1.检测输入数据
        text = self.inputLineEdit.text()
        if not text or text == "":
            print("Please Input Correct Data")
            QtWidgets.QMessageBox.warning(self, "出现错误", "请输入抽奖的文本票",
                QtWidgets.QMessageBox.Ok
                # |QtWidgets.QMessageBox.Cancel
                )
            return

        # 1.5 显示进度条
        self.stackedWidget.setCurrentIndex(1)

        # 2.开始抽奖
        # 添加进度条或者抽奖动画，然后弹出二维码
        index = randint(1, len(self.data))
        base64str = gen_qrcode(self.data[index-1])
        # self.LuckLabel.setPixmap(QtGui.QPixmap("qrcode_temp.png"))
        
        self.pm = QtGui.QPixmap()
        self.pm.loadFromData(base64.b64decode(base64str))
        self.LuckLabel.setPixmap(self.pm)

def main():
    qapp = QtWidgets.QApplication(sys.argv)
    w = LuckyWidget()
    w.show()
    return qapp.exec_()

def main2():
    with open('LuckyDrawBox.txt', 'r', encoding='utf8') as f:
        data = f.readlines()
    flag = True
    records = []
    while flag:
        sign = input('Please input your sign! -->: ')

        # 添加进度条或者抽奖动画，然后弹出二维码
        index = randint(1, len(data))
        records.append(sign + ' --> ' + data[index-1])
        gen_qrcode(data[index-1])
        im = Image.open('qrcode_temp.png')
        im.show()

        data.pop(index-1)
        if len(data) == 1:
            print('奖箱快空了')
        if len(data) == 0:
            break
    with open('records.txt', 'w')as f:
        i = 1
        for item in records:
            f.write(str(i) + '、 ' + item)
            i +=1
    print('抽奖箱已空！')


if __name__ == '__main__':
    main()

#! python3
# -*- coding:utf-8 -*-
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     label = QLabel('Hello World!')
#     label.show()
#     sys.exit(app.exec_())


class Window(QWidget):
    def __init__(self):
        # QWidget 提供了默认的构造方法
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('老子是标题')
        # 窗口大小
        self.resize(300, 300)
        # 窗口位置
        self.move(500, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Window()
    sys.exit(app.exec_())
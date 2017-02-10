# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

'''
code no.2
An application icon
'''

class Sample(QWidget):
    def __init__(self):
        super().__init__()
        self.initU()

    def initU(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('code 2')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sample()
    sys.exit(app.exec_())


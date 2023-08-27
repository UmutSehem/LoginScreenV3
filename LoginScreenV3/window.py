import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui2()
        self.setWindowTitle("MainWindow")
        self.setGeometry(100, 100, 800, 600)

    def init_ui2(self):
        print("Hello")











        self.resize(800,500)
        self.show()
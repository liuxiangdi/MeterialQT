from PyQt5.QtWidgets import (
    QWidget
)
from PyQt5 import Qt
from PyQt5.QtCore import QFile
from components.buttons import MPushButton

def read_style():
    qss = QFile("stylesheet.qss")
    qss.open(QFile.ReadOnly)
    qtBytes = qss.readAll()
    pyBytes = qtBytes.data()
    styleStr = pyBytes.decode("utf-8")
    return styleStr


class UI(QWidget):
    def __init__(self, app, parent=None):
        super(UI, self).__init__(parent)
        self.setObjectName("Main")
        self._app = app

        self.setupUI()

    def setupUI(self):
        self.setFixedSize(1366, 768)
        btn = MPushButton(self)
        btn.setGeometry(100,100, 100,50)

        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setStyleSheet("background-color:rgb(250, 250, 250)")
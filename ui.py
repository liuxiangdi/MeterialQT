from PyQt5 import Qt
from PyQt5.QtCore import QFile
from components.widgets import MFrame
from components.buttons import MPushButton, MTextButton, MContaindedButton, MOutlinedButton


def read_style():
    qss = QFile("stylesheet.qss")
    qss.open(QFile.ReadOnly)
    qtBytes = qss.readAll()
    pyBytes = qtBytes.data()
    styleStr = pyBytes.decode("utf-8")
    return styleStr


class UI(MFrame):
    def __init__(self, app, parent=None):
        super(UI, self).__init__(parent)
        self.setObjectName("Main")
        self._app = app

        self.setupUI()

    def setupUI(self):
        self.setGeometry(200, 100, 1566, 968)
        self.setStyleSheet("background-color:white")

        btn = MOutlinedButton("BUTTON", self)
        btn.setGeometry(100, 100, 200, 80)

        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

    def mousePressEvent(self, Qevent):
        pass

    def mouseMoveEvent(self, Qevent):
        pass

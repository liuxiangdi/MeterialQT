import time
from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import QFile
from components.widgets import MFrame
from components.buttons import MPushButton, MTextButton, MContaindedButton, MOutlinedButton
from components.topbar import MTopBar
from components.cards import MCards
from components.utils import read_style


class UI(MFrame):
    def __init__(self, app, parent=None):
        super(UI, self).__init__(parent)
        self.setObjectName("Main")
        self._app = app

        self.setupUI()

    def setupUI(self):
        self.setGeometry(200, 100, 1566, 968)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        main_window = MFrame(self)
        main_window.setGeometry(0, 0, 1566, 968)
        main_window.setStyleSheet("background-color:#f0f0f0;border-radius:10px;")

        top_bar = MTopBar(main_window, self)

        btn = MCards(main_window)
        btn.move(100, 100)

    def mousePressEvent(self, Qevent):
        pass

    def mouseMoveEvent(self, Qevent):
        pass

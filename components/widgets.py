from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import pyqtSignal


class MFrame(QFrame):
    press_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(MFrame, self).__init__(parent)

    def mousePressEvent(self, Qevent):
        self.press_signal.emit(True)

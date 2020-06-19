from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import pyqtSignal


class MFrame(QFrame):
    press_signal = pyqtSignal(bool)
    moveX = pyqtSignal(int)
    moveY = pyqtSignal(int)

    initX = 0
    initY = 0
    def __init__(self, parent=None):
        super(MFrame, self).__init__(parent)

    def mousePressEvent(self, Qevent):
        self.press_signal.emit(True)
        self.initX = Qevent.globalX()
        self.initY = Qevent.globalY()


    def mouseMoveEvent(self, Qevent):
        moveX = Qevent.globalX() - self.initX
        moveY = Qevent.globalY() - self.initY
        self.moveX.emit(moveX)
        self.moveY.emit(moveY)


class MDrawerFrame(QFrame):
    press_signal = pyqtSignal(bool)
    moveX = pyqtSignal(int)
    moveY = pyqtSignal(int)
    initX = 0
    initY = 0

    def __init__(self, parent=None):
        super(MDrawerFrame, self).__init__(parent)
        self.draw_flag = False

    def mousePressEvent(self, Qevent):
        self.press_signal.emit(True)
        self.initX = Qevent.globalX()

        self.initY = Qevent.globalY()
        if Qevent.x() < 50:
            self.draw_flag = True

    def mouseReleaseEvent(self, Qevent):
        self.draw_flag = False

    def mouseMoveEvent(self, Qevent):
        moveX = Qevent.globalX() - self.initX
        moveY = Qevent.globalY() - self.initY
        if not self.draw_flag:
            return
        self.moveX.emit(moveX)
        self.moveY.emit(moveY)

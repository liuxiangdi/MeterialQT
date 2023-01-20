from PyQt5.QtWidgets import (
    QPushButton
)
from components.widgets import MFrame
from PyQt5.QtCore import QPropertyAnimation, QPoint, QAbstractAnimation


class MNavigationDrawer(MFrame):
    def __init__(self, parent):
        super(MNavigationDrawer, self).__init__(parent)

        self._parent = parent

        self.show_animation = None
        self.appear_btn = None

        self.set_style()

    def set_style(self, width=200, height=None, background_color="#FFFFFF"):
        if not height:
            height = self._parent.height()
        self.setGeometry(-width, 0, width, height)

        hide_btn = QPushButton(parent=self)
        hide_btn.setGeometry(int(width / 2 - 18), int(height - 60), 36, 36)
        hide_btn.setStyleSheet("border-image:url('assests/back.svg')")
        hide_btn.clicked.connect(self.disappear)

        self.show_animation = QPropertyAnimation(self, b"pos")
        self.show_animation.setStartValue(QPoint(-width, 0))
        self.show_animation.setEndValue(QPoint(0, 0))
        self.show_animation.setDuration(200)
        self.show_animation.setDirection(QAbstractAnimation.Forward)
        self.setStyleSheet("background-color:{};border-right:1px solid #e0e0e0".format(background_color))

    def drawerEvent(self, Qevent):
        if Qevent <= 0:
            return
        self.move(min(Qevent - self.width(), 0), 0)

    def appear(self):
        # 如果采用 btn trigger使得menu出现，可使用该方法
        if self.appear_btn is not None:
            self.appear_btn.hide()
        self.show_animation.setStartValue(self.pos())
        self.show_animation.setDirection(QAbstractAnimation.Forward)
        self.show_animation.start()

    def disappear(self):
        if self.appear_btn is not None:
            self.appear_btn.show()
        self.show_animation.setEndValue(self.pos())
        self.show_animation.setDirection(QAbstractAnimation.Backward)
        self.show_animation.start()

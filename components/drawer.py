from PyQt5.QtWidgets import (
    QLabel,
)
from components.buttons import MPushButton
from components.widgets import MFrame
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import QPropertyAnimation, Qt, QPoint, QAbstractAnimation


class MSideMenu(MFrame):
    def __init__(self, parent):
        super(MSideMenu, self).__init__(parent)

        self.show_animation = None
        self.appear_btn = None

    def set_style(self, style_map):
        width = style_map['width']
        height = style_map['height']
        self.setGeometry(-width, 0, width, height)

        background_color = style_map['background-color']
        header_img_path = style_map['header_img']

        header_img = QLabel(self)
        header_img.setGeometry(int(width / 2 - 32), 32, 64, 64)
        header_img.setStyleSheet("border-image:url({});".format(header_img_path))

        info_label = QLabel("1578608950@qq.com", self)
        info_label.setGeometry(0, 100, width, 60)
        info_label.setAlignment(Qt.AlignCenter)
        font_id = QFontDatabase.addApplicationFont("font/Roboto-Regular-14.ttf")
        font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_name, 10, 1)
        info_label.setFont(font)

        hide_btn = MPushButton(parent=self)
        hide_btn.setGeometry(int(width / 2 - 24), int(height - 80), 48, 48)
        hide_btn.setStyleSheet("border-image:url('assests/back.svg')")

        hide_btn.clicked.connect(self.disappear)

        self.show_animation = QPropertyAnimation(self, b"pos")
        self.show_animation.setStartValue(QPoint(-width, 0))
        self.show_animation.setEndValue(QPoint(0, 0))
        self.show_animation.setDuration(200)
        self.show_animation.setDirection(QAbstractAnimation.Forward)
        self.setStyleSheet("background-color:{}".format(background_color))
        self.setup_btns()

    def set_trigger_btn(self, btn):
        btn.clicked.connect(self.appear)
        self.appear_btn = btn

    def appear(self):
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

    def setup_btns(self):
        """
        user should rewrite this function
        """
        pass

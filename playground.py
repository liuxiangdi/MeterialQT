from PyQt5.QtWidgets import (
    QLabel,
    QGraphicsDropShadowEffect,
)
from components.buttons import MPushButton
from components.widgets import MFrame
from PyQt5.QtGui import QColor, QFontDatabase, QFont
from PyQt5.QtCore import QPropertyAnimation, QRect


class PlayGround(MFrame):
    def __init__(self, parent=None):
        super(PlayGround, self).__init__(parent)

        # 效果
        self.shadow_effect = None
        self.shadow_animation = None
        # 控件
        self.top_bar = None
        self.line_label = None
        self.view_box = None
        self.setup_ui()

    def setup_ui(self):
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(1)
        shadow_effect.setColor(QColor(200, 200, 200))
        shadow_effect.setOffset(0, 0)
        self.shadow_effect = shadow_effect
        self.setGraphicsEffect(self.shadow_effect)
        self.setStyleSheet("MFrame{margin:0px;padding:0px;border:1px solid;"
                           "border-color:rgb(220,220,220);background-color:white}")
        self.setGeometry(100, 100, 1366, 768)
        self.top_bar = MFrame(self)
        self.top_bar.setGeometry(0, 0, 1366, 80)

        font_id = QFontDatabase.addApplicationFont("font/Roboto-Regular-14.ttf")
        font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_name, 14, 1)
        config_label = QLabel("Configuration", self.top_bar)
        config_label.setGeometry(1030, 1, 150, 78)
        config_label.setStyleSheet("color: rgb(100, 100, 100)")
        config_label.setFont(font)

        self.line_label = QLabel(self.top_bar)
        self.line_label.setStyleSheet("background-color:rgb(80, 80, 80)")
        self.line_label.setGeometry(50, 76, 200, 4)

        view_box = MFrame(self)
        view_box.setGeometry(0, 80, 1000, 688)
        view_box.setStyleSheet("border-top:none;background-color:#fafafa")
        self.view_box = view_box
        self.fillViewBox()

        self.buildupTopBtns()
        self.line_label.raise_()

        options = MFrame(self)
        options.setGeometry(1000, 80, 366, 688)
        options.setStyleSheet("border-top:none;border-left:none;")

        option_label = QLabel("Options", options)
        option_label.setGeometry(30, 30, 150, 60)
        font = QFont(font_name, 13, 1)
        option_label.setStyleSheet("color: rgb(100, 100, 100)")
        option_label.setFont(font)

        self.shadow_animation = QPropertyAnimation(self)
        self.shadow_animation.setTargetObject(self.shadow_effect)
        self.shadow_animation.setPropertyName(b"blurRadius")
        self.shadow_animation.setStartValue(1)
        self.shadow_animation.setEndValue(40)
        self.shadow_animation.setDuration(500)

    def buildupTopBtns(self):
        pass

    def buildupOptions(self):
        pass

    def fillViewBox(self):
        pass

    def moveSlider(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.line_label)
        animation.setPropertyName(b"geometry")
        animation.setStartValue(self.line_label.geometry())
        geo = self.sender().geometry()
        animation.setEndValue(QRect(geo.x(), 76, geo.width(), 4))
        animation.setDuration(200)
        animation.start()

    def enterEvent(self, Qevent):
        self.shadow_animation.start()

    def leaveEvent(self, Qevent):
        self.shadow_animation.stop()
        self.shadow_effect.setBlurRadius(1)


class ButtonsPlayGround(PlayGround):
    def __init__(self, parent=None):
        super(ButtonsPlayGround, self).__init__(parent)
        self.contained_btn = None
        self.text_btn = None

    def buildupTopBtns(self):
        contained_btn = MPushButton("CONTAINED", self.top_bar)
        contained_btn.setGeometry(50, 1, 180, 78)
        style_sheet = contained_btn.styleSheet()
        style_sheet = style_sheet.replace("500", "300").replace("8px", "0px").replace("#f4f0f9", "#f9f9f9")
        contained_btn.setStyleSheet(style_sheet)

        text_btn = MPushButton("TEXT", self.top_bar)
        text_btn.setGeometry(230, 1, 150, 78)
        text_btn.setStyleSheet(style_sheet)

        contained_btn.released.connect(self.moveSlider)
        contained_btn.clicked.connect(text_btn.deactivate)
        contained_btn.clicked.connect(self.contained_btn.show)
        contained_btn.clicked.connect(self.text_btn.hide)
        text_btn.released.connect(self.moveSlider)
        text_btn.clicked.connect(contained_btn.deactivate)
        text_btn.clicked.connect(self.contained_btn.hide)
        text_btn.clicked.connect(self.text_btn.show)
        self.line_label.setGeometry(50, 76, 180, 4)

    def fillViewBox(self):
        width = self.view_box.width()
        height = self.view_box.height()
        font_id = QFontDatabase.addApplicationFont("font/Roboto-Regular-14.ttf")
        font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_name, 14, 500)

        self.contained_btn = MPushButton("BUTTON", self.view_box, "contained")
        self.contained_btn.setFont(font)
        self.contained_btn.setGeometry(int(width / 2 - 90), int(height / 2 - 30), 160, 60)

        self.text_btn = MPushButton("BUTTON", self.view_box)
        self.text_btn.setFont(font)
        style_sheet = self.text_btn.styleSheet().replace("white", "#fafafa")
        style_sheet = style_sheet.replace("#808080", "#6e14ef")

        self.text_btn.setStyleSheet(style_sheet)
        self.text_btn.setGeometry(int(width / 2 - 90), int(height / 2 - 30), 160, 60)
        self.text_btn.hide()

    def buildupOptions(self):
        pass

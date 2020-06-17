from PyQt5.QtWidgets import (
    QPushButton,
    QGraphicsDropShadowEffect,
)
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation
from PyQt5.QtGui import QFontDatabase, QFont


class MPushButton(QPushButton):
    """
    MPushButton has three style:
    """
    clicked = pyqtSignal(bool)
    released = pyqtSignal(bool)

    def __init__(self, text=None, parent=None, style="text"):
        super(MPushButton, self).__init__(text, parent)
        self.style = style
        if text:
            self.setText(text)
        fontID = QFontDatabase.addApplicationFont("font/Roboto-Regular-14.ttf")
        fontName = QFontDatabase.applicationFontFamilies(fontID)[0]
        self.font = QFont(fontName, 14, 1)

        self.setupStyle(style)

    def setupStyle(self, style):
        baseStyle = "border:none;border-radius:8px;color:#808080;"
        self.setFont(self.font)
        if style.lower() == "text":
            styleSheet = "QPushButton{*}QPushButton:hover{^}"
            styleSheet = styleSheet.replace('*', "background-color:white;" + baseStyle)
            styleSheet = styleSheet.replace('^', "background-color: #f4f0f9")
            self.setStyleSheet(styleSheet)

        elif style.lower() == "contained":
            styleSheet = "QPushButton{*}QPushButton:hover{^}"
            styleSheet = styleSheet.replace('*', baseStyle + "color:white;" + "background-color:#6200ee")
            styleSheet = styleSheet.replace('^', "background-color:#6e14ef")
            self.setStyleSheet(styleSheet)

            shadow_effect = QGraphicsDropShadowEffect()
            shadow_effect.setBlurRadius(1)
            shadow_effect.setOffset(0, 0)
            self.effect = shadow_effect

            shadow_animation = QPropertyAnimation(self)
            shadow_animation.setTargetObject(self.effect)
            shadow_animation.setPropertyName(b"blurRadius")
            shadow_animation.setStartValue(1)
            shadow_animation.setEndValue(20)
            shadow_animation.setDuration(300)
            self.shadow_animation = shadow_animation

            self.setGraphicsEffect(self.effect)
        else:
            pass

    def enterEvent(self, Qevent):
        if self.style == 'contained':
            self.effect.setOffset(0, 3)
            self.shadow_animation.start()
        else:
            pass

    def leaveEvent(self, Qevent):
        if self.style == 'contained':
            self.effect.setBlurRadius(1)
            self.effect.setOffset(0, 0)

    def mouseReleaseEvent(self, Qevent):
        self.released.emit(True)

    def mousePressEvent(self, Qevent):
        if self.style == 'text':
            style = self.styleSheet().replace("background-color:white", "background-color:#ECECEC")
            style = style.replace("#808080", "#404040")
            self.setStyleSheet(style)
        if self.style == 'contained':
            style = self.styleSheet().replace("background-color:#6200ee", "background-color:#883DF2")
            style = style.replace("#808080", "#404040")
            self.setStyleSheet(style)
        self.clicked.emit(True)

    def deactivate(self, Qevent):
        if self.style == 'text':
            style = self.styleSheet().replace("background-color:#ECECEC", "background-color:white")
            style = style.replace("#404040", "#808080")
            self.setStyleSheet(style)
        if self.style == 'contained':
            style = self.styleSheet().replace("background-color:#883DF2", "background-color:#6200ee")
            style = style.replace("#404040", "#808080")
            self.setStyleSheet(style)

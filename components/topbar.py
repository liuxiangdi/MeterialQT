from PyQt5.QtWidgets import (
    QLabel,
    QPushButton
)
from components.widgets import MFrame
from PyQt5.QtGui import QFont, QFontDatabase


class MTopBar(MFrame):
    def __init__(self, parent, rootFrame):
        super(MTopBar, self).__init__(parent)
        self._parent = parent
        self._rootFrame = rootFrame

        self.setStyle()

    def setStyle(self, background_color="#555555", style="mac", height=80, logo=None, title=None):
        # 设定几何尺寸
        width = self._rootFrame.width()
        self.setGeometry(0, 0, width, height)
        # 设定属性
        minimize_btn = QPushButton(parent=self)
        minimize_btn.setGeometry(width - 100, int(height / 2 - 12), 24, 24)
        minimize_btn.setFlat(True)
        close_btn = QPushButton(parent=self)
        close_btn.setGeometry(width - 50, int(height / 2 - 12), 24, 24)
        close_btn.setFlat(True)
        if style == "mac":
            minimize_btn.setStyleSheet("border-image: url('assests/minimize.svg')")
            close_btn.setStyleSheet("border-image: url('assests/close.svg')")
        else:
            # TODO
            pass
        self.setStyleSheet("background-color:{};".format(background_color) +
                           "border-bottom-left-radius:0px;border-bottom-right-radius:0px")

        if logo:
            logo_label = QLabel(self)
            logo_label.setGeometry(20, height / 2 - 24, 48, 48)
            logo_label.setStyleSheet("border-image: url({})".format(logo))
        if not logo and title:
            title_label = QLabel(title, self)
            title_label.setGeometry(20, 0, 200, self.height())
            title_label.setStyleSheet("color:white;")
            fontID = QFontDatabase.addApplicationFont("font/Roboto-Regular-14.ttf")
            fontName = QFontDatabase.applicationFontFamilies(fontID)[0]
            font = QFont(fontName, 14, 500)
            title_label.setFont(font)
        elif logo and title:
            title_label = QLabel(title, self)
            title_label.setGeometry(100, 0, 200, self.height())
            title_label.setStyleSheet("color:white;")
            fontID = QFontDatabase.addApplicationFont("font/Roboto-Regular-14.ttf")
            fontName = QFontDatabase.applicationFontFamilies(fontID)[0]
            font = QFont(fontName, 16, 500)
            title_label.setFont(font)

        close_btn.clicked.connect(self._rootFrame.close)
        minimize_btn.clicked.connect(self._rootFrame.showMinimized)

    def mousePressEvent(self, Qevent):
        self.mouseX = Qevent.globalX()
        self.mouseY = Qevent.globalY()
        self.windowX = self._rootFrame.x()
        self.windowY = self._rootFrame.y()

    def mouseMoveEvent(self, Qevent):
        distX = Qevent.globalX() - self.mouseX
        distY = Qevent.globalY() - self.mouseY
        self._rootFrame.move(self.windowX + distX, self.windowY + distY)

from PyQt5 import Qt
from PyQt5.QtCore import QFile
from components.drawer import MSideMenu
from components.widgets import MFrame
from components.topbar import MTopBar
from playground import ButtonsPlayGround


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

        top_bar = MTopBar(self, self)
        styleMap = {}
        styleMap["height"] = 80
        styleMap["style"] = 'mac'
        styleMap['logo'] = 'assests/hd_logo.png'
        styleMap['title'] = "PLAYGROUND"
        styleMap["background-color"] = "#404080"
        top_bar.setStyle(styleMap)

        playground = ButtonsPlayGround(self)
        playground.setGeometry(100, 100, 1366, 768)

        # left menu bar

        menu_bar = MSideMenu(self)
        style_map = {}
        style_map['width'] = 300
        style_map['height'] = self.height()
        style_map['background-color'] = "#f0f0f0"
        style_map['header_img'] = "assests/logo.png"

        # trigger_btn = MPushButton(parent=self)
        # trigger_btn.setGeometry(0, int(style_map['height']/2)-24, 48, 48)
        # trigger_btn.setStyleSheet("border-image:url('assests/trigger_btn.svg')")

        menu_bar.set_style(style_map)
        # menu_bar.set_trigger_btn(trigger_btn)

        self.menu_bar = menu_bar
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

    def mousePressEvent(self, Qevent):
        self.mouseX = Qevent.globalX()
        self.windowX = self.menu_bar.x()

    def mouseMoveEvent(self, Qevent):
        distX = Qevent.globalX() - self.mouseX
        if self.menu_bar.x() < 0:
            self.menu_bar.move(min(self.windowX + distX, 0), 0)

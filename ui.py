import time
from PyQt5 import Qt
from PyQt5 import QtCore
from components.tabs import MHTabs
from components.widgets import MFrame, MDrawerFrame
from components.buttons import MPushButton, MTextButton, MContaindedButton, MOutlinedButton
from components.topbar import MTopBar
from components.cards import MCards
from components.utils import read_style
from components.navigation import MNavigationDrawer
from components.page_button_group import MPageButtonsGroup


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
        main_window.setStyleSheet("background-color:#f5f5f5;border-radius:10px;")

        top_bar = MTopBar(main_window, self)
        contents = MDrawerFrame(self)
        contents.setGeometry(0, 80, 1566, 968-80)
        contents.setStyleSheet("background-color:#f5f5f5;border-radius:0px;")


        page_button_group = MPageButtonsGroup(contents)
        page_button_group.move(100, 100)

        menu = MNavigationDrawer(contents)
        menu.set_style()

        regular_style_sheet = "border:none;color:#808080;background-color:#FFFFFF;"
        activate_style_sheet = "border:none;color:#404040;background-color:#EFEFEF;"
        hover_style_sheet = "border:none;color:#404040;background-color:#ECECEC;"

        btn_button = MTextButton("BUTTONS", menu)
        btn_button.setGeometry(0, 0, menu.width()-1, 60)
        btn_button.set_styles(regular_style_sheet, activate_style_sheet, hover_style_sheet)

        card_button = MTextButton("Cards", menu)
        card_button.setGeometry(0, 60, menu.width()-1, 60)
        card_button.set_styles(regular_style_sheet, activate_style_sheet, hover_style_sheet)

        tabs = MHTabs(contents)
        tabs.set_buttons([["CONTAINED", 200, 76], ["TEXT", 150, 76], ["OUTLINED", 200, 76]])
        tabs.move(100, 20)

        btn_button.clicked.connect(card_button.set_regular)
        card_button.clicked.connect(btn_button.set_regular)

        contents.moveX.connect(menu.drawerEvent)

        # btn = MCards(main_window)
        # btn.move(100, 100)


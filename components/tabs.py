from PyQt5.QtWidgets import QLabel
from components.widgets import MFrame
from PyQt5.QtCore import QPropertyAnimation, QRect
from components.buttons import MTextButton

class MHTabs(MFrame):
    """
    横向的Tabs
    """
    def __init__(self, parent=None, height=80, width=None):
        super(MHTabs, self).__init__(parent)

        self.tabs = []
        self.line = None
        if not width:
            width = parent.width()
        self.setFixedSize(width, height)
        self.set_style()

    def set_style(self):
        line = QLabel(self)
        line.setStyleSheet("background-color:#6200ee;")

        animation = QPropertyAnimation(line, b'geometry')
        animation.setDuration(200)

        self.line = line
        self.animation = animation

    def set_buttons(self, btns):
        """
        [["Buttons1", width, height], ["Buttons2", width, height], ["Buttons3", width, height]]
        """
        x = 0
        regular_style_sheet = "border:none;color:#a0a0a0;background-color:#f5f5f5;"
        activate_style_sheet = "border:none;color:#6200ee;background-color:#E9DDF9;"
        hover_style_sheet = "border:none;color:#6200ee;background-color:#F4F0F9;"
        for btn in btns:
            _btn = MTextButton(btn[0], self)
            _btn.setGeometry(x, 0, btn[1], btn[2])
            _btn.set_shadow_effect(activate=False)
            _btn.set_styles(regular_style_sheet, activate_style_sheet, hover_style_sheet)
            x += btn[1]
            self.tabs.append(_btn)
        self.line.setGeometry(0, self.height()-4, self.tabs[0].width(), 4)

        for btn in self.tabs:
            btn.clicked.connect(self.line_move)
            for _btn in self.tabs:
                if btn != _btn:
                    btn.clicked.connect(_btn.set_regular)

    def line_move(self, Qevent):
        self.animation.setStartValue(self.line.geometry())
        self.animation.setEndValue(QRect(self.sender().x(), self.line.y(), self.sender().width(), 4))
        self.animation.start()

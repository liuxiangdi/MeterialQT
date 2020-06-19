from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtGui import QFont
from components.widgets import QFrame
from components.buttons import MOutlinedButton
from components.utils import get_roboto_font

class MPageButtonsGroup(QFrame):
    """
    default style is github style
    """
    def __init__(self, parent=None, max_page=100):
        super(MPageButtonsGroup, self).__init__(parent)

        self.pre_btn = None
        self.next_btn = None
        self.page_btns = []
        self.max_page = max_page
        self.current_page = 1

        self.set_style()
        self.set_connects()

    def set_style(self):
        regular_style = "border:1px solid #e0e0e0;border-radius:0px;color:#0361D6;background-color:#FFFFFF;border-left:0px"
        activate_style = "border:1px solid #e0e0e0;border-radius:0px;color:#FFFFFF;background-color:#0366D6;border-left:0px"
        hover_style = "border:1px solid #e0e0e0;border-radius:0px;color:#0361D6;background-color:#EFF3F6;border-left:0px;"
        lay_out = QHBoxLayout(self)
        lay_out.setSpacing(0)
        font = QFont(get_roboto_font(), 11, 1)
        for i in range(10):
            btn = MOutlinedButton(str(i+1), self)
            btn.set_styles(regular_style, activate_style, hover_style)
            btn.setFixedSize(50, 40)
            btn.setFont(font)
            btn.set_shadow_effect(activate=False)
            self.page_btns.append(btn)

        font = QFont(get_roboto_font(), 11, 100)
        self.pre_btn = MOutlinedButton("上一页", self)
        pre_regular_style = "border:1px solid #e0e0e0;border-top-left-radius:8px;border-bottom-left-radius:8px;" \
                            "color:#0361D6;background-color:#FFFFFF;"
        pre_hover_style = "border:1px solid #e0e0e0;border-top-left-radius:8px;border-bottom-left-radius:8px;" \
                      "color:#0361D6;background-color:#EFF3F6;"
        self.pre_btn.set_styles(pre_regular_style, pre_hover_style, pre_hover_style)
        self.pre_btn.setFont(font)
        self.pre_btn.setFixedSize(120, 40)
        self.pre_btn.set_shadow_effect(activate=False)

        next_regular_style = "border:1px solid #e0e0e0;border-top-right-radius:8px;border-bottom-right-radius:8px;" \
                            "color:#0361D6;background-color:#FFFFFF;border-left:0px"
        next_hover_style = "border:1px solid #e0e0e0;border-top-right-radius:8px;border-bottom-right-radius:8px;" \
                          "color:#0361D6;background-color:#EFF3F6;border-left:0px;"
        self.next_btn = MOutlinedButton("下一页", self)
        self.next_btn.set_styles(next_regular_style, next_hover_style, next_hover_style)
        self.next_btn.setFont(font)
        self.next_btn.setFixedSize(120, 40)
        self.next_btn.set_shadow_effect(activate=False)

        lay_out.addWidget(self.pre_btn)
        for btn in self.page_btns:
            lay_out.addWidget(btn)
        lay_out.addWidget(self.next_btn)
        self.on_click_page(None, 1)

    def set_connects(self):
        for btn in self.page_btns:
            btn.clicked.connect(self.on_click_page)
        self.pre_btn.clicked.connect(self.on_click_direction)
        self.next_btn.clicked.connect(self.on_click_direction)

    def on_click_page(self, Qevent, current_page=None):
        if not current_page:
            self.current_page = int(self.sender().text())
        else:
            self.current_page = current_page

        print(self.current_page)

        if self.current_page < 5:
            for i in range(10):
                self.page_btns[i].setText(str(i+1))
                if i == self.current_page-1:
                    self.page_btns[i].set_activate()
                else:
                    self.page_btns[i].set_regular()
        else:
            for i in range(10):
                if i == 4:
                    self.page_btns[i].set_activate()
                else:
                    self.page_btns[i].set_regular()
                self.page_btns[i].setText(str(self.current_page+i-4))

    def on_click_direction(self):
        if self.sender() == self.pre_btn:
            current_page = min(max(self.current_page - 1, 1), self.max_page)
            self.on_click_page(None, current_page)
        else:
            current_page = min(max(self.current_page + 1, 1), self.max_page)
            self.on_click_page(None, current_page)
from PyQt5.QtWidgets import (
    QLabel,
    QGraphicsDropShadowEffect,
    QVBoxLayout,
)
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation, Qt
from PyQt5.QtGui import QFont, QColor, QPixmap
from components.utils import get_roboto_font
from components.widgets import MFrame


class MCards(MFrame):
    """
    用户可用的设置函数为:
    """
    clicked = pyqtSignal(bool)
    released = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(MCards, self).__init__(parent)
        self.shadow_effect = None
        self.shadow_effect_config = None
        self.shadow_animation = None
        self.init_style()

    def set_shadow_effect(self, enter_radius=20, enter_offset=(0, 2), leave_radius=5, leave_offset=(0, 2),
                          activate=True):
        """
        effect 创造后不会回收，所有只创建一个effect，检查到该effect已存在后跳过
        """
        if getattr(self, "shadow_effect", None):
            # print("已存在effect")
            pass
        else:
            shadow_effect = QGraphicsDropShadowEffect(self)
            shadow_effect.setColor(QColor(180, 180, 180))
            shadow_effect.setBlurRadius(5)
            shadow_effect.setOffset(0, 2)
            self.shadow_effect_config = [enter_radius, enter_offset, leave_radius, leave_offset]
            self.shadow_effect = shadow_effect
        if not activate:
            self.shadow_effect.setEnabled(False)

    def get_shadow_effect(self):
        return self.shadow_effect

    def set_shadow_animation(self, start_val=5, end_val=20, duration=300, activate=True):
        if getattr(self, "shadow_animation", None):
            # print("已存在animation")
            pass
        else:
            shadow_animation = QPropertyAnimation(self)
            shadow_animation.setTargetObject(self.shadow_effect)
            shadow_animation.setPropertyName(b"blurRadius")
            shadow_animation.setStartValue(start_val)
            shadow_animation.setEndValue(end_val)
            shadow_animation.setDuration(duration)
            self.shadow_animation = shadow_animation
        if not activate:
            self.shadow_animation.setDuration(1)

    def get_shadow_animation(self):
        return self.shadow_animation

    def init_style(self):
        title_font = QFont(get_roboto_font(), 18, 500)
        text_font = QFont(get_roboto_font(), 10, 1)

        layout = QVBoxLayout(self)

        image_label = QLabel()
        _image = QPixmap("assests/image.png")
        image_label.setFixedSize(300, int(300/_image.width()*_image.height()))
        image_label.setStyleSheet("border-image:url('assests/image.png');border-bottom-left-radius:0px;border-bottom-right-radius:0px;")

        title_label = QLabel("Title")
        title_label.setFont(title_font)
        title_label.setMargin(10)

        text_label = QLabel("They should be easy to scan for relevant and actionable information. "
                            "Elements, like text and images, "
                            "should be placed on them in a way that clearly indicates hierarchy.")
        text_label.setWordWrap(True)
        text_label.setFixedWidth(300)
        text_label.setFont(text_font)
        text_label.setAlignment(Qt.AlignTop)
        text_label.setContentsMargins(10, 0, 10, 10)

        layout.addWidget(image_label)
        layout.addWidget(title_label)
        layout.addWidget(text_label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.image_label = image_label
        self.title_label = title_label
        self.text_label = text_label

        self.setLayout(layout)
        self.setStyleSheet("background-color:white;border-radius:10px;")

        self.set_shadow_effect()
        self.set_shadow_animation()

        self.setGraphicsEffect(self.shadow_effect)

    def set_image(self, path):
        style = self.image_label.styleSheet() + "border-image:url({});".format(path)
        self.image_label.setStyleSheet(style)

    def set_title(self, title):
        self.title_label.setText(title)

    def set_text(self, text):
        self.text_label.setText(text)

    def enterEvent(self, evt):
        # 进入/悬停时,自动显示阴影效果,并显示悬停样式
        self.shadow_effect.setBlurRadius(self.shadow_effect_config[0])
        self.shadow_effect.setOffset(self.shadow_effect_config[1][0], self.shadow_effect_config[1][1])
        self.shadow_animation.start()

    def leaveEvent(self, evt):
        # 离开悬停时，关闭阴影效果，并回到进入前的样式
        self.shadow_animation.stop()
        self.shadow_effect.setBlurRadius(self.shadow_effect_config[2])
        self.shadow_effect.setOffset(self.shadow_effect_config[3][0], self.shadow_effect_config[3][1])

from PyQt5.QtWidgets import (
    QPushButton,
    QGraphicsDropShadowEffect,
)
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation
from PyQt5.QtGui import QFont, QColor
from components.utils import get_roboto_font


class MPushButton(QPushButton):
    """
    用户可用的设置函数为:
    set_shadow_effect  set_shadow_animation  set_regular_style  set_activate_style  set_hover_style
    """
    clicked = pyqtSignal(bool)
    released = pyqtSignal(bool)

    def __init__(self, text=None, parent=None):
        super(MPushButton, self).__init__(text, parent)
        # 设定Button文字
        if text:
            self.setText(text)

        self.shadow_effect = None
        self.shadow_effect_config = None
        self.shadow_animation = None

        # normal
        self.regular_style = None
        # pressed
        self.activate_style = None
        # hover
        self.hover_style = None
        # state 0(regular)/1(pressed),离开悬停状态后需要回到上一个状态
        self.style_state = 0

        # 设定默认style
        self.set_regular_style()
        self.set_activate_style()
        self.set_hover_style()
        self.setup_style()

    def set_shadow_effect(self, enter_radius=10, enter_offset=(0, 3), leave_radius=1, leave_offset=(0, 0),
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
            shadow_effect.setBlurRadius(1)
            shadow_effect.setOffset(0, 0)
            self.shadow_effect_config = [enter_radius, enter_offset, leave_radius, leave_offset]
            self.shadow_effect = shadow_effect
        if not activate:
            self.shadow_effect.setEnabled(False)

    def get_shadow_effect(self):
        return self.shadow_effect

    def set_shadow_animation(self, start_val=1, end_val=20, duration=300, activate=True):
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

    def set_regular_style(self, style_sheet=None):
        self.regular_style = style_sheet

    def set_activate_style(self, style_sheet=None):
        self.activate_style = style_sheet

    def set_hover_style(self, style_sheet=None):
        self.hover_style = style_sheet

    def set_styles(self, regular_style=None, activate_style=None, hover_style=None):
        self.regular_style = regular_style
        self.activate_style = activate_style
        self.hover_style = hover_style
        self.setup_style()

    def setup_style(self):
        """
        用户应自己设定style sheet
        """
        # 设定默认字体
        font = QFont(get_roboto_font(), 14, 1)
        self.setFont(font)
        # 设定效果
        self.set_shadow_effect()
        self.set_shadow_animation()
        self.setGraphicsEffect(self.shadow_effect)
        # 设定为常规格式
        if self.regular_style:
            self.setStyleSheet(self.regular_style)

    def enterEvent(self, evt):
        # 进入/悬停时,自动显示阴影效果,并显示悬停样式
        self.setStyleSheet(self.hover_style)
        self.shadow_effect.setBlurRadius(self.shadow_effect_config[0])
        self.shadow_effect.setOffset(self.shadow_effect_config[1][0], self.shadow_effect_config[1][1])
        self.shadow_animation.start()

    def leaveEvent(self, evt):
        # 离开悬停时，关闭阴影效果，并回到进入前的样式
        self.shadow_animation.stop()

        self.shadow_effect.setBlurRadius(self.shadow_effect_config[2])
        self.shadow_effect.setOffset(self.shadow_effect_config[3][0], self.shadow_effect_config[3][1])
        if self.style_state == 0:
            self.set_regular()
        else:
            self.set_activate()
    def mouseReleaseEvent(self, evt):
        self.released.emit(True)

    def mousePressEvent(self, evt):
        self.set_activate()
        self.clicked.emit(True)

    def set_regular(self, evt=None):
        self.style_state = 0
        self.setStyleSheet(self.regular_style)

    def set_activate(self, evt=None):
        self.style_state = 1
        self.setStyleSheet(self.activate_style)


class MTextButton(MPushButton):
    """
    这是一个典型的TEXT button的实现方式
    """
    def __init__(self, text=None, parent=None):
        super(MTextButton, self).__init__(text, parent)


    def set_regular_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:none;border-radius:8px;color:#808080;background-color:#FFFFFF;"
        self.regular_style = style_sheet
        print('regular')

    def set_activate_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:none;border-radius:8px;color:#404040;background-color:#F4F0F9;"
        self.activate_style = style_sheet

    def set_hover_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:none;border-radius:8px;color:#808080;background-color:#ECECEC;"
        self.hover_style = style_sheet


class MContaindedButton(MPushButton):
    """
    这是一个典型的Contained Button的实现方式
    """

    def __init__(self, text=None, parent=None):
        super(MContaindedButton, self).__init__(text, parent)

    def set_regular_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:none;border-radius:8px;color:#FFFFFF;background-color:#6200EE;"
        self.regular_style = style_sheet

    def set_activate_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:none;border-radius:8px;color:#FFFFFF;background-color:#883DF2;"
        self.activate_style = style_sheet

    def set_hover_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:none;border-radius:8px;color:#FFFFFF;background-color:#6E14EF;"
        self.hover_style = style_sheet


class MOutlinedButton(MPushButton):
    """
    这是一个典型的Outlined Button的实现方式
    """

    def __init__(self, parent=None, text=None):
        super(MOutlinedButton, self).__init__(parent, text)
        # self.set_shadow_effect(activate=False)
        # self.set_shadow_animation(activate=False)

    def set_regular_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:1px solid #6200EE;border-radius:8px;color:#6200EE;background-color:#FFFFFF;"
        self.regular_style = style_sheet

    def set_activate_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:1px solid #6200EE;border-radius:8px;color:##6200EE;background-color:#E9DDF9;"
        self.activate_style = style_sheet

    def set_hover_style(self, style_sheet=None):
        if style_sheet is None:
            style_sheet = "border:1px solid #6200EE;border-radius:8px;color:#6200EE;background-color:#F4F0F9;"
        self.hover_style = style_sheet

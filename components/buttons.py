from PyQt5.QtWidgets import QPushButton

class MPushButton(QPushButton):
    """
    MPushButton has three style:
    """
    def __init__(self, parent=None, style="text"):
        super(MPushButton, self).__init__(parent)
        self.setText("BUTTON")
        self.setupStyle(style)

    def setupStyle(self, style):
        color = "color:#6200ee;"
        border_color = "rgb(150, 150, 150);"
        fontstyle =  "font:26px;font-weight:500;font-family:'Calibri';"
        none_border = "border:none;"
        bg_color = "background-color: #f4f0f9;"
        self.setFixedSize(150, 50)
        if style.lower() == "text":
            styleSheet = "QPushButton{*}QPushButton:hover{^}"
            styleSheet = styleSheet.replace('*', color+fontstyle+none_border)
            styleSheet = styleSheet.replace('^', bg_color)
            self.setStyleSheet(styleSheet)
        elif style.lower() == "contained":
            styleSheet = "QPushButton{*}QPushButton:hover{^}"
            styleSheet = styleSheet.replace('*', color+fontstyle+none_border)
            styleSheet = styleSheet.replace('^', bg_color)
        else:

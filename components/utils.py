from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import QFile


def get_roboto_font():
    font_id = QFontDatabase.addApplicationFont("font/Roboto-Regular-14.ttf")
    font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
    return font_name


def read_style():
    qss = QFile("stylesheet.qss")
    qss.open(QFile.ReadOnly)
    qtBytes = qss.readAll()
    pyBytes = qtBytes.data()
    styleStr = pyBytes.decode("utf-8")
    return styleStr

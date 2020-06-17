from PyQt5.QtGui import QFontDatabase, QFont


def get_roboto_font():
    font_id = QFontDatabase.addApplicationFont("font/Roboto-Regular-14.ttf")
    font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
    return font_name


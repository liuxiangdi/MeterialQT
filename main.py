import sys
from ui import UI
from PyQt5.QtWidgets import QApplication


class APP():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = UI(self)


def run():
    app = APP()
    app.ui.show()
    sys.exit(app.app.exec_())


if __name__ == "__main__":
    run()

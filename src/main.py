import sys

from PyQt5.QtWidgets import QApplication

from src.gui.screen_base import BaseScreen


def main():
    app = QApplication(sys.argv)
    window = BaseScreen()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
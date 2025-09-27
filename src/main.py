import sys
from PyQt5.QtWidgets import QApplication
from src.gui.screen_waiting_plate_reading import WaitingScreen


def main():
    app = QApplication(sys.argv)
    window = WaitingScreen()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
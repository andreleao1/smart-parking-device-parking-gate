from PyQt5.QtCore import Qt, QDateTime, QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QApplication


class WaitingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Parking")

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        datetime_container = QWidget()
        datetime_container.setStyleSheet("background-color: #ADD8E6;")
        datetime_layout = QHBoxLayout(datetime_container)
        datetime_layout.setAlignment(Qt.AlignRight)

        self.date_label = QLabel()
        self.time_label = QLabel()
        font_info = QFont("Manrope", 14)
        self.date_label.setFont(font_info)
        self.time_label.setFont(font_info)

        self.date_label.setStyleSheet("color: black;")
        self.time_label.setStyleSheet("color: black;")

        datetime_layout.addWidget(self.date_label)
        datetime_layout.addWidget(self.time_label)

        top_hbox = QHBoxLayout()
        top_hbox.addStretch(1)
        top_hbox.addWidget(datetime_container)

        main_layout.addLayout(top_hbox)

        main_layout.addStretch(1)

        icon_label = QLabel()
        pixmap = QPixmap('assets/icons/magnifying_glass.png')
        scaled_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(scaled_pixmap)
        icon_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(icon_label)

        title = QLabel("Waiting vehicle plate reading...")
        title.setFont(QFont("Manrope", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        subtitle = QLabel("The system is already to read the next vehicle plate.")
        subtitle.setFont(QFont("Manrope", 12))
        subtitle.setStyleSheet("color: gray;")
        subtitle.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(subtitle)

        main_layout.addStretch(1)

        self.setLayout(main_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)
        self.update_datetime()

    def update_datetime(self):
        now = QDateTime.currentDateTime()
        self.date_label.setText(now.toString("dd/MM/yyyy"))
        self.time_label.setText(now.toString("HH:mm:ss"))
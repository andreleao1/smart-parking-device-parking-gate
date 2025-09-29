from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QStackedLayout
)

from src.gui.screen_waiting_plate_reading import WaitingScreen
from src.gui.screen_checkout_successful import CheckoutSuccessfulScreen


class BaseScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Parking")
        self.resize(800, 600)  # tamanho inicial da janela

        # --- Layout principal ---
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        # --- Data e hora ---
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

        # --- Stack de telas ---
        self.stack = QStackedLayout()
        self.stack.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(self.stack, stretch=1)

        self.setLayout(main_layout)

        # --- Timer para atualizar data e hora ---
        self.timer_datetime = QTimer(self)
        self.timer_datetime.timeout.connect(self.update_datetime)
        self.timer_datetime.start(1000)
        self.update_datetime()

        # --- Criação das telas ---
        self.waiting_screen = WaitingScreen()
        self.checkout_screen = CheckoutSuccessfulScreen()
        self.stack.addWidget(self.waiting_screen)
        self.stack.addWidget(self.checkout_screen)

        # --- Tela inicial ---
        self.stack.setCurrentWidget(self.waiting_screen)

        # --- Timer para alternar telas automaticamente ---
        self.switch_timer = QTimer(self)
        self.switch_timer.timeout.connect(self.switch_screen)
        self.switch_timer.start(5000)  # troca a cada 5 segundos
        self.showing_waiting = True

    def update_datetime(self):
        now = QDateTime.currentDateTime()
        self.date_label.setText(now.toString("dd/MM/yyyy"))
        self.time_label.setText(now.toString("HH:mm:ss"))

    def switch_screen(self):
        """Alterna entre WaitingScreen e CheckoutSuccessfulScreen"""
        if self.showing_waiting:
            self.stack.setCurrentWidget(self.checkout_screen)
        else:
            self.stack.setCurrentWidget(self.waiting_screen)
        self.showing_waiting = not self.showing_waiting

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class SmartParkingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Smart Parking')
        self.setGeometry(100, 100, 800, 600)  # Define a posição e o tamanho da janela
        self.init_ui()

    def init_ui(self):
        # Layout principal da janela
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Configura o layout para centralizar o conteúdo
        main_layout.setAlignment(Qt.AlignCenter)

        # --- Título Superior ---
        # Este é apenas um exemplo. Em um projeto real, você usaria um layout mais complexo
        # para a barra superior.
        title_label = QLabel('Smart Parking')
        title_font = QFont('Arial', 24)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #0d6efd;")
        title_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title_label)

        # --- Conteúdo Central ---
        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignCenter)

        # Imagem da lupa
        # Você precisará ter um arquivo de imagem 'lupa.png' no mesmo diretório do script.
        # Caso contrário, substitua o caminho abaixo.
        try:
            pixmap = QPixmap('lupa.png')
            if not pixmap.isNull():
                lupa_label = QLabel()
                # Redimensiona a imagem para caber na tela
                lupa_label.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                lupa_label.setAlignment(Qt.AlignCenter)
                center_layout.addWidget(lupa_label)
        except Exception as e:
            print(f"Não foi possível carregar a imagem: {e}")
            lupa_label = QLabel("Ícone da Lupa") # Exibe um texto alternativo
            lupa_label.setAlignment(Qt.AlignCenter)
            center_layout.addWidget(lupa_label)

        # Texto principal
        main_text_label = QLabel('Aguardando detecção do veículo...')
        main_text_font = QFont('Arial', 20, QFont.Bold)
        main_text_label.setFont(main_text_font)
        main_text_label.setAlignment(Qt.AlignCenter)
        center_layout.addWidget(main_text_label)

        # Texto de instrução
        instruction_label = QLabel('O sistema está pronto para ler a placa do próximo carro.')
        instruction_font = QFont('Arial', 12)
        instruction_label.setFont(instruction_font)
        instruction_label.setAlignment(Qt.AlignCenter)
        instruction_label.setStyleSheet("color: #888;")
        center_layout.addWidget(instruction_label)

        # Adiciona o layout central ao layout principal
        main_layout.addLayout(center_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SmartParkingApp()
    window.show()
    sys.exit(app.exec_())
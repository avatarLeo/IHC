import sys
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QPalette, QImage

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reprodutor de Vídeo")

        # Criar widget para exibir o vídeo
        self.video_widget = QLabel()
        self.video_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Criar botão para reproduzir o vídeo
        self.play_button = QPushButton("Reproduzir")
        self.play_button.clicked.connect(self.play_video)

        # Criar botão para pausar o vídeo
        self.pause_button = QPushButton("Pausar")
        self.pause_button.clicked.connect(self.pause_video)

        # Criar layout para organizar os widgets
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)

        # Definir layout como layout principal da janela
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Criar media player
        self.media_player = QMediaPlayer()

        # Carregar o vídeo
        self.media_player.setSource(QUrl.fromLocalFile("teste.mp4"))

    def play_video(self):
        self.media_player.play()

    def pause_video(self):
        self.media_player.pause()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayer()
    window.show()
    sys.exit(app.exec())

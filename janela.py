import sys
from PyQt6.QtCore import Qt, QUrl, QRect
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QGridLayout, QPushButton, QLabel, QLineEdit)


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.create_component()
        self.setGeometry(20, 20, 600, 250)


    def create_component(self):
        rigth_layout = QVBoxLayout()
        left_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        main_layout = QGridLayout()

        lbl_name = QLabel("Nonme:")
        left_layout.addWidget(lbl_name)
        txt_name = QLineEdit()
        left_layout.addWidget(txt_name)

        lbl_email = QLabel("Email:")
        left_layout.addWidget(lbl_email)
        self.txt_email = QLineEdit()
        left_layout.addWidget(self.txt_email)

        btn_clear = QPushButton("Limpar")
        button_layout.addWidget(btn_clear)
        btn_clear.setProperty("class", "clear")
        btn_save = QPushButton("Salvar")
        button_layout.addWidget(btn_save)
        btn_save.clicked.connect(self.play)

        left_layout.addLayout(button_layout)

        main_layout.addLayout(left_layout, 0, 0)

        main_widget = QWidget()

        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
        rigth_layout.setGeometry(QRect(100, 100, 11, 16))

        # video

        self.player = QMediaPlayer()
        self.player.setSource(QUrl.fromLocalFile("teste.mp4"))
        videoWidget = QVideoWidget()
        videoWidget.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        # videoWidget.setGeometry(QRect(100, 200, 11, 16))
        self.player.setVideoOutput(videoWidget)
        rigth_layout.addWidget(videoWidget)
        main_layout.addLayout(rigth_layout, 0, 1)
        main_layout.setColumnStretch(1, 5)
        # videoWidget.show()
        # player.play()

        with open('style.css', 'r') as file:
            self.setStyleSheet(file.read())

    def play(self):
        self.player.play()
        print(self.txt_email)
        

    
    def play_video(self):
        ...



app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
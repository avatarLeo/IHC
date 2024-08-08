from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QSplitter
from PyQt5.QtGui import QPixmap
import sys


class Janela(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 800, 500)
        self.create_component()

    def create_component(self):
        right_widget = QWidget()
        left_widget = QWidget()
        
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        layout = QVBoxLayout()

        

        input_email_layout = QHBoxLayout()
        input_password_layout = QHBoxLayout()

        self.icon_sound_email = QLabel('icon')
        self.icon_sound_email.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))
        self.icon_sound_password = QLabel('icon')
        self.icon_sound_password.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))



        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText('Email')

        input_email_layout.addWidget(self.txt_email)
        input_email_layout.addWidget(self.icon_sound_email)

        self.txt_password = QLineEdit()
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_password.setPlaceholderText('Senha')
        input_password_layout.addWidget(self.txt_password)
        input_password_layout.addWidget(self.icon_sound_password)

        self.btn_login = QPushButton('Login')

        self.forgot_password = QLabel('Esquci a senha')

        self.icon_profile = QLabel()
        self.icon_profile.setPixmap(self.add_image(200, 200, 'img/profile.svg'))

        left_layout.addWidget(self.icon_profile)
        left_layout.addLayout(input_email_layout)
        left_layout.addLayout(input_password_layout)
        left_layout.addWidget(self.btn_login)
        left_layout.addWidget(self.forgot_password)
        left_widget.setLayout(left_layout)

        #right layout

        self.cat_icon = QLabel('Cat icon')
        self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))

        self.create_profile = QPushButton('Criar usuário')
        right_layout.addWidget(self.cat_icon)
        right_layout.addWidget(self.create_profile)

        right_widget.setLayout(right_layout)


        splitter_layout = QSplitter()
        
        splitter_layout.addWidget(left_widget)
        splitter_layout.addWidget(right_widget)

        splitter_layout.setSizes([600, 400])
        layout.addWidget(splitter_layout)

        self.setLayout(layout)


    def add_image(self, width, height, path_image):
        self.pixmap_profile = QPixmap(path_image)
        pixmap_profile_resize = self.pixmap_profile.scaled(width, height, Qt.AspectRatioMode.IgnoreAspectRatio)
        return pixmap_profile_resize



    



if __name__ == '__main__':
    app = QApplication(sys.argv)

    jan = Janela()
    jan.show()

    sys.exit(app.exec())
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton,
                            QSplitter)
from PyQt5.QtGui import QPixmap
import sys


class Janela_login(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 800, 500)
        self.create_component()

    def create_component(self):

        with open('style.css', 'r') as file:
            self.setStyleSheet(file.read())


        right_widget = QWidget()
        left_widget = QWidget()
        left_container = QWidget()

        left_widget.setProperty('class', 'left_widget')
        
        left_layout = QVBoxLayout()
        container_layout = QVBoxLayout()
        container_layout.addWidget(left_widget)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        left_container.setLayout(container_layout)
        left_container.setProperty('class', 'left_container')
        right_layout = QVBoxLayout()
        layout = QVBoxLayout()

        

        input_email_layout = QHBoxLayout()
        input_password_layout = QHBoxLayout()

        self.icon_sound_email = QLabel('icon')
        self.icon_sound_email.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))
        self.icon_sound_password = QLabel('icon')
        self.icon_sound_password.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))



        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText('Nome')

        input_email_layout.addWidget(self.txt_email)
        input_email_layout.addWidget(self.icon_sound_email)

        self.txt_password = QLineEdit()
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_password.setPlaceholderText('Senha')
        input_password_layout.addWidget(self.txt_password)
        input_password_layout.addWidget(self.icon_sound_password)

        self.btn_login = QPushButton('Login')
        # self.btn_login.setSizePolicy(QSizePolicy())
    

        self.forgot_password = QPushButton('Esquci a senha')
        self.forgot_password.setProperty('class', 'forgot_password')

        self.icon_profile = QLabel()
        self.icon_profile.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_profile.setPixmap(self.add_image(200, 200, 'img/profile.svg'))

        left_layout.addWidget(self.icon_profile,stretch=3)
        left_layout.addLayout(input_email_layout, 0)
        left_layout.addLayout(input_password_layout, 1)
        left_layout.addWidget(self.btn_login, 1)
        left_layout.addWidget(self.forgot_password, 0, Qt.AlignmentFlag.AlignHCenter)
        left_widget.setLayout(left_layout)


        left_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #right layout

        self.cat_icon = QLabel('Cat icon')
        self.cat_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))

        self.create_profile = QPushButton('Criar usuário')
        self.create_profile.setProperty('class', 'create_profile')
        right_layout.addWidget(self.cat_icon, 2)
        right_layout.addWidget(self.create_profile, 0, Qt.AlignmentFlag.AlignCenter)

        right_widget.setLayout(right_layout)


        splitter_layout = QSplitter()
        
        splitter_layout.addWidget(left_container)
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

    jan = Janela_login()
    jan.show()

    sys.exit(app.exec())
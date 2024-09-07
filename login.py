from PyQt5.QtCore import Qt, QEvent, QSize
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton,
                            QSplitter, QMessageBox)
from PyQt5.QtGui import QPixmap, QMovie, QIcon
from acessibility import *
from sttings import JanelaDeConfiguracao
import sys


class Janela_login(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 800, 500)
        self.create_component()
        self.new_window = JanelaDeConfiguracao()

    def create_component(self):

        with open('style.css', 'r') as file:
            self.setStyleSheet(file.read())


        right_widget = QWidget()
        left_widget = QWidget()
        self.left_container = QWidget()

        left_widget.setProperty('class', 'left_widget')

        btn_settings = QPushButton()
        btn_settings.setIcon(QIcon(self.add_image(300, 300, 'img/settings.png')))
        btn_settings.setIconSize(QSize(40, 40))
        btn_settings.setProperty('class', 'settings')
        btn_settings.clicked.connect(self.window_settings)
        
        left_layout = QVBoxLayout()
        container_layout = QVBoxLayout()
        container_layout.addWidget(btn_settings, 0, Qt.AlignmentFlag.AlignRight)
        container_layout.addWidget(left_widget)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.left_container.setLayout(container_layout)
        self.left_container.setProperty('class', 'left_container')
        self.right_layout = QVBoxLayout()
        layout = QVBoxLayout()

        

        input_email_layout = QHBoxLayout()
        input_password_layout = QHBoxLayout()

        self.icon_sound_email = QLabel('icon')
        self.icon_sound_email.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))
        self.icon_sound_password = QLabel('icon')
        self.icon_sound_password.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))



        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText('Email')
        self.txt_email.installEventFilter(self)

        input_email_layout.addWidget(self.txt_email)
        input_email_layout.addWidget(self.icon_sound_email)

        self.txt_password = QLineEdit()
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_password.setPlaceholderText('Senha')
        self.txt_password.installEventFilter(self)
        input_password_layout.addWidget(self.txt_password)
        input_password_layout.addWidget(self.icon_sound_password)

        self.btn_login = QPushButton('Login')
        self.btn_login.installEventFilter(self)
        self.btn_login.setDefault(True)
        self.btn_login.clicked.connect(self.login)
        # self.btn_login.setSizePolicy(QSizePolicy())
    

        self.forgot_password = QPushButton('Esquci a senha')
        self.forgot_password.installEventFilter(self)
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
        self.create_profile.installEventFilter(self)
        self.create_profile.setProperty('class', 'create_profile')
        self.right_layout.addWidget(self.cat_icon, 2)
        self.right_layout.addWidget(self.create_profile, 0, Qt.AlignmentFlag.AlignCenter)

        right_widget.setLayout(self.right_layout)


        splitter_layout = QSplitter()
        
        splitter_layout.addWidget(self.left_container)
        splitter_layout.addWidget(right_widget)

        splitter_layout.setSizes([600, 400])
        layout.addWidget(splitter_layout)

        self.setLayout(layout)


    def add_image(self, width, height, path_image):
        self.pixmap_profile = QPixmap(path_image)
        pixmap_profile_resize = self.pixmap_profile.scaled(width, height, Qt.AspectRatioMode.IgnoreAspectRatio)
        return pixmap_profile_resize
    
    def eventFilter(self, width, event):
        if event.type() == QEvent.Type.FocusIn:
            if self.deficiency_type() == SEM_DEFICIENCIA:
                self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))

            if width == self.txt_email:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))
                    sounds('sound/login/email.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-login/email.gif')
            elif width == self.txt_password:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))
                    sounds('sound/login/senha.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-login/senha.gif')
            elif width == self.btn_login:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))
                    sounds('sound/login/login.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-login/login.gif')
            elif width == self.create_profile:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))
                    sounds('sound/login/criar-usuario.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-login/criar-usuario.gif')
            elif width == self.forgot_password:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))
                    sounds('sound/login/esqueceu-senha.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-login/esqueceu-senha.gif')
        


        return super().eventFilter(width, event)
        
    
    def deficiency_type(self):
        return self.new_window.deficiency
    

    def movies(self, path_movie='', in_focus=True):
        if in_focus:    
            move = QMovie(path_movie)
            
            self.cat_icon.setMovie(move)
            move.start()
           
        else:
            self.cat_icon.clear()


    def login(self):
        email = self.txt_email

        text = 'Login feito com sucesso'
        # voice(text)
        QMessageBox.information(self, 'Feito!', 'Login feito com sucesso!')

    def window_settings(self):
        self.new_window.show()



    



if __name__ == '__main__':
    app = QApplication(sys.argv)

    jan = Janela_login()
    jan.show()

    sys.exit(app.exec())
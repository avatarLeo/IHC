from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton,
                            QSplitter, QRadioButton, QComboBox)
from PyQt5.QtGui import QPixmap
import sys


class Janela_cadastro(QWidget):
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
        
        self.left_layout = QVBoxLayout()
        container_layout = QVBoxLayout()
        container_layout.addWidget(left_widget)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        left_container.setLayout(container_layout)
        left_container.setProperty('class', 'left_container')
        right_layout = QVBoxLayout()
        layout = QVBoxLayout()

        

        input_nome_layout = QHBoxLayout()
        input_raca_layout = QHBoxLayout()
        input_idade_layout = QHBoxLayout()

        self.icon_sound_nome = QLabel('icon')
        self.icon_sound_nome.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))

        self.icon_sound_raca = QLabel('icon')
        self.icon_sound_raca.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))

        self.icon_sound_idade = QLabel('icon')
        self.icon_sound_idade.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))



        self.txt_nome = QLineEdit()
        self.txt_nome.setPlaceholderText('Nome')

        self.txt_raca = QLineEdit()
        self.txt_raca.setPlaceholderText('Raça')


        self.txt_idade = QLineEdit()
        self.txt_idade.setPlaceholderText('idade')

        input_nome_layout.addWidget(self.txt_nome)
        input_nome_layout.addWidget(self.icon_sound_nome)

       
        input_raca_layout.addWidget(self.txt_raca)
        input_raca_layout.addWidget(self.icon_sound_raca)

        input_idade_layout.addWidget(self.txt_idade)
        input_idade_layout.addWidget(self.icon_sound_idade)

        self.btn_login = QPushButton('Login')
    

        self.forgot_password = QPushButton('Esquci a senha')
        self.forgot_password.setProperty('class', 'forgot_password')

        self.title = QLabel('Cadastre o seu pet')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.left_layout.addWidget(self.title,stretch=2)
        self.left_layout.addLayout(input_nome_layout, 1)
        self.left_layout.addLayout(input_raca_layout, 1)
        self.left_layout.addLayout(input_idade_layout, 1)
        self.create_combobox()
        self.create_radio_button()
        self.left_layout.addWidget(self.btn_login, 1)
        self.left_layout.addWidget(self.forgot_password, 0, Qt.AlignmentFlag.AlignHCenter)
        left_widget.setLayout(self.left_layout)


        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

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


    def create_combobox(self):
        
        self.service_layout = QHBoxLayout()
        lbl_service = QLabel('Serviços:')
        self.service_comboBox = QComboBox()
        service_list = ['Tosa e Banho', 'Veterinário', 'Banho']

        self.service_comboBox.addItems(service_list)

        self.service_comboBox.setItemData(0, 'Serviço de banho e tosa')
        self.service_comboBox.setItemData(1, 'Realise uma consulta com o veterinário')
        self.service_comboBox.setItemData(2, 'Apenas o serviço de banho')

        self.service_layout.addWidget(lbl_service)
        self.service_layout.addWidget(self.service_comboBox,  2, Qt.AlignmentFlag.AlignLeft)

        self.service_comboBox.activated.connect(self.show_data)

        self.left_layout.addLayout(self.service_layout, 1)

    def show_data(self):
        print(self.service_comboBox.currentIndex())

    def create_radio_button(self):
        radio_cat = QRadioButton('Gato', self)
        radio_cat.toggled.connect(self.update)
        radio_dog = QRadioButton('Cachorro', self)
        radio_dog.toggled.connect(self.update)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(radio_cat)
        radio_layout.addWidget(radio_dog)

        self.left_layout.addLayout(radio_layout, 1)

    def update(self):
        rb = self.sender()

        if rb.isChecked():
            print(rb.text())


    



if __name__ == '__main__':
    app = QApplication(sys.argv)

    jan = Janela_cadastro()
    jan.show()

    sys.exit(app.exec())
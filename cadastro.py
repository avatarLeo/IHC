from PyQt5.QtCore import Qt, QEvent, QSize
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton,
                            QSplitter, QRadioButton, QComboBox)
from PyQt5.QtGui import QPixmap, QMovie, QIcon
from acessibility import *
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

        btn_settings = QPushButton()
        btn_settings.setIcon(QIcon(self.add_image(300, 300, 'img/settings.png')))
        btn_settings.setIconSize(QSize(40, 40))
        btn_settings.setProperty('class', 'settings')
        
        self.left_layout = QVBoxLayout()
        container_layout = QVBoxLayout()
        container_layout.addWidget(btn_settings, 0, Qt.AlignmentFlag.AlignRight)
        container_layout.addWidget(left_widget)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        left_container.setLayout(container_layout)
        left_container.setProperty('class', 'left_container')
        right_layout = QVBoxLayout()
        layout = QVBoxLayout()
        

        input_nome_layout = QHBoxLayout()
        input_raca_layout = QHBoxLayout()
        input_idade_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()

        self.icon_sound_nome = QLabel('icon')
        self.icon_sound_nome.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))

        self.icon_sound_raca = QLabel('icon')
        self.icon_sound_raca.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))

        self.icon_sound_idade = QLabel('icon')
        self.icon_sound_idade.setPixmap(self.add_image(30, 30, 'img/sound-transparent.png'))



        self.txt_nome = QLineEdit()
        self.txt_nome.installEventFilter(self)
        self.txt_nome.setPlaceholderText('Nome')

        self.txt_raca = QLineEdit()
        self.txt_raca.installEventFilter(self)
        self.txt_raca.setPlaceholderText('Raça')


        self.txt_idade = QLineEdit()
        self.txt_idade.installEventFilter(self)
        self.txt_idade.setPlaceholderText('idade')

        input_nome_layout.addWidget(self.txt_nome)
        input_nome_layout.addWidget(self.icon_sound_nome)

       
        input_raca_layout.addWidget(self.txt_raca)
        input_raca_layout.addWidget(self.icon_sound_raca)

        input_idade_layout.addWidget(self.txt_idade)
        input_idade_layout.addWidget(self.icon_sound_idade)


        self.btn_cadastrar = QPushButton('Cadastrar')
        self.btn_cadastrar.installEventFilter(self)
        self.btn_cadastrar.setDefault(True)
    

        self.btn_clear = QPushButton('Limpar')
        self.btn_clear.installEventFilter(self)
        self.btn_clear.setDefault(True)
        self.btn_clear.setProperty('class', 'limpar')

        self.title = QLabel('Cadastre o seu pet')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.left_layout.addWidget(self.title, stretch=2)
        self.left_layout.addLayout(input_nome_layout, 1)
        self.left_layout.addLayout(input_raca_layout, 1)
        self.left_layout.addLayout(input_idade_layout, 1)
        self.create_combobox()
        self.create_radio_button()
        self.button_layout.addWidget(self.btn_clear)
        self.button_layout.addWidget(self.btn_cadastrar)
        left_widget.setLayout(self.left_layout)
        self.left_layout.addLayout(self.button_layout)


        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #right layout

        self.cat_icon = QLabel('Cat icon')
        self.cat_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cat_icon.setPixmap(self.add_image(300, 300, 'img/cat.png'))

        right_layout.addWidget(self.cat_icon, 2)

        right_widget.setLayout(right_layout)


        splitter_layout = QSplitter()
        
        splitter_layout.addWidget(left_container)
        splitter_layout.addWidget(right_widget)

        splitter_layout.setSizes([600, 400])
        layout.addWidget(splitter_layout)

        self.setLayout(layout)


    def add_image(self, widget, height, path_image):
        self.pixmap_profile = QPixmap(path_image)
        pixmap_profile_resize = self.pixmap_profile.scaled(widget, height, Qt.AspectRatioMode.IgnoreAspectRatio)
        return pixmap_profile_resize


    def create_combobox(self):
        
        self.service_layout = QHBoxLayout()
        lbl_service = QLabel('Serviços:')
        self.service_comboBox = QComboBox()
        self.service_comboBox.installEventFilter(self)
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
        service_index = self.service_comboBox.currentIndex()

        match service_index:
            case 0:
                self.service_type = 'Tosa e Banhho'
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/tosa-banho.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/tosa-banho.gif')
            case 1:
                self.service_type = 'Veterinário'
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/veterinario.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/veterinario.gif')
            case 2:
                self.service_type = 'Banho'
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/banho.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/banho.gif')

    def create_radio_button(self):
        self.radio_cat = QRadioButton('Gato', self)
        self.radio_cat.installEventFilter(self)
        self.radio_cat.toggled.connect(self.update)
        self.radio_dog = QRadioButton('Cachorro', self)
        self.radio_dog.installEventFilter(self)
        self.radio_dog.toggled.connect(self.update)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio_cat)
        radio_layout.addWidget(self.radio_dog)

        self.left_layout.addLayout(radio_layout, 1)

    def update(self):
        rb = self.sender()

        if rb.isChecked():
            print(rb.text())


    def eventFilter(self, widget, event):
        if event.type() == QEvent.Type.FocusIn:
            if widget == self.txt_nome:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/nome.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/nome.gif')
            elif widget == self.txt_raca:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/raca.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/raca.gif')
            elif widget == self.txt_idade:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/idade.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/idade.gif')
            elif widget == self.service_comboBox:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/serviços.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/servicos.gif')
            elif widget == self.radio_cat:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/gato.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/gato.gif')
            elif widget == self.radio_dog:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/cachorro.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/cachorro.gif')
            elif widget == self.btn_cadastrar:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/cadastrar.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/cadastrar.gif')
            elif widget == self.btn_clear:
                if self.deficiency_type() == COM_DEFICIENCIA_VISUAL:
                    sounds('sound/cadastro/limpar.mp3')
                elif self.deficiency_type() == COM_DEFICIENCIA_AUDITIVA:
                    self.movies('gifs/gifs-cadastro/limpar.gif')
        elif QEvent.Type.KeyPress == event.type():
            print(Qt.Key.Key_Enter, QEvent.Type.KeyPress, event.key())
            if Qt.Key_Return == event.key() and self.radio_cat == widget:
                self.radio_cat.setChecked(True)
            elif Qt.Key_Return == event.key() and self.radio_dog == widget:
                self.radio_dog.setChecked(True)

        return super().eventFilter(widget, event)
        
    
    def deficiency_type(self):
        self.deficiency = COM_DEFICIENCIA_AUDITIVA
        return self.deficiency
    

    def movies(self, path_movie='', in_focus=True):
        if in_focus:    
            move = QMovie(path_movie)
            
            self.cat_icon.setMovie(move)
            move.start()
           
        else:
            self.cat_icon.clear()


    



if __name__ == '__main__':
    app = QApplication(sys.argv)

    jan = Janela_cadastro()
    jan.show()

    sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSplitter
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QEvent

from playsound import playsound

import pyttsx3

class ClientesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cadastro de Clientes')
        self.setGeometry(100, 100, 800, 400)

        left_layout  = QVBoxLayout()   #Parte esquerda: campos de cadastro
        btn_layout   = QHBoxLayout()   #Layout dos botões
        self.right_layout = QVBoxLayout()   #Parte direita: Area para vídeo

        # ========================= Montando os elementos da tela
        # Rótulos
        lbl_nome       = QLabel('Nome:')
        lbl_email      = QLabel('Email:')
        lbl_telefone   = QLabel('Telefone:')
        lbl_endereco   = QLabel('Endereço:')
        self.lbl_movie = QLabel()       
        
        # Campos de entrada de texto
        self.nome_edit      = QLineEdit()
        self.email_edit     = QLineEdit()        
        self.telefone_edit  = QLineEdit()
        self.endereco_edit  = QLineEdit()

        self.nome_edit.installEventFilter(self)
        self.email_edit.installEventFilter(self)       
        self.telefone_edit.installEventFilter(self)
        self.endereco_edit.installEventFilter(self)

        # Botões de ação
        limpar_btn = QPushButton('Limpar')
        cadastrar_btn = QPushButton('Cadastrar')

        # Personalizando botões
        limpar_btn.setStyleSheet('background-color: #ff0000; color: white;')
        cadastrar_btn.setStyleSheet('background-color: #00ff00; color: white;')

        # Atribuíndo ações aos botões
        limpar_btn.clicked.connect(self.limpar_campos)
        cadastrar_btn.clicked.connect(self.cadastrar_cliente)
        

        # ========================= Adicionando itens ao layout Esquerdo
        left_layout.addWidget(lbl_nome)
        left_layout.addWidget(self.nome_edit)

        left_layout.addWidget(lbl_email)
        left_layout.addWidget(self.email_edit)

        left_layout.addWidget(lbl_telefone)
        left_layout.addWidget(self.telefone_edit)

        left_layout.addWidget(lbl_endereco)
        left_layout.addWidget(self.endereco_edit)

        
        # ========================= Adicionando botões ao layout de botões
        btn_layout.addWidget(limpar_btn)
        btn_layout.addWidget(cadastrar_btn)

        # ========================= Adicionando ao layout esquerdo o layout dos botões
        left_layout.addLayout(btn_layout)

        
      
        
        #Criando os QWidgets que vão para o splitter
        left_widget  = QWidget()
        right_widget = QWidget()

        left_widget.setLayout(left_layout)
        right_widget.setLayout(self.right_layout)

        splitter = QSplitter()
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([400, 400])

        layout = QHBoxLayout()
        layout.addWidget(splitter)

        self.setLayout(layout)

        with open('style.css', 'r') as file:
            self.setStyleSheet(file.read())

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.FocusIn:
            if obj == self.nome_edit:
                self.insert_movie('gifs/name.gif')
                self.play_son('sound/nome.wav')
            elif obj == self.email_edit:
                self.insert_movie('gifs/world.gif')
                self.play_son('sound/email.wav')
            elif obj == self.telefone_edit:
                self.insert_movie('gifs/thank.gif')
                self.play_son('sound/telefone.wav')
            elif obj == self.endereco_edit:
                self.insert_movie('gifs/libras_bom_dia.gif')
                self.play_son('sound/endereco.mp3')

        elif event.type() == QEvent.Type.FocusOut:
            self.insert_movie(in_focus=False)

        return super().eventFilter(obj, event)

    def insert_movie(self, path_movie='', in_focus=True):
        
        if in_focus:    
            move = QMovie(path_movie)
            
            self.lbl_movie.setMovie(move)
            move.start()

            self.right_layout.addWidget(self.lbl_movie)
           
        else:
            self.lbl_movie.clear()
        
       


    def play_son(self, audio_path):
        playsound(audio_path)


    def limpar_campos(self):
        self.nome_edit.clear()
        self.email_edit.clear()
        self.telefone_edit.clear()
        self.endereco_edit.clear()

    def cadastrar_cliente(self):
        nome = self.nome_edit.text()
        email = self.email_edit.text()
        telefone = self.telefone_edit.text()
        endereco = self.endereco_edit.text()

        t = ''
        for n in telefone:
            t += n + ';'

        text = f'conferindo informações; nome {nome}, email {email}, telefone {t}, endereço {endereco}, precione enter para confirmar ou esc pra voltar'
        self.voice(text)

        # Aqui você pode adicionar o código para cadastrar o cliente
        # Por exemplo, pode exibir uma mensagem de confirmação
        QMessageBox.information(self, 'Cadastro realizado', f'Cliente {nome} cadastrado com sucesso.')

    def voice(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')


        #language
        engine.setProperty("voice", "brazil")
        #speed
        engine.setProperty("rate", 120)

        engine.say(text)
        engine.runAndWait()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientesWindow()
    window.show()
    sys.exit(app.exec_())
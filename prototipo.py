from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QSplitter
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

        self.txt_email = QLineEdit()
        self.icon_sound = QLabel('icon')
        son = self.icon_sound
        input_email_layout.addWidget(self.txt_email)
        input_email_layout.addWidget(self.icon_sound)

        self.txt_password = QLineEdit()
        input_password_layout.addWidget(self.txt_password)
        input_password_layout.addWidget(son)

        self.icon_profile = QLabel('icon profile')

        self.btn_login = QPushButton('Login')

        self.forgot_password = QLabel('Esquci a senha')

        left_layout.addWidget(self.icon_profile)
        left_layout.addLayout(input_email_layout)
        left_layout.addLayout(input_password_layout)
        left_layout.addWidget(self.btn_login)
        left_layout.addWidget(self.forgot_password)
        right_widget.setLayout(left_layout)


        splitter_layout = QSplitter()
        
        splitter_layout.addWidget(right_widget)
        splitter_layout.addWidget(left_widget)

        splitter_layout.setSizes([400, 400])
        layout.addWidget(splitter_layout)

        self.setLayout(layout)



        #right layout

        self.cat_icon = QLabel()
        self.create_profile = QPushButton()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    jan = Janela()
    jan.show()

    sys.exit(app.exec())
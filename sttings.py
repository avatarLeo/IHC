from PyQt5.QtCore import Qt, QEvent, QSize
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton,
                            QSplitter, QRadioButton, QComboBox)
from PyQt5.QtGui import QPixmap, QMovie, QIcon
from acessibility import *
import sys


class JanelaDeConfiguracao(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 400, 250)
        self.create_component()
        self.deficiency = 1

    def create_component(self):

        with open('style.css', 'r') as file:
            self.setStyleSheet(file.read())
    
        self.horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()

        self.info = QLabel('Informe qual o seu tipo de deficiência')

        btn_ok = QPushButton('Ok')
        btn_ok.setProperty('class', 'deficiency_settings')
        btn_ok.clicked.connect(self.ok)

        vertical_layout.addWidget(self.info)
     

        vertical_layout.addLayout(self.horizontal_layout)
        vertical_layout.addWidget(btn_ok, 0, Qt.AlignmentFlag.AlignRight)

        self.setLayout(vertical_layout)
        self.create_combobox()

    def create_combobox(self):
        
        self.service_layout = QHBoxLayout()
        lbl_service = QLabel('Opções')
        self.service_comboBox = QComboBox()
        self.service_comboBox.installEventFilter(self)
        service_list = ['Sem deficiênci', 'Com Deficiência Visual', 'Com Deficiência Auditiva']

        self.service_comboBox.addItems(service_list)

        self.service_comboBox.setItemData(0, 'Para pessoas sem deficiência')
        self.service_comboBox.setItemData(1, 'Para pessoas com deficiência auditiva')
        self.service_comboBox.setItemData(2, 'Para pessoas com deficiência visual')

        self.service_layout.addWidget(lbl_service)
        self.service_layout.addWidget(self.service_comboBox,  2, Qt.AlignmentFlag.AlignLeft)

        self.service_comboBox.activated.connect(self.show_data)

        self.horizontal_layout.addLayout(self.service_layout, 1)

    def show_data(self):
        self.deficiency = self.service_comboBox.currentIndex()

    def ok(self):
        self.hide()

    




if __name__ == '__main__':
    app = QApplication(sys.argv)

    jan = JanelaDeConfiguracao()
    jan.show()

    sys.exit(app.exec())
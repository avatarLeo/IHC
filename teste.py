import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(100, 100, 200, 30)

        self.button = QPushButton('Chamar função', self)
        self.button.setGeometry(100, 150, 200, 30)
        self.button.clicked.connect(self.lineEdit.setFocus)

        self.lineEdit.focusInEvent.connect(self.lineEditEmFoco)

        self.setWindowTitle('Exemplo de Foco em QLineEdit')
        self.show()

    def lineEditEmFoco(self):
        print('LineEdit em Foco!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Janela(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 800, 500)


app = QApplication(sys.argv)

jan = Janela()
jan.show()

sys.exit(app.exec())
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        

    def create_component(self):
        ...


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
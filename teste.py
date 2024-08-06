import sys
from PyQt6 import QtWidgets


class Main(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Qt Testing")
        self.setGeometry(0, 0, 640, 120)

        h = QtWidgets.QHBoxLayout()

        w = ColorQLineEdit("one")
        h.addWidget(w)

        w = ColorQLineEdit("two")
        h.addWidget(w)

        self.setLayout(h)


class ColorQLineEdit(QtWidgets.QLineEdit):

    def focusInEvent(self, event):
        print("in")
        self.setStyleSheet("background-color: yellow; color: red;")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        print("out")
        self.setStyleSheet("background-color: white; color: black;")
        super().focusOutEvent(event)

app = QtWidgets.QApplication(sys.argv)
jan = Main()
jan.show()

sys.exit(app.exec())
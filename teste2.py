import sys
from PyQt6.QtCore import QCoreApplication, Qt, QEvent
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel("Clique em mim", self)
        self.label.setGeometry(100, 100, 200, 50)
        self.txt_text = QLineEdit(self)
        self.txt_text.setGeometry(100, 200, 200, 50)
        self.txt_text2 = QLineEdit(self)
        self.txt_text2.setGeometry(100, 300, 200, 50)
        self.txt_text.installEventFilter(self)
        self.txt_text2.installEventFilter(self)
    

        self.label.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.FocusIn and obj == self.txt_text:
            self.label.setText(f"txt 1")
        elif event.type() == QEvent.Type.FocusIn and obj == self.txt_text2:
            self.label.setText("txt 2")

        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())

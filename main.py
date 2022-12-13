import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Ui.ui', self)
        self.btn_create_circle.clicked.connect(self.create_circle)
        self.draw = False

    def create_circle(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QBrush(QColor('yellow')))
            painter.setPen(QColor('yellow'))
            width = height = randint(50, 100)
            painter.drawEllipse(randint(width, self.width() - width), randint(height, self.height() - height),
                                width, height)
            painter.end()
            self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

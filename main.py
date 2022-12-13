import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from interface import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_create_circle.clicked.connect(self.create_circle)
        self.draw = False

    def create_circle(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            painter = QPainter()
            painter.begin(self)
            color = randint(0, 255), randint(0, 255), randint(0, 255)
            painter.setBrush(QBrush(QColor(*color)))
            painter.setPen(QColor(*color))
            width = height = randint(50, 100)
            painter.drawEllipse(randint(0, self.width() - width), randint(height, self.height() - height),
                                width, height)
            painter.end()
            self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

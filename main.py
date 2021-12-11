import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.circle = []

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circ(qp)
            qp.end()

    def draw_circ(self, qp):
        x = random.randint(1, 400)
        y = random.randint(1, 400)
        r = random.randint(10, 100)
        self.circle.append([x, y, r])
        for i in self.circle:
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(i[0], i[1], i[2], i[2])

    def paint(self):
        self.do_paint = True
        self.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


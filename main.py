import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import Qt, QPoint
from random import randint


class Suprematizm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        x = randint(200, 800)
        y = randint(200, 800)
        self.setGeometry(300, 300, x, y)
        self.setWindowTitle('Рисование')
        self.flag = False
        self.status = 0
        self.point = [0, 0]
        self.show()
        self.setMouseTracking(True)


    def paints(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
            self.run()
            self.qp.end()

    def mouseMoveEvent(self, event):
        self.point[0] = event.x()
        self.point[1] = event.y()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.status = 1
        elif (event.button() == Qt.RightButton):
            self.status = 2
        self.paints()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
        self.paints()

    def run(self):
        w = randint(50, 70)
        h = randint(50, 70)
        if self.status == 1:
            self.qp.drawEllipse(*self.point, w, w)
        elif self.status == 2:
            self.qp.drawRect(*self.point, w, h)
        elif self.status == 3:
            x, y = self.point
            poly = QPolygon([QPoint(x, y + w), QPoint(x + h, y - w), QPoint(x - h, y - w)])
            self.qp.drawPolygon(poly)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematizm()

    sys.exit(app.exec_())

import sys

from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.painter)

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()

    def painter(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        # Рисуем прямоугольник заданной кистью
        qp.begin(self)
        r = randint(200, 500)
        qp.drawEllipse(100, 100, r, r)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

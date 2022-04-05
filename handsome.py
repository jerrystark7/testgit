from random import randint
from PySide2.QtGui import QIcon
from PySide2.QtCore import QFile,Qt,QSize
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox, QApplication


class handsome:
    def __init__(self):
        hs_file = QFile("handsome.ui")
        hs_file.open(QFile.ReadOnly)
        hs_file.close()
        self.ui = QUiLoader().load(hs_file)
        self.ui.button1.setIcon(QIcon('p.png'))
        self.ui.button1.setIconSize(QSize(30,30))
        self.ui.button2.setIcon(QIcon('wz.png'))
        self.ui.button2.setIconSize(QSize(30,30))
        self.ui.button1.clicked.connect(self.shuai)
        self.ui.button2.clicked.connect(self.bushuai)

    def shuai(self):
        QMessageBox.warning(self.ui, 'yjm', "确实")
        app.closeAllWindows()

    def bushuai(self):
        self.ui.window().move(randint(0, 1000), randint(0, 500))


if __name__ == '__main__':
    app = QApplication()
    app.setWindowIcon(QIcon('p.png'))
    cool = handsome()
    cool.ui.show()
    app.exec_()

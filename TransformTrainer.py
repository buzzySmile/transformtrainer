#!/usr/bin/python
# coding=utf-8
import sys
from PyQt4 import QtCore, QtGui
from TransformTrainer_ui import Ui_Dialog

class MyForm(QtGui.QDialog):
    """
    В конструкторе мы делаем всё, что необходимо для запуска нашего приложения, которое
    создаёт QApplication в __init__ методе, затем добваляет наши виджеты и, наконец,
    запускает exec_loop
    """
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

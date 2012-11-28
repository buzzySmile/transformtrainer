#!/usr/bin/python
# coding=utf-8
import sys
from PyQt4 import QtGui, QtCore
#from PyQt4 import QtGui, QtCore
from TransformTrainer_ui import Ui_Dialog
import Metronome

class MyForm(QtGui.QDialog):
    """
    В конструкторе мы делаем всё, что необходимо для запуска нашего приложения, которое
    создаёт QApplication в __init__ методе, затем добваляет наши виджеты и, наконец,
    запускает exec_loop
    """
    def __init__(self, parent=None):
        super.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.metr = Metronome(self.ui.sbBPM.value())
        self.connect(self.metr, QtCore.SIGNAL("tick(str)"), self.ui.lKey.setText)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

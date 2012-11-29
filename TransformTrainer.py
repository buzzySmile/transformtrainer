#!/usr/bin/python
# coding=utf-8
import sys
from PyQt4 import QtGui, QtCore, uic
#from TransformTrainer_ui import Ui_Dialog
import Metronome


class MyForm(QtGui.QDialog):
    
    def __init__(self, parent=None):
        # Запускаем родительский конструктор
        super(MyForm, self).__init__(parent)
        #self.ui = Ui_Dialog()
        self.ui = uic.loadUi("TransformTrainer.ui", self)        
        #self.ui.setupUi(self)
        bpm = self.ui.sbBPM.value()
        #self.metr = Metronome(bpm)
        #self.connect(self.metr, QtCore.SIGNAL("tick(str)"), self.ui.lKey.setText)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

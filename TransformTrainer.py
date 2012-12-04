#!/usr/bin/python
# coding=utf-8
import sys, random
from PyQt4 import QtGui, QtCore, uic
from Metronome import Metronome

key = ["A", "B", "C", "D", "E", "F", "G"]
transform = ["3/5", "6", "6/4"]


class MyForm(QtGui.QDialog):
    
    def __init__(self, parent=None):
        # Запускаем родительский конструктор
        super(MyForm, self).__init__(parent)
        self.ui = uic.loadUi("TransformTrainer.ui", self)        
        self.metr = Metronome(self.ui.sbBPM.value())
        self.connect(self.metr, QtCore.SIGNAL("tick(QString)"), self.ui.lTick.setText)
        self.connect(self.ui.sbBPM, QtCore.SIGNAL("valueChanged(int)"), self.metr.changeBpm)
        self.connect(self.ui.pbStart, QtCore.SIGNAL("toggled(bool)"), self.mode)
        
    def mode(self, state):
        if state == True:
            self.connect(self.metr, QtCore.SIGNAL("bar()"), self.change_key)
        else:
            self.disconnect(self.metr, QtCore.SIGNAL("bar()"), self.change_key)    
            
    
    def change_key(self):
        self.ui.lKey.setText(random.choice(key))
        self.ui.lTransform.setText(random.choice(transform))
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()    
    sys.exit(app.exec_())

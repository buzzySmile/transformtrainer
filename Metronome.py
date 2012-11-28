#!/usr/bin/python
# coding=utf-8
#import sys
from PyQt4 import QtCore

class Metronome(QtCore.QObject):
    ticks = ["1", "2", "3", "4"]
    tick_index = 0
    def __init__(self, bpm = 75):
        ms_per_beat = 60000/bpm
        self.timer = QtCore.QTimer()
        self.timer.start(ms_per_beat)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.generateTick())
                               
    def generateTick(self):
        self.tick_index += 1
        if(self.tick_index > 3):
            self.tick_index = 0
        self.emit(QtCore.SIGNAL("tick(str)"), self.ticks[self.tick_index])
    
    def changeBpm(self, new_bpm):
        self.timer.setInterval(new_bpm)
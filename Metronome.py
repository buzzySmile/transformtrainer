#!/usr/bin/python
# coding=utf-8
#import sys
from PyQt4.QtCore import QObject, QTimer, SIGNAL


class Metronome(QObject):
    ticks = ["1", "2", "3", "4"]
    tick_index = 0
    
    def __init__(self, bpm = 75):
        QObject.__init__(self)
        ms_per_beat = 60000/bpm
        self.timer = QTimer()
        self.timer.timeout.connect(self.generate_tick)
        self.timer.start(ms_per_beat)
        #self.connect(self.timer, SIGNAL("timeout()"), self, SLOT("generateTick()"))
                               
    def generate_tick(self):
        self.tick_index += 1
        if(self.tick_index > 3):
            self.tick_index = 0
        self.emit(SIGNAL("tick(str)"), self.ticks[self.tick_index])
    
    def change_bpm(self, new_bpm):
        self.timer.setInterval(new_bpm)        
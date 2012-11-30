#!/usr/bin/python
# coding=utf-8
import sys
from PyQt4.QtCore import QObject, QTimer, SIGNAL, QString
from Tkinter import *
from tkSnack import *


class Metronome(QObject):
    ticks = ["1", "2", "3", "4"]
    tick_index = 0
    
    def __init__(self, bpm=75):
        QObject.__init__(self)
        self.root = Tkinter.Tk()
        initializeSnack(self.root)
        self.s = Sound(load='stickhit.wav') 
        #self.s.read('stickhit.wav')         
        ms_per_beat = 60000/bpm
        self.timer = QTimer()   
        self.timer.timeout.connect(self.generate_tick)
        self.timer.start(ms_per_beat)
        #self.connect(self.timer, SIGNAL("timeout()"), self, SLOT("generateTick()"))
                                       
    def generate_tick(self):
        self.s.play()
        self.tick_index += 1
        if(self.tick_index > 3):
            self.tick_index = 0
            self.emit(SIGNAL("bar()"))
        t_str = QString(self.ticks[self.tick_index])    
        self.emit(SIGNAL("tick(QString)"), t_str)
    
    def _setBpm(self, new_bpm):
        ms_per_beat = 60000/new_bpm
        self.timer.setInterval(ms_per_beat)
    
    def changeBpm(self, new_bpm):
        ms_per_beat = 60000/new_bpm
        self.timer.setInterval(ms_per_beat)
        
    bpm = property(fset=_setBpm)
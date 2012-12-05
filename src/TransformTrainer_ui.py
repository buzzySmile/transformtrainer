#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TransformTrainer.ui'
#
# Created: Thu Nov 22 17:39:52 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(340, 221)
        Dialog.setMinimumSize(QtCore.QSize(340, 0))
        Dialog.setMaximumSize(QtCore.QSize(340, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("key.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lTick = QtGui.QLabel(Dialog)
        self.lTick.setMinimumSize(QtCore.QSize(155, 0))
        self.lTick.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lTick.setFont(font)
        self.lTick.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lTick.setLineWidth(1)
        self.lTick.setAlignment(QtCore.Qt.AlignCenter)
        self.lTick.setObjectName(_fromUtf8("lTick"))
        self.horizontalLayout_2.addWidget(self.lTick)
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.sbBPM = QtGui.QSpinBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sbBPM.setFont(font)
        self.sbBPM.setAlignment(QtCore.Qt.AlignCenter)
        self.sbBPM.setMaximum(260)
        self.sbBPM.setProperty("value", 75)
        self.sbBPM.setObjectName(_fromUtf8("sbBPM"))
        self.horizontalLayout_2.addWidget(self.sbBPM)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lKey = QtGui.QLabel(Dialog)
        self.lKey.setMinimumSize(QtCore.QSize(85, 0))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.lKey.setFont(font)
        self.lKey.setFrameShape(QtGui.QFrame.Panel)
        self.lKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lKey.setObjectName(_fromUtf8("lKey"))
        self.horizontalLayout.addWidget(self.lKey)
        self.lTransform = QtGui.QLabel(Dialog)
        self.lTransform.setMinimumSize(QtCore.QSize(85, 0))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.lTransform.setFont(font)
        self.lTransform.setFrameShape(QtGui.QFrame.Panel)
        self.lTransform.setAlignment(QtCore.Qt.AlignCenter)
        self.lTransform.setObjectName(_fromUtf8("lTransform"))
        self.horizontalLayout.addWidget(self.lTransform)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pbStart = QtGui.QPushButton(Dialog)
        self.pbStart.setMinimumSize(QtCore.QSize(0, 25))
        self.pbStart.setCheckable(True)
        self.pbStart.setObjectName(_fromUtf8("pbStart"))
        self.verticalLayout.addWidget(self.pbStart)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Transforms Trainer", None, QtGui.QApplication.UnicodeUTF8))
        self.lTick.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "BPM:", None, QtGui.QApplication.UnicodeUTF8))
        self.lKey.setText(QtGui.QApplication.translate("Dialog", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.lTransform.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" vertical-align:super;\">3</span>/<span style=\" vertical-align:sub;\">5</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStart.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))


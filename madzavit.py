#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QCoreApplication, Qt,QBasicTimer, QPoint
from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap, QIcon, QFont, QPixmap, QPalette
from PyQt5.QtWidgets import (QFileDialog, QScrollArea, QSizePolicy)
from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )



class MainFrame(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(700, 700)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setWindowOpacity(0.4)

        #f = args[0]
        self.bw=True
        f='madzavit.png'
        image = QImage(f)
        self.imageLabel = QLabel()
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.scrollArea = QScrollArea()
        #self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        #self.resize(1600, 600)
        #self.setCentralWidget(self.scrollArea)
        #self.imageLabel.setPixmap(QPixmap.fromImage(image))
        #self.printAct.setEnabled(True)
        #self.scrollArea.setWidgetResizable(True)
        #self.updateActions()

        image = QImage(f)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.imageLabel.setAttribute(Qt.WA_TranslucentBackground)
        #self.imageLabel.setStyleSheet("background-image: madzavit.svg;")
        self.imageLabel.adjustSize()
        #self.imageLabel.resize(1600, 600)

        layout = QtWidgets.QHBoxLayout(self)
        #layout.addWidget(QtWidgets.QPushButton("TEST"))
        layout.addWidget(self.imageLabel)
        self.setAttribute(Qt.WA_TranslucentBackground)


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        if app.mouseButtons() & QtCore.Qt.LeftButton:
            if self.bw:
                f='madzavit-yellow.png'
            else:
                f='madzavit.png'
            self.bw = not self.bw
            image = QImage(f)
            self.imageLabel.setPixmap(QPixmap.fromImage(image))

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Escape]:
            self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Frame = MainFrame(None)
    Frame.show()
    app.exec_()

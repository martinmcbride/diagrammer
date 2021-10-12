# Diagrammer
# MIT licence
# Copyright 2021 Martin McBride

from PySide2 import QtGui
from PySide2.QtWidgets import QWidget


class Canvas(QWidget):

    def __init__(self, parent, document):
        super(Canvas, self).__init__(parent=parent)
        self.document = document

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        print("here")
        painter.begin(self)
        self.document.paint(painter)
        painter.end()

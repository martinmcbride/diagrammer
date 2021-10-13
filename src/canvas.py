# Diagrammer
# MIT licence
# Copyright 2021 Martin McBride

from PySide2 import QtGui
from PySide2.QtWidgets import QWidget

from layout import Layout


class Canvas(QWidget):

    def __init__(self, parent, document):
        super(Canvas, self).__init__(parent=parent)
        self.document = document
        self.layout = Layout(self)
        self.mouseItem = None

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.document.paint(painter)
        painter.end()

    def mousePressEvent(self, event):
        self.mouseItem = self.document.getSelectedItem(event.x(), event.y())
        if self.mouseItem:
            self.mouseItem.getMouseHandler().handleMousePressEvent(event, self.layout)

    def mouseMoveEvent(self, event):
        if self.mouseItem:
            self.mouseItem.getMouseHandler().handleMouseMoveEvent(event, self.layout)
            self.update()

    def mouseReleaseEvent(self, event):
        if self.mouseItem:
            self.mouseItem.getMouseHandler().handleMouseReleaseEvent(event, self.layout)
        self.mouseItem = None


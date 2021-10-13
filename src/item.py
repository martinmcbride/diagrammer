# Diagrammer
# MIT licence
# Copyright 2021 Martin McBride

from PySide2.QtGui import QColor

from mouse import MouseHandler


class Item:

    def __init__(self, position):
        self.position = position
        self.size = (100, 100)
        self.mouse_handler = MouseHandler(self)

    def paint(self, painter):
        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(*self.position, *self.size)

    def hasMouseOver(self, x, y):
        return (self.position[0] <= x <= self.position[0] + self.size[0] and
                self.position[1] <= y <= self.position[1] + self.size[1])

    def getMouseHandler(self):
        return self.mouse_handler

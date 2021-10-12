# Diagrammer
# MIT licence
# Copyright 2021 Martin McBride

from PySide2.QtGui import QColor


class Item:

    def __init__(self, position):
        self.position = position
        self.size = (100, 100)

    def paint(self, painter):
        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(*self.position, *self.size)

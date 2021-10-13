# Diagrammer
# MIT licence
# Copyright 2021 Martin McBride

from item import Item


class Document:

    def __init__(self):
        self.items = [Item((10, 10)), Item((200, 300))]

    def paint(self, painter):
        for item in self.items:
            item.paint(painter)

    def getSelectedItem(self, x, y):
        for item in self.items:
            if item.hasMouseOver(x, y):
                return item
        return None

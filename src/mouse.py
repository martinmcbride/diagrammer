# Diagrammer
# MIT licence
# Copyright 2021 Martin McBride

class MouseHandler:

    def __init__(self, item):
        self.item = item
        self.isDragging = False
        self.initialMousePosition = (0, 0)
        self.initialObjectPosition = (0, 0)

    def handleMousePressEvent(self, event, layout):
        self.isDragging = True
        self.initialMousePosition = (event.x(), event.y())
        self.initialObjectPosition = self.item.position

    def handleMouseMoveEvent(self, event, layout):
        if self.isDragging:
            self.item.position = layout.getPosition((event.x(), event.y()))

    def handleMouseReleaseEvent(self, event, layout):
        self.isDragging = False


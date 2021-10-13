# Diagrammer
# MIT licence
# Copyright 2021 Martin McBride

class Layout:

    def __init__(self, document):
        self.document = document

    def getPosition(self, position):
        return (position[0]//10)*10, (position[1]//10)*10

# Diagrammer
# MIT licence
# Copyright 2021 Martin McBride
import random

from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout
import sys
from PySide2.QtGui import QIcon

from canvas import Canvas
from document import Document


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diagrammer")
        self.setGeometry(300, 300, 500, 400)

        self.create_menu()

        self.document = Document()
        self.canvas = Canvas(self, self.document)

        self.setCentralWidget(self.canvas)
        self.show()
        self.canvas.update()

    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")

        openAction = QAction(QIcon('open.png'), "Open", self)
        openAction.setShortcut("Ctrl+O")

        saveAction = QAction(QIcon('save.png'), "Save", self)
        saveAction.setShortcut("Ctrl+S")

        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut("Ctrl+X")

        exitAction.triggered.connect(self.exit_app)

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

    def exit_app(self):
        self.close()


myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)

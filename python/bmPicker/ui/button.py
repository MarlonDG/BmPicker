"""
Module to manage the selection buttons
"""

import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore

class Button(QtWidgets.QPushButton):
    def __init__(self):
        super(Button, self).__init__()
        self._assignation = str

    @property
    def assignation(self):
        pass

    @assignation.setter
    def assignation(self):
        pass

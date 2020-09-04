import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore

import button
reload(button)

class BmPickerMainWindow(QtWidgets.QMainWindow):
    def __init__(self, inWindowTitleStr):
        super(BmPickerMainWindow, self).__init__()
        toolName = inWindowTitleStr
        self.setWindowTitle(toolName)

        self.setCentralWidget(self.workSpace())

    def workSpace(self):
        #Temporary method
        # Note: the workspacewidget should be the whole picker tab.
        workspaceWidget = QtWidgets.QWidget()
        workspaceLayout = QtWidgets.QVBoxLayout()
        workspaceWidget.setLayout(workspaceLayout)

        workspaceLayout.addWidget(button.Button())

        return workspaceWidget

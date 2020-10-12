from PySide2 import QtWidgets

import workspace
reload(workspace)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, inWindowTitleStr):
        """
        BmPicker Main Window Class.

        Args:
            inWindowTitleStr (str): Given name to set the window name.

        """
        super(MainWindow, self).__init__()
        self._mainWorkspace = None

        self.setWindowTitle(inWindowTitleStr)
        self.setGeometry(500, 100, 700, 900)

        self.mainWorkspace = workspace.WorkSpace(parent=self)

    @property
    def mainWorkspace(self):
        """
        Gets the main workspace.

        Returns:
            QtWidgets.QWidget: Widget used as main workspace.
        """
        return self._mainWorkspace

    @mainWorkspace.setter
    def mainWorkspace(self, inWorkspace):
        '''
        Sets the main workspace.

        Args:
            inWorkspace(QtWidgets.QWidget): Given widget to set as main workspace.
        '''
        self.setCentralWidget(inWorkspace)

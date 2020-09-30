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

        self.setWindowTitle(inWindowTitleStr)
        self.setGeometry(500, 100, 700, 900)

        # Initialize the main workspace.
        self.mainWorkspace()

    def mainWorkspace(self):
        """
        Sets the main workspace for the tool.

        Returns:
              None.
        """
        # Instance of the workspace.
        workSpace = workspace.WorkSpace()

        # Sets the toolBar.
        self.addToolBar(workSpace.toolBarWidget)
        self.setCentralWidget(workSpace)

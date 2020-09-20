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
        self.setGeometry(500, 100, 1000, 900)

        # Instance of the workspace.
        workSpace = workspace.WorkSpace()

        # Sets the toolBar.
        self.addToolBar(workSpace.toolBarWidget())

        self.setCentralWidget(workSpace)

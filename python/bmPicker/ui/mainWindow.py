from PySide2 import QtWidgets

from ..core import tab


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, inWindowTitleStr):
        """
        BmPicker Main Window Class.

        Args:
            inWindowTitleStr (str): Given name to set the window name.

        Returns:
            None.
        """
        super(MainWindow, self).__init__()

        toolName = inWindowTitleStr

        self.setWindowTitle(toolName)
        self.setGeometry(500, 100, 1000, 900)

        self.setMenuBar(self.menuBar())
        self.toolBar()
        self.workSpace()

    def addTab(self):
        self.workspaceLayout.addWidget(tab.PickTab())



    def menuBar(self):
        """
        Sets the main menu bar of the window.

        Returns:
            QtWidgets.QMenuBar: Main menu bar of the tool.
        """
        # File Actions.
        newFileAction = QtWidgets.QAction('New File', self)
        openFileAction = QtWidgets.QAction('Open File', self)

        saveFileAction = QtWidgets.QAction('Save', self)
        saveAsFileAction = QtWidgets.QAction('Save As', self)

        # Init the main menu bar to the window.
        mainMenuBar = QtWidgets.QMenuBar()

        fileMenu = mainMenuBar.addMenu('File')
        fileMenu.addAction(newFileAction)
        fileMenu.addAction(openFileAction)
        fileMenu.addSeparator()

        fileMenu.addAction(saveFileAction)
        fileMenu.addAction(saveAsFileAction)

        helpMenu = mainMenuBar.addMenu('Help')
        helpMenu.addAction('BmPicker Version 001')

        return mainMenuBar

    def toolBar(self):
        """
        Creates and toolbar for the window.

        Returns:
            None.
        """
        mainToolBar = self.addToolBar('BmPickerToolBar')
        mainToolBar.setMovable(False)

        addTabAction = QtWidgets.QAction('Add Tab', self)
        addTabAction.triggered.connect(self.addTab)

        removeTabAction = QtWidgets.QAction('Remove Tab', self)

        mainToolBar.addAction(addTabAction)
        mainToolBar.addAction(removeTabAction)

    def workSpace(self):
        """
        Initialize the workspace for the tool,
        where all the widgets will be called.

        Returns:
            None.
        """
        # Init the main widget and main layout.
        workspaceWidget = QtWidgets.QWidget()
        self.workspaceLayout = QtWidgets.QVBoxLayout()
        workspaceWidget.setLayout(self.workspaceLayout)

        #TODO: adding the main widget to the window should be a
        # single argument
        self.setCentralWidget(workspaceWidget)


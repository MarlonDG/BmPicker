from PySide2 import QtWidgets
from PySide2 import QtCore

class ToolBar(QtWidgets.QToolBar):
    addTabSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        """
        Generic Class to instance and manage a tool bar.

        Args:
            parent (QtWidgets.QWidget): Parent widget

        Signals:
            addTabSignal (QtCore.Signal): Signal to add a new tab to the mainlayout.
        """
        super(ToolBar, self).__init__()
        self.setParent = parent
        self.setMovable(False)

        # Init the main QActions.
        self.manageFileActions()

    def manageFileActions(self):
        """
        Sets the main QActions to be added to the toolbar.

        Returns:
            None.
        """
        addTabAction = QtWidgets.QAction('New File', self)
        addTabAction.triggered.connect(self.addNewTab)

        removeTabAction = QtWidgets.QAction('Remove File', self)

        self.addAction(addTabAction)
        self.addAction(removeTabAction)

    def addNewTab(self):
        """
        Slot method to add a new tab to the mainLayout.

        Returns:
            None.
        """
        tabNameInput, nameValue = QtWidgets.QInputDialog.getText(self,
                                                                 'TabName',
                                                                 'Enter the name of the tab:')
        self.addTabSignal.emit(tabNameInput)

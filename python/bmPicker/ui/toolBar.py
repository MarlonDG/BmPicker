from PySide2 import QtWidgets
from PySide2 import QtCore

from ..core import itemManager
reload(itemManager)

from ..utilities import constants

class ToolBar(QtWidgets.QToolBar):
    newTabSignal = QtCore.Signal(object)

    def __init__(self, parent=None):
        """
        Class to instance and manage a tool bar.

        Args:
            parent (QtWidgets.QWidget): Parent widget.

        Signals:
            addTabSignal (QtCore.Signal): Signal to add a new tab to the mainLayout.
        """
        super(ToolBar, self).__init__()
        self.setParent = parent
        self.setMovable(False)

        self.itemManager = itemManager.ItemManager()

        # Initialize the main QActions.
        self.mainActions()

    def mainActions(self):
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
        self.newTabSignal.emit(self.itemManager.newItem(constants.TAB_ITEM_TYPE))


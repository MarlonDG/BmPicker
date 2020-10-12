from PySide2 import QtWidgets
from PySide2 import QtCore

class Tab(QtWidgets.QTabWidget):
    def __init__(self):
        """
        Generic class to instance a Tab Widget.

        Args:
            inTabName (QtWidgets.QTabWidget): Instance of the tab or name of it.
        """
        super(Tab, self).__init__()
        # Set the default name of the tab as 'NewPicker'
        self._name = 'NewPicker'

        # Adds a new tab, with a GraphicView instance attached, by default.
        self.addTab(GraphicView(), self._name)

        # Initialize the context menu.
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)

        self.setStyleSheet(""" 
                           QTabWidget::pane {
                                             margin: 0px, 0px, 0px, 0px;
                                             padding: -1px
                                             }
                           """)

    def contextMenu(self, position):
        """
        Creates the context menu with its actions.

        Args:
            position(QtCore.QPoint): Given point where the QMenu will be displayed.

        Returns:
            None.
        """
        #TODO: this method could be in the itemScene pherhaps.
        changeNameAction = QtWidgets.QAction('RenameTab', self)
        changeNameAction.triggered.connect(self.rename)

        contextMenu = QtWidgets.QMenu(self)
        contextMenu.addAction(changeNameAction)

        point = self.mapToGlobal(position)
        contextMenu.move(point)
        contextMenu.show()

    def rename(self):
        """
        Slot method to change the name of the tab.

        Returns:
            None.
        """
        inputName, inputValue = QtWidgets.QInputDialog.getText(self,
                                                               'RenameTab',
                                                               'New Name:')
        if inputName:
            self.name = inputName

    @property
    def name(self):
        """
        Gets the name of this tab.

        Returns:
            str: Current tab's name.
        """
        return self._name

    @name.setter
    def name(self, inTabNameStr):
        """
        Sets the name for this tab.

        Args:
            inTabNameStr(str): Given name to set for this tab.
        Returns:
            None.
        """
        if inTabNameStr:
            self._name = inTabNameStr
            self.setTabText(self.currentIndex(), self._name)

class GraphicView(QtWidgets.QGraphicsView):
    def __init__(self):
        super(GraphicView, self).__init__()


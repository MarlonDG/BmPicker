from PySide2 import QtWidgets
from PySide2 import QtCore

class ItemScene(QtWidgets.QGraphicsView):
    def __init__(self):
        super(ItemScene, self).__init__()
        graphicsScene = QtWidgets.QGraphicsScene(self)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)

    def contextMenu(self, position):
        """
        Creates the context menu with its actions.

        Args:
            position(QtCore.QPoint): Given point where the QMenu will be displayed.

        Returns:
            None.
        """

        addItemButtonAction = QtWidgets.QAction('Add Item Button', self)

        # Init menu for the context menu.
        contextMenu = QtWidgets.QMenu(self)
        contextMenu.addAction(addItemButtonAction)

        point = self.mapToGlobal(position)
        contextMenu.move(point)
        contextMenu.show()

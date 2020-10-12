from PySide2 import QtWidgets

import toolBar
reload(toolBar)

class WorkSpace(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """
        Generic class to manage the workspace.
        Adds the basic widgets for the tool(Layout and ToolBar).
        """
        super(WorkSpace, self).__init__()
        self._parentWidget = parent

        # Instance the main layout.
        self._mainLayout = QtWidgets.QVBoxLayout()
        self._mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._mainLayout)

        # Add the tool Bar.
        self._parentWidget.addToolBar(toolBar.ToolBar(parent=self))

    @property
    def mainLayout(self):
        """
        Gets the mainLayout.

        Returns:
            QtWidgets.QLayout: Layout used as main Layout.
        """
        return self._mainLayout

    @mainLayout.setter
    def mainLayout(self, inLayout):
        """
        Gets the mainLayout.

        Args:
            inLayout(QtWidgets.QLayout): Given widget used as main Layout.
        """

        self._mainLayout = inLayout

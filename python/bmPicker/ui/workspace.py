from PySide2 import QtWidgets

import toolBar
reload(toolBar)

class WorkSpace(QtWidgets.QWidget):
    def __init__(self):
        """
        Generic class to manage the workspace.
        Adds the basic widgets for the tool(Layout and ToolBar).
        """
        super(WorkSpace, self).__init__()
        # Instance the main layout.
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)

        self.toolBarWidget = toolBar.ToolBar(parent=self)
        self.toolBarWidget.newTabSignal.connect(self.newTab)

    def newTab(self, inTabWidget):
        """
        Slot method to add a new picker Tab.

        Args:
            inTabWidget(QtWidgets.QTabWidget): Given widget to be added to the main Layout.

        Returns:
            None.
        """
        if inTabWidget:
            self.mainLayout.addWidget(inTabWidget)

from PySide2 import QtWidgets

import toolBar
reload(toolBar)

from ..core import pickerManager
reload(pickerManager)

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

    def toolBarWidget(self):
        """
        Creates the main toolBar.

        Returns:
            QtWidgets.QToolBar: Picker Main tool bar.
        """
        toolBarWidget = toolBar.ToolBar(parent=self)
        toolBarWidget.addTabSignal.connect(self.addNewTab)

        return toolBarWidget

    def addNewTab(self, inTabLabelStr):
        """
        Slot Method to add a new tab to the main to the main layout.

        Args:
            inTabLabelStr(basestring): Given name to be set in the tab's label.

        Returns:
            QtWidgets.QTabWidget: Widget type of this class.
        """
        if inTabLabelStr:
            self.mainLayout.addWidget(pickerManager.PickerManager().addTab(inTabLabelStr).widget())

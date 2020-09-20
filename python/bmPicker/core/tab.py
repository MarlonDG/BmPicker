from PySide2 import QtWidgets

class Tab(QtWidgets.QTabWidget):
    def __init__(self, inTabName=None):
        """
        Generic class to instance a Tab Widget.

        Args:
            inTabName (QtWidgets.QTabWidget | basestring): Instance of the tab or name of it.

        """
        super(Tab, self).__init__()
        if isinstance(inTabName, QtWidgets.QTabWidget):
            self._widget = inTabName

        elif isinstance(inTabName, str):
            self._tabName = inTabName

        else:
            raise NotImplementedError

    @classmethod
    def create(cls, inTabNameStr):
        """
        Creates an instance of a QTabWidget.

        Args:
            inTabNameStr(basestring): Given name to be set in the tab's label.

        Returns:
            tab.Tab: Instance of the tab class.

        """
        tabWidget = QtWidgets.QTabWidget()
        tabWidget.addTab(QtWidgets.QWidget(), inTabNameStr)

        return cls(tabWidget)

    def name(self):
        """
        Gets the tab's name.

        Returns:
            str: Tab's name.
        """
        return self._tabName

    def widget(self):
        """
        Gets the widget type.

        Returns:
              QtWidgets.QTabWidget: Widget type of this class.
        """
        return self._widget

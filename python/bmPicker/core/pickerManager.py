from ..core import tab
reload(tab)

class PickerManager(object):
    """
    Generic Class used to manage the elements of the picker.

    Returns:
        None.
    """

    @staticmethod
    def addTab(inTabNameStr):
        """
        Adds a new tab with a given label/text.

        Args:
            inTabNameStr (str): Given name to be set in the tba's label.

        Returns:
            tab.Tab: Instance of the tab created

        """
        return tab.Tab.create(inTabNameStr)


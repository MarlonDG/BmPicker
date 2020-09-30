from ..utilities import constants

from ..ui import tab
reload(tab)

class ItemManager(object):
    """
    Class used to manage items of the picker.
    An Item could be a tab or a button.

    Returns:
        None.
    """
    @staticmethod
    def newItem(inItemType):
        """
        Creates a new tab with a given label/text.

        Args:
            inItemType (str): Given name to be set in the tba's label.

        Returns:
            QtWidget.QTabWidget: Created Tab as QWidget.

        """
        if not inItemType:
            return

        elif inItemType == constants.TAB_ITEM_TYPE:
            return tab.Tab()

        elif inItemType == constants.BUTTON_ITEM_TYPE:
            pass


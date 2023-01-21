"""
An unordered bag implementation of items. It supports the following operations.

size(self)
    Return number of items stored in this bag.

is_empty(self)
    Check whether this bag is empty or not.

contains(self, item)
    Check whether this bag contains the given item or not.

add(self, item)
    Inserts the item into the bag. It overwrites the old 
    value with the new value if the item is already in the bag. If 
    the value is None, this effectively deletes the item from the table.

"""


class Bag():
    """ bag implementation using linked list.

    The Bag class represents an unordered bag of  generic items.
    """

    #*************************** Nested Node Class ***************************#
    class Node():
        """ Creates the inner Node class. """
        def __init__(self, item, nxt=None):
            self.item = item  # the item
            self.next = nxt  # the next linked sublist

    #************************ End of Nested Node Class ***********************#

    def __init__(self):
        self.first = None  # head of the linked bag items
        self.n = 0  # number of items in the bag

    def size(self):
        """ Return number of items stored in this bag."""
        return self.n

    def is_empty(self):
        """ Check whether this bag is empty or not."""
        return self.n == 0 and self.first is None

    def add(self, item):
        """ Inserts the item into the bag.
        
        Args:
            item   -> the item given as string
        """
        if item is None:
            raise ValueError("Can't insert 'None'")
        self.n += 1
        if self.first is None:
            self.first = self.Node(item)
            return
        self.first = self.Node(item, self.first)

    #************************ Python Special Methods: ************************#

    def __len__(self):
        return self.size()

    def __iter__(self):
        x = self.first
        while x is not None:
            yield x.item
            x = x.next

    #********************* End of Python Special Methods *********************#

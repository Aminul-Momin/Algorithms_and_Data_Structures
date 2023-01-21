from typing import Optional, TypeVar, Generic
from typing_extensions import Protocol
from abc import abstractmethod
##=============================================================================

T = TypeVar("T", bound="Comparable")
V = TypeVar("V")


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: T, other: T) -> bool:
        pass


class Node(Generic[T]):
    """The node to be used with tree like data structures.
    """
    def __init__(self, key, left=None, right=None):
        """Initialize the Node.

        Args:
            key (T): the key of this node.
            left (Optional[Node]): the left child of this node.
            right (Optional[Node]): the right child of this node.
        """
        self._key: T = key  # the key
        self._left: Optional[Node] = left  # left subtree
        self._right: Optional[Node] = right  # right subtree

    def __iter__(self):
        yield from self.left if self.left is not None else ()
        yield self.key
        yield from self.right if self.right is not None else ()


# ************************* BST Symbol Table Node *************************#
class AVLNode(Generic[T, V]):
    """A Node in a `BinarySearchTreeST`.
    """
    def __init__(self, key, value, size, height, left=None, right=None):
        """Initialize the DLLNode.

        Args:
            key (T): the key of this node.
            value (V): the payload of this node.
            size (int): the size of this node.
            height (int): the height of this node.
            left (Optional[Node]): the left child of this node.
            right (Optional[Node]): the right child of this node.
        """
        self._key = key  # the key of this node
        self._value = value  # the value associated with the key
        self._left = left  # left subtree
        self._right = right  # right subtree
        self._size = size  # number of subtree rooted at this tree
        self._height = height  # height of the subtree

    def __iter__(self):
        yield from self._left if self._left is not None else ()
        yield self._key
        yield from self._right if self._right is not None else ()


################################## BST Node ##################################


class BSTNode(Generic[T]):
    """A node in the vanilla `BST` tree."""
    def __init__(self, parent, k):
        """Creates a node.
        Args:
            parent: The node's parent.
            k: key of the node."""

        self._key = k
        self._parent = parent
        self._left = None
        self._right = None

    def _str(self):
        """Internal method for ASCII art."""
        label = str(self._key)
        if self._left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self._left._str()

        if self._right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self._right._str()

        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (
                middle - len(label)
        ) % 2 == 1 and self._parent is not None and self is self._parent._left and len(
                label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '

        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
                 [left_line + ' ' * (width - left_width - right_width) + right_line for left_line, right_line in zip(left_lines, right_lines)]

        return lines, pos, width

    def __str__(self):
        return '\n'.join(self._str()[0])

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this node.
        Args:
            k: The key of the node we want to find."""
        if k == self._key:
            return self
        elif k < self._key:
            if self._left is None:
                return None
            else:
                return self._left.find(k)
        else:
            if self._right is None:
                return None
            else:
                return self._right.find(k)

    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted at this
        node.

        Returns:
            The node with the minimum key.
        """
        current = self
        while current._left is not None:
            current = current._left
        return current

    def next_larger(self):
        """Returns the node with the next larger key (the successor) in the BST.
        """
        if self._right is not None:
            return self._right.find_min()
        current = self
        while current._parent is not None and current is current._parent._right:
            current = current._parent
        return current._parent

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.

        Args:
            node: The node to be inserted.
        """
        if node is None:
            return  # --> return None
        if node._key < self._key:
            if self._left is None:
                node._parent = self
                self._left = node
            else:
                self._left.insert(node)
        else:
            if self._right is None:
                node._parent = self
                self._right = node
            else:
                self._right.insert(node)

    def delete(self):
        """Deletes and returns this node from the BST."""
        if self._left is None or self._right is None:
            if self is self._parent._left:
                self._parent._left = self._left or self._right
                if self._parent._left is not None:
                    self._parent._left._parent = self._parent
            else:
                self._parent._right = self._left or self._right
                if self._parent._right is not None:
                    self._parent._right._parent = self._parent
            return self
        else:
            s = self.next_larger()
            self._key, s._key = s._key, self._key
            return s.delete()

    def check_ri(self):
        """Checks the BST representation invariant around this node.

        Raises an exception if the RI is violated.
        """
        if self._left is not None:
            if self._left._key > self._key:
                raise RuntimeError("BST RI violated by a left node key")
            if self._left._parent is not self:
                raise RuntimeError("BST RI violated by a left node parent "
                                   "pointer")
            self._left.check_ri()
        if self._right is not None:
            if self._right._key < self._key:
                raise RuntimeError("BST RI violated by a right node key")
            if self._right._parent is not self:
                raise RuntimeError("BST RI violated by a right node parent "
                                   "pointer")
            self._right.check_ri()


################################ Min BST Node ################################


class MinBSTNode(BSTNode):
    """A BSTNode which is augmented to keep track of the node with the
    minimum key in the subtree rooted at this node."""
    def __init__(self, parent, key):
        """Creates a node.
        Args:
            parent: The node's parent.
            k     : key of the node."""

        super(MinBSTNode, self).__init__(parent, key)
        self.min = self

    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted at this
        node.

        Returns:
            The node with the minimum key.
        """
        return self.min

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.

        Args:
            node: The node to be inserted.
        """
        if node is None:
            return
        if node._key < self._key:
            # Updates the min of this node if the inserted node has a smaller
            # key.
            if node._key < self.min._key:
                self.min = node
            if self._left is None:
                node._parent = self
                self._left = node
            else:
                self._left.insert(node)
        else:
            if self._right is None:
                node._parent = self
                self._right = node
            else:
                self._right.insert(node)

    def delete(self):
        """Deletes this node itself.

        Returns:
            This node.
        """
        if self._left is None or self._right is None:
            if self is self._parent._left:
                self._parent._left = self._left or self._right
                if self._parent._left is not None:
                    self._parent._left._parent = self._parent
                    self._parent.min = self._parent._left.min
                else:
                    self._parent.min = self._parent
                # Propagates the changes upwards.
                c = self._parent
                while c._parent is not None and c is c._parent._left:
                    c._parent.min = c.min
                    c = c._parent
            else:
                self._parent._right = self._left or self._right
                if self._parent._right is not None:
                    self._parent._right._parent = self._parent
            return self
        else:
            s = self.next_larger()
            self._key, s._key = s._key, self._key
            return s.delete()

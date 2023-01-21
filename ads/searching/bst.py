## taken from: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/

from random import *
from collections import deque

################################ Node: BSTNode ################################


class BSTNode(object):
    """A node in the vanilla BST tree."""
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


################################# Node: MinBSTNode ############################


class MinBSTNode(BSTNode):
    """A BSTNode which is augmented to keep track of the node with the
    minimum key in the subtree rooted at this node."""
    def __init__(self, parent, key):
        """Creates a node.
        Args:
            parent: The node's parent.
            k: key of the node."""

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


############################## End of MinBSTNode ##############################


###############################################################################
################################ Tree: BST ####################################
###############################################################################
class BST(object):
    """Binary Search Tree which can contain repetable elements.
    """
    def __init__(self, klass: BSTNode = BSTNode):
        """Creates an empty BST.
        
        Args:
            klass: The class of the node in the BST. Default to BSTNode.
        """

        self._root = None
        self._klass = klass

    def __str__(self):
        if self._root is None:
            return '<empty tree>'
        return str(self._root)

    ##*************************************************************************

    def __getitem__(self, key):
        return self.find(key)

    def __contains__(self, key):
        return self.find(key) != None

    def __delitem__(self, key):
        self.delete(key)

    """
    def __iter__(self):
        ''' Return: an iterator object (AVLTree)  '''
        return self


    def __next__(self):

        q = deque()

        if self._root is not None:
            que = deque()
            que.append(self._root)
            while len(que) > 0:
                x = que.popleft()
                q.append(x)

                if x._left is not None:
                    que.append(x._left)
                if x._right is not None:
                    que.append(x._right)

        if len(q) == 0: raise StopIteration
        else: return q.popleft()._key
    """

    def keys():
        ''' Return: an iterable such as queue, deque, list '''

        pass

    ##*************************************************************************

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this
        node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key k or None if the tree is empty.
        """
        return self._root and self._root.find(k)

    def find_min(self):
        """Returns the minimum node of this BST."""

        return self._root and self._root.find_min()

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.

        Args:
            k: The key of the node to be inserted.

        Returns:
            The node inserted.
        """
        node = self._klass(None, k)
        if self._root is None:
            # The root's parent is None.
            self._root = node
        else:
            self._root.insert(node)
        return node

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.

        Args:
            k: The key of the node that we want to delete.

        Returns:
            The deleted node with key k.
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self._root:
            pseudoroot = self._klass(None, 0)
            pseudoroot._left = self._root
            self._root._parent = pseudoroot
            deleted = self._root.delete()
            self._root = pseudoroot._left
            if self._root is not None:
                self._root._parent = None
            return deleted
        else:
            return node.delete()

    def next_larger(self, k):
        """Returns the node that contains the next larger (the successor) key in
        the BST in relation to the node with key k.

        Args:
            k: The key of the node of which the successor is to be found.

        Returns:
            The successor node.
        """
        node = self.find(k)
        return node and node.next_larger()

    def check_ri(self):
        """Checks the BST representation invariant.

        Raises:
            An exception if the RI is violated.
        """
        if self._root is not None:
            if self._root._parent is not None:
                raise RuntimeError("BST RI violated by the root node's parent "
                                   "pointer.")
            self._root.check_ri()


############################### End of BST ##################################


###############################################################################
############################# Tree: MinBST ####################################
###############################################################################
class MinBST(BST):
    """An augmented BST that keeps track of the node with the minimum key."""
    def __init__(self):
        # ---> BST.__init__(klass = MinBSTNode)
        super(MinBST, self).__init__(MinBSTNode)


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node._left), height(node._right)) + 1


############################## End of MinBST #################################

###############################################################################
############################# Tree: AVL Tree ##################################
###############################################################################


class AVL(BST):
    """
        AVL binary search tree implementation.
        Supports insert, delete, find, find_min, next_larger each in O(lg n) time.
    """
    def left_rotate(self, x):
        y = x._right
        y._parent = x._parent
        if y._parent is None: self._root = y
        else:
            if y._parent._left is x: y._parent._left = y
            elif y._parent._right is x: y._parent._right = y
        x._right = y._left
        if x._right is not None: x._right._parent = x
        y._left = x
        x._parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x._left
        y._parent = x._parent
        if y._parent is None: self._root = y
        else:
            if y._parent._left is x: y._parent._left = y
            elif y._parent._right is x: y._parent._right = y

        x._left = y._right
        if x._left is not None: x._left._parent = x
        y._right = x
        x._parent = y
        update_height(x)
        update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node._left) >= 2 + height(node._right):
                if height(node._left._left) >= height(node._left._right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node._left)
                    self.right_rotate(node)
            elif height(node._right) >= 2 + height(node._left):
                if height(node._right._right) >= height(node._right._left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node._right)
                    self.left_rotate(node)
            node = node._parent

    ## find(k), find_min(), and next_larger(k) inherited from bst.BST

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        This AVL version guarantees the balance property: h = O(lg n).

        Args:
            k: The key of the node to be inserted.
        """
        node = super(AVL, self).insert(k)
        self.rebalance(node)

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        This AVL version guarantees the balance property: h = O(lg n).

        Args:
            k: The key of the node that we want to delete.

        Returns:
            The deleted node with key k.
        """
        node = super(AVL, self).delete(k)
        ## node._parent is actually the old parent of the node,
        ## which is the first potentially out-of-balance node.
        self.rebalance(node._parent)


############################## End of AVLTree #################################


def test_with_python3(args=None, BSTtype=BST):
    import random
    import sys

    if not args: args = sys.argv[1:]
    if not args:
        print(
            'usage: {0} <number-of-random-items | item item item ...>'.format(
                sys.argv[0]))
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in range(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print(tree)
    for item in items:
        tree.insert(item)
        print()
        print(tree)


def my_test():

    bTree = BST()
    minTree = MinBST()
    avlTree = AVL()

    for item in range(51):
        element = randint(0, 51)

        bTree.insert(element)
        minTree.insert(element)
        avlTree.insert(element)

    print('This is a Binary Search Tree:')
    print(bTree)
    print('This is a Min BST: ')
    print(minTree)
    print('This is a AVL Tree: ')
    print(avlTree)


###############################################################################
################################# Client: #####################################
###############################################################################

if __name__ == '__main__':

    # my_test()
    test_with_python3()

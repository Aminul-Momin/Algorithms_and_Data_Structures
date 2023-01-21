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


# ************************ Singly Linked List Node ************************#
class SLLNode(Generic[T]):
    """The node to be used with singly linked list data structures.
    """
    def __init__(self, key, nxt=None):
        """Initialize the SLLNode.

        Args:
            key (T): the key of this node.
            value(V): the payload of this node.
            nxt (Optional[Node]): the next node of this node.
        """
        self._key: T = key  # the key
        self._next: Optional[SLLNode] = nxt  # the next linked sublist

    def __str__(self):
        return 'SLLNode(' + str(self._key) + ')'

    def __iter__(self):
        x = self
        while x is not None:
            yield x._key
            x = x._next


# ************************ Doubly Linked List Node ************************#
class DLLNode(SLLNode):
    """The node to be used with Doubly linked list data structures.
    """
    def __init__(self, key, nxt=None, prev=None):
        """Initialize the DLLNode.

        Args:
            key (T): the key of this node.
            value(V): the payload of this node.
            nxt (Optional[Node]): the next node of this node.
            prev (Optional[Node]): the previous node of this node.
        """
        super(DLLNode, self).__init__(key, nxt)
        self._prev: Optional[SLLNode] = prev  # the next linked sublist

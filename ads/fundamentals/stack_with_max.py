from collections import namedtuple
from typing import List


class Stack:

    Node = namedtuple('Node', ('element', 'max'))

    def __init__(self) -> None:
        self._stk: List[Stack.Node] = []

    def is_empty(self) -> bool:

        return len(self._stk) == 0

    def max(self) -> int:

        return self._stk[-1].max

    def pop(self) -> int:

        return self._stk.pop().element

    def push(self, x: int) -> None:
        node = self.Node(x, x if self.is_empty() else max(x, self.max()))
        self._stk.append(node)

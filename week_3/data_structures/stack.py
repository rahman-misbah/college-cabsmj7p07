from typing import Any, Optional

class Stack:
    """Simple LIFO Stack"""
    def __init__(self):
        self._stack : list[Any] = list()

    def __len__(self) -> int:
        return len(self._stack)

    def push(self, item:Any) -> None:
        self._stack.append(item)

    def pop(self, non_blocking:bool = False) -> Optional[Any]:
        if not self.is_empty():
            return self._stack.pop()

        if non_blocking:
            return None

        raise IndexError("pop from empty stack")

    def peek(self, non_blocking:bool = False) -> Optional[Any]:
        if not self.is_empty():
            return self._stack[-1]

        if non_blocking:
            return None

        raise IndexError("peek from empty stack")

    def is_empty(self) -> bool:
        return not self._stack
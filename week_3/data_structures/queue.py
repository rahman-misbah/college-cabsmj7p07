from collections import deque
from typing import Any, Optional

class Queue:
    def __init__(self):
        self._queue = deque()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, item:Any) -> None:
        self._queue.append(item)

    def dequeue(self, silent:bool = False) -> Optional[Any]:
        if not self.is_empty():
            return self._queue.popleft()

        if silent:
            return None

        raise IndexError("dequeue from empty queue")
    
    def peek(self, silent:bool = False) -> Optional[Any]:
        if not self.is_empty():
            return self._queue[0]

        if silent:
            return None

        raise IndexError("peek from empty queue")

    def is_empty(self) -> bool:
        return not self._queue
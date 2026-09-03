import heapq
from typing import Any, Optional


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._counter = 0

    def __len__(self):
        return len(self._queue)

    def enqueue(self, item: Any, priority: int | float) -> None:
        # Counter provides deterministic tie-breaking when priorities are equal
        heapq.heappush(self._queue, (priority, self._counter, item))
        self._counter += 1

    def dequeue(self, silent: bool = False) -> Optional[Any]:
        if not self.is_empty():
            _, _, item = heapq.heappop(self._queue)
            return item

        if silent:
            return None

        raise IndexError("dequeue from empty priority queue")

    def peek(self, silent: bool = False) -> Optional[Any]:
        if not self.is_empty():
            _, _, item = self._queue[0]
            return item

        if silent:
            return None

        raise IndexError("peek from empty priority queue")

    def is_empty(self) -> bool:
        return not self._queue
from abc import ABC, abstractmethod

from typing import Any


class ProblemBase[T](ABC):

    @abstractmethod
    def actions(self, current_state: T) -> list[T]:
        pass

    @abstractmethod
    def goal_test(self, current_state: T) -> bool:
        pass

    @property
    @abstractmethod
    def initial_state(self) -> T:
        pass
from abc import ABC, abstractmethod
from models import Cell


class ProblemBase(ABC):

    @abstractmethod
    def actions(self, current_cell: Cell) -> list[Cell]:
        pass

    @abstractmethod
    def goal_test(self, current_cell: Cell) -> bool:
        pass

    @property
    @abstractmethod
    def initial_state(self) -> Cell:
        pass
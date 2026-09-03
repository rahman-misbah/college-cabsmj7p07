from abc import ABC, abstractmethod

class TraverseProblemBase[T](ABC):

    @abstractmethod
    def actions(self, current_state: T) -> list[T]:
        pass

    @property
    @abstractmethod
    def initial_state(self) -> T:
        pass

class GoalProblemBase[T](TraverseProblemBase[T]):
    @abstractmethod
    def goal_test(self, current_state: T) -> bool:
        pass
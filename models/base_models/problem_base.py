"""Defines the base abstractions for problems

The possible problem types can be traversal problems or goal search problems
"""

from abc import ABC, abstractmethod

from . import StateBase

class TraversalProblemBase[T: StateBase](ABC):

    # PUBLIC METHODS ------------------------------------------------------------------------------

    @abstractmethod
    @property
    def initial_state(self) -> T:
        pass

    # PUBLIC METHODS ------------------------------------------------------------------------------

    @abstractmethod
    def actions(self) -> list[T]:
        """Return a list of all valid next states"""
        pass

class GoalProblemBase[T: StateBase](TraversalProblemBase[T]):

    # PUBLIC METHODS ------------------------------------------------------------------------------

    @abstractmethod
    def goal_test(self, current_state: T) -> bool:
        """Checks whether current_state is a valid goal state"""
        pass
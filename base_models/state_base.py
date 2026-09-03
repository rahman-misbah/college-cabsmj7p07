"""Defines the base abstraction for a state class"""

from abc import ABC, abstractmethod

class StateBase(ABC):

    # DUNDER METHODS ------------------------------------------------------------------------------

    @abstractmethod
    def __eq__(self):
        pass

    def __hash__(self):
        pass
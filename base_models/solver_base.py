"""Defines the base abstractions for solvers

The possible solver types are goal solvers and traversal solvers
"""

from . import StateBase, TraversalProblemBase, GoalProblemBase

from abc import ABC, abstractmethod

class TraversalSolverBase[T](ABC):

    # PUBLIC METHODS ------------------------------------------------------------------------------

    @classmethod
    def solve(cls, problem: TraversalProblemBase[T]) -> list[T]:
        """Returns the list of all visited states in a traversal"""
        return cls._solve(problem)

    # PRIVATE METHODS -----------------------------------------------------------------------------

    @abstractmethod
    def _solve(problem: TraversalProblemBase[T]) -> list[T]:
        """Implementation of the solution process"""
        pass

class GoalSolverBase[T](ABC):

    # PUBLIC METHODS ------------------------------------------------------------------------------

    @classmethod
    def solve(cls, problem: GoalProblemBase[T]) -> list[list[T]]:
        parent_dict: dict[T, None | T]
        goal_states: set[T]

        parent_dict, goal_states = cls._solve(problem)
        solutions = cls._construct_solutions(parent_dict, goal_states)

        return solutions

    # PRIVATE METHODS -----------------------------------------------------------------------------

    @abstractmethod
    def _solve(problem: GoalProblemBase[T]) -> tuple[dict[T, None | T], set[T]]:
        pass

    @staticmethod
    def _construct_solutions(parent_dict: dict[T, None | T], goal_states: set[T]):
        solution_list:list[list[T]] = list()
        
        for goal in goal_states:
            current_solution:list[T] = list()
            current_state:T = goal

            while current_state is not None:
                current_solution.append(current_state)
                current_state = parent_dict[current_state]
                    
            current_solution.reverse()
            solution_list.append(current_solution)
                
        return solution_list
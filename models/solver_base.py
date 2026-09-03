from typing import Optional
from abc import ABC, abstractmethod

from problem_base import TraverseProblemBase, GoalProblemBase

class TraverseSolverBase[T](ABC):
    def __init__(self, problem:TraverseProblemBase[T]):
        self._problem : TraverseProblemBase[T] = problem
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def problem(self) -> TraverseProblemBase[T]:
        return self._problem
    
    # PRIVATE METHODS -----------------------------------------------------------------------------

    @abstractmethod
    def _solve(self) -> list[T]:
        pass
    
    # PUBLIC METHODS ------------------------------------------------------------------------------

    def solve(self) -> list[T]:
        return self._solve()

class GoalSolverBase[T](TraverseSolverBase[T]):
    def __init__(self, problem: GoalProblemBase, early_exit:bool = True):
        super().__init__(problem)
        self._early_exit : bool = early_exit

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def early_exit(self) -> bool:
        return self._early_exit

    # PRIVATE METHODS -----------------------------------------------------------------------------

    @abstractmethod
    def _solve(self) -> tuple[dict[T, Optional[T]], set[T]]:
        pass

    def _construct_solutions(self, 
                             parent_dict:dict[T, Optional[T]], 
                             goal_states:set[T]
                             ) -> list[list[T]]:
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

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def toggle_early_exit(self) -> None:
        self._early_exit = not self._early_exit

    def solve(self) -> list[list[T]]:
        parent_dict, goal_states = self._solve()
        solutions = self._construct_solutions(parent_dict, goal_states)

        return solutions
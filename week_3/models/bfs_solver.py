from typing import Optional

from . import ProblemBase
from data_structures import Queue

class BFSSolver[T]:
    def __init__(self, maze_problem:ProblemBase, early_exit:bool = True):
        self._maze_problem : ProblemBase = maze_problem
        self._early_exit : bool = early_exit
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def maze_problem(self) -> ProblemBase:
        return self._maze_problem
    
    @property
    def early_exit(self) -> bool:
        return self._early_exit
    
    # PRIVATE METHODS -----------------------------------------------------------------------------

    def _solve_bfs(self):
        parent_dict:dict[T, Optional[T]] = dict()
        goal_states:set[T] = set()
        queue : Queue = Queue()

        queue.enqueue(self.maze_problem.initial_state)
        parent_dict[self.maze_problem.initial_state] = None

        while not queue.is_empty():
            current_state:T = queue.dequeue()

            if self.maze_problem.goal_test(current_state):
                goal_states.add(current_state)

                if self.early_exit:
                    return parent_dict, goal_states
            
            next_state:T
            for next_state in self.maze_problem.actions(current_state):
                if next_state not in parent_dict:
                    parent_dict[next_state] = current_state
                    queue.enqueue(next_state)
        
        return parent_dict, goal_states
    
    def _construct_solutions(self, parent_dict:dict[T, Optional[T]], goal_states:set[T]):
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
    
    def solve(self):
        parent_dict, goal_states = self._solve_bfs()
        solutions = self._construct_solutions(parent_dict, goal_states)

        return solutions
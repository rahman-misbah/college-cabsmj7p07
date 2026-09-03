from typing import Optional

from .solver_base import TraverseSolverBase, GoalSolverBase
from .problem_base import TraverseProblemBase, GoalProblemBase
from data_structures import Stack

class DFSSolver[T]:
    def solve(problem: TraverseProblemBase[T] | GoalProblemBase[T]):
        pass

class DFSTraverseSolver[T](GoalSolverBase[T]):
    pass

class DFSGoalSolver[T](TraverseSolverBase[T]):
    def _solve(self) -> tuple[dict[T, Optional[T]], set[T]]:
        parent_dict:dict[T, Optional[T]] = dict()
        goal_states:set[T] = set()
        stack : Stack = Stack()

        stack.push(self.problem.initial_state)
        parent_dict[self.problem.initial_state] = None

        while not stack.is_empty():
            current_state:T = stack.pop()

            if self.problem.goal_test(current_state):
                goal_states.add(current_state)

                if self.early_exit:
                    return parent_dict, goal_states
            
            next_state:T
            for next_state in self.problem.actions(current_state):
                if next_state not in parent_dict:
                    parent_dict[next_state] = current_state
                    stack.push(next_state)
        
        return parent_dict, goal_states
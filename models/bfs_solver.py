from typing import Optional

from .solver_base import TraverseSolverBase
from data_structures import Queue

class BFSSolver[T](TraverseSolverBase[T]):
    def _solve(self) -> tuple[dict[T, Optional[T]], set[T]]:
        parent_dict:dict[T, Optional[T]] = dict()
        goal_states:set[T] = set()
        queue : Queue = Queue()

        queue.enqueue(self.problem.initial_state)
        parent_dict[self.problem.initial_state] = None

        while not queue.is_empty():
            current_state:T = queue.dequeue()

            if self.problem.goal_test(current_state):
                goal_states.add(current_state)

                if self.early_exit:
                    return parent_dict, goal_states
            
            next_state:T
            for next_state in self.problem.actions(current_state):
                if next_state not in parent_dict:
                    parent_dict[next_state] = current_state
                    queue.enqueue(next_state)
        
        return parent_dict, goal_states
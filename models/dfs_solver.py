"""Defines the DFSSolver class to solve state search problems using DFS

Expects the problem to be an implementation fo TraversalProblemBase or GoalProblemBase
"""

from base_models import StateBase, TraversalProblemBase, TraversalSolverBase, GoalProblemBase, GoalSolverBase
from ..data_structures import Stack

class DFSSolver[T: StateBase]:
    def solve(problem: TraversalProblemBase | GoalProblemBase, early_exit: bool = True):
        """Calls the appropriate DFS Solver according to problem type
        
        Note:
            early_exit(bool) is only relevant if problem is a GoalProblem type
        """
        if isinstance(problem, GoalProblemBase):
            return _DFSGoalSolver.solve(problem, early_exit)
        
        if isinstance(problem, TraversalProblemBase):
            return _DFSTraversalSolver.solve(problem)

        raise TypeError(f"Unknown problem type (type: {type(problem)})")

class _DFSTraversalSolver[T: StateBase](TraversalSolverBase[T]):

    # PRIVATE METHODS -----------------------------------------------------------------------------

    @staticmethod
    def _solve(problem: TraversalProblemBase[T]) -> list[T]:
        visited: set[T] = set()
        traversal_order: list[T] = list()
        stack = Stack()

        stack.push(problem.initial_state)

        while not stack.is_empty():
            current_node = stack.pop()
            visited.add(current_node)
            traversal_order.append(current_node)

            next_nodes = problem.actions(current_node)
            for next_node in next_nodes:
                if next_node in visited: continue
                stack.push(next_node)

        return traversal_order

class _DFSGoalSolver[T: StateBase](GoalSolverBase[T]):

    @staticmethod
    def _solve(problem: GoalProblemBase[T], early_exit: bool = True) -> tuple[dict[T, T | None], set[T]]:
        parent_dict: dict[T, T | None] = dict()
        goal_states: set[T] = set()
        stack = Stack()

        stack.push(problem.initial_state)
        parent_dict[problem.initial_state] = None

        while not stack.is_empty():
            current_node = stack.pop()

            if problem.goal_test(current_node):
                goal_states.add(current_node)

                if early_exit:
                    return parent_dict, goal_states

            next_nodes = problem.actions(current_node)

            for next_node in next_nodes:
                if next_node in parent_dict: continue

                parent_dict[next_node] = current_node
                stack.push(next_node)

        return parent_dict, goal_states
"""Defines the BFSSolver class to solve state search problems using DFS

Expects the problem to be an implementation fo TraversalProblemBase or GoalProblemBase
"""

from models.base_models import StateBase, TraversalProblemBase, TraversalSolverBase, GoalProblemBase, GoalSolverBase
from data_structures import Queue

class BFSSolver[T: StateBase]:
    def solve(
            problem: TraversalProblemBase | GoalProblemBase,
            early_exit: bool = True
            ) -> list[list[T]] | list[T]:
        """Calls the appropriate BFS Solver according to problem type

        Args:
            problem(TraversalProblemBase | GoalProblemBase): The problem to be solved. Must be an implementation of the appropriate base class.
            early_exit(bool): Whether to exit once a single goal has been found (only relevant to GoalProblemBase type problems)
        """
        if isinstance(problem, GoalProblemBase):
            return _BFSGoalSolver.solve(problem, early_exit)
        
        if isinstance(problem, TraversalProblemBase):
            return _BFSTraversalSolver.solve(problem)

        raise TypeError(f"Unknown problem type (type: {type(problem)})")

class _BFSTraversalSolver[T: StateBase](TraversalSolverBase[T]):

    # PRIVATE METHODS -----------------------------------------------------------------------------

    @staticmethod
    def _solve(problem: TraversalProblemBase[T]) -> list[T]:
        visited: set[T] = set()
        traversal_order: list[T] = list()
        queue = Queue()

        queue.enqueue(problem.initial_state)

        while not queue.is_empty():
            current_node = queue.dequeue()
            visited.add(current_node)
            traversal_order.append(current_node)

            next_nodes = problem.actions(current_node)
            for next_node in next_nodes:
                if next_node in visited: continue
                queue.enqueue(next_node)

        return traversal_order

class _BFSGoalSolver[T: StateBase](GoalSolverBase[T]):

    @staticmethod
    def _solve(problem: GoalProblemBase[T], early_exit: bool = True) -> tuple[dict[T, T | None], set[T]]:
        parent_dict: dict[T, T | None] = dict()
        goal_states: set[T] = set()
        queue = Queue()

        queue.enqueue(problem.initial_state)
        parent_dict[problem.initial_state] = None

        while not queue.is_empty():
            current_node = queue.dequeue()

            if problem.goal_test(current_node):
                goal_states.add(current_node)

                if early_exit:
                    return parent_dict, goal_states

            next_nodes = problem.actions(current_node)

            for next_node in next_nodes:
                if next_node in parent_dict: continue

                parent_dict[next_node] = current_node
                queue.enqueue(next_node)

        return parent_dict, goal_states
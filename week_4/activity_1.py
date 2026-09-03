from ..models import Cell, Maze, GoalProblemBase, GoalSolverBase
from ..data_structures.priority_queue import PriorityQueue

def manhattan_distance(current_cell: Cell, goal_cell: Cell) -> int:
    return abs(current_cell.x - goal_cell.x) + abs(current_cell.y - goal_cell.y)

class AStarNode:
    def __init__(self, cell: Cell, path_cost: int = 0):
        self._cell = cell
        self._path_cost = path_cost

    @property
    def cell(self):
        return self._cell

    @property
    def path_cost(self):
        return self._path_cost

    @path_cost.setter
    def path_cost(self, new_cost):
        self._path_cost = new_cost

    def distance_to(self, target_cell: Cell):
        return manhattan_distance(self.cell, target_cell)

class AStarProblem(GoalProblemBase[AStarNode]):
    def __init__(self, raw_maze: Maze):
        self._maze = raw_maze

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def maze(self) -> Maze:
        return self._maze
    
    @property
    def initial_state(self) -> AStarNode:
        return AStarNode(self.maze.start_cell)

    # ACTIONS -------------------------------------------------------------------------------------

    def _up(self, current_cell:Cell) -> Cell:
        return Cell(current_cell.x, current_cell.y - 1)
    
    def _right(self, current_cell:Cell) -> Cell:
        return Cell(current_cell.x + 1, current_cell.y)
    
    def _down(self, current_cell:Cell) -> Cell:
        return Cell(current_cell.x, current_cell.y + 1)
    
    def _left(self, current_cell:Cell) -> Cell:
        return Cell(current_cell.x - 1, current_cell.y)

    def actions(self, current_node: AStarNode) -> list[AStarNode]:
            all_moves:list = [self._up,
                         self._right,
                         self._down,
                         self._left
                         ]
            
            possible_moves:list[AStarNode] = list()
    
            for move in all_moves:
                current_cell = current_node.cell
                current_path_cost = current_node.path_cost
                new_cell = move(current_cell)
    
                if 0 <= new_cell.x < self.maze.width and 0 <= new_cell.y < self.maze.height:
                    if self.maze[new_cell] == '0':
                        possible_moves.append(AStarNode(new_cell, current_path_cost + 1))
            
            return possible_moves

    def goal_test(self, current_node: AStarNode) -> bool:
        return self.maze.goal_cell == current_node.cell

class AStarSolver(GoalSolverBase[AStarNode]):
    def __init__(self, problem: AStarProblem, early_exit: bool = True):
        super().__init__(problem, early_exit)

    def _solve(self):
        parent_dict = dict()
        queue = PriorityQueue()
        goal_states = set()

        queue.enqueue(self.problem.initial_state, 1)
        parent_dict[self.problem.initial_state] = None

        while not queue.is_empty():
            current_node = queue.dequeue()

            if self.problem.goal_test(current_node):
                goal_states.add(current_node)

                if self.early_exit:
                    return parent_dict, goal_states

            new_nodes = self.problem.actions(current_node)

            for new_node in new_nodes:
                if new_node in parent_dict: continue

                estimated_cost = new_node.distance_to(self.problem.maze.goal_cell) + new_node.path_cost
                parent_dict[new_node] = current_node
                queue.enqueue(new_node, estimated_cost)

        return parent_dict, goal_states


if __name__ == "__main__":
    raw_maze = [
        ['0', '0', '0', '1', '0', '0', '0'],
        ['1', '1', '0', '1', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '1', '0'],
        ['0', '1', '1', '1', '0', '1', '0'],
        ['0', '0', '0', '1', '0', '0', '0'],
        ['0', '1', '0', '0', '0', '1', '1'],
        ['0', '0', '0', '1', '0', '0', '0']
    ]

    maze = Maze(raw_maze, (0, 0), (6, 6))

    a_star_problem = AStarProblem(maze)
    a_star_solver = AStarSolver(a_star_problem)

    solutions = a_star_solver.solve()

    print(solutions[0])

    
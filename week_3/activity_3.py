from models import Grid, Cell
from models.cell import right, down
from models.base_models import GoalProblemBase
from algorithms import BFSSolver
from utils import display_path

class RobotProblem(GoalProblemBase[Cell]):
    def __init__(self, grid: list[list[int]], start_cell: tuple[int, int], goal_cell: tuple[int, int]):
        self._grid = Grid(grid)
        self._start_cell = Cell(*start_cell)
        self._goal_cell = Cell(*goal_cell)

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __str__(self) -> str:
        result = list()

        result.append(str(self.grid))
        result.append(f"Start Cell: {self.start_cell}")
        result.append(f"Goal Cell: {self.goal_cell}")

        return '\n'.join(result)

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def grid(self) -> Grid:
        return self._grid

    @property
    def start_cell(self) -> Cell:
        return self._start_cell

    @property
    def goal_cell(self) -> Cell:
        return self._goal_cell

    @property
    def initial_state(self):
        return self.start_cell

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def actions(self, current_cell: Cell) -> list[Cell]:
        all_actions = [right, down]
        valid_actions = list()

        for action in all_actions:
            next_cell = action(current_cell)

            if not 0 <= next_cell.x < self.grid.width: continue
            if not 0 <= next_cell.y < self.grid.height: continue
            if self.grid[next_cell] == 0:
                valid_actions.append(next_cell)

        return valid_actions

    def goal_test(self, current_cell: Cell) -> bool:
        return current_cell == self.goal_cell

if __name__ == "__main__":
    raw_grid = [
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 0]

        ]

    start_cell = (0, 0)
    goal_cell = (3, 3)

    problem = RobotProblem(raw_grid, start_cell, goal_cell)
    print(problem)

    result = BFSSolver.solve(problem)

    display_path(result[0])
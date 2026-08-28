from models import Cell, Maze, ProblemBase, MazeSolver

class MazeProblem(ProblemBase):
    def __init__(self, maze:Maze):
        self._maze:Maze = maze
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def maze(self) -> Maze:
        return self._maze
    
    @property
    def initial_state(self) -> Cell:
        return self.maze.start_cell
    
    # PRIVATE METHODS -----------------------------------------------------------------------------
    # ACTIONS

    def _up(self, current_cell:Cell) -> Cell:
        return Cell(current_cell.x, current_cell.y - 1)
    
    def _right(self, current_cell:Cell) -> Cell:
        return Cell(current_cell.x + 1, current_cell.y)
    
    def _down(self, current_cell:Cell) -> Cell:
        return Cell(current_cell.x, current_cell.y + 1)
    
    def _left(self, current_cell:Cell) -> Cell:
        return Cell(current_cell.x - 1, current_cell.y)
    
    # PUBLIC METHODS ------------------------------------------------------------------------------
    
    def actions(self, current_cell:Cell) -> list[Cell]:
        all_moves:list = [self._up,
                     self._right,
                     self._down,
                     self._left
                     ]
        
        possible_moves:list[Cell] = list()

        for move in all_moves:
            new_cell = move(current_cell)

            if 0 <= new_cell.x < self.maze.width and 0 <= new_cell.y < self.maze.height:
                if self.maze[new_cell] == '0':
                    possible_moves.append(new_cell)
        
        return possible_moves
    
    def goal_test(self, current_cell:Cell) -> bool:
        return current_cell == self.maze.goal_cell

if __name__ == "__main__":
    maze = [
        ['0', '0', '0', '1', '0', '0', '0'],
        ['1', '1', '0', '1', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '1', '0'],
        ['0', '1', '1', '1', '0', '1', '0'],
        ['0', '0', '0', '1', '0', '0', '0'],
        ['0', '1', '0', '0', '0', '1', '1'],
        ['0', '0', '0', '1', '0', '0', '0']
    ]

    initial_state = (0, 0)
    goal_state = (6, 6)

    maze_2d = Maze(maze, initial_state, goal_state)
    maze_problem = MazeProblem(maze_2d)

    solver = MazeSolver(maze_problem)
    solutions = solver.solve()

    print(maze_2d)
    print(solutions[0])
# Solving Maze using BFS
# Maze is represented by a 2D grid, where S is start, E is end, 0 is open path, 1 is wall

import copy
from typing import Union

class State:
    def __init__(self, x:int, y:int):
        self._x : int = x
        self._y : int = y

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"State({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other : State) -> bool:
        return self.x == other.x and self.y == other.y

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    # PUBLIC METHODS ------------------------------------------------------------------------------

    def up(self):
        return State(self.x, self.y + 1)
    
    def down(self):
        return State(self.x, self.y - 1)
    
    def left(self):
        return State(self.x - 1, self.y)
    
    def right(self):
        return State(self.x + 1, self.y)

class Maze:
    def __init__(self, maze: list[list[str]], initial_state:tuple[int], goal_state:tuple[int]):
        self._maze : Maze = copy.deepcopy(maze)
        self._width : int = len(maze[0])
        self._height : int = len(maze)

        self._initial_state : State = State(*initial_state)
        self._goal_state : State = State(*goal_state)

        self._process_maze()

        self._maze_str : str = self._generate_str()
    
    # DUNDER METHODS ------------------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"Maze({self.maze}, {self.initial_state}, {self.goal_state})"
    
    def __str__(self) -> str:
        return self._maze_str
    
    def __getitem__(self, key:Union[State, tuple[int]]) -> str:
        """Expects key in x, y when passed as tuple format"""
        if isinstance(key, State):
            return self.query(key.x, key.y)
        return self.query(*key)

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def maze(self) -> list[list[str]]:
        return self._maze

    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def initial_state(self) -> State:
        return self._initial_state
    
    @property
    def goal_state(self) -> State:
        return self._goal_state
    
    # PRIVATE METHODS -----------------------------------------------------------------------------

    def _process_maze(self):
        """Places S and E at relevant positions"""
        self._maze[self.initial_state.y][self.initial_state.x] = 'S'
        self._maze[self.goal_state.y][self.goal_state.x] = 'E'
    
    def _generate_str(self):
        result : list = []

        for row in self.maze:
            result.append(str(row))
        
        result.append(f"Start: {self.initial_state}")
        result.append(f"Goal: {self.goal_state}")

        return '\n'.join(result)
    
    # PUBLIC METHODS ------------------------------------------------------------------------------
    def query(self, x:int, y:int) -> str:
        if not 0 <= x < self.width:
            raise IndexError("x coordinate out of bounds")
        
        if not 0 <= y < self.height:
            raise IndexError("y coordinate out of bounds")
        
        return self._maze[y][x]

class MazeSolver:
    def __init__(self, maze:Maze):
        self._maze : Maze = maze
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def maze(self):
        return self._maze

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def actions(self, current_state: State) -> set:
        possible_moves : set = set()
        moves = [current_state.up(),
                 current_state.right(),
                 current_state.down(),
                 current_state.left()
                 ]
        
        for state in moves:
            if 0 <= state.y < self.maze.height and 0 <= state.x < self.maze.width:
                if self.maze[state] in ('S', 'E', '0'):
                    possible_moves.add(state)
        
        return possible_moves

def goal_test(current_state:State, goal_state:State) -> bool:
    return current_state == goal_state

if __name__ == "__main__":
    pass
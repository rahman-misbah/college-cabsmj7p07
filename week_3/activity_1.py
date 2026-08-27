# Solving Maze using BFS
# Maze is represented by a 2D grid, where S is start, E is end, 0 is open path, 1 is wall

class State:
    def __init__(self, x:int, y:int):
        self._x : int = x
        self._y : int = y

    def __repr__(self) -> str:
        return f"State({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

class Maze:
    def __init__(self, maze: list[list[str]], initial_state:tuple[int], goal_state:tuple[int]):
        self._initial_state = State(*initial_state)
        self._goal_state = State(*goal_state)
        self._maze = maze

    def __repr__(self) -> str:
        pass

def goal_test(current_state:State, goal_state:State) -> bool:
    return current_state == goal_state
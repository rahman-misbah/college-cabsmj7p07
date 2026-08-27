# Solving Maze using BFS
# Maze is represented by a 2D grid, where S is start, E is end, 0 is open path, 1 is wall

import copy
from typing import Union, Optional

from data_structures.queue import Queue


class State:
    def __init__(self, x: int, y: int):
        self._x: int = x
        self._y: int = y

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"State({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: State) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def up(self) -> State:
        return State(self.x, self.y - 1)

    def down(self) -> State:
        return State(self.x, self.y + 1)

    def left(self) -> State:
        return State(self.x - 1, self.y)

    def right(self) -> State:
        return State(self.x + 1, self.y)


class Maze:
    def __init__(
        self,
        maze: list[list[str]],
        initial_state: tuple[int, int],
        goal_state: tuple[int, int]
    ):
        self._maze: list[list[str]] = copy.deepcopy(maze)
        self._width: int = len(maze[0])
        self._height: int = len(maze)

        self._initial_state: State = State(*initial_state)
        self._goal_state: State = State(*goal_state)

        self._process_maze()

        self._maze_str: str = self._generate_str()

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"Maze({self.maze}, {self.initial_state}, {self.goal_state})"

    def __str__(self) -> str:
        return self._maze_str

    def __getitem__(self, key: Union[State, tuple[int, int]]) -> str:
        """Expects x, y when passed in tuple format."""
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

    def _process_maze(self) -> None:
        """Places S and E at the relevant positions."""
        self._maze[self.initial_state.y][self.initial_state.x] = 'S'
        self._maze[self.goal_state.y][self.goal_state.x] = 'E'

    def _generate_str(self) -> str:
        result: list[str] = []

        for row in self.maze:
            result.append(str(row))

        result.append(f"Start: {self.initial_state}")
        result.append(f"Goal: {self.goal_state}")

        return '\n'.join(result)

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def query(self, x: int, y: int) -> str:
        if not 0 <= x < self.width:
            raise IndexError("x coordinate out of bounds")

        if not 0 <= y < self.height:
            raise IndexError("y coordinate out of bounds")

        return self._maze[y][x]


class MazeSolver:
    def __init__(self, maze: Maze):
        self._maze: Maze = maze

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def maze(self) -> Maze:
        return self._maze

    # PRIVATE METHODS -----------------------------------------------------------------------------

    def _actions(self, current_state: State) -> list[State]:
        possible_moves: list[State] = []
        moves: list[State] = [
            current_state.up(),
            current_state.right(),
            current_state.down(),
            current_state.left()
        ]

        for state in moves:
            if 0 <= state.y < self.maze.height and 0 <= state.x < self.maze.width:
                if self.maze[state] in ('S', 'E', '0'):
                    possible_moves.append(state)

        return possible_moves

    def _goal_test(self, current_state: State) -> bool:
        return current_state == self.maze.goal_state

    def _solve_bfs(self) -> tuple[dict[State, Optional[State]], Optional[State]]:
        """Solves the maze using BFS and returns the parent dictionary and goal state."""
        queue = Queue()
        initial_state: State = self.maze.initial_state
        parent_dict: dict[State, Optional[State]] = {initial_state: None}

        queue.enqueue(initial_state)

        while not queue.is_empty():
            current_state: State = queue.dequeue()

            if self._goal_test(current_state):
                return parent_dict, current_state

            for next_state in self._actions(current_state):
                # Skip already visited states.
                if next_state in parent_dict:
                    continue

                parent_dict[next_state] = current_state
                queue.enqueue(next_state)

        return parent_dict, None

    def _process_raw_result(
        self,
        parent_dict: dict[State, Optional[State]],
        goal: Optional[State]
    ) -> Optional[list[State]]:
        if goal is None:
            return None

        path: list[State] = []
        current_state: Optional[State] = goal

        while current_state is not None:
            path.append(current_state)
            current_state = parent_dict[current_state]

        path.reverse()
        return path

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def solve(self) -> Optional[list[State]]:
        parent_dict, goal = self._solve_bfs()
        path = self._process_raw_result(parent_dict, goal)

        return path


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

    maze = Maze(maze, initial_state, goal_state)

    print("MAZE")
    print(maze)

    solver = MazeSolver(maze)
    path = solver.solve()

    print("\nSOLUTION PATH")
    if path is None:
        print("No path found.")
    else:
        for state in path:
            print(state)
"""Defines a simple 2D grid

- 0 represents an open path
- 1 represents a closed path
"""

import copy

from models import Cell

class Grid:
    def __init__(self, raw_grid = list[list[int]]):
        self._grid = copy.deepcopy(raw_grid)
        self._width = len(self._grid[0])
        self._height = len(self._grid)

        self._str = Grid._generate_str(self._grid)

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __str__(self) -> str:
        return self._str

    def __repr__(self) -> str:
        return f"Grid({self._grid})"

    def __getitem__(self, key: tuple[int, int] | Cell) -> int:
        return self.query_cell(key)

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def query_cell(self, key: tuple[int, int] | Cell) -> int:
        """Expects input in (x,y) format"""

        if isinstance(key, Cell):
            x, y = key.x, key.y
        else:
            x, y = key

        if not 0 <= x < self.width:
            raise IndexError("x out of bounds")

        if not 0 <= y < self.height:
            raise IndexError("y out of bounds")

        return self._grid[y][x]

    # PRIVATE METHODS -----------------------------------------------------------------------------

    @staticmethod
    def _generate_str(grid: list[list[int]]) -> str:
        result = list()
        separator_len = len(grid[0]) + (len(grid[0]) - 1) * 3 + 4

        result.append('-' * separator_len)

        for row in grid:
            row = list(map(str, row))
            row = ' | '.join(row)
            row = '| ' + row + ' |'

            result.append(row)
            result.append('-' * separator_len)

        return '\n'.join(result)
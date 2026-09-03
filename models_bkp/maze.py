from types import MappingProxyType
from .cell import Cell

class Maze:
    def __init__(self, maze:list[list[str]], start_cell: tuple[int, int], goal_cell: tuple[int, int]):
        self._maze = maze
        self._start_cell = Cell(*start_cell)
        self._goal_cell = Cell(*goal_cell)

        self._height = len(self._maze)      # Number of rows
        self._width = len(self._maze[0])    # Number of columns
    
    # DUNDER METHODS ------------------------------------------------------------------------------

    def __getitem__(self, key:tuple[int, int] | Cell) -> str:
        if isinstance(key, Cell):
            return self.check_cell(key.x, key.y)
        return self.check_cell(*key)    # Expects a 2 item tuple
    
    def __str__(self) -> str:
        result = []

        for row in self._maze:
            result.append(str(row))
        
        result.append(f"Start Cell: {self.start_cell}")
        result.append(f"Goal Cell: {self.goal_cell}")

        return '\n'.join(result)
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def maze(self) -> MappingProxyType:
        return MappingProxyType(self._maze)
    
    @property
    def start_cell(self) -> Cell:
        return self._start_cell
    
    @property
    def goal_cell(self) -> Cell:
        return self._goal_cell
    
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def check_cell(self, x:int, y:int):
        if not 0 <= x < self.width:
            raise IndexError("x out of bounds")

        if not 0 <= y < self.height:
            raise IndexError("y out of bounds")
        
        return self._maze[y][x]
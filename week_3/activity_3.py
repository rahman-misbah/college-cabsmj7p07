# Robot grid problem
# Robot can move right or bottom

from types import MappingProxyType

class Cell:
    def __init__ (self, x:int, y:int):
        self._x = x
        self._y = y

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"Cell({self.x, self.y})"
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y

class Maze:
    def __init__(self, maze:list[list[str]], start_cell:tuple[int, int], goal_cell:tuple[int, int]):
        """Expects cells in (x, y) format"""
        self._maze = maze
        self._start_cell = Cell(*start_cell)
        self._goal_cell = Cell(*goal_cell)

        self._width = len(self._maze[0])
        self._height = len(self._maze)
    
    # DUNDER METHODS ------------------------------------------------------------------------------

    def __getitem__(self, key):
        if isinstance(key, Cell):
            return self.query(Cell.x, Cell.y)
        return self.query(*key)
        
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

    def query(self, coordinate:tuple[int, int]):
        """Expects coordinates in (x, y) format"""
        x:int
        y:int
        x, y = coordinate

        if not 0 <= x < self.width:
            raise IndexError("x out of bounds")
        
        if not 0 <= y < self.height:
            raise IndexError("y out of bounds")
        
        return self._maze[y][x]
        
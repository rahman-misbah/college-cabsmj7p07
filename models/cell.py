"""Defines a simple grid cell, represented using (x,y) coordinates"""

from models.base_models import StateBase

class Cell(StateBase):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __repr__(self) -> str:
        return f"Cell({self.x},{self.y})"

    def __eq__(self, other: Cell) -> bool:
        return self.x == other.x and self.y == other._y

    def __hash__(self) -> int:
        return hash(str(self))

    # PROPERTIES

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

# Cell Moves

def up(current_cell: Cell) -> Cell:
    return Cell(current_cell.x, current_cell.y - 1)

def right(current_cell: Cell) -> Cell:
    return Cell(current_cell.x + 1, current_cell.y)

def down(current_cell: Cell) -> Cell:
    return Cell(current_cell.x, current_cell.y + 1)

def left(current_cell: Cell) -> Cell:
    return Cell(current_cell.x - 1, current_cell.y)
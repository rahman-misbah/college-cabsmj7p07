class Cell:
    def __init__(self, user_x:int, user_y:int):
        self._x = user_x
        self._y = user_y
    
    # DUNDER METHODS ------------------------------------------------------------------------------

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

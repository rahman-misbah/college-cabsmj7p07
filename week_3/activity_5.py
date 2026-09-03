from models.base_models import StateBase, GoalProblemBase
from algorithms import BFSSolver
from utils import display_path

# Farmer Fox Chicken Grain
class FFCGState(StateBase):
    def __init__(self, left_bank: set[str], right_bank: set[str], farmer_position: str):
        """Defines a simple state for the Farmer Fox Chicken Grain problem
        
        Args:
            left_bank(set[str]): Represents the entities on the left side of the river bank
            right_bank(set[str]): Represents the entities on the right side of the river bank
            farmer_position(str): Represents the farmer's position. Can be 'left' or 'right'
        
        Note:
            The tuple can only have the following symbols:
            - 'F' : Fox
            - 'C' : Chicken
            - 'G' : Grain
        """
        self._left_bank = set(left_bank)
        self._right_bank = set(right_bank)
        self._farmer_position = farmer_position

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __str__(self) -> str:
        left_bank = list(self.left_bank)
        right_bank = list(self.right_bank)

        left_bank.sort()
        right_bank.sort()

        farmer: str
        if self.farmer_current_position == "left":
            farmer = "f__"
        else:
            farmer = "__f"

        return f"({', '.join(left_bank)}){farmer}({', '.join(right_bank)})"

    def __repr__(self) -> str:
        return f"FFCGState({self.left_bank}, {self.right_bank}, {self.farmer_current_position})"

    def __eq__(self, other:FFCGState) -> bool:
        left_bank_check = self.left_bank == other.left_bank
        right_bank_check = self.right_bank == other.right_bank
        farmer_position_check = self.farmer_current_position == other.farmer_current_position

        return left_bank_check and right_bank_check and farmer_position_check

    def __hash__(self) -> int:
        return hash(str(self))

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def left_bank(self) -> tuple[str, ...]:
        return tuple(self._left_bank)

    @property
    def right_bank(self) -> tuple[str, ...]:
        return tuple(self._right_bank)

    @property
    def farmer_bank(self) -> tuple[str, ...]:
        """Returns the bank the farmer is on"""
        if self.farmer_current_position == "right":
            return self.right_bank
        return self.left_bank

    @property
    def opposite_bank(self) -> tuple[str, ...]:
        """Returns the bank opposite to the farmer"""
        if self.farmer_current_position == "right":
            return self.left_bank
        return self.right_bank

    @property
    def farmer_current_position(self) -> str:
        return self._farmer_position

    @property
    def farmer_next_position(self) -> str:
        if self.farmer_current_position == "right":
            return "left"
        return "right"


    # PUBLIC METHODS ------------------------------------------------------------------------------

    def toggle_farmer_position(self) -> None:
        self._farmer_position = self.farmer_next_position

class FFCGProblem(GoalProblemBase):
    def __init__(self):
        self._initial_state = FFCGState({'C', 'F', 'G'}, set(), 'left')
        self._goal_state = FFCGState(set(), {'C', 'F', 'G'}, 'right')

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def initial_state(self) -> FFCGState:
        return self._initial_state

    @property
    def goal_state(self) -> FFCGState:
        return self._goal_state

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def actions(self, current_state: FFCGState) -> list[FFCGState]:
        all_next_states = list()

        # Farmer moves an entity
        for entity in current_state.farmer_bank:
            new_farmer_bank = list(current_state.farmer_bank)
            new_farmer_bank.remove(entity)

            new_opposite_bank = list(current_state.opposite_bank)
            new_opposite_bank.append(entity)

            if current_state.farmer_current_position == "left":
                new_state = FFCGState(new_farmer_bank, new_opposite_bank, current_state.farmer_next_position)
            else:
                new_state = FFCGState(new_opposite_bank, new_farmer_bank, current_state.farmer_next_position)

            all_next_states.append(new_state)

        # Farmer doesn't move an entity
        all_next_states.append(FFCGState(current_state.left_bank, current_state.right_bank, current_state.farmer_next_position))

        return [state for state in all_next_states if not self._fail(state)]

    def goal_test(self, current_state: FFCGState) -> bool:
        return current_state == self.goal_state

    # PRIVATE METHODS -----------------------------------------------------------------------------

    def _fail(self, current_state: FFCGState) -> bool:
        """Returns true if the current state is invalid"""

        opposite_bank = current_state.opposite_bank

        # Checks
        if 'F' in opposite_bank and 'C' in opposite_bank:
            return True

        if 'C' in opposite_bank and 'G' in opposite_bank:
            return True

        return False

if __name__ == "__main__":
    problem = FFCGProblem()
    solutions = BFSSolver.solve(problem)
    display_path(solutions[0])
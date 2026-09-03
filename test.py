from models.base_models import StateBase, TraversalProblemBase
from algorithms import DFSSolver
from utils import display_list

class Person(StateBase):
    def __init__(self, name: str):
        self._name = name

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Person({self.name})"

    def __eq__(self, other: Person) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(str(self))

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def name(self) -> str:
        return self._name

class FamilyTreeProblem(TraversalProblemBase[Person]):
    def __init__(self, family_tree: dict[str, list[str]], ancestor: str = None):
        self._family_tree = {Person(k): [Person(v) for v in family_tree[k]] for k in family_tree}

        self._ancestor = None
        if ancestor is not None:
            self._ancestor = Person(ancestor)
        

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def ancestor(self) -> Person | None:
        return self._ancestor

    @ancestor.setter
    def ancestor(self, new_ancestor: str) -> None:
        new_ancestor = Person(new_ancestor)

        if new_ancestor not in self._family_tree:
            raise IndexError(f"{new_ancestor} is not a valid ancestor!")

        self._ancestor = new_ancestor

    @property
    def initial_state(self):
        if self.ancestor is None:
            raise ValueError("No ancestor set!")
        
        return self.ancestor

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def actions(self, current_person: Person) -> list[Person]:
        children = self._family_tree[current_person]
        return children

if __name__ == "__main__":
    family_tree = {
        "Alice": ["Bob", "Charlie"],
        "Bob": ["Diana", "Eve"],
        "Charlie": ["Frank"],
        "Diana": [],
        "Eve": ["Grace"],
        "Frank": [],
        "Grace": []
        }

    problem = FamilyTreeProblem(family_tree, "Alice")
    descendants = DFSSolver.solve(problem)
    display_list(descendants)
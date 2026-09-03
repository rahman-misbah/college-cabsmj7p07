from models import TraverseProblemBase, DFSGoalSolver


class Person:
    def __init__(self, name: str):
        self._name: str = name
    
    # DUNDER METHODS ------------------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"Person({self.name})"
    
    def __str__(self) -> str:
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, other:Person) -> bool:
        return self.name == other.name
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def name(self) -> str:
        return self._name

class FamilyTreeProblem(TraverseProblemBase[Person]):
    def __init__(self, family_tree:dict[str, list[str]], ancestor:str):
        self._family_tree:dict[Person, list[Person]] = {Person(parent):[Person(child) for child in children] for parent, children in family_tree.items()}
        self._ancestor:Person = Person(ancestor)

    def actions(self, current_state: Person) -> list[Person]:
        return self._family_tree.get(current_state, [])

    def goal_test(self, current_state: Person) -> bool:
        return True

    def update_ancestor(self, new_ancestor:str) -> None:
        self._ancestor = Person(new_ancestor)
    
    @property
    def initial_state(self) -> Person:
        return self._ancestor
    
    @property
    def family_tree(self) -> dict[Person, list[Person]]:
        return self._family_tree

if __name__ == "__main__":
    family_tree: dict[str, list[str]] = {
        "Adam": ["Alice", "Bob"],
        "Alice": ["Carol", "David"],
        "Bob": ["Eve"],
        "David": ["Frank"],
    }

    problem = FamilyTreeProblem(family_tree, "Adam")
    solver = DFSGoalSolver(problem, False)
    solutions = solver.solve()

    combined_solution = set()
    for solution in solutions:
        combined_solution.update(solution)
    
    combined_solution.discard(problem.initial_state)
    
    print(combined_solution)
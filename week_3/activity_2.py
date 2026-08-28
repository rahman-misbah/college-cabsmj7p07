from types import MappingProxyType

from data_structures.stack import Stack


class Person:
    def __init__(self, name: str):
        self._name: str = name
    
    # DUNDER METHODS ------------------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"Person({self.name})"
    
    def __str__(self) -> str:
        return self.name
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def name(self) -> str:
        return self._name


class FamilyTreeProblem:
    def __init__(self, family_tree: dict[str, list[str]]):
        self._family_tree: dict[str, list[Person]] = {
            parent: [Person(child) for child in children]
            for parent, children in family_tree.items()
        }
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def family_tree(self) -> dict[str, list[Person]]:
        return MappingProxyType(self._family_tree)
    
    # PUBLIC METHODS ------------------------------------------------------------------------------

    def children(self, person: Person) -> list[Person]:
        return self._family_tree.get(person.name, [])


class FamilyTreeSolver:
    def __init__(self, problem: FamilyTreeProblem):
        self._problem: FamilyTreeProblem = problem
    
    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def problem(self) -> FamilyTreeProblem:
        return self._problem
    
    # PUBLIC METHODS ------------------------------------------------------------------------------

    def solve(self, ancestor: Person) -> list[Person]:
        descendants: list[Person] = []
        stack: Stack = Stack()

        stack.push(ancestor)

        while not stack.is_empty():
            current_person: Person = stack.pop()
            children: list[Person] = self.problem.children(current_person)

            for child in children:
                descendants.append(child)
                stack.push(child)
        
        return descendants


if __name__ == "__main__":
    family_tree: dict[str, list[str]] = {
        "Adam": ["Alice", "Bob"],
        "Alice": ["Carol", "David"],
        "Bob": ["Eve"],
        "David": ["Frank"],
    }

    problem = FamilyTreeProblem(family_tree)
    solver = FamilyTreeSolver(problem)

    ancestor = Person("Alice")
    descendants = solver.solve(ancestor)

    print("Family Tree:")
    for parent, children in problem.family_tree.items():
        children_str = ", ".join(str(child) for child in children)
        print(f"{parent} -> {children_str}")

    print(f"\nDescendants of {ancestor}:")
    for person in descendants:
        print(person)
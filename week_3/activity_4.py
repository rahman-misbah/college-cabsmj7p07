from models.base_models import StateBase, GoalProblemBase
from algorithms import DFSSolver
from utils import display_path

import copy

type Site = dict[str, Site]

class WebpageState(StateBase):
    def __init__(self, current_page: str, remaining_site: Site):
        self._current_page = current_page
        self._remaining_site = copy.deepcopy(remaining_site)

    # DUNDER METHODS ------------------------------------------------------------------------------

    def __str__(self) -> str:
        return self.page

    def __repr__(self) -> str:
        return f"WebpageState({self.page, self._remaining_site})"

    def __eq__(self, other: WebpageState) -> bool:
        return self.page == other.page

    def __hash__(self) -> int:
        return hash(str(self))

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def page(self) -> str:
        return self._current_page

    @property
    def remaining_site(self) -> Site:
        return self._remaining_site

class WebpageHierarchyProblem(GoalProblemBase[WebpageState]):
    def __init__(self, site_map: Site, target_page: str | None = None):
        self._site_map = copy.deepcopy(site_map)

        self._target_page = None
        if target_page is not None:
            self._target_page = target_page

    # PROPERTIES ----------------------------------------------------------------------------------

    @property
    def target_page(self) -> str:
        return self._target_page

    @target_page.setter
    def target_page(self, new_target_page: str) -> None:
        self._target_page = new_target_page

    @property
    def initial_state(self) -> str:
        return WebpageState('site', self._site_map)

    # PUBLIC METHODS ------------------------------------------------------------------------------

    def actions(self, current_state: WebpageState) -> list[WebpageState]:
        result = list()

        if current_state.page == "site":
            for next_page in self._site_map:
                result.append(WebpageState(next_page, self._site_map[next_page]))
        else:
            for next_page in current_state.remaining_site:
                result.append(WebpageState(next_page, current_state.remaining_site[next_page]))

        return result

    def goal_test(self, current_state: WebpageState) -> bool:
        return current_state.page == self.target_page

if __name__ == "__main__":
    site = {
        "Home": {
            "About": {
                "Team": {},
                "History": {},
            },
            "Products": {
                "Laptops": {},
                "Phones": {},
            },
            "Contact": {},
        }
    }

    problem = WebpageHierarchyProblem(site, "Phones")
    solutions = DFSSolver.solve(problem)

    display_path(solutions[0])
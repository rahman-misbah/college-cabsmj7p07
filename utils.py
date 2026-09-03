"""Small utility functions"""

from typing import Any

def display_path(path: list[Any]) -> None:
    result = list()

    for item in path:
        result.append(str(item))

    result = ' -> '.join(result)
    print(result)

def display_list(item_list: list[Any]) -> None:
    result = list()

    for item in item_list:
        result.append(str(item))

    result = ', '.join(result)
    print(result)
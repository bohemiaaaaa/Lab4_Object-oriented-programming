from typing import Dict, List, Set, Tuple

numbers: List[int] = [1, 2, 3]
grades: Dict[str, float] = {"math": 4.5, "physics": 5.0}
record: Tuple[str, int] = ("John", 25)
tags: Set[str] = {"python", "typing"}

numbers_new: list[int] = [1, 2, 3]
grades_new: dict[str, float] = {"math": 5.0}


def min_max(values: list[int]) -> Tuple[int, int]:
    return min(values), max(values)


def min_max_new(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)

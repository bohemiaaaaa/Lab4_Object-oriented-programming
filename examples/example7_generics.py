from typing import Generic, List, TypeVar

T = TypeVar("T")


def first(items: List[T]) -> T:
    return items[0]


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


b1 = Box[int](42)
b2 = Box[str]("Hello")

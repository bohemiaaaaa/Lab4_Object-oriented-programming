class Student:
    name: str
    grades: list[int]

    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    def average(self) -> float:
        return sum(self.grades) / len(self.grades)


class Person:
    name: str
    age: int


class Employee(Person):
    position: str
    salary: float

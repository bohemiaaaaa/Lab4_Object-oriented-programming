#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Generic, Tuple, TypeVar

T = TypeVar("T")


class UniversalPair(Generic[T]):
    def __init__(self, first: T, second: T) -> None:
        self.first = first
        self.second = second

    def get_pair(self) -> Tuple[T, T]:
        return (self.first, self.second)

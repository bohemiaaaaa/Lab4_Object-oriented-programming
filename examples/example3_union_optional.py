#!/usr/bin/env python3
# -*- coding: utf-8 -*


from typing import Optional, Union


def normalize(value: Union[int, float, str]) -> float:
    if isinstance(value, str):
        value = value.replace(",", ".")
    return float(value)


def normalize_new(value: int | float | str) -> float:
    if isinstance(value, str):
        value = value.replace(",", ".")
    return float(value)


def find_user_id(name: str) -> Optional[int]:
    users = {"Alice": 1, "Bob": 2}
    return users.get(name)

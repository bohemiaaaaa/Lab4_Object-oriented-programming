#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from universal_pair import UniversalPair


def test_universal_pair_int():
    pair = UniversalPair[int](10, 20)
    result = pair.get_pair()
    assert result == (10, 20)
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)


def test_universal_pair_str():
    pair = UniversalPair[str]("hello", "world")
    result = pair.get_pair()
    assert result == ("hello", "world")
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)


def test_universal_pair_same_type():
    pair = UniversalPair[float](3.14, 2.71)
    result = pair.get_pair()
    assert all(isinstance(x, float) for x in result)


def test_universal_pair_different_types_error():
    with pytest.raises(TypeError):
        UniversalPair[int]("string", 10)

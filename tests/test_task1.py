#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from printer_function import printer


def test_printer_return_type():
    """Проверяет что printer возвращает None"""
    result = printer("test")
    assert result is None


def test_printer_annotations():
    """Проверяет аннотации функции printer"""
    annotations = printer.__annotations__
    assert annotations["value"] == str
    assert annotations["return"] is type(None)


def test_printer_output(capsys: pytest.CaptureFixture[str]):
    """Проверяет вывод функции printer с использованием pytest"""
    printer("test message")
    captured = capsys.readouterr()
    assert captured.out == "test message\n"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from printer_function import printer


def test_printer_return_type():
    result = printer("test")
    assert result is None


def test_printer_annotations():
    annotations = printer.__annotations__
    assert annotations["value"] == str
    assert annotations["return"] is None


def test_printer_output(capsys: pytest.CaptureFixture[str]):
    printer("test message")
    captured = capsys.readouterr()
    assert captured.out == "test message\n"

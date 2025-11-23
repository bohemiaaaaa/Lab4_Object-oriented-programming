#!/usr/bin/env python3
# -*- coding: utf-8 -*


from typing import Literal


def set_status(status: Literal["new", "in_progress", "done"]) -> None:
    print(f"Текущий статус: {status}")


set_status("new")
set_status("in_progress")

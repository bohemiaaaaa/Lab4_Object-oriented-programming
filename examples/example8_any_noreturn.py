import sys
from typing import Any, NoReturn


def show(value: Any) -> None:
    print(f"Получено значение: {value}")


def fatal_error(msg: str) -> NoReturn:
    print(f"Фатальная ошибка: {msg}")
    sys.exit(1)

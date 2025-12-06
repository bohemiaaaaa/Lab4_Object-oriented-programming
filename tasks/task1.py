#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from printer_function import printer


def main():
    result = printer("Hello, World!")
    print(f"Тип возвращаемого значения: {type(result)}")
    print(f"Значение возвращаемого значения: {result}")
    print(f"Является ли NoneType: {result is None}")


if __name__ == "__main__":
    main()

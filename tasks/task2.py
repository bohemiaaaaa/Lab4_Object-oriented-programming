#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from universal_pair_package.universal_pair import UniversalPair


def main():
    # С целыми числами - тип автоматически определяется как int
    int_pair = UniversalPair(10, 3)
    print(f"Пара целых чисел: {int_pair.get_pair()}")

    # Со строками - тип автоматически определяется как str
    str_pair = UniversalPair("hello", "world")
    print(f"Пара строк: {str_pair.get_pair()}")

    # С числами с плавающей точкой - тип автоматически определяется как float
    float_pair = UniversalPair(3.14, 2.71)
    print(f"Пара дробных чисел: {float_pair.get_pair()}")


if __name__ == "__main__":
    main()

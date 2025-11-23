#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from universal_pair_package.universal_pair import UniversalPair


def main():
    # С целыми числами
    int_pair = UniversalPair[int](10, 20)
    print(f"Пара целых чисел: {int_pair.get_pair()}")

    # Со строками
    str_pair = UniversalPair[str]("hello", "world")
    print(f"Пара строк: {str_pair.get_pair()}")

    # С числами с плавающей точкой
    float_pair = UniversalPair[float](3.14, 2.71)
    print(f"Пара дробных чисел: {float_pair.get_pair()}")


if __name__ == "__main__":
    main()

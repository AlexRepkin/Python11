#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def negative():
    print("It seems to us that value is negative!")


def test():
    """Определение числа, положительное или отрицательное."""

    number = int(input("Good day! Please, enter your value - "))
    if number >= 0:
        positive()
    else:
        negative()


def positive():
    print("It seems to us that value is positive!")


if __name__ == '__main__':
    test()

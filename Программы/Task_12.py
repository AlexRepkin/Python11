#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply():
    new_value = int(input("Good day! Please, enter your first value - "))
    if new_value == 0:
        return 0
    answer = 1

    """Ввод чисел до тех пор, пока не будет получен 0."""

    while new_value != 0:
        answer *= new_value
        new_value = int(input("Next value - "))
    return answer


if __name__ == '__main__':
    # answer = multiply()

    """Перемножение введённых пользователем чисел."""

    print("Very well, multiplying all the values gives us - ", multiply())

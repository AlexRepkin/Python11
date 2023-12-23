#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    """Получение строки"""

    return input("Good day! Please, enter the line - ")


def test_input(word):
    """Анализ строки, можно ли преобразовать в число"""

    if word.isdigit():
        return True
    else:
        return False


def str_to_int(value):
    """Преобразование в число"""

    return int(value)


def print_int(value):
    """Вывод числа на экран"""

    print(value)


if __name__ == '__main__':
    """Вызов функций для анализа строки. Если число - преобразовать и вывести."""

    value = get_input()
    if test_input(value):
        print_int(str_to_int(value))
        # to_print = str_to_int(value)
        # print_int(to_print)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi  # Весь math не нужен, его импорт уже будет антипаттерном


def cylinder():

    def circle(radius):
        """Определение площади круга"""

        return pi * (radius ** 2)

    variant = input(
        '''Good day! If you want to get square of cylinder's border, print 1.
If you want to get square of the whole cylinder, print anything else - ''')
    radius = float(input("\nGreat! Now, please, give us the radius - "))
    height = float(input("And height - "))
    answer = 2*pi*radius*height

    """Определение требуемой площади, если нужна всего цилиндра, то домножается ответ на 2 круга"""

    if variant == "1":
        print("\nAccording to our calculations, the answer is -", answer)
    else:
        print("\nAccording to our calculations, the answer is -",
              answer + 2*circle(radius))


if __name__ == '__main__':
    cylinder()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def circle_area_decorator(func):
    """
    Декоратор функции, выводящий на экран «Площадь круга равна = <число>».
    """
    
    def wrapper(radius):
        """
        Функция-обертка
        """
        area = func(radius)
        print(f"Площадь круга равна = {area:.2f}")
        return area
    return wrapper


@circle_area_decorator
def circle_area(radius):
    """
    Вычисляет площадь круга
    """
    return 3.1415 * radius**2

if __name__ == "__main__":
    radius_value = 8
    circle_area(radius_value)
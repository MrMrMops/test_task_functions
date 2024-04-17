"""
   1. Написать функцию, которая принимает на вход список целых чисел и
   возвращает новый список, содержащий только уникальные элементы из
   исходного списка. Есть два способа:
"""
#1
from datetime import datetime


def get_unique_numbers1(numbers):

    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique
#2
def get_unique_numbers2(numbers):
    return list(set(numbers))



def get_prime_numbers(min_num, max_num):
    """
        2. Написать функцию, которая принимает на вход два целых числа
        (минимум и максимум) и возвращает список всех простых чисел в
        заданном диапазоне.
    """

    prime_numbers = []

    for number in range(min_num, max_num + 1):
        if number <= 1:
            continue
        if number <= 3:
            prime_numbers.append(number)
            continue
        elif number % 2 == 0 or number % 3 == 0:
            continue

        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                break
            i += 6
        else:
            prime_numbers.append(number)

    return prime_numbers

class Point():
    """
       3. Создать класс Point, который представляет собой точку в двумерном
       пространстве. Класс должен иметь методы для инициализации координат точки,
       вычисления расстояния до другой точки,
       а также для получения и изменения координат.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, name: str):
        return self.__dict__[f"_{name}"]

    def __setattr__(self, name, value):
        try:
            self.__dict__[f"_{name}"] = int(value)
        except ValueError:
            raise ValueError("Coordinates must be a numeric.")

    def get_distance_to(self, x: int, y: int) -> float:
        return ((self.x - x) ** 2 + (self.y - y) ** 2)**2

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

def sort_strings(lst) -> list:
    """
    4. Написать программу, которая сортирует список строк по длине,
    сначала по возрастанию, а затем по убыванию.
    """
    lst = sorted(lst, key=len)
    lst = sorted(lst, key=len, reverse=True)
    return lst



if __name__ == "__main__":
    import doctest
    doctest.testmod()
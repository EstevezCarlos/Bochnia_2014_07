from typing import Any


class Calc:
    def __init__(self, price) -> None:
        self.price: float = price   # attribute / property

    @staticmethod
    def add(a, b):                  # method add, specific kind of attribute
        return a + b


my_calc = Calc(35)                  # instance of class Calc
print(my_calc.add(4, 5))

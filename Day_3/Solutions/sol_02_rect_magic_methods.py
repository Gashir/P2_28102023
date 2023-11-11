"""
Используем класс Rect() с длиной и шириной в качестве атрибутов
Дополнительные задания на magic methods:
1) __repr__() - отобразить в виде текста

2) __str__() - отобразить в виде текста

3) r1 * 5 (__mul__()) - обе стороны станут в 5 раз больше
   добавить проверкy, что тип аргумента метода __mul__ это int или float
   # Variant 1, но python -O отключает все assert'ы
   assert type(arg) in (int, float), 'Bad type'

   # Variant 2
   if type(arg) in (int, float):
       pass
   else:
       raise TypeError

4) r1 < r2, r1 == r2, r1 <= r1 и т.п.

Шесть методов для сравнения:
__lt__() -> '<'
__gt__() -> '>'
__le__() -> '<='
__ge__() -> '>='
__eq__() -> '=='
__ne__() -> '!='
Сравнить по площади.

def __gt__(self, other):
	# ...
	# return True/False
"""


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(x={self.width},y={self.height})'

    def __repr__(self):
        return f'Rect{self.width, self.height}'

    def __mul__(self, value):
        if type(value) in (int, float):
            self.width *= value
            self.height *= value
        else:
            raise TypeError('Bad type of value')

    def area(self) -> int | float:
        return self.width * self.height

    def __lt__(self, other) -> bool:
        return self.area() < other.area()

    def __gt__(self, other) -> bool:
        return self.area() > other.area()

    def __le__(self, other) -> bool:
        return self.area() <= other.area()

    def __ge__(self, other) -> bool:
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()


print("Тестовая часть")

r1 = Rect(2, 5)
r2 = Rect(4, 6)
print(f'{r1 = }, {r1.area() = }')
print(f'{r2 = }, {r2.area() = }')

print("Before:")
print(r1 == r2)
print(r1 != r2)
print(r1 < r2)
print(r1 <= r2)
print(r1 > r2)
print(r1 >= r2)
print('=' * 25)
print("After:")
r1 * 5
print(f'{r1 = }, {r1.area() = }')
print(f'{r2 = }, {r2.area() = }')
print(r1 == r2)
print(r1 != r2)
print(r1 < r2)
print(r1 <= r2)
print(r1 > r2)
print(r1 >= r2)

print("Check __mul__:")
r1 * True # Вспомнить и проверить


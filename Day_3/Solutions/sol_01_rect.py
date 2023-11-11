"""
Прямоугольник по двум сторонам.
Создать класс прямоугольник:

а) при создании указывается ширина и длина

r = Rect(5, 10)

б) методы для площади и периметра

print(r.area()) # возвращает площадь
print(r.perimeter()) # возвращает периметр

в) масштабирование и поворот

r.scale(10) - ширина и длина увеличиваются в 10 раз
r.scale(0.1) - ширина и длина уменьшаются в 10 раз
r.rotate() - меняется местами ширина и длина

г) перегрузить магические методы __repr__ и __str__
"""
import random


class Rect:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def perimeter(self):
        return 2 * (self.x + self.y)

    def area(self):
        return self.x * self.y

    def rotate(self):
        self.x, self.y = self.y, self.x

    def scale(self, value: int | float):
        self.x *= value
        self.y *= value

    def __str__(self):
        return f'Rectangle(x={self.x},y={self.y})'

    def __repr__(self):
        return f'Rect{self.x, self.y}'


# Тестовая часть
rect = Rect(5, 10)
print("Площадь: ", rect.area())
print("Периметр: ", rect.perimeter())

if random.randint(0, 1):
    rect.scale(10)
    # Покажи значение rect, используя метод __str__()
    print(f"Увеличение: {rect!s}")
else:
    rect.scale(0.1)
    print(f"Уменьшение: {rect!s}")


print("Площадь: ", rect.area())
print("Периметр: ", rect.perimeter())
print(rect)
print(repr(rect))
print("Before rotate: ", rect)
rect.rotate()
print("After rotate: ", rect)


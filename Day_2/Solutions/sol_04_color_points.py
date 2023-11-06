from typing import Self


class Point:
    def __init__(self, x, y, color='white'):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point: Self) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# пример работы метода
# p1 = Point(4, 4)
# p2 = Point(3, 3)
#
# result = p1.distance(p2)
# print(result)

def triangle_area(p1: Point, p2: Point, p3: Point) -> float:
    """ Функция для подсчета площади треугольника """
    a = p1.distance(p2)
    b = p2.distance(p3)
    c = p1.distance(p3)
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр

reds = []
greens = []
for point in points:
    if point.color == "red":
        reds.append(point)
    elif point.color == "green":
        greens.append(point)

print("Площадь красного треугольника = ", triangle_area(*reds))
print("Площадь зеленого треугольника = ", triangle_area(*greens))

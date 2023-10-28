class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Используем подсказки типов(hinting) в сигнатуре функции
def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    result = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    return result


def bad_distance(p1, p2):
    """ Расстояние между двумя точками """
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


if __name__ == '__main__':
    # Дано две точки на координатной плоскости
    point1 = Point(2, 4)
    point2 = Point(5, -2)

    # Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()
    print("Расстояние между точками = ", distance(point1, point2))
    print("Расстояние между точками = ", bad_distance(point1, point2))

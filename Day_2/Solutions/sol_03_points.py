class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    
    
# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
# Variant 1
zero_point = Point(0, 0)
max_dist = 0
max_point = None  # Пример аккуратного кода
for point in points:
    if (curr_dist := distance(zero_point, point)) > max_dist:
        max_dist = curr_dist
        max_point = point


print(f"Координаты наиболее удаленной точки = {max_point.x, max_point.y}")

# Variant 2
ZERO = Point(0, 0)
distances = []
for point in points:
    distances.append(distance(ZERO, point))

max_dist = max(distances)
idx = distances.index(max_dist)
print(f"Координаты наиболее удаленной точки = {points[idx].x, points[idx].y}")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
# First step(algorithm, private case)
AB = distance(points[0], points[1])
BC = distance(points[1], points[2])
CD = distance(points[2], points[3])
DE = distance(points[3], points[4])
length_line = AB + BC + CD + DE
print("Длина ломаной линии = ", length_line)

# Second step(universal algorithm)
# Variant 1
length = 0
for index in range(len(points) - 1):
    length += distance(points[index], points[index + 1])

print("Длина ломаной линии = ", length)

# Variant 2
lengths = []
for index in range(1, len(points)):
    lengths.append(distance(points[index - 1], points[index]))

print("Длина ломаной линии = ", sum(lengths))

# Variant 3
pts = points
print("Длина ломаной линии = ", sum([distance(pts[i], pts[i+1]) for i in range(len(pts)-1)]))

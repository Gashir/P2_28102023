def func(a: float, b: float):
    """ Функция принимает 2 числовых аргумента """
    return a + b, a - b


value1 = 100
value2 = 89.4

print(func(value1, value2))


print(func('hello', 'python'))
import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.choice(['heads', 'tails'])  # возвращаем одно из значений списка
        # return side # Это ошибка, здесь return не нужен


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

# Пошаговый алгоритм решения задачи

# DONE 0. Реализовать метод flip()

# DONE 1. Создать список монет
n = int(input('Введите количество монет: '))
coins = []
for _ in range(n):
    coin = Coin()
    coins.append(coin)

# ========================================
# print('Check before run flip() method:')
# for coin in coins:
#     print(coin.side)
# ========================================

# 2. Взять каждую монету и вызвать у нее метод flip()
for coin in coins:
    coin.flip()  # Coin.flip(coin)
# =====================================
# print('Check after run flip() method:')
# for coin in coins:
#     print(coin.side)
# =====================================

# 3. Подсчитать количество монет, у которых значение атрибута side == 'heads' и то же самое для 'tails'
heads = tails = 0
for coin in coins:
    if coin.side == 'heads':
        heads += 1
    elif coin.side == 'tails':
        tails += 1

# 4. Вывести процентное соотношение орлов и решек
# Как форматировать: умножить на 100, округлить до 2-х знаков после запятой и добавить знак %
print(f'Орлы: {heads/n:.2%}')
print(f'Решки: {tails/n:.2%}')


# Подсказки
# ===================================================================
# coin_one = Coin()
# coin_two = Coin()
# lst = [coin_one, coin_two]
#
# lst = [str(88), int('5'), bool('hello')]
# for value in lst:  # value = '88', value = 5, value = True
#     print(value)
#
# print(f'{value = }')  # True
#
# f = float('89.12')
# lst.append(f)
# lst.append(float('90.12'))
#
# print(lst)
# ===================================================================

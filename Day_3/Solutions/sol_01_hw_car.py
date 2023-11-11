"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...

# Значит должны быть значения по умолчанию
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезает бензина (capacity)
* "расход топлива на 100 км" (gas_per_100km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то бак заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
выведет сообщение "проехали ... километров",
в результате поездки потратится бензин и увеличится пробег.
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (вывести количество бензина в баке и пробег)
"""


class Car:
    def __init__(self, gas=10, capacity=100, gas_per_100km=10, mileage=2000):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, liters=100):
        if liters > (self.capacity - self.gas):
            print(f'Лишние литры: {liters - self.capacity + self.gas}')
            self.gas = self.capacity
        else:
            self.gas += liters

    def ride(self, km=220):
        if (self.gas / self.gas_per_100km) * 100 > km:
            print(f'Едем {km} километров')
            self.gas -= km * self.gas_per_100km / 100
            self.mileage += km
        else:
            print(f'Едем {(self.gas / self.gas_per_100km) * 100} километров')
            self.mileage += (self.gas / self.gas_per_100km) * 100
            self.gas = 0

    def info(self):
        print(f'Количество бензина в баке: {self.gas}\nПробег: {self.mileage}')


car1 = Car()
car1.info()
print('=' * 25)

car1.fill(20)
car1.info()
print('=' * 25)

car1.ride(100)
car1.info()
print('=' * 25)

car1.fill(200)
car1.info()
print('=' * 25)

car1.ride(2000)
car1.info()
print('=' * 25)
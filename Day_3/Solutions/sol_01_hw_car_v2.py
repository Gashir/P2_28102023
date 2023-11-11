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
    def __init__(self, gas=0, capacity=55, gas_per_100km=8, mileage=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, gas) -> None:
        if gas + self.gas <= self.capacity:
            self.gas += gas
        else:
            print(f"Вы заказали на {gas + self.gas - self.capacity} л топлива больше, чем вмещает бак")
            self.gas = self.capacity

    def ride(self, km) -> None:
        gas_used = km * self.gas_per_100km/100
        if gas_used <= self.gas:
            km_passed = km
        else:
            km_passed = self.gas/self.gas_per_100km*100
        print(f"проехали {km_passed} км")

        if gas_used > self.gas:
            self.gas = 0
        else:
            self.gas -= gas_used

        self.mileage += km_passed

    def info(self):
        print(f"топливо = {self.gas} л, пробег = {self.mileage} км")


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
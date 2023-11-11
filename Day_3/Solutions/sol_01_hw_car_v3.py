class Car:
    def __init__(self, gas=0, capacity=40, gas_per_100km=10, mileage=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, gas):
        new_gas = self.gas + gas
        if new_gas <= self.capacity:
            self.gas += gas
        else:
            self.gas = self.capacity
            print(f"Лишние - {new_gas - self.capacity} л.")

    def ride(self, distance):
        gas_per_km = self.gas_per_100km / 100
        gas_expense = distance * gas_per_km
        if self.gas >= gas_expense:
            actual_distance = distance
            self.gas -= gas_expense
        else:
            actual_distance = self.gas / gas_per_km
            self.gas = 0
        print(f"Проехали {actual_distance} км")
        self.mileage += actual_distance

    def info(self):
        print(f"Бензина в баке - {self.gas}, пробег - {self.mileage}")


if __name__ == '__main__':
    car1 = Car(10, 100, 25, 100000)
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
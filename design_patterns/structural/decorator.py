class Car:
    def __init__(self):
        self.price = 30000

class LeatherSeats:
    def __init__(self, car):
        car.price += 2000

class PerformanceBreaks:
    def __init__(self, car):
        car.price += 3000

class DolbeSoundSystem:
    def __init__(self, car):
        car.price += 3000

car = Car()

print("base car price:", car.price)

LeatherSeats(car)
PerformanceBreaks(car)
DolbeSoundSystem(car)

print("new car price:", car.price)
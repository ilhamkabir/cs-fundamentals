from dataclasses import dataclass

@dataclass
class Car:
    make    : str
    model   : str

class Ferrari(Car):

    def __init__(self):
        self.make = 'Ferrari'

class Lamborghini(Car):

    def __init__(self):
        self.make = 'Lamborghini'

class SportsCarFactory:
    '''
    Factory Class

    Creates representations of several different classes.
    '''

    @staticmethod
    def create_ferrari_enzo():
        enzo = Ferrari()
        enzo.model = 'Enzo'
        return enzo

    @staticmethod
    def create_lamborghini_aventador():
        aventador = Lamborghini()
        aventador.model = 'Aventador'
        return aventador


enzo = SportsCarFactory.create_ferrari_enzo()
aventador = SportsCarFactory.create_lamborghini_aventador()

print(enzo.make, enzo.model)
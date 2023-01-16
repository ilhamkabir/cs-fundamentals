from dataclasses import dataclass

@dataclass
class Car:
    make    : str
    model   : str

class Tesla(Car):

    def __init__(self):
        self.make = 'Tesla'

class TeslaModel3Factory:
    '''
    Factory Class

    Only creates one type of Tesla.
    '''
    
    @staticmethod
    def create_model3():
        model3 = Tesla()
        model3.model = 'Model 3'
        return model3


model3 = TeslaModel3Factory.create_model3()

print(model3.make, model3.model)
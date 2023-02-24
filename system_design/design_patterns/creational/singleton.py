'''
This is just one implmentation of a Singtlon!

Singletons can also be created via:
    - Factory Objects
    - Meta Classes
    - MonoState Classes
'''

class Singleton:
    _instances = {}     # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in Singleton._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Person(Singleton):

    def __init__(self, name):
        self.name = name

john = Person("John")
bob = Person("Bob")

# ------------------

print("john and bob are the same object?: ", john is bob)